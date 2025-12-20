# LEGO Exchange

A minimal web application for **temporary LEGO set swaps** between families at a school.

## Overview

This app allows families in a school community to:

- List LEGO sets they own  
- Propose temporary swaps with other families  
- Set start and return dates for exchanges  

It’s designed for **simplicity, low cost, and ease of use**. No login is required; families interact directly using their names.

Built with **FastAPI** and **SQLite**, making it easy to deploy on free hosting platforms like Render.

---

## Project Structure

```
lego-exchange/
├── main.py           # FastAPI server
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## Installation (Local)

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/lego-exchange.git
cd lego-exchange
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
uvicorn main:app --reload
```

5. Open your browser and go to:  
```
http://127.0.0.1:8000
```

You should see a simple “Server running 🚀” message.

---

## Deployment on Render

1. Push your code to **GitHub**.
2. Go to **[Render.com](https://render.com)** and create a **New Web Service**.
3. Connect your GitHub repository.
4. Configure:
   - **Build Command:** `pip install -r requirements.txt`  
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 10000`  
   - **Plan:** Free
5. Deploy. Render will provide a public URL (e.g., `https://lego-exchange.onrender.com`).

Optional: the school can create a **subdomain** (e.g., `lego.schoolname.edu`) pointing to this URL via CNAME.

---

## Next Steps

- Add **SQLite database** for families, sets, and exchanges  
- Implement **CRUD** operations for sets and exchanges  
- Create **HTML templates** for browsing and proposing exchanges  
- Add **return date logic** for temporary swaps  

---

## License

MIT License – free to use for **school communities**.
