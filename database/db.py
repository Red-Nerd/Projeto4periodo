import sqlite3

def save_profile(data):
    conn = sqlite3.connect('user_profiles.db')
    cursor = conn.cursor()

    # Create the users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL
        )
    ''')


    # Insert the user profile data
    cursor.execute('INSERT INTO users (name, email, age, gender) VALUES (?, ?, ?, ?)', 
                   (data['name'], data['email'], data['age'], data['gender']))


    conn.commit()
    conn.close()
