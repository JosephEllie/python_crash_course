import pytest
from employee import Employee


@pytest.fixture
def amount_raise():
    default_raise = Employee('Joe', 'Coops', 10)
    return default_raise


def test_give_default_raise(amount_raise):
    assert amount_raise.give_raise() == amount_raise.annual_salary


def test_give_custom_raise(amount_raise):
    assert amount_raise.give_raise(4000) == amount_raise.annual_salary
