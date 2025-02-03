Image Resizer Tool
📸 A Simple and Free Tool to Resize Images Using Flask and OpenCV

Are you tired of paying for expensive software just to resize images? This lightweight Flask-based application allows you to upload and resize images quickly and easily, all from your computer. It's free, open-source, and perfect for anyone who needs a hassle-free solution.

🌟 Features
Upload and Resize: Upload any image (PNG, JPG, JPEG) and resize it to your desired dimensions.
Custom Dimensions: Specify the width and height for resizing.
Easy Setup: Quick installation with minimal dependencies.
Open Source: Fully customizable and free to use.
Cross-Platform: Works on any system with Python installed.
🛠️ Installation
Prerequisites
Python 3.x installed on your system.
Download it from python.org .
Pip (Python package manager) should be installed.
Install the required dependencies by running:

pip install flask opencv-python
Steps to Run the Application
Clone the Repository:

git clone https://github.com/cihankilicarslan/PictureRsize.git
cd image-resizer
Set Up the Upload Folder:
Ensure the uploads folder exists in the project directory. If not, create it manually or let the app create it automatically when you run the server.

mkdir uploads
Run the Flask App:
Start the Flask development server:

python app.py
Access the Application:
Open your browser and navigate to:

http://127.0.0.1:5000/
🚀 How to Use
Upload an Image:
Click the "Choose File" button to select an image from your computer.
Supported formats: PNG, JPG, JPEG.
Set Dimensions:
Enter the desired width and height for your resized image.
Resize and Download:
Click the "Upload and Resize" button.
The resized image will be displayed on the page, and you can download it from the uploads folder.
📂 Project Structure

/image-resizer
    ├── app.py                # Main Flask application file
    ├── uploads/              # Folder to store uploaded and resized images
    ├── templates/
    │   └── index.html        # HTML template for the frontend
    ├── static/
    │   └── style.css         # CSS file for styling
    └── README.md             # This file
🔧 Dependencies
Flask: Lightweight web framework for Python.
OpenCV-Python: Library for image processing.
Install all dependencies using:

pip install -r requirements.txt
🤝 Contributing
Contributions are welcome! If you find a bug or want to add a new feature, feel free to open an issue or submit a pull request. Here’s how you can contribute:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeatureName).
Commit your changes (git commit -m "Add some feature").
Push to the branch (git push origin feature/YourFeatureName).
Open a pull request.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙏 Acknowledgments
Thanks to the Flask and OpenCV communities for their amazing tools and libraries.
Inspired by the need for a simple, free, and accessible image resizing tool.
📧 Contact
If you have any questions or suggestions, feel free to reach out:

Email: cihankilicarslan06@gmail.com
GitHub: cihankilicarslan
