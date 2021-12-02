from src import menu
import mock
import builtins

USER = 'test_user'

def test_add_user():
    with mock.patch.object(builtins, 'input', lambda _: USER):
        assert menu.add_user() == True

def test_add_user_already_exists():
    with mock.patch.object(builtins, 'input', lambda _: USER):
        assert menu.add_user() == False

########### TEMPORARY FOR SORT_USERS #############

def test_add_user1():
    with mock.patch.object(builtins, 'input', lambda _: 'auser'):
        assert menu.add_user() == True

def test_add_user2():
    with mock.patch.object(builtins, 'input', lambda _: 'cuser'):
        assert menu.add_user() == True

def test_add_user3():
    with mock.patch.object(builtins, 'input', lambda _: 'beuser'):
        assert menu.add_user() == True

def test_add_user4():
    with mock.patch.object(builtins, 'input', lambda _: 'bauser'):
        assert menu.add_user() == True

##################################################

def test_delete_user():
    """ Check if user is successfully removed from list
    """
    with mock.patch.object(builtins, 'input', lambda _: USER):
        assert menu.delete_user() == True

def test_delete_user_not_exist():
    """ Check if del_user returns false when user does not exist
    """
    with mock.patch.object(builtins, 'input', lambda _: USER):
        assert menu.delete_user() == False


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
        assert menu.users == []

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
        assert menu.main_menu() == False
    with mock.patch.object(builtins, 'input', lambda: 'abc'):
        assert menu.main_menu() == False