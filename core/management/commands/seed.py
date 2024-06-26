import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from core.models import Course, Extra


class Command(BaseCommand):
    help = "Load courses from csv file"

    def handle(self, *args, **options):
        datafile = settings.BASE_DIR / "core" / "data" / "courses.csv"
        extrasdatafile = settings.BASE_DIR / "core" / "data" / "extras.csv"
        with open(datafile) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                Course.objects.get_or_create(
                    name=row[0],
                    instructor=row[1],
                    duration=int(row[2]),
                    rating=float(row[3]),
                )
        with open(extrasdatafile) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                Extra.objects.get_or_create(
                    name=row[0],
                )
