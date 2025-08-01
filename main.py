from flask import Flask, send_file
import qrcode
import io
import datetime

app = Flask(__name__)

@app.route("/")
def generate_qr():
    now = datetime.datetime.now()
    unique_url = f"https://tr.ee/cMbDNO43pY?t={now.strftime('%Y%m%d%H%M%S')}"
    img = qrcode.make(unique_url)
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
