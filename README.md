# SoloDungeon

SoloDungeon is a D&D inspired game where you can create your own character, explore dungeons, and engage in thrilling combats. This project is structured into backend, frontend, database, enhancements, testing, and documentation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Node.js and npm
- AWS account with DynamoDB

### Installation

1. Clone the repository
```bash
git clone https://github.com/username/SoloDungeon.git
```

2. Install Python dependencies
```bash
pip install -r requirements.txt
```

3. Install JavaScript dependencies
```bash
cd frontend
npm install
```

4. Set up your AWS credentials for DynamoDB access in `database/dynamodb_config.py`

5. Run the Flask server
```bash
python backend/app.py
```

6. In a new terminal window, start the React app
```bash
cd frontend
npm start
```

## Project Structure

- `backend/`: Contains the Python code for the Flask server, game mechanics, and API endpoints.
- `database/`: Contains the Python code for DynamoDB configuration, schema design, and CRUD operations.
- `frontend/`: Contains the React code for the user interface.
- `enhancements/`: Contains the Python code for advanced features and improvements.
- `tests/`: Contains the Python and JavaScript code for unit and integration tests.
- `docs/`: Contains the Python and Markdown files for code and project documentation.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- Dungeons & Dragons for the inspiration and game mechanics.
- Flask and React for the robust web development frameworks.
- AWS DynamoDB for the scalable and reliable database service.