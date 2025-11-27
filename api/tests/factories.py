# we import some staffs below
import factory  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from api.models import AfricanLeaders  # type: ignore
from faker import Faker  # type: ignore


# we initialize faker object below
faker = Faker()


# we create class user factory below
class UserFactory(factory.django.DjangoModelFactory):  # type: ignore
    class Meta:  # type: ignore
        model = User

    username = "kaham mlau"


# # we create factory for user class
# class UserFactory(factory.django.DjangoModelFactory): # type: ignore
#     class Meta: # type: ignore
#         model =  User
#     username = factory.Sequence(lambda n: f"user {n}") # type: ignore
#     password = factory.PostGenerationMethodCall("set_password","k@h@m123") # type: ignore


# we create class african leaders factory below
class AfricanLeadersFactory(factory.django.DjangoModelFactory):  # type: ignore
    class Meta:  # type: ignore
        model = AfricanLeaders

    # we use faker to generate data feed
    name = faker.name()  # type: ignore
    country = faker.country()  # type: ignore
    capital = faker.email()  # type: ignore
    party = factory.Faker("name")  # type: ignore
    population = factory.Faker("country")  # type: ignore
    gender = factory.Faker("email")  # type: ignore
    age = faker.text()  # type: ignore
