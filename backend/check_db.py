import sqlite3

conn = sqlite3.connect("../scan_results.db")
cursor = conn.cursor()

# Print all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Print schema if scan_results exists
if ('scan_results',) in tables:
    cursor.execute("PRAGMA table_info(scan_results);")
    columns = cursor.fetchall()
    print("\nscan_results schema:")
    for col in columns:
        print(col)
else:
    print("\n❌ scan_results table not found.")

conn.close()
