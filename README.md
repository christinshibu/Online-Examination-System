# Online Exam System

A Django-based web application for conducting online examinations with student verification and admin management.

## Features

- **Student Registration**: Students can register with personal details and upload ID card images for verification.
- **Admin Approval System**: Student accounts require admin approval before they can access exams.
- **Multiple-Choice Exams**: Exams consist of multiple-choice questions with automatic scoring.
- **Result Tracking**: Students can view their exam results, scores, and pass/fail status.
- **CSV Question Upload**: Admins can upload questions in bulk via CSV files.
- **Dashboard**: Students have a dashboard to view their profile and exam history.
- **Profile Management**: Students can edit their profiles and update ID cards.

## Installation

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd online-exam-system
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```
   pip install django
   ```

4. **Navigate to the project directory**:
   ```
   cd exam_project
   ```

5. **Run database migrations**:
   ```
   python manage.py migrate
   ```

6. **Create a superuser (admin account)**:
   ```
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```
   python manage.py runserver
   ```

8. **Access the application**:
   Open your browser and go to `http://localhost:8000`.

## Usage

- **Student Registration**: Visit the registration page, fill in details, and upload front and back ID card images.
- **Admin Approval**: Admins log in to the Django admin panel (`/admin/`) to approve student accounts.
- **Taking Exams**: Approved students can log in and take exams from their dashboard.
- **Uploading Questions**: Admins can upload CSV files containing questions through the upload interface.
- **Viewing Results**: Students can view their exam results on the dashboard.

## CSV Format for Questions

The CSV file for uploading questions should have the following columns (no header row):
- Question text
- Option 1
- Option 2
- Option 3
- Option 4
- Correct answer (must match one of the options exactly)

Example:
```
What is 2+2?,4,3,5,6,4
What is the capital of France?,Paris,London,Berlin,Madrid,Paris
```

## Requirements

- Python 3.8+
- Django 6.0

## Project Structure

- `exam_project/`: Main Django project directory
  - `settings.py`: Project settings
  - `urls.py`: URL configurations
- `core/`: Main application
  - `models.py`: Database models (Question, Result, StudentProfile)
  - `views.py`: View functions for handling requests
  - `templates/`: HTML templates
  - `static/`: Static files (images, CSS, JS)
- `media/`: Uploaded media files (ID cards)
- `db.sqlite3`: SQLite database file

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make your changes and test them.
4. Submit a pull request.

## License

This project is licensed under the MIT License.
<img width="1919" height="880" alt="Image1" src="https://github.com/user-attachments/assets/eab47c7f-6891-4ea2-935b-fcd108d9d172" />
<img width="1918" height="902" alt="Image2" src="https://github.com/user-attachments/assets/30d345e7-616a-4154-9243-90912b3439b7" />
<img width="1918" height="901" alt="Image3" src="https://github.com/user-attachments/assets/be950736-aeab-4a54-8b10-2dd5a4c7ab1e" />
<img width="1906" height="897" alt="Image4" src="https://github.com/user-attachments/assets/c21a2a48-c352-42e2-8f1b-ac375262024d" />
<img width="1896" height="904" alt="Image5" src="https://github.com/user-attachments/assets/7c0856d7-dafb-4df4-9948-b0bbd20c133c" />




