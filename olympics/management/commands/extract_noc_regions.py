from django.core.management.base import BaseCommand
from olympics.models import Noc
import pandas as pd
import os


class Command(BaseCommand):
    help = 'Extract NOC and region from csv file'

    def handle(self, *args, **options):
        try:
            path = os.path.join('olympics', 'management', 'noc_regions.csv')
            df = pd.read_csv(path, encoding='utf-8', sep=',')
            df.apply(lambda row: Noc.objects.update_or_create(id=row['NOC'],
                                                              defaults={'region': row['region'],
                                                                        'notes': None if pd.isna(row['notes']) else
                                                                        row['notes']}), axis=1)
        except Exception as e:
            print(e)
