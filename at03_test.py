import pytest
from main_at03 import get_cat_photo

def test_get_cat_photo(mocker):
    mock_get = mocker.patch('main_at03.requests.get')
    # Создаем мок-ответ для успешного запроса
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'id': 'iapoHxQxL',
        'url': 'https://cdn2.thecatapi.com/images/iapoHxQxL.jpg',
        'width': 1600,
        'height': 1067
    }

    api_key = 'test_api_key'
    cat = get_cat_photo(api_key)
    assert cat == {
        'id': 'iapoHxQxL',
        'url': 'https://cdn2.thecatapi.com/images/iapoHxQxL.jpg',
        'width': 1600,
        'height': 1067
   }

def test_get_test_get_cat_photo_failure(mocker):
    mock_get = mocker.patch('main_at03.requests.get')
    # Создаем мок-ответ для неуспешного запроса
    mock_get.return_value.status_code = 404
    api_key = 'test_api_key'
    cat = get_cat_photo(api_key)
    assert cat is None

