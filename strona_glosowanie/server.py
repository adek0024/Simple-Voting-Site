from flask import Flask, request, send_from_directory

app = Flask(__name__)

voted_ips = set()

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/vote", methods=["POST"])
def vote():
    ip = request.remote_addr
    data = request.json
    photo_id = data["photo_id"]

    if ip in voted_ips:
        return "Już oddałeś głos!"

    voted_ips.add(ip)

    print("NOWY GŁOS")
    print("IP:", ip)
    print("Zdjęcie:", photo_id)

    return "Dziękujemy za głos!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)