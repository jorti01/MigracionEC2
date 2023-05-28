import pandas as pd
from django.core.management import BaseCommand
from app.models import User,HojasdeVida



class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        id_inicial = 144
        df=pd.read_csv('/opt/bitnami/apache/htdocs/VIA/app/management/commands/datos.csv',sep=';')
        row_iter = df.iterrows()
        for index, row in row_iter:
                m = HojasdeVida.objects.get(id=id_inicial)
                if m.nombre == "Juan" and m.apellidos =="Ortiz":
                    break
                else:
                    print(m,id_inicial)
                    m.nombre_usuario = (row['Nombre'].split()[0] + "." + row['Apellidos'].split()[0]).lower()
                    m.email = row['Correo']
                    m.save()
                    id_inicial += 1
