# Number Classification API

This is a FastAPI-based API that classifies and provides detailed information about numbers. It allows users to query a number and receive various properties such as whether it's prime, perfect, Armstrong, and more.

## Features

- Classify a number as `alphabet` (if input is alphabetic) or `invalid` (if input contains non-numeric characters).
- Determine whether the number is a prime number, perfect number, or Armstrong number.
- Return the sum of the digits of the number.
- Identify whether the number is odd or even.
- Handle negative numbers and append "negative" to properties if necessary.
- Provide a fun fact about the number using [Numbers API](http://numbersapi.com).

## Endpoints

### `GET /api/classify-number`

#### Query Parameters

- `number`: The number to classify (can be a string, numeric, or alphabetic).

#### Responses

- **Success (200)**: Returns a JSON object with the classification and properties of the number.
- **Error (400)**: Returns a JSON object with an error if the number is invalid or alphabetic.

#### Example Requests

1. **Valid Number:**

   ```bash
   curl -X GET "http://127.0.0.1:8000/api/classify-number?number=371" | jq
   ```

   **Response:**

   ```json
   {
     "number": 371,
     "is_prime": false,
     "is_perfect": false,
     "properties": ["armstrong", "odd"],
     "digit_sum": 11,
     "fun_fact": "371 is an Armstrong number."
   }
   ```

2. **Alphabetic Input:**

   ```bash
   curl -X GET "http://127.0.0.1:8000/api/classify-number?number=abc" | jq
   ```

   **Response:**

   ```json
   {
     "number": "alphabet",
     "error": true
   }
   ```

3. **Invalid Input:**

   ```bash
   curl -X GET "http://127.0.0.1:8000/api/classify-number?number=123a" | jq
   ```

   **Response:**

   ```json
   {
     "number": "invalid",
     "error": true
   }
   ```

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the FastAPI app)
- Requests (for fetching fun facts)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/number-classifier-api.git
   cd number-classifier-api
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be running at `http://127.0.0.1:8000`.

### Testing the API

You can now test the API with any of the example requests mentioned above using `curl` or a tool like Postman.

## Dependencies

- `fastapi`
- `uvicorn`
- `requests`
