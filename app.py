# This server provides a single "joke" tool.

# To run this server:
# 1. Ensure you have Python installed.
# 2. Install Flask: pip install Flask
# 3. Save this code as `app.py`.
# 4. Run the server from your terminal: python app.py

# This server will start on http://127.0.0.1:5000.
# You will need to host this server publicly to submit it to the hackathon.

from flask import Flask, request, jsonify

# Create the Flask application instance.
app = Flask(__name__)

# A simple list of jokes to be used by our "tool".
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Did you hear about the restaurant on the moon? Great food, no atmosphere!",
]

# This is the main "tool" endpoint that Puch AI will call.
# It expects a POST request and will return a random joke.
@app.route('/tool_code', methods=['POST'])
def tool_endpoint():
    """
    Handles requests to the tool endpoint.
    
    This function will be triggered by a POST request. It will
    select a random joke from the JOKES list and return it in a 
    JSON response.
    """
    # Import the random library inside the function scope to ensure it's
    # available for this specific endpoint.
    import random

    try:
        # For a more complex tool, you would process the user's prompt
        # from request.json.get('prompt') here.
        # For now, we will simply ignore the prompt and generate a joke.
        # prompt = request.json.get('prompt')

        # Select a random joke from our list.
        joke = random.choice(JOKES)

        # Return a JSON response with the result of our tool.
        # The structure of this response may need to be adjusted based on
        # the official hackathon documentation.
        response = {
            "result": joke,
            "success": True,
            "tool_name": "joke-generator"
        }
        return jsonify(response), 200
    except Exception as e:
        # Handle any errors gracefully and return an error message.
        error_response = {
            "error": str(e),
            "success": False
        }
        return jsonify(error_response), 500

# A simple health check endpoint. This is good practice for any server.
# It allows the platform to check if your server is running.
@app.route('/', methods=['GET'])
def health_check():
    """
    A basic health check to ensure the server is running.
    
    Returns a simple "OK" message.
    """
    return jsonify({"status": "OK", "message": "MCP Server is up and running!"}), 200

# This block ensures the app only runs when the script is executed directly.
if __name__ == '__main__':
    # By default, Flask runs on port 5000.
    # The debug=True flag provides helpful error messages during development.
    app.run(debug=True, host='0.0.0.0')

