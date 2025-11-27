import sqlite3

def check_database():
    conn = sqlite3.connect('parking.db')
    cursor = conn.cursor()
    
    print('Checking database tables and data...\n')
    
    # Check all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    for table in tables:
        table_name = table[0]
        print(f'=== Table: {table_name} ===')
        
        # Check table structure
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        column_info = ', '.join([f'{col[1]} ({col[2]})' for col in columns])
        print(f'Structure: {column_info}')
        
        # Check table data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        print(f'Rows: {len(rows)}')
        
        # Print first 5 rows if any
        if rows:
            print(f'First few rows:')
            for row in rows[:5]:
                print(row)
        
        print()
    
    conn.close()
    print('Database check completed!')

if __name__ == '__main__':
    check_database()