from redupy.api import Redu

client = Redu("yourconsumerkey", "yoursecretkey", "yourpin")
resposta = client.postEnvironment(name="O nome do ava", path="o path",
initials="as iniciais", description="a descricao")
#a resposta deve ser um objeto do tipo enviroment contento as informacoes do
#ava criado
print resposta
