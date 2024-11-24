import qrcode

# Cambia la URL si subes la página a internet
url = "http://localhost:8000"

# Crear el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Guardar el QR como imagen
img = qr.make_image(fill_color="black", back_color="white")
img.save("codigo_qr.png")

print("¡QR generado como codigo_qr.png!")
