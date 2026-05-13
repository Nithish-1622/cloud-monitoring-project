from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>AWS Monitoring Project</title>
        </head>

        <body style="font-family: Arial; text-align:center; margin-top:50px;">
            <h1>🚀 Containerized AWS Application</h1>
            <h2>Cloud Monitoring System</h2>

            <p>Docker + AWS + CloudWatch + Lambda</p>

            <h3>Status: RUNNING SUCCESSFULLY ✅</h3>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
