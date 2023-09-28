from datetime import datetime


class TestTransactionController:
    def test_list_transactions(self, client, api_token):
        response = client.get("/transactions", headers={"Authorization": api_token})
        assert response.status_code == 200

    def test_create_transaction(self, client, api_token):
        time = datetime.now().isoformat()
        response = client.post(
            "/transactions",
            json={
                "description": "test",
                "amount": 10,
                "category": "test",
                "time": time,
            },
            headers={"Authorization": api_token},
        )
        assert response.status_code == 200
        assert response.json[0]["description"] == "test"
        assert response.json[0]["amount"] == 10
        assert response.json[0]["category"] == "test"

    def test_get_transaction(self, client, api_token):
        response = client.get("/transactions", headers={"Authorization": api_token})
        transaction_id = response.json[0]["id"]
        response = client.get(
            f"/transactions/{transaction_id}", headers={"Authorization": api_token}
        )
        assert response.status_code == 200
        assert response.json["id"] == transaction_id

    def test_update_transaction(self, client, api_token):
        response = client.get("/transactions", headers={"Authorization": api_token})
        transaction_id = response.json[0]["id"]
        response = client.put(
            f"/transactions/{transaction_id}",
            json={"description": "test2"},
            headers={"Authorization": api_token},
        )
        assert response.status_code == 200
        assert response.json["description"] == "test2"

    def test_delete_transaction(self, client, api_token):
        response = client.get("/transactions", headers={"Authorization": api_token})
        transaction_id = response.json[0]["id"]
        response = client.delete(
            f"/transactions/{transaction_id}", headers={"Authorization": api_token}
        )
        assert response.status_code == 200
        response = client.get("/transactions", headers={"Authorization": api_token})
        assert transaction_id not in [
            transaction["id"] for transaction in response.json
        ]
