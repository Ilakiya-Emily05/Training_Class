import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database.session import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.base import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_leave.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_apply_and_approve_leave():
    # Create employee
    client.post("/auth/register", json={
        "name": "Employee",
        "email": "emp@example.com",
        "password": "password123",
        "role": "EMPLOYEE"
    })
    # Login
    login = client.post("/auth/login", data={"username": "emp@example.com", "password": "password123"})
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Apply leave
    response = client.post("/employee/leaves", json={
        "start_date": "2026-03-01",
        "end_date": "2026-03-03",
        "reason": "Vacation"
    }, headers=headers)
    assert response.status_code == 200
    leave_id = response.json()["id"]
    assert response.json()["status"] == "PENDING"

    # Approve leave (simulate admin)
    client.post("/auth/register", json={
        "name": "Admin",
        "email": "admin@example.com",
        "password": "password123",
        "role": "ADMIN"
    })
    login_admin = client.post("/auth/login", data={"username": "admin@example.com", "password": "password123"})
    admin_token = login_admin.json()["access_token"]
    admin_headers = {"Authorization": f"Bearer {admin_token}"}

    approve_resp = client.patch(f"/manager/leaves/{leave_id}", json={"status": "APPROVED"}, headers=admin_headers)
    assert approve_resp.status_code == 200
    assert approve_resp.json()["status"] == "APPROVED"