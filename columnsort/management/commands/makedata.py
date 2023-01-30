from django.core.management.base import BaseCommand
from faker import Faker
from ...models import AddressList


class Command(BaseCommand):

    def handle(self, *args, **options):

        fake = Faker('en_US')
        AddressList.objects.all().delete()

        for _ in range(500):
            address = AddressList(
                first=fake.first_name(),
                last=fake.last_name(),
                address=fake.street_address(),
                city=fake.city(),
                state=fake.state_abbr(),
                zip=fake.postalcode())
            address.save()
            print(address)
