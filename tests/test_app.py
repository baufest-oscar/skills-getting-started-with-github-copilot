def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert expected_activity in data


def test_signup_adds_participant_to_activity(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "newstudent@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": student_email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {student_email} for {activity_name}"

    updated_activity = client.get("/activities").json()[activity_name]
    assert student_email in updated_activity["participants"]


def test_unregister_removes_participant_from_activity(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": student_email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {student_email} from {activity_name}"

    updated_activity = client.get("/activities").json()[activity_name]
    assert student_email not in updated_activity["participants"]
