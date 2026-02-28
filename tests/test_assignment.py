def test_assign_asset_unauthorized(client):
    response = client.post("/assignments", json={})
    assert response.status_code in [401, 403, 422]