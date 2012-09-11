# ReduPy

Esse pacote simple encapsula todas as funcionalidades da api do Redu para que o desenvolvedor não precise se preocupar como as requisições são feitas. 

Foram utilizados:

- Python 2.7
- Simplejson
- Rauth


## Instalação


```
$ sudo pip install -r requirements.txt
```

Copie o redupy para a pasta do seu projeto.


## QuickStart

Comece criando um novo objeto Redu, fornecendo seu consumer token e secret token:

```python
from redupy.api import Redu
client = Redu("yourconsumerkey", "yoursecretkey")
```

Adquira o seu authpin e inicie o cliente:

```python
print ("Follow this url: {0}".format(client.getAuthorizeUrl()))
pin = raw_input("Enter your pin:")
client.initClient(pin)
```

Teste a autenticação com uma requisição simples, este metódo deve retornar as informações do seu login:

```python
print client.getMe()
```

*Obs:

Só é preciso pedir o pin uma vez, depois de adquirido basta iniciar o client dessa maneira:

```python
client = Redu("yourconsumerkey", "yoursecretkey", "yourpin")
```

Mais exemplos [aqui](https://github.com/redu/redupy/examples).

## Como contribuir

1. Fork redupy no github.com
2. Crie um novo branch
3. Dê commit nas mudanças
4. Mande um pull request

## Copyright

Copyright (c) 2012 Redu Educational Technologies

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.