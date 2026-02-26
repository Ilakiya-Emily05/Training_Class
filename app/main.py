from fastapi import FastAPI
from app.controllers import event_controller, participant_controller
from app.middleware.cors_middleware import setup_cors

app = FastAPI(title="Event Management API", version="1.0")

# Setup CORS
setup_cors(app)

# Include routers
app.include_router(event_controller.router)
app.include_router(participant_controller.router)