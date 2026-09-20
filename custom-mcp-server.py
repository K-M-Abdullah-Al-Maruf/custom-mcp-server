from fastmcp import FastMCP

mcp = FastMCP("Deployed Tools Server")

@mcp.tool
def bmi_calculator(weight_kg: float, height_m: float) -> str:
    """
    Calculate BMI (Body Mass Index) from weight in kilograms and height in meters.
 
    Args:
        weight_kg: Weight in kilograms
        height_m: Height in meters, e.g. 1.75
    """
    if weight_kg <= 0 or height_m <= 0:
        return "weight_kg and height_m must both be positive numbers."
 
    bmi = weight_kg / (height_m ** 2)
 
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
 
    return f"BMI: {round(bmi, 1)} ({category})"
 
 
if __name__ == "__main__":
    mcp.run(transport="stdio")
