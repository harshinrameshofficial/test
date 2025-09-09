# My Python App

This project is a simple AI assistant application that provides personal information, current date and time, and weather information for specified cities. The application is structured into separate modules for better organization and maintainability.

## Project Structure

```

├── tools
│   ├── personal_info.py
│   ├── date_time.py
│   └── get_weather.py
├── prompt
│   └── restrictive_prompt.txt
├── llm
│   └── model.py
├── main.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd my-python-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```
2. Interact with the AI assistant by typing your queries. You can ask for:
   - Personal information about the assistant
   - The current date and time
   - Weather information for any city

3. Type 'quit' to exit the application.

## Tools

- **personal_info.py**: Contains a function to return personal information about the AI assistant.
- **date_time.py**: Contains a function to return the current date and time.
- **get_weather.py**: Contains a function to return weather information for a specified city.

## Prompts

- **restrictive_prompt.txt**: Contains the prompt that defines the allowed behaviors and responses for the AI assistant.

## Model

- **model.py**: Contains the implementation and configuration of the AI model used for generating responses.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License. See the LICENSE file for details.
