
import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Ứng dụng CI/CD Python + Docker" in response.get_data(
        as_text=True
    )


def test_health_status(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "service": "cicd-python-demo",
    }


def test_greeting_with_name(client):
    response = client.get("/api/greeting?name=An")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Xin chào, An!"
    }


def test_greeting_without_name(client):
    response = client.get("/api/greeting")

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Xin chào, bạn!"
    }


def test_greeting_with_vietnamese_name(client):
    response = client.get(
        "/api/greeting",
        query_string={"name": "Nguyễn Văn A"},
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Xin chào, Nguyễn Văn A!"
    }
