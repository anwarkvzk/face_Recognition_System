from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from sympy import root


class Face_Recognition_System:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #First image
        img = Image.open("/home/anvar/Desktop/face_recognition/download.jpeg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        
        #Second Image
        img1 = Image.open("/home/anvar/Desktop/face_recognition/facialrecognition.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)


        #Third image
        img2 = Image.open("/home/anvar/Desktop/face_recognition/dd.jpeg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)


        #Background image
        img3 = Image.open("/home/anvar/Desktop/face_recognition/bgimage.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)


        title_lbl = Label(bg_img, text="FACE RECOGNITION SYSTEM ATTENDENCE SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()