from app import app, greet


def test_greet_default():
    assert greet() == "hello, world!"


def test_greet_name():
    assert greet("DevSecOps") == "hello, DevSecOps!"


def test_index_route():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data.decode() == "hello, world!"


def test_health_route():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}
