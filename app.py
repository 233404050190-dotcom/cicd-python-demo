from flask import Flask, jsonify, request

app = Flask(__name__)


def make_greeting(name: str) -> str:
    return f"Xin chào, {name.strip() or 'bạn'}!"


@app.get("/")
def home():
    return """<!doctype html>
<html lang="vi">
<head>
    <meta charset="utf-8">
    <title>CI/CD Python Demo</title>
</head>
<body style="font-family: Arial; max-width: 700px;
             margin: 80px auto; line-height: 1.6;">
    <h1>Ứng dụng CI/CD Python + Docker</h1>
    <p>Ứng dụng Flask đã chạy thành công trong container Docker.</p>
    <p>Kiểm tra hệ thống: <a href="/health">/health</a></p>
    <p>API thử nghiệm: <a href="/api/greeting?name=Sinh%20vien">
        /api/greeting</a></p>
</body>
</html>"""


@app.get("/health")
def health():
    return jsonify(status="ok", service="cicd-python-demo"), 200


@app.get("/api/greeting")
def greeting():
    name = request.args.get("name", "")
    return jsonify(message=make_greeting(name))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
