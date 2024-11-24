import qrcode

# URL de tu GitHub Pages
url = "https://totiML.github.io/mi-regalo/"

# Generar el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Guardar el QR como imagen
img = qr.make_image(fill_color="black", back_color="white")
img.save("codigo_qr.png")
print("Código QR generado con éxito.")
