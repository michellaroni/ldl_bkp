import urllib.parse
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib, base64
from .models import Vendas

def raml(request):
    # Busca dados no MySQL/PortgreSQL/SQLite, etc.
    vendas = Vendas.objects.all().values()
    df = pd.DataFrame(vendas)

    # Cria o gráfico
    fig, ax = plt.subplots()
    df.plot(x='ano', y='vendas', ax=ax)

    # Salva o gráfico em um buffer
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request, 'paineis/raml.html', {'data': uri})