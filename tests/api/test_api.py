class User:

    def __init__(self) -> None:
        self.name = "Sergii"
        self.second_name = "Butenko"

user = User()

def test_remove_name():
    user.name = ''
    assert user.name == ''


def test_name():
    assert user.name == "Sergii"


def test_second_name():
    assert user.second_name == "Butenko"
