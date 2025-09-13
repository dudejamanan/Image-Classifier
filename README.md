🖼️ Image Classifier using Deep Learning

A simple Image Classification Web App built with Deep Learning (CNNs) on the CIFAR-10 dataset.
Users can upload an image (or drag & drop), and the trained model will predict the class (e.g., cat 🐱, airplane ✈️, ship 🚢, etc.).

live app: https://image-classifier-2c80.onrender.com/



📸 Dataset

The project uses the CIFAR-10 dataset:

60,000 images (32x32 pixels, RGB)

10 classes:

✈️ Airplane
🚗 Automobile
🐦 Bird
🐱 Cat
🦌 Deer
🐶 Dog
🐸 Frog
🐎 Horse
🚢 Ship
🚚 Truck



🔧 Tech Stack

Deep Learning: TensorFlow/Keras

Model: Convolutional Neural Network (Conv2D, MaxPooling, Dropout, BatchNorm)

Backend: Flask

Frontend: HTML/CSS (basic, vibe coded 😅)

Deployment: Render



📚 Features

✅ Train a CNN on CIFAR-10 dataset

✅ Save and load the trained model (.h5)

✅ Upload/drag-drop custom images for prediction

✅ Display predicted class on the web app

✅ Deployed online for public use




📊 Model Performance


Achieved ~70% accuracy on CIFAR-10 test set

Improvements came from:

Adding Batch Normalization

Using Dropout layers to reduce overfitting

Tuning learning rate & optimizer




⚡ Challenges Faced


Handling RGBA vs RGB input mismatch

Accuracy plateau before tuning hyperparameters

Connecting ML model with Flask for live predictions



🌟 Future Improvements


Improve accuracy with data augmentation & deeper CNNs

Add Top-3 predictions with probabilities

UI improvements (drag-drop zone, better styling)

Support for more datasets



🤝 Contributing

Pull requests are welcome! If you’d like to suggest improvements, feel free to open an issue.

