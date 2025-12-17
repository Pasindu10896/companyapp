import sqlite3

# Connect or create database
conn = sqlite3.connect('inspection.db')
c = conn.cursor()

# Create the table if it doesn’t exist
c.execute('''
CREATE TABLE IF NOT EXISTS inspections (
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

)
''')

conn.commit()
conn.close()
print("✅ Database and 'inspections' table initialized successfully!")
