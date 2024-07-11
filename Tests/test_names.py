from get_username import get_username


def test_check_first_last_name():
    formatted_name = get_username('Joseph', 'Cooper')
    assert formatted_name == 'Joseph Cooper'


def test_fullname():
    formatted_name = get_username("Adama", "Cooper", "Wisdom")
    assert formatted_name == 'Adama Wisdom Cooper'



