def test_get_assets_unauthorized(client):
    response = client.get("/assets")
    assert response.status_code in [401, 403]