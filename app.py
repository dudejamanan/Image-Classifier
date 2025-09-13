# Updated app.py (small changes for deployment)
from flask import Flask, render_template, request, redirect
import tensorflow as tf
import numpy as np
import os
from werkzeug.utils import secure_filename
from PIL import Image

# Initialize Flask app
app = Flask(__name__)

# Create static directory if it doesn't exist
os.makedirs('static', exist_ok=True)

# Load trained model
model = tf.keras.models.load_model("model/cifar_model.h5")

# CIFAR-10 class names
class_names = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

def preprocess_image(file):
    # Open image with PIL
    img = Image.open(file)

    # Convert RGBA → RGB (remove alpha channel if present)
    img = img.convert("RGB")

    # Resize to CIFAR-10 input size
    img = img.resize((32, 32))

    # Convert to numpy array
    img_array = np.array(img)

    # Normalize (same as training step)
    img_array = img_array.astype("float32") / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        # Save uploaded file
        filepath = os.path.join("static", secure_filename(file.filename))
        file.save(filepath)

        # Preprocess and predict
        img = preprocess_image(filepath)
        predictions = model.predict(img)
        predicted_label = class_names[np.argmax(predictions)]

        return render_template("index.html", 
                               prediction=predicted_label, 
                               filename=filepath)
    return render_template("index.html")

if __name__ == "__main__":
    # Use environment port for deployment, default to 5000 for local
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)