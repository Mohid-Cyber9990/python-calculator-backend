# Calculator Application

This is a simple calculator application that provides a backend implementation for basic arithmetic operations. The application exposes a RESTful API for performing calculations.

## Project Structure

```
calculator-app
├── backend
│   ├── __init__.py
│   ├── calculator.py
│   └── server.py
├── tests
│   └── test_calculator.py
├── requirements.txt
└── README.md
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd calculator-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the server, execute the following command:
```
python backend/server.py
```

The server will start and listen for requests.

## API Endpoints

The following endpoints are available for performing calculations:

- **Addition**
  - **Endpoint:** `/add`
  - **Method:** `POST`
  - **Request Body:** `{ "a": number, "b": number }`
  - **Response:** `{ "result": number }`

- **Subtraction**
  - **Endpoint:** `/subtract`
  - **Method:** `POST`
  - **Request Body:** `{ "a": number, "b": number }`
  - **Response:** `{ "result": number }`

- **Multiplication**
  - **Endpoint:** `/multiply`
  - **Method:** `POST`
  - **Request Body:** `{ "a": number, "b": number }`
  - **Response:** `{ "result": number }`

- **Division**
  - **Endpoint:** `/divide`
  - **Method:** `POST`
  - **Request Body:** `{ "a": number, "b": number }`
  - **Response:** `{ "result": number }`

## Running Tests

To run the unit tests for the Calculator class, use the following command:
```
python -m unittest tests/test_calculator.py
```

## License

This project is licensed under the MIT License.