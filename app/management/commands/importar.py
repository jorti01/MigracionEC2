import pandas as pd
from django.core.management import BaseCommand
from app.models import User

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        df=pd.read_csv('datos.csv',sep=';')
        row_iter = df.iterrows()
        for index, row in row_iter:

                User.objects.create_user(
                    username = (row['Nombre'].split()[0] + "." + row['Apellidos'].split()[0]).lower(),
                    email = row['Correo'],
                    password = "12345678",
)
