from flask import Flask, render_template, request
import sqlite3
import os
from pyzbar.pyzbar import decode
import cv2
import time

app = Flask(__name__)

# ✅ Database path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")


# ✅ Check product in database
def check_product(product_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id=?", (product_id,))
    result = cursor.fetchone()
    conn.close()
    return result


# ✅ QR Scanner function
def scan_qr(image_path):
    img = cv2.imread(image_path)
    decoded_objects = decode(img)

    for obj in decoded_objects:
        return obj.data.decode("utf-8")

    return None


# ✅ Main route
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':

        product_id = None

        # 🔹 Case 1: Manual input
        if request.form.get('product_id'):
            product_id = request.form['product_id'].strip()

        # 🔹 Case 2: QR upload
        elif 'qr_image' in request.files:
            file = request.files['qr_image']

            if file.filename != "":
                file_path = os.path.join(BASE_DIR, "temp.png")
                file.save(file_path)

                product_id = scan_qr(file_path)

                if product_id:
                    product_id = product_id.strip()
                    print("Scanned QR:", product_id)
                else:
                    result = "❌ No QR code detected"
                    return render_template('index.html', result=result)

        # 🔹 Check product
        if product_id:
            start = time.time()
            data = check_product(product_id)
            end = time.time()
            response_time = end - start
            print("Response time:", response_time)

            if data:
                result = "✅ Genuine Product (Verified in Database)"
            else:
                result = "❌ Warning: This product may be counterfeit"

    return render_template('index.html', result=result)


# ✅ Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)