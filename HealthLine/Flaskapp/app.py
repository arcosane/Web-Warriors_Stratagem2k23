from flask import Flask,render_template,request
from deepface import DeepFace
import cv2 as cv

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("Register.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/facial_input")
def facial_input():
    return render_template("facial_input.html")

@app.route("/verification")
def verification():
    return render_template("verification.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/verify" , methods = ['POST' , 'GET'])
def verify():
    output = request.form.to_dict()
    pname = str(output["p_name"])
    pid = str(output["p_id"])

    if pname == "chhand" and pid == "01" and verification() == True:
        return render_template("verification.html" , status = "verified")
    else:
        return render_template("verification.html" , status = "Not verified")



def verification():
    cam = cv.VideoCapture(0)

    cv.namedWindow("Webcam")

    img_counter = 1

    while True:
        ret , frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv.imshow("Test",frame)

        k = cv.waitKey(1)
        if k%256 == 27:
            print("Verifying Face...")
            break
        elif k%256 == 32:
            img_name = "image{}.jpg".format(img_counter)
            cv.imwrite("static/"+img_name,frame)
            print("Screenshot taken {}".format(img_counter))
            img_counter += 1

    cam.release()


    verification1 = DeepFace.verify(img1_path="static/img1.jpg" , img2_path="static/image1.jpg")
    verification2 = DeepFace.verify(img1_path="static/img1.jpg" , img2_path="static/image2.jpg")
    verification3 = DeepFace.verify(img1_path="static/img1.jpg" , img2_path="static/image3.jpg")
    verification4 = DeepFace.verify(img1_path="static/img1.jpg" , img2_path="static/image4.jpg")
    verification5 = DeepFace.verify(img1_path="static/img1.jpg" , img2_path="static/image5.jpg")

    if verification1['verified'] == True or verification2['verified'] == True or verification3['verified'] == True or verification4['verified'] == True or verification5['verified'] == True:
        print(verification1['verified'])
        print(verification2['verified'])
        print(verification3['verified'])
        print(verification4['verified'])
        print(verification5['verified'])
        print("Face Matched")
        return True

    else:
        return False

if __name__ == "__main__":
    app.run(debug = True , port = 5001)