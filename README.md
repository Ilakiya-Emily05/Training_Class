# Event Management System API (V1.0)

## Overview
Backend API for managing events and participants.

### Features
- Create events
- List events
- Get event by ID
- Filter events by location
- Register participants
- Fetch participant details

### Architecture
- Clean Architecture (Controller → Service → Repository → In-Memory Storage)
- Each layer has single responsibility
- No real database (in-memory storage)

### Requirements
- Python 3.12+
- FastAPI
- Uvicorn
- Pydantic
- python-dotenv
