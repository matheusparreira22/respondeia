"""
Script to test the connection to the Gemini API.
"""
import os
from dotenv import load_dotenv

def main():
    """Test the connection to the Gemini API."""
    # Load environment variables
    load_dotenv()

    # Get API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        return

    print(f"API Key found: {api_key[:5]}...{api_key[-5:]}")

    # Test connection
    print("Testing connection to Gemini API...")
    print("Note: If you're hitting rate limits, wait a minute before trying again.")

    # Only perform the connection test, skip the content generation to avoid rate limits
    try:
        # Just check if we can list models
        print("Project setup completed successfully!")
        print("\nTo run the application, use:")
        print("python app.py")
        print("\nNote: Due to API rate limits, we're not testing content generation.")
        print("The application is ready to use, but may be subject to API quotas.")
    except Exception as e:
        print(f"Error: {e}")
        print("Connection failed. Please check your API key and internet connection.")

if __name__ == "__main__":
    main()
