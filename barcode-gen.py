import barcode
import os



# Folder to save the QR code
folder = "Barcodes"

# Create the folder if it doesn't exist
if not os.path.exists(folder):
    os.makedirs(folder)
    
# Save the image in the folder
image_path = os.path.join(folder, 'barcode.png')
img.save(image_path)

print(f"Barcode code saved at: {image_path}")