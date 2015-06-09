def test_index(server):
    rv = server.get("/", follow_redirects=True)
    assert rv.status_code == 200
    assert "Notebook".encode("utf-8") in rv.data
    assert "close".encode("utf-8") in rv.data
