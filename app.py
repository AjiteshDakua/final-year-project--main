from flask import Flask, render_template, Response, jsonify
import camera
import os


app = Flask(__name__)


@app.route("/")
def home():
    camera.reset_scan()
    return render_template("index.html")


@app.route("/scan")
def scan():
    camera.reset_scan()
    return render_template("scan.html")


@app.route("/start-scan")
def start_scan():
    camera.start_scan()  # ✅ proper start
    return jsonify({"started": True})


@app.route("/check-palm")
def check_palm():
    return jsonify({"detected": camera.palm_detected, "confidence": camera.confidence})


@app.route("/video")
def video():
    return Response(
        camera.gen_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
