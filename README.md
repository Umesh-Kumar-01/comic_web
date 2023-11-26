# Comic Creator Web Application

## Objective

Developed a simple web application that allows users to create and share a 10-panel comic strip. The comic is generated by inputting text into a form, which is then sent to a text-to-image API using a provided API key.

## Key Features

### User Interface

- Designed a user-friendly UI with a form for inputting text for 10 comic panels.
- Included a display area for the generated comic panels.
- Ensured the application is responsive and functional on both desktop and mobile browsers.

### API Integration

- Used the provided API key to integrate with the text-to-image API.
- Handled API responses appropriately and display the images in their respective panels.

### Error Handling and Rate Limiting

- Implemented user feedback mechanisms for failed API calls or internal errors.

## Bonus Features Added

- Ability to add text annotations on the images.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) (version 3.x)
- [Django](https://www.djangoproject.com/download/) (version 4.x)
- [Text-to-image API Key](#API_KEY# )(which converts text to image)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/comic-creator.git
    ```
2. Change into the project directory:
    ```bash
    cd comic-creator
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

The application will be available at http://127.0.0.1:8000/.

## Usage

1. Visit http://127.0.0.1:8000/ to start creating your comic strips.
2. Input text for each of the 10 comic panels.
3. Submit the form to generate the comic strip with images.
4. Share the unique link with others.

Note: This application has been developed as part of the Dashtoon hiring process assignment.

