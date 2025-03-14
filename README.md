baseball_dashboard/        # Root project folder
│── backend/               # Django backend
│   ├── backend/           # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   ├── asgi.py
│   │   ├── __init__.py
│   ├── schedule/          # Django app for scheduling
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── serializers.py
│   │   ├── admin.py
│   │   ├── __init__.py
│   │   ├── migrations/
│   ├── manage.py
│── frontend/              # React frontend
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Different pages (Schedule, Stats, News)
│   │   ├── App.js
│   │   ├── index.js
│   ├── public/
│   ├── package.json
│── venv/                  # Python virtual environment
│── .gitignore
│── README.md


Steps to Build This Project

Phase 1: Django Backend
Set up Django & Django REST Framework

Create a virtual environment, install Django, start the backend.
Create the schedule app

Define models for storing baseball schedules.
Create a serializer to convert data into JSON format.
Set up views and URL routes to expose the schedule via API.
Set up a simple API to return the schedule

Use Django REST Framework to serve schedule data.
Test API with Postman or Django’s browsable API

Phase 2: React Frontend
Initialize React in the frontend/ folder

npx create-react-app frontend
cd frontend
npm start
Set up React Router for different pages (Schedule, Stats, News)

Fetch schedule data from Django API and display it in a table

Create UI components for schedule, stats, and news

Phase 3: Enhancements
Style the dashboard for a clean UI (CSS or TailwindCSS)
Integrate a baseball API for live scores and player stats
Optionally, add user authentication if needed
Package the project for deployment (local or cloud hosting)

**WISHLIST**
- Add border to spring training cells
- Strike out or somehow indicate games that have already been played
- Start with basic public API use of displaying previous game scores in table
