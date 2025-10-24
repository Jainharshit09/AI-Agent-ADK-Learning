from google.adk.agents import Agent
from google.adk.tools import FunctionTool

def Calucation_tool(operation: str, num1: float, num2: float) -> dict:
    """Performs basic arithmetic operations.

    Args:
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        dict: A dictionary containing the result of the operation or an error message.
    """
    if operation == "add":
        return {"result": num1 + num2}
    elif operation == "subtract":
        return {"result": num1 - num2}
    elif operation == "multiply":
        return {"result": num1 * num2}
    elif operation == "divide":
        if num2 != 0:
            return {"result": num1 / num2}
        else:
            return {"error": "Division by zero is not allowed."}
    else:
        return {"error": f"Unsupported operation '{operation}'. Supported operations are add, subtract, multiply, divide."}
    
calucation_tool=FunctionTool(func=Calucation_tool);


root_agent=Agent(
    name="math_tool",
    model="gemini-2.0-flash",
    description="Math agent",
    instruction="""You are a helpful assistant that performs basic arithmetic operations using the `Calucation_tool`.
        **When the user provides two numbers and specifies an operation (add, subtract, multiply, divide), use the `Calucation_tool` to perform the calculation.**
        **If the operation is successful, provide the result to the user.**""",
    tools=[calucation_tool]
)