import sqlite3

def create_db():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS chats (
            user TEXT,
            bot TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def save_chat(user, bot):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    
    c.execute("INSERT INTO chats VALUES (?, ?)", (user, bot))
    
    conn.commit()
    conn.close()