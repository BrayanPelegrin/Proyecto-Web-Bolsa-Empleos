# Pytest 
import pytest 

# Owns 
from users.models import UserAccount


@pytest.mark.django_db
def test_user_creation():
    user = UserAccount.objects.create_user(
        username = 'django08',
        first_name = 'Python',
        last_name = 'Django',
        email = 'django@gmail.com'
    )
    assert user.username == 'django08'
    assert user.first_name == 'Python'
    assert user.last_name == 'Django'
    assert user.email == 'django@gmail.com'

@pytest.mark.django_db
def test_user_creation():
    user = UserAccount.objects.create_superuser(
        username = 'django08',
        first_name = 'Python',
        last_name = 'Django',
        email = 'django@gmail.com'
    )
    assert user.username == 'django08'
    assert user.first_name == 'Python'
    assert user.last_name == 'Django'
    assert user.email == 'django@gmail.com'
