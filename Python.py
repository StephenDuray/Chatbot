import requests

# Replace 'YOUR_API_KEY' with your actual Google Places API key
API_KEY = 'Phillipines'
BASE_URL = 'https://maps.googleapis.com/maps/api/place/textsearch/json'

# Function to get tourist spots from Google Places API
def get_tourist_spots(location):
    params = {
        'query': f"tourist spots in {location}, Philippines",
        'key': API_KEY
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        
        # Print the raw JSON response for debugging
        print("Debug - Raw JSON response:", response.json())
        
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            if results:
                return [result['name'] for result in results[:5]]  # Return top 5 spots
            else:
                # Handle case where no results were found
                return ["No tourist spots found."]
        else:
            # Handle HTTP request errors
            return [f"Error fetching data: {data.get('error_message', 'Unknown error')}"]
    except Exception as e:
        return [f"An exception occurred: {str(e)}"]

# Simple chatbot function
def chatbot():
    print("Welcome to the Philippine Tourism Chatbot!")
    print("Ask me about popular tourist spots in different cities or provinces in the Philippines.")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Chatbot: Thank you for chatting! Enjoy exploring the Philippines!")
            break
        else:
            # Call the API function to get tourist spots
            spots = get_tourist_spots(user_input)
            response = f"Popular tourist spots in {user_input}:\n" + "\n".join(spots)
        
        print("Chatbot:", response)

# Directly calling the chatbot function
chatbot()