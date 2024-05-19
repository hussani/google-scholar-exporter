# Google Scholar Exporter

Google Scholar Exporter is a tool for extracting and processing search results from Google Scholar.

## Features

- Extract search results from Google Scholar
- Process and format results for easy use

## Requirements

- Python 3.x
- Required packages listed in `requirements.txt`

## Installation

### Using Virtualenv

1. Clone the repository:
   ```bash
   git clone https://github.com/hussani/google-scholar-exporter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd google-scholar-exporter
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the extractor script to fetch search results:
   ```bash
   python extractor.py
   ```
2. Process the results with:
   ```bash
   python process_results.py
   ```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License

This project is licensed under the MIT License.
