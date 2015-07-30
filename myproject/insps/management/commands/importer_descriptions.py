from django.core.management.base import BaseCommand, CommandError
from insps.lib.import_descriptions import load_csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_csv()