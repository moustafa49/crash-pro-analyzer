from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json.get('history', [])
        if not data: return jsonify({"error": "فارغ"}), 400
        avg = sum(data) / len(data)
        status = "مخاطرة عالية" if avg < 1.8 else "فرصة جيدة"
        return jsonify({"average": round(avg, 2), "status": status})
    except:
        return jsonify({"error": "خطأ في البيانات"}), 500
      
