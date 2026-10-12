# student_project
# NearU

NearU is a student-focused local discovery platform for Indore that helps students find verified stays, food options, essentials, and nearby campus-area recommendations. The project combines a Flask backend, SQLAlchemy models, and a React + Vite frontend to provide a modern marketplace experience for students and local vendors.

## Overview

The platform lets users:

- Browse listings for stays, food, and essentials by area and category
- Search by destination, price, rating, and availability
- Filter by distance and amenities such as Wi-Fi, AC, and food inclusion
- Create an account and verify it via OTP-based email flow
- Add favorite listings and leave reviews
- View a map-based, campus-centered discovery experience
- List new places for discovery and outreach

This repository contains both the backend API and the frontend web app in a single project.

## Project Structure

```text
student_project/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── routes.py
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── frontend/
│   ├── public/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
├── .env.example
├── .gitignore
├── config.py
├── migrate_db.py
├── requirements.txt
├── run.py
├── seed_db.py
├── test_api.py
└── README.md
