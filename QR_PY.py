import qrcode
data ="Bhagyesh Patil"

qr = qrcode.make(data)
qr.save("QR.png")

print("QR code generated successfully")

