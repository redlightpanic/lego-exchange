from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serveix la carpeta static a /static
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <html>
        <head>
            <title>LEGO Exchange</title>
            <link rel="stylesheet" type="text/css" href="/static/style.css">
        </head>
        <body>
            <h1>LEGO Exchange</h1>
            <div class="container">
                <div class="box"><a href="/add-family">Afegir família</a></div>
                <div class="box"><a href="/configure-family">Configurar família</a></div>
                <div class="box"><a href="/request-swap">Demanar intercanvi</a></div>
            </div>
        </body>
    </html>
    """
    return html

# ---------- Placeholder routes ----------

@app.get("/add-family", response_class=HTMLResponse)
def add_family():
    return "<h2>Pàgina per afegir família (en construcció)</h2>"

@app.get("/configure-family", response_class=HTMLResponse)
def configure_family():
    return "<h2>Pàgina per configurar família (en construcció)</h2>"

@app.get("/request-swap", response_class=HTMLResponse)
def request_swap():
    return "<h2>Pàgina per demanar intercanvi (en construcció)</h2>"
