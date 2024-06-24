import face_recognition
from imutils.video import VideoStream
import numpy as np
import imutils
import cv2
import datetime
d=datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

img_counter = 0

class abc:
    # loop over the frames from the video stream

    def check_face(self, lid, atm_id):
        print("[INFO] starting video stream...")
        vs = VideoStream(src=0).start()

        path = r"D:\Project softwares\Project\Secure_ATM\Secure_ATM_app\static\\"
        imgpath=r"D:\Project softwares\Project\Secure_ATM\Secure_ATM_app\static\images\\"
        # time.sleep(2.0)
        while True:
            # grab the frame from the threaded video stream and resize it
            # to have a maximum width of 400 pixels
            frame = vs.read()
            frame = imutils.resize(frame,width=400)
            imgname = path+"h3.jpg".format(img_counter)
            cv2.imwrite(imgname, frame)
            print("inside")

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            # if key == ord("q"):
            #     break
            break

        cv2.destroyAllWindows()
        vs.stop()


        lid=str(lid)
        from PIL import Image
        from DBConnection import Db
        qry = "select * from secure_atm_app_customer where id='"+lid+"'"
        # qry = "select * from criminal"
        db = Db()
        res = db.select(qry)
        res2=db.select("select * from secure_atm_app_authorized_person where USER_id='"+lid+"'")
        knownlist=[]
        for j in res:
            knownlist.append({'user_id':j['id'], 'name':j['name'], 'image':j['image']})
        for k in res2:
            knownlist.append({'user_id':k['id'], 'name':k['name'], 'image':k['image']})
        print(knownlist)
        known_faces = []
        userids = []
        person_name = []
        identified = []
        if res is not None:
            for result in knownlist:
                picc = result["image"]
                pname = picc.split("/")
                img = imgpath + pname[len(pname) - 1]
                print(img)
                b_img = face_recognition.load_image_file(img)
                b_imgs = face_recognition.face_encodings(b_img)[0]
                known_faces.append(b_imgs)
                userids.append(result["user_id"])
                person_name.append(result["name"])
                print(str(len(known_faces)) + " done")

            # unknown_image = face_recognition.load_image_file(staticpath + "a_270.jpg")
            unknown_image = face_recognition.load_image_file(path + "h3.jpg")
            unkonownpersons = face_recognition.face_encodings(unknown_image)
            print(len(unkonownpersons), "llllllllllllllllllllllll")
            if len(unkonownpersons) > 0:

                for i in range(0, len(unkonownpersons)):
                    h = unkonownpersons[i]

                    red = face_recognition.compare_faces(known_faces, h, tolerance=0.45)  # true,false,false,false]
                    print(red)
                    for i in range(0, len(red)):
                        if red[i] == True:
                            identified.append(userids[i])
                print(identified,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
                l=identified
                print("LL", l)
                if len(l) > 0:
                    return "ok"

                else:
                    import time
                    dt = time.strftime("%Y%m%d_%H%M%S")
                    cv2.imwrite(r"D:\Project softwares\Project\Secure_ATM\Secure_ATM_app\static\block_images\\" + dt + ".jpg", frame)
                    path = "/static/block_images/" + dt + ".jpg"

                    db = Db()
                    print("PPP  ", atm_id)
                    db.insert("insert into secure_atm_app_block_details values(null, curdate(), curtime(), 'blocked', '" + path + "', '" + str(
                        atm_id) + "')")
                    db.update(
                        "update secure_atm_app_atm_card set status='blocked' where id='" + str(atm_id) + "'")

                    print("Fraud detected")
                    return "no"


