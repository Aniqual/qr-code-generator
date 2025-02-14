from flask import Flask, request, jsonify, send_file, render_template
import qrcode
from io import BytesIO

app = Flask(__name__)

# Route to serve the frontend (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# Route to generate QR code
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.json.get('data')
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Save QR code to a BytesIO object
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)