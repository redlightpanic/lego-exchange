from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
import sqlite3

app = FastAPI()

DB_NAME = "data.db"


# ---------- DATABASE ----------

def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS families (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT
        )
    """)

    conn.commit()
    conn.close()


init_db()


# ---------- ROUTES ----------

@app.get("/", response_class=HTMLResponse)
def home():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email FROM families")
    families = cursor.fetchall()

    conn.close()

    html = """
    <html>
        <head>
            <title>Lego Exchange</title>
        </head>
        <body>
            <h1>Families</h1>

            <ul>
    """

    for f in families:
        html += f"<li>{f[1]} ({f[2] if f[2] else 'no email'})</li>"

    html += """
            </ul>

            <h2>Add family</h2>
            <form method="post" action="/families">
                <input type="text" name="name" placeholder="Family name" required>
                <br><br>
                <input type="email" name="email" placeholder="Email (optional)">
                <br><br>
                <button type="submit">Add</button>
            </form>
        </body>
    </html>
    """

    return html


@app.post("/families")
def add_family(name: str = Form(...), email: str = Form(None)):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO families (name, email) VALUES (?, ?)",
        (name, email)
    )

    conn.commit()
    conn.close()

    return RedirectResponse(url="/", status_code=303)
