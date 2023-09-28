class TestAuthController:
    def test_user_login(self, client):
        response = client.post(
            "/login", json={"username": "admin@admin.com", "password": "123456"}
        )
        assert response.status_code == 200
        assert "token" in response.json

    def test_user_login_with_invalid_credentials(self, client):
        response = client.post(
            "/login", json={"username": "admin@admin.com", "password": "654321"}
        )
        assert response.status_code != 200
