from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
import requests
import math

# app = FastAPI()
app = FastAPI(default_response_class=ORJSONResponse)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/classify-number")
async def classify_number(number: str):
    # Check if input consists only of alphabetic characters
    if number.isalpha():
        return {"number": "alphabet", "error": True}

    # Check if input is a valid number (allows negative numbers)
    if not number.lstrip("-").isdigit():
        return {"number": "invalid", "error": True}


    num = int(number)
    abs_num = abs(num)  # Use absolute value for calculations

    # Check number properties
    is_prime = check_prime(abs_num)
    is_perfect = check_perfect(abs_num)
    is_armstrong = check_armstrong(abs_num)
    digit_sum = sum_digits(abs_num)

    # Assign properties
    properties = []
    if is_armstrong:
        properties.append("armstrong")
    properties.append("even" if abs_num % 2 == 0 else "odd")

    # Handle negative numbers
    if num < 0:
        properties.append("negative")

    # Get a fun fact
    fun_fact = get_fun_fact(abs_num)

    return {
        "number": num,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

def check_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check_perfect(n: int) -> bool:
    if n <= 0:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def check_armstrong(n: int) -> bool:
    power = len(str(n))
    return sum(int(digit) ** power for digit in str(n)) == n

def sum_digits(n: int) -> int:
    return sum(int(digit) for digit in str(n))

def get_fun_fact(n: int) -> str:
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json", timeout=3)
        return response.json().get("text", "No fun fact available.")
    except:
        return "No fun fact available."

