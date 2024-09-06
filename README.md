# StoryBuddy

**StoryBuddy** is a Django-based web application that allows users to create and explore interactive stories with branching narratives. Authenticated users can create stories and add branches, while all users can view stories and their engagement metrics, such as view counts.

## Features

- **User Authentication**: 
  - **Signup, Login, and Logout**: Secure user authentication system with options for new users to sign up, log in, and log out.
  - **Authenticated Story Creation**: Only logged-in users can create stories and add branches.
- **Story Management**:
  - **Create Stories**: Authenticated users can create stories with titles, details, and hierarchical relationships.
  - **Add Branches**: Extend stories by adding branches to create complex, multi-layered narratives.
- **Public Viewing**:
  - **View Story Hierarchies**: Display stories in a tree-like structure.
  - **View Counts**: All users can see the number of views each story has received, providing insights into story engagement.
- **Summary and Analytics**:
  - **View Counts Display**: Highlight the popularity of stories by showing view counts alongside each story title.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- **Python 3.x**
- **Django 3.x or later**
- **django-mptt**

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Raghib6/StoryBuddy.git
    cd StoryBuddy
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the application:**

    Open your browser and navigate to [http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/) to access the application.

## Usage

1. **Sign Up / Log In:**
   - Use the signup option to create an account or log in with an existing account to start creating stories.

2. **Create and Manage Stories:**
   - Navigate to the "Create Story" section to start a new story.
   - Use the "Add Branch" feature to expand your story with sub-stories.

3. **View Stories and Analytics:**
   - All users can view stories in a tree-like structure and see the total views for each story, providing insights into which stories are most popular.

4. **Authentication Options:**
   - Use the navigation links to log out of your account when done.

## Project Structure

```
StoryBuddy/                 # Root directory of the project
├── StoryProject/             # Main Django project folder
├── templates/                # Directory for HTML templates
├── story_app/                # Main application directory for managing stories
├── env/                      # Virtual environment directory
├── db.sqlite3                # SQLite database file
├── manage.py                 # Django management script
├── README.md                 # Project README file
├── requirements.txt          # List of project dependencies
```