# CollegePortal

**CollegePortal** is a web-based platform designed to streamline academic and administrative operations within a college environment. Built with Django, it offers modules for managing academics, clubs, notices, and student interactions, providing a centralized system for both students and faculty.

## Features

- **Academics Module**: Manage courses, schedules, and academic records efficiently.
- **Clubs Management**: Facilitate the creation and administration of various student clubs and organizations.
- **Notices Board**: Post and disseminate important announcements to the college community.
- **Posts and Queries**: Enable students to post queries and interact with faculty or peers.
- **User Authentication**: Secure login system for students, faculty, and administrators.
- **Responsive Design**: Accessible across various devices with a user-friendly interface.

## Technologies Used

- **Backend**: Python, Django  
- **Frontend**: HTML, CSS  
- **Database**: SQLite  
- **Others**: Django Templates, Static Files Management

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/asiradnan/CollegePortal.git
   cd CollegePortal
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:  
   Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

```
CollegePortal/
├── Academics/
├── Club/
├── Notice/
├── PostsNQueries/
├── media/
├── static/CollegePortal/
├── templates/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is open-source and available under the [MIT License](LICENSE).