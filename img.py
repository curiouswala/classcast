from flask import send_file
from flask import Flask
from PIL import ImageGrab

app = Flask(__name__)

@app.route("/")
def get_image():
	ImageGrab.grab().save("x.jpg", "JPEG")
	return send_file("x.jpg", mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)