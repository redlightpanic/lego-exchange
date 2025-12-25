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
            <!-- Bootstrap CSS -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
            <!-- CSS propi -->
            <link rel="stylesheet" type="text/css" href="/static/style.css">
        </head>
        <body class="bg-light text-center">
            <div class="container py-5">
                <h1 class="mb-5 display-4">LEGO Exchange</h1>
                <div class="row justify-content-center g-4">
                    <div class="col-md-3">
                        <div class="card lego-card">
                            <div class="card-body d-flex align-items-center justify-content-center">
                                <a href="/add-family" class="stretched-link">Afegir família</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card lego-card">
                            <div class="card-body d-flex align-items-center justify-content-center">
                                <a href="/configure-family" class="stretched-link">Configurar família</a>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="card lego-card">
                            <div class="card-body d-flex align-items-center justify-content-center">
                                <a href="/request-swap" class="stretched-link">Demanar intercanvi</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </body>
    </html>
    """
    return html
