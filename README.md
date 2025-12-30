# Student_Management_System
A full-featured Student Management System built with Django and SQLite. It provides secure authentication using Django’s User model, student profile management, course and subject modules, attendance tracking, and marks management. Admins manage records via the Django admin panel, following MVC best practices.

# 🎓 Student Management System (Django)

A full-featured **Student Management System** built using **Django** and **SQLite**.  
This web application helps manage students, courses, subjects, attendance, and marks with **secure authentication** and an **admin dashboard**.

---

## 🚀 Features

- Secure user authentication using Django User model  
- Student profile management  
- Course and subject management  
- Attendance tracking (Present / Absent)  
- Marks management (Internal / External exams)  
- Django Admin Panel for full control  
- Clean MVC (Models, Views, Templates) architecture  

---

## 🛠 Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS (can be extended with Bootstrap)  
- **Database:** SQLite  
- **Authentication:** Django built-in auth system  

---

## 📂 Project Structure

student_management_system/
│
├── sms/
│ ├── sms/
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ ├── students/
│ │ ├── models.py
│ │ ├── views.py
│ │ ├── admin.py
│ │ ├── forms.py
│ │ ├── urls.py
│ │ └── templates/
│ └── manage.py
│
└── db.sqlite3

