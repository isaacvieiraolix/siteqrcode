import pyqrcode 
from PIL import Image
link = input("Enter the link: ")
qr_code = pyqrcode.create(link)
qr_code.png("qrcode.png", scale=4)
img = Image.open("qrcode.png")
img.show()