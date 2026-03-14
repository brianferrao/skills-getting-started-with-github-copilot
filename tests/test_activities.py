def test_get_activities_returns_expected_shape(client):
    # Arrange
    expected_activities = {"Chess Club", "Programming Class", "Gym Class"}
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert set(payload.keys()) == expected_activities

    for details in payload.values():
        assert required_fields.issubset(details.keys())
        assert isinstance(details["participants"], list)
