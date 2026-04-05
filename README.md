# 🔍 Product Authenticity Verification System

A web-based system to detect counterfeit products using QR codes or manual product ID verification.

---

## 🚀 Features

- 🔎 Verify product authenticity using unique product ID  
- 📷 QR code scanning support (upload-based)  
- ⚡ Fast verification with near real-time response  
- 🗄️ Database with 1000+ product records  
- 🌐 Simple and user-friendly web interface  

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)  
- **Database:** SQLite  
- **QR Processing:** OpenCV, Pyzbar  
- **Frontend:** HTML, CSS  

---

## 📊 Project Highlights

- Processed **1000+ product records** for verification  
- Achieved **near real-time response performance**  
- Designed scalable architecture for future expansion  

---

## ▶️ How It Works

1. User enters product ID OR uploads QR code  
2. System extracts product ID  
3. Backend verifies against database  
4. Displays result:
   - ✅ Genuine Product  
   - ❌ Counterfeit Product  

---

## 📂 Project Structure
auth-system/
│
├── app.py
├── database.db
├── requirements.txt
├── runtime.txt
├── templates/
│ └── index.html
├── static/

---

## ⚙️ Setup Instructions

1. Clone the repository  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. python app.py
4. http://127.0.0.1:5000
5. Live Demo: https://product-auth-system.onrender.com
🌐 Future Improvements
📱 Real-time camera QR scanning
☁️ Cloud database integration
🔐 Secure and encrypted product IDs
📊 Product details display (batch, manufacturer, etc.)
