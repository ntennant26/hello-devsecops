"""Minimal "hello, world!" web app used to demonstrate a DevSecOps CI/CD pipeline."""
from flask import Flask

app = Flask(__name__)


def greet(name: str = "world") -> str:
    """Return a greeting. Kept as a pure function so it is easy to unit test."""
    return f"hello, {name}!"


@app.route("/")
def index():
    return greet()


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    # Bind to localhost by default; the container uses gunicorn instead.
    app.run(host="127.0.0.1", port=8080)
