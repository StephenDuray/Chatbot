import requests

def get_tourist_spots(location):
    # Query for tourist attractions in the specified location
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    area["name"="{location}"]["boundary"="administrative"]->.searchArea;
    node["tourism"="attraction"](area.searchArea);
    out;
    """

    try:
        response = requests.get(overpass_url, params={'data': query})
        
        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            elements = data.get("elements", [])
            if elements:
                # Extract the name of each tourist spot
                spots = [element.get("tags", {}).get("name", "Unnamed Attraction") for element in elements[:5]]
                return spots if spots else ["No tourist spots found."]
            else:
                return ["No tourist spots found in this area."]
        else:
            return [f"Error fetching data: HTTP {response.status_code}"]
    except Exception as e:
        return [f"An exception occurred: {str(e)}"]

# Simple chatbot function
def simple_tourism_chatbot():
    print("Welcome to the Philippine Tourism Chatbot!")
    print("Ask me about popular tourist spots in different cities or provinces in the Philippines.")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Chatbot: Thank you for chatting! Enjoy exploring the Philippines!")
            break
        else:
            # Call the function to get tourist spots
            spots = get_tourist_spots(user_input)
            response = f"Popular tourist spots in {user_input}:\n" + "\n".join(spots)

        print("Chatbot:", response)

# Run the chatbot
simple_tourism_chatbot()
