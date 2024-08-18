# CSV Generator Django Project

## Overview

This project is a web application built with Django and Django REST Framework. It provides a simple user interface that allows users to generate CSV files based on their input. Users can specify column names, types, and the number of records they want in the CSV file. Once the form is submitted, a CSV file is dynamically generated and made available for download.

## Features

- **User Interface:** A web form for inputting column names, types, and the number of records.
- **CSV Generation:** Dynamically generates a CSV file based on user input.
- **File Download:** Provides a direct link for users to download the generated CSV file.

## Technologies Used

- **Django:** A high-level Python web framework that simplifies the development of web applications.
- **Django REST Framework:** A powerful toolkit for building Web APIs.
- **Pandas:** A data analysis library used for creating and manipulating data frames.
- **HTML/JavaScript:** For creating the user interface and handling form submissions.

## Project Setup

### Prerequisites

Ensure you have the following installed:

- Python (>= 3.6)
- pip (Python package installer)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

4. **Create a Requirements File (Optional):**

   ```bash
   pip freeze > requirements.txt

5. **Apply Database Migrations:**

   ```bash
   python manage.py migrate

6. **Run the Development Server:**

   ```bash
   python manage.py runserver

## Project Structure

- **`csvgenerator/`**: The Django project directory.
  - **`settings.py`**: Configuration settings for the Django project.
  - **`urls.py`**: URL declarations for the project.

- **`generator/`**: The Django application directory.
  - **`views.py`**: Contains views for rendering the form and handling CSV generation.
  - **`serializers.py`**: Contains serializers for validating and processing incoming data.
  - **`urls.py`**: URL declarations for the app.
  - **`templates/generator/index.html`**: HTML template for the user interface.

## API Endpoints

- **`POST /api/generate/`**: Generates a CSV file based on the provided columns and number of records.

  **Request Body:**
  ```json
  {
      "columns": [
          {"name": "column_name", "dtype": "int"},
          {"name": "another_column", "dtype": "float"}
      ],
      "num_records": 100
  }


### Explanation:

- **Project Structure:** Lists the directory structure and the purpose of key files.
- **API Endpoints:** Details the endpoint for generating CSV files, including request and response formats.
- **HTML Form Details:** Describes how the form works, including how to add columns and generate the CSV file.
- **Troubleshooting:** Offers tips for resolving common issues.
- **License:** Information about the project's license.
- **Contributing:** Instructions for contributing to the project.
