from waitress import serve
from app import app
import atexit
import file.send as send
def cleanup_function():
    # Add your cleanup logic here
    print("Flask app is closing. Performing cleanup...")

    send.send_files()


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
    # Register the cleanup function to be called on app exit
    atexit.register(cleanup_function)
