from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Linux XFCE + Web VNC</h1>
    <p>Click below to access the desktop:</p>
    <a href="/vnc.html" target="_blank">Open Desktop</a>
    """

if __name__ == "__main__":
    # Run Flask on port 5000 (internal)
    app.run(host="0.0.0.0", port=5000)
