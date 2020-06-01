from flask import Flask, jsonify
from tasks import process_image

app = Flask("DevConAPI")


@app.route("/", methods=['GET'])
def home():
    process_image.delay(data={"filename": "imaginary", "location": "some s3 bucket"})

    return jsonify({"app": "DevCon"})


if __name__ == "__main__":
    app.run(debug=True)
