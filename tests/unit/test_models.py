from datetime import datetime
from app.models import Assessment, User


def test_new_user():
    new_user = User('usernam1', 'password', datetime(2020, 1, 1), True)
    assert new_user.username == 'usernam1'
    assert new_user.password != 'password'
    assert new_user.signup_date == datetime(2020, 1, 1)
    assert new_user.is_admin == True


def test_new_assessment():
    new_assessment = Assessment('question', '56')
    assert new_assessment.question == 'question'
    assert new_assessment.answer == '56'
