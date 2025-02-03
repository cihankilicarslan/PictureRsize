from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import cv2  # OpenCV library for image processing
import os  # For file path operations

# Initialize the Flask application
app = Flask(__name__)

# Folder where uploaded images will be stored
UPLOAD_FOLDER = '/Users/cihankilicarslan/PictureRsize/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home page route
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file was included in the request
        if 'file' not in request.files:
            return "No file part in the request"
        
        file = request.files['file']
        
        # If no file is selected
        if file.filename == '':
            return "No file selected"
        
        # If a valid file is selected
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)  # Save the uploaded file
            
            try:
                # Read the image using OpenCV
                img = cv2.imread(filepath)
                if img is None:
                    return "Invalid image format"
                
                # Convert image from BGR to RGB (OpenCV uses BGR by default)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
                # Get width and height values from the form (default: 300x300)
                width = int(request.form.get('width', 300))
                height = int(request.form.get('height', 300))
                
                # Resize the image
                img_resized = cv2.resize(img, (width, height))
                
                # Generate a new filename for the resized image
                resized_filename = 'resized_' + file.filename
                resized_filepath = os.path.join(app.config['UPLOAD_FOLDER'], resized_filename)
                
                # Save the resized image in RGB format (convert back to BGR for saving)
                cv2.imwrite(resized_filepath, cv2.cvtColor(img_resized, cv2.COLOR_RGB2BGR))
                
                # Redirect to the uploaded file route
                return redirect(url_for('uploaded_file', filename=resized_filename))
            
            except Exception as e:
                return f"An error occurred: {str(e)}"
    
    # For GET requests, render the HTML template with the filename if available
    filename = request.args.get('filename')
    return render_template('index.html', filename=filename)

# Route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Run the Flask app
if __name__ == '__main__':
    # Create the upload folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)  # Run the app in debug mode