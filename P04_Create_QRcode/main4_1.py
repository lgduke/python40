import qrcode

qr_data = "www.daum.net"
qr_img = qrcode.make(qr_data)

save_path = 'P04_Create_QRcode/' + qr_data + '.png'
qr_img.save(save_path)