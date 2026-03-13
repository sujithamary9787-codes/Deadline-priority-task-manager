# Deadline-priority-task-manager
Smart Task Manager is a simple web-based task management system developed using Python and Flask. The application allows users to add tasks with deadlines and automatically determines the priority level based on the remaining time. The project demonstrates backend development, database integration, and basic task management functionality.

## Features

- Add tasks with deadlines
- Automatic priority assignment (High, Medium, Low)
- View all tasks in a structured table
- Delete tasks
- Lightweight SQLite database

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript

## Project Structure

Smart_Task_Manager

app.py  
tasks_database.db  

templates  
 index.html  

static  
 style.css  
 script.js  

## Priority Logic

High Priority – Deadline is today or overdue  
Medium Priority – Deadline within 3 days  
Low Priority – Deadline more than 3 days away

## How to Run the Project

1. Install Flask

pip install flask

2. Run the application

python app.py

3. Open browser

http://127.0.0.1:5000

## Future Improvements

- User authentication system
- Task completion status
- Dashboard with analytics
- Email notifications for deadlines

## Author

Developed as a learning project to demonstrate full stack web development using Flask.
