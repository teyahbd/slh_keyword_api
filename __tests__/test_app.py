import json
from app import app

# endpoint testing:

def test_home_route():
    response = app.test_client().get("/")
    res = json.loads(response.data.decode("utf-8")).get("Endpoints")

    assert type(res) is dict
    assert "/model" in res
    assert res["/model"] == "accepts POST request containing keywords which returns related keywords"
    assert response.status_code == 200

def test_model_route():
    expected_keywords = [
		[
			"queen",
			0.8523604273796082
		],
		[
			"throne",
			0.7664334177970886
		]
	]

    response = app.test_client().post("/model", json={"positive": ["king", "woman"], "negative": ["man"]})
    res = json.loads(response.data.decode("utf-8")).get("keywords")

    assert type(res) is list
    assert len(res) == 2
    for i in res:
        assert type(i[0]) is str
        assert type(i[1]) is float
    assert res == expected_keywords
    assert response.status_code == 200

# endpoint error handling testing:

def test_404_not_found():
    response = app.test_client().get("/doesnotexist")
    res = response.data.decode("utf-8")

    assert type(res) is str
    assert "<h1>Not Found</h1>" in res
    assert response.status_code == 404

def test_400_missing_required_fields():
    response = app.test_client().post("/model", json={"positive": ["king", "woman"]})
    res = response.data.decode("utf-8")

    assert type(res) is str
    assert "<h1>Bad Request</h1>" in res
    assert response.status_code == 400

def test_400_keyword_not_in_data():
    response = app.test_client().post("/model", json={"positive": ["kinggfgfd", "woman"], "negative": ["man"]})
    res = response.data.decode("utf-8")

    assert type(res) is str
    assert "<h1>Bad Request</h1>" in res
    assert response.status_code == 400
