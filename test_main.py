import builtins
import mock
from src import menu

USER = 'test_user'

def test_add_user():
    """
    Adding a user to the list
    """
    with mock.patch.object(builtins, 'input', lambda _: USER):
        assert menu.add_user() is True

def test_add_user_already_exists():
    """
    Returns false when user already exists in the list
    """
    with mock.patch.object(builtins, 'input', lambda _: USER):
        assert menu.add_user() is False

########### TEMPORARY FOR SORT_USERS #############

def test_add_user1():
    """
    Adding a user to the list for sorting users function
    """
    with mock.patch.object(builtins, 'input', lambda _: 'auser'):
        assert menu.add_user() is True

def test_add_user2():
    """
    Adding a user to the list for sorting users function
    """
    with mock.patch.object(builtins, 'input', lambda _: 'cuser'):
        assert menu.add_user() is True

def test_add_user3():
    """
    Adding a user to the list for sorting users function
    """
    with mock.patch.object(builtins, 'input', lambda _: 'beuser'):
        assert menu.add_user() is True

def test_add_user4():
    """
    Adding a user to the list for sorting users function
    """
    with mock.patch.object(builtins, 'input', lambda _: 'bauser'):
        assert menu.add_user() is True

##################################################

def test_delete_user():
    """ Check if user is successfully removed from list
    """
    with mock.patch.object(builtins, 'input', lambda _: USER):
        assert menu.delete_user() is True

def test_delete_user_not_exist():
    """ Check if del_user returns false when user does not exist
    """
    with mock.patch.object(builtins, 'input', lambda _: USER):
        assert menu.delete_user() is False


def test_sort_users():
    """ Check if users are sorted correctly
    """
    menu.sort_users()
    assert menu.users == ['auser', 'bauser', 'beuser', 'cuser']


def test_del_users():
    """ Check if all users are purged from list
    """
    with mock.patch.object(builtins, 'input', lambda _: 'Y'):
        menu.del_all()
        assert not menu.users

def test_main_menu():
    """ Test main menu functionality
    """
    with mock.patch.object(builtins, 'input', lambda: '1'):
        assert menu.main_menu() == menu.list_users()
    # with mock.patch.object(builtins, 'input', lambda: '2'):
    #     assert menu.main_menu() == menu.add_user()
    # with mock.patch.object(builtins, 'input', lambda _: '3'):
    #     assert menu.main_menu() == menu.delete_user()
    # with mock.patch.object(builtins, 'input', lambda: '4'):
    #     assert menu.main_menu() == menu.change_user()
    # with mock.patch.object(builtins, 'input', lambda _: '5'):
    #     assert menu.main_menu() == menu.sort_users()
    # with mock.patch.object(builtins, 'input', lambda _: '6'):
    #     assert menu.main_menu() == menu.find_user()
    # with mock.patch.object(builtins, 'input', lambda _: '7'):
    #     assert menu.main_menu() == menu.del_all()
    # with mock.patch.object(builtins, 'input', lambda _: '8'):
    #     assert menu.main_menu() == menu.save_list()
    # with mock.patch.object(builtins, 'input', lambda _: '9'):
    #     assert menu.main_menu() == menu.read_list()
    with mock.patch.object(builtins, 'input', lambda: '10'):
        assert menu.main_menu() is False
    with mock.patch.object(builtins, 'input', lambda: 'abc'):
        assert menu.main_menu() is False
