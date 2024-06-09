from flask import Flask

# Create an instance of the Flask application.
app = Flask(__name__)
 
# Define a basic route.
@app.route('/')
def home():
    return 'Hello, Flask!'

# Run the application.
if __name__ == '__main__':
    app.run(debug=True)
