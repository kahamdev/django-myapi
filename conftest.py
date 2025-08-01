# we add some staffs below
import pytest
from pytest_factoryboy import register
from api.tests.factories import UserFactory,AfricanLeadersFactory

# we register our factory
register(UserFactory)
register(AfricanLeadersFactory)


# we add fixture to the method test_user_factory
@pytest.fixture
def test_user_factory(user_factory): # type: ignore
    # we use .build() if we are not save
    user = user_factory.build() # type: ignore
    # we use .create() if we want save
    # user = user_factory.create() # type: ignore
    return user # type: ignore


# we add fixture to the method test_african_leaders_factory
@pytest.fixture
def test_african_leaders_factory(african_leaders_factory): # type: ignore
    # we use .build() if we are not save
    african_leaders = african_leaders_factory.build() # type: ignore
    return african_leaders # type: ignore
  

