# api/index.py
import sys
import os

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the Flask app from app.py
from app import app as application

# Vercel looks for a variable named 'app' (or 'handler') by default
# We'll just alias it
app = application
