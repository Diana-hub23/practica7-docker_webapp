from flask import Flask
from database import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
        dbname = result[0]

        return f"""
        <html>
        <head>
            <title>Docker Web App</title>
            <style>
                body {{
                    margin: 0;
                    font-family: 'Segoe UI', Tahoma, sans-serif;
                    background: linear-gradient(135deg, #4f83ff, #6dd5fa, #ffffff);
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    color: #333;
                }}
                .container {{
                    background: white;
                    padding: 40px;
                    width: 420px;
                    border-radius: 18px;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
                    text-align: center;
                }}
                h1 {{
                    margin-bottom: 10px;
                    font-size: 28px;
                    color: #2a2a2a;
                }}
                p {{
                    font-size: 18px;
                }}
                .status {{
                    margin-top: 20px;
                    text-align: left;
                    font-size: 17px;
                    line-height: 1.7;
                }}
                .ok {{
                    color: #28a745;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>HOLA MUNDO 🚀 Web App en Docker</h1>
                <p>Flask + MySQL funcionando correctamente</p>

                <div class="status">
                    <p>✔ <span class="ok">Conexión establecida</span></p>
                    <p>✔ Base de datos: <strong>{dbname}</strong></p>
                    <p>✔ Backend corriendo en <strong>Docker</strong></p>
                    <p>✔ Servicio MySQL activo</p>
                </div>
            </div>
        </body>
        </html>
        """
    except Exception as e:
        return f"""
        <h1 style='color:red;'>Error conectando a MySQL</h1>
        <p>{e}</p>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

