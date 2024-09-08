import qrcode
import os

#Data to encode
qr_code = "youtube.com"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version=1, box_size=10, border=5)

#add data to instance qr
qr.add_data(qr_code)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Folder to save the QR code
folder = "QR Codes"

# Create the folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)
    
# Save the image in the folder
image_path = os.path.join(folder, 'QR.png')
img.save(image_path)

print(f"QR code saved at: {image_path}")