# database.py
import sqlite3

def connect_db():
    conn = sqlite3.connect('rule_engine.db')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_string TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_rule(rule_string):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rules (rule_string) VALUES (?)", (rule_string,))
    conn.commit()
    conn.close()

def get_all_rules():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rules")
    return cursor.fetchall()
