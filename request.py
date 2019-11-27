import smtplib
import ssl
import requests
import shutil
import sys
from scipy.linalg import norm
from scipy import sum, average
import glob
import numpy as np
from PIL import Image
import tkinter as tk
from PIL import ImageTk, Image


class Email:
    """
    Construct email
    :param message:
    """

    def __init__(self, message):
        # SSL port
        self.port = 465
        self.smtp_server = "smtp.gmail.com"

        self.email_sender = "architecturelogiciel.projet@gmail.com"
        self.password_sender = "davidtennant"

        self.email_receiver = "karenoreau11@gmail.com"

        self.message = message

    """
    Call the function to send an email
    """

    def send_email(self):
        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=context) as server:
            server.login(self.email_sender, self.password_sender)
            server.sendmail(self.email_sender, self.email_receiver, self.message)


"""
help:
https://stackoverflow.com/questions/189943/how-can-i-quantify-difference-between-two-images
"""


class Images:
    def __init__(self):
        self.file_list = glob.glob('images/*.jpg')
        self.path_first_image = "images/photo1"
        self.path_second_image = "images/photo3"

        self.first_image = []
        self.second_image = []

    def get_first_array(self):
        x = np.array([np.array(Image.open(self.file_list[0]))])
        print(x)

    def get_second_array(self):
        y = np.array([np.array(Image.open(self.file_list[1]))])
        print(y)


"""
Init program
"""

url = 'http://172.16.12.131/Streaming/channels/1/picture'
reponse = requests.get(url, auth=('admin', 'linux111'))
if reponse.status_code == 200:
    with open(r"/Users/sher/Desktop/test.jpg", 'wb') as f:
        f.write(reponse.content)
email = Email("you are my hero")
email.send_email()

# images = Images()
# images.get_first_array()
# print("next image")
# images.get_second_array()

window = tk.Tk()
window.title("Join")
window.geometry("300x300")
window.configure(background='grey')

path = "images/photo1.jpg"

# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))


# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image=img)

# The Pack geometry manager packs widgets in rows or columns.
panel.pack(side="bottom", fill="both", expand="yes")

# Start the GUI
window.mainloop()
