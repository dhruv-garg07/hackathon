# A simple MCP server using Flask for the Puch AI Hackathon.
# This server provides a "joke" and a "validate" tool.

# To run this server:
# 1. Ensure you have Python and Flask installed.
# 2. Save this code as `app.py`.
# 3. Run the server from your terminal: python app.py

# This server will start on http://127.0.0.1:5000.
# You will need to host this server publicly to submit it to the hackathon.

from flask import Flask, request, jsonify

# Create the Flask application instance.
app = Flask(__name__)

# A simple list of jokes to be used by our "joke-generator" tool.
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Did you hear about the restaurant on the moon? Great food, no atmosphere!",
]

# This is the main "tool" endpoint that Puch AI will call.
# It expects a POST request and will route to the correct tool function.
@app.route('/tool_code', methods=['POST'])
def tool_endpoint():
    """
    Handles requests to the tool endpoint.
    
    This function processes the incoming JSON request, identifies the
    tool to be used, and calls the appropriate function to get a result.
    """
    import random

    # Check if the request body is valid JSON.
    if not request.is_json:
        return jsonify({"error": "Request must be JSON", "success": False}), 400

    request_data = request.get_json()
    tool_name = request_data.get('tool_name')

    if tool_name == 'joke-generator':
        # Select a random joke from our list.
        joke = random.choice(JOKES)
        response = {
            "result": joke,
            "success": True,
            "tool_name": tool_name
        }
        return jsonify(response), 200
    
    elif tool_name == 'validate':
        # The 'validate' tool returns a user's number in a specific format.
        # This is a hackathon requirement.
        # **IMPORTANT**: Replace this placeholder with your actual number.
        my_number = "+1-123-456-7890"  # Example format: {country_code}{number}
        response = {
            "result": my_number,
            "success": True,
            "tool_name": tool_name
        }
        return jsonify(response), 200
        
    else:
        # Handle cases where the requested tool is not found.
        error_response = {
            "error": f"Tool '{tool_name}' not found.",
            "success": False
        }
        return jsonify(error_response), 404

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
    # The host='0.0.0.0' is important for making the server accessible 
    # outside your local machine's localhost.
    app.run(debug=True, host='0.0.0.0')
