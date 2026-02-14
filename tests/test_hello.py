
def test_index_is_success(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json.get('status') == 'online'

def test_hello_page_is_success(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Hello, World'

def test_not_found(client):
    response = client.get('/does-not-exist')
    assert response.status_code == 404
