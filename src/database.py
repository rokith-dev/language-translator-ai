import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="translator_db"
    )


def save_translation(input_text, language, translated_text):
    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO translations
    (input_text, language, translated_text)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (input_text, language, translated_text)
    )

    conn.commit()
    conn.close()

def get_history():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        input_text,
        language,
        translated_text,
        created_at
    FROM translations
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data