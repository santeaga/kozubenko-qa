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

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    # r = github_api.search_repo('kozubenko-qa')
    # print(r)
    assert r['total_count'] == 29
    assert 'become-qa-auto-aug2020' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('kozubenko_qa_repo')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0
