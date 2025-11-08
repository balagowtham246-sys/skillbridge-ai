import sqlite3
import os
import sys

# Path: backend/scripts/inspect_db.py -> analytics.db at backend/../analytics.db
script_dir = os.path.dirname(__file__)

# Try several likely locations for analytics.db:
# 1) backend/analytics.db (legacy)
# 2) project root analytics.db (current)
db_candidates = [
    os.path.abspath(os.path.join(script_dir, '..', 'analytics.db')),
    os.path.abspath(os.path.join(script_dir, '..', '..', 'analytics.db')),
]

db_path = None
for p in db_candidates:
    if os.path.exists(p):
        db_path = p
        break

if not db_path:
    print('MISSING_DB - looked for:', db_candidates)
    sys.exit(2)

conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
print('TABLES:', tables)

for t in tables:
    tname = t[0]
    print('\n--- Table:', tname, '---')
    try:
        cur.execute(f"PRAGMA table_info({tname})")
        cols = cur.fetchall()
        print('COLUMNS:')
        for c in cols:
            print('  ', c)

        cur.execute(f"SELECT * FROM {tname} LIMIT 20")
        rows = cur.fetchall()
        print('ROWS_COUNT:', len(rows))
        for r in rows:
            print('  ', r)
    except Exception as e:
        print('ERROR reading table', tname, ':', e)

conn.close()
print('\nDone.')
