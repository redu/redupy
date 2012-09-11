from redupy.api import Redu

client = Redu("yourconsumerkey", "yoursecretkey", "yourpin")
wall = client.getStatusBySpace(id="id de uma disciplina que voce tenha acesso", type="activity")
#Retorna uma lista contendo todos os posts dessse space que sejam do tipo activity
for post in wall:
    print post
