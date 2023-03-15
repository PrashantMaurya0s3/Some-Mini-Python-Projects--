

import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4, )

qr.add_data("Put the link here to build the QR Code")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("my.jpg")

