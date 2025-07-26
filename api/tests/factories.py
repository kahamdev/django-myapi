# we import some staffs below
import factory
from django.contrib.auth.models import User
from api.models import AfricanLeaders

# we create factory for user class
class UserFactory(factory.django.DjangoModelFactory): # type: ignore
    class Meta: # type: ignore
        model =  User
        username = factory.Sequence(lambda n: f"user {n}") # type: ignore
        password = factory.PostGenerationMethodCall("set_password","password123") # type: ignore


class AfricanLeadersFactory(factory.django.DjangoModelFactory): # type: ignore
    class Meta: # type: ignore
        model = AfricanLeaders

    name = factory.Faker("Test Faker Name",nb_words=3)    # type: ignore
    country = factory.Faker("Test Faker Country")    # type: ignore
    capital = factory.Faker("Test Faker Capital")    # type: ignore
    party = factory.Faker("Test Faker Party")    # type: ignore
    population = factory.Faker("Test Faker Population")    # type: ignore
    gender = factory.Faker("Test Faker Gender")    # type: ignore
    age = factory.Faker("Test Faker Age")    # type: ignore