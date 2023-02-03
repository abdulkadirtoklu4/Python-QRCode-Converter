import pyqrcode

print("Choose Program Language: (TR / EN)")

language = input()

if language == "tr" or language == "Tr" or language == "TR":
    
    url = input("Qr Koda Dönüştürmek İçin Url Adresi Girin: ")
    qr_code = pyqrcode.create(url)
    qr_code.svg('qrcode.svg', scale=5)

elif language == "en" or language == "En" or language == "EN":
    url = input("Input Url Address to Convert to Qr Code: ")
    qr_code = pyqrcode.create(url)
    qr_code.svg('qrcode.svg', scale=5)

else:
    print("You Pressed The Wrong Key")