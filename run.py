from flask import Flask
from app import app

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    # Start the combined application
    run_simple('localhost', 5000, application, use_reloader=True, use_debugger=True)
