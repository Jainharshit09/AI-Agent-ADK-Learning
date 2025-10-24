from google.adk.agents import Agent
from google.adk.tools import FunctionTool

def weather_tool(location:str)->dict:
    """Fetches the current weather for a given location.
    Args:
        location (str): The location to fetch the weather for.
    Returns:
        dict: A dictionary containing the weather information or an error message.
    """
    if location.lower() == "new york":
        return {"location": "New York", "temperature": "15°C", "condition": "Cloudy"}
    elif location.lower() == "san francisco":
        return {"location": "San Francisco", "temperature": "18°C", "condition": "Sunny"}
    else:
        return {"error": f"Weather data for '{location}' is not available."}

Weather_tool=FunctionTool(func=weather_tool);
    
def book_flight_tool(src:str, destination:str,date:str)->dict:
    """ Books a flight from source to destination on a given date.
    Args:
        src (str): The source location.
        destination (str): The destination location.
        date (str): The date of the flight in 'YYYY-MM-DD' format.
    Returns:
        dict: A dictionary containing the booking confirmation or an error message.
    """
    if src.lower() == "new york" and destination.lower() == "san francisco":
        return {"confirmation": f"Flight booked from {src} to {destination} on {date}.", "flight_number": "NY123SF"}
    else:
        return {"error": f"No flights available from '{src}' to '{destination}' on {date}."}

Book_flight_tool=FunctionTool(func=book_flight_tool);

def trip_planner(src:str,destination:str,departure_date:str)->dict:
    """Plans a trip by booking a flight and fetching weather information.
    Args:
        src (str): The source location.
        destination (str): The destination location.
        departure_date (str): The date of departure in 'YYYY-MM-DD' format.
    Returns:
        dict: A dictionary containing the trip details or an error message.
    """
    weather_info = weather_tool(destination)
    if "error" in weather_info:
        return weather_info
    
    flight_info = book_flight_tool(src, destination, departure_date)
    if "error" in flight_info:
        return flight_info
    
    return {
        "trip_summary": f"Weekend trip to  `src` to `destination` planned successfully!",
        "flight_info": flight_info,
        "weather_info": weather_info
    }
Trip_planner_tool=FunctionTool(func=trip_planner);
root_agent=Agent(
    name="trip_tool",
    model="gemini-2.0-flash",
    description="Trip planning agent",
    instruction="""You are a helpful assistant that helps users plan their trips using the `weather_tool` and `book_flight_tool`.
        **When the user provides a location, use the `weather_tool` to fetch the current weather for that location.**
        **When the user provides source, destination, and date, use the `book_flight_tool` to book a flight.**
        **If the tool returns an error, inform the user about it.**""",
    tools=[Weather_tool,Book_flight_tool,Trip_planner_tool]
)
