from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('inspection.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS inspections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        method TEXT,
        material TEXT,
        batch_no TEXT,
        received_qty INTEGER,
        inspection_level TEXT,
        aql REAL,
        sample_size INTEGER,
        ac TEXT,
        re TEXT,
        defects INTEGER,
        result TEXT,
        inspector TEXT,
        lab_test TEXT,
        test_type TEXT,
        attachments TEXT,
        remarks TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

# Helper function for safe value insertion
def safe(val, default, typ="text"):
    if typ == "int":
        try:
            if val is None or val == "" or val == "-":
                return default
            return int(val)
        except Exception:
            return default
    elif typ == "float":
        try:
            if val is None or val == "" or val == "-":
                return default
            return float(val)
        except Exception:
            return default
    else:  # text
        return val if val not in (None, "-", "") else default

# Route: Load frontend
@app.route('/')
def index():
    return render_template('Document5.html')

# Route: Save records
@app.route('/save', methods=['POST'])
def save_record():
    data = request.get_json()
    conn = sqlite3.connect('inspection.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO inspections (
        method, material, batch_no, received_qty, inspection_level, aql,
        sample_size, ac, re, defects, result, inspector, lab_test,
        test_type, attachments, remarks
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
        safe(data.get('method'), "", "text"),
        safe(data.get('material'), "", "text"),
        safe(data.get('batch_no'), "", "text"),
        safe(data.get('received_qty'), 0, "int"),
        safe(data.get('inspection_level'), "", "text"),
        safe(data.get('aql'), 0.0, "float"),
        safe(data.get('sample_size'), 0, "int"),
        safe(data.get('ac'), "", "text"),
        safe(data.get('re'), "", "text"),
        safe(data.get('defects'), 0, "int"),
        safe(data.get('result'), "", "text"),
        safe(data.get('inspector'), "", "text"),
        safe(data.get('lab_test'), "", "text"),
        safe(data.get('test_type'), "", "text"),
        safe(data.get('attachments'), "", "text"),
        safe(data.get('remarks'), "", "text")
    ))
    conn.commit()
    conn.close()
    return jsonify({"message": "Record saved successfully!"})

# Route: Fetch records
@app.route('/records', methods=['GET'])
def get_records():
    conn = sqlite3.connect('inspection.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inspections")
    records = cursor.fetchall()
    conn.close()
    return jsonify(records)

if __name__ == '__main__':
    app.run(debug=True)