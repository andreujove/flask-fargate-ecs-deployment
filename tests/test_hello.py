
def test_hello_page(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.data == b'Hello, World'

def test_not_found(client):
    response = client.get('/notfound')
    assert response.status_code == 404
