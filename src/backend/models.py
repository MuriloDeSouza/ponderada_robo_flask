#criação do banco de dados
from tinydb  import TinyDB
from datetime import datetime

class PosicaoRobo: #temos que colocar o self pq é uma regra para o banco de dados
    def __init__(self, db_path): #db_path é o caminho do banco de dados que depois eu coloco na rota
        
        self.db = TinyDB(db_path)
        self.table = self.db.table('Posicao_robo') #colocando o nome na tabela

    def coordenadas_add(self, x, y, z, r): #criando variáveis para poder inserir os pontos de ccord/
        self.table.insert({
            'x': x,
            'y': y,
            'z': z,
            'r': r,
            'hora': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    def valores(self): #pegando todos os valores da minha tabela
        return self.table.all()