from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    qr = False

    if request.method == "POST":
        link = request.form["link"]

        img = qrcode.make(link)
        img.save("static/imagem.png")

        qr = True

    return render_template("index.html", qr=qr)

if __name__ == "__main__":
    app.run(debug=True)
