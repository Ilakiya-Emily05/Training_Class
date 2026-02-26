# LMS – Learning Management System (Course Enrollment Platform)

## Project Overview
This backend system manages Courses, Students, and Enrollments for an EdTech platform (similar to Udemy or Coursera).  
Built using **FastAPI** and following **Clean Architecture principles**.

## Features
- **Course Management**
  - Create courses
  - List all courses
  - View course details
- **Student Management**
  - Register new students
  - View student profiles
- **Enrollment Management**
  - Enroll students in courses
  - Prevent duplicate enrollments
  - List enrollments by student or course

## Architecture
- **Controller Layer** – Handles API requests
- **Service Layer** – Business logic & validations
- **Repository Layer** – Data access (in-memory v1.0)
- **Schema Layer** – Pydantic models for validation
- **Core** – Global configuration & database initialization
- **Middleware** – Cross-cutting concerns (e.g., CORS)
- **Dependencies** – Dependency injection for services & repositories