import qrcode

# Temporary local app link
app_url = "http://localhost:8501"

# Generate QR
qr = qrcode.make(app_url)

# Save QR image
qr.save("assets/heal_ai_qr.png")

print("QR Code Generated Successfully")