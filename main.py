from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="LEGO Exchange")

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>LEGO Exchange</title>
        </head>
        <body>
            <h1>LEGO Exchange</h1>
            <p>Server running 🚀</p>
        </body>
    </html>
    """
