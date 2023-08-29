import qrcode

file_path = r'P04_Create_QRcode/qr_list.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_lines = f.readlines()
    
    for line in read_lines:
        line = line.strip()
        print(line)
        


# qr_img = qrcode.make(qr_data)

# save_path = 'P04_Create_QRcode/' + qr_data + '.png'
# qr_img.save(save_path)
