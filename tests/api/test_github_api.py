import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exist(github_api):
    # api = GitHub()
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'
    # print(user, "\n")

@pytest.mark.api
def test_user_not_exist(github_api):
    # api = GitHub()
    r = github_api.get_user('butenkosergii')
    # print(r)
    assert r['message'] == 'Not Found'
