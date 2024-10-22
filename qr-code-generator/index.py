import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter the Filename: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color="black", back_color="white")
if not filename.endswith(".png"):
    filename += ".png"
image.save(filename)
print(f'QR Code Save as {filename}')
