# paineis/management/commands/import_excel.py
import os
import pandas as pd
from django.core.management.base import BaseCommand
from paineis.models import Revistas
from unidecode import unidecode

class Command(BaseCommand):
    help = 'Importa dados do Excel para o modelo Revistas'

    def handle(self, *args, **kwargs):
# Lista de possíveis caminhos para o arquivo Excel
        possible_paths = [
            r'C:\apps_bb\python\django\ldl\dados.xlsx',
            r'C:\projetos\python\django\ldl\dados.xlsx'
        ]
        
        # Inicializa file_path como None
        file_path = None
        
        # Verifica a existência do arquivo nos possíveis caminhos
        for path in possible_paths:
            if os.path.exists(path):
                file_path = path
                break

        # Verifica se um file_path válido foi encontrado
        if file_path is None:
            self.stdout.write(self.style.ERROR('Arquivo Excel não encontrado nos caminhos especificados.'))
            return
        
        # Apagar todos os registros existentes na tabela Revistas
        Revistas.objects.all().delete()
        
        # Lê o arquivo Excel usando pandas
        df = pd.read_excel(file_path)
        
        # Remover espaços em branco no início e no fim de todas as células de texto
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
        
        # Itera sobre cada linha do DataFrame e cria objetos Revistas
        for _, row in df.iterrows():
            autor_clean = unidecode(row['autor']).upper() if pd.notna(row['autor']) else ''
            genero_textual_clean = unidecode(row['genero_textual']).upper() if pd.notna(row['genero_textual']) else ''

            Revistas.objects.create(
                ano=row['ano'],  # Acesso direto, assume que a coluna 'ano' sempre existe
                volume=row['volume'],  # Acesso direto
                tema=row['tema'],  # Acesso direto
                secao=row['secao'],  # Acesso direto
                autor=autor_clean,  # Remove acentos e converte para maiúsculas
                titulo=row['titulo'],  # Acesso direto
                genero_textual=genero_textual_clean,  # Remove acentos e converte para maiúsculas
                palavra_chave1=row['palavra_chave1'],  # Acesso direto
                palavra_chave2=row.get('palavra_chave2', None),  # Acesso com fallback para None
                palavra_chave3=row.get('palavra_chave3', None),  # Acesso com fallback para None
                sexo_autor=row['sexo_autor'],  # Acesso direto
            )
        
        # Mensagem de sucesso
        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))
