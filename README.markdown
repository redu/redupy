# ReduPy

Esse pacote encapsula as funcionalidades da API REST abstraindo a lógica das requisições HTTP.

Depedências utilizados:

- Python 2.7
- Simplejson
- Rauth
- Requests

## Instalação

```sh
$ sudo pip install git+git://github.com/redu/redupy.git
```

## Como usar a api

A implementação da biblioteca segue os mesmos padrões definidos na [documentação](http://developers.redu.com.br). Ou seja, os argumentos dos metódos possuem os mesmos nomes que foram documentados.
Por exemplo, se na documentação há uma requisição tipo ``GET`` onde é possível passar um parâmetro ``type`` via querystring, a chamada da função Python teria esse formato:

```python
client.nomeDaFuncao(id="um id", type="um type")
```

Para ver os detalhes de todas as funções bastar usar a função ``help`` no shell interativo Python:

```python
> from redupy.api import Redu
> help(Redu)
```

## QuickStart

Comece instanciando um novo objeto ``Redu``. Esse objeto recebe sua **consumer key**  e **consumer secret**. Mais instruções sobre como obte-las podem ser encontradas na [página de desenvolvedores](http://developers.redu.com.br).

```python
from redupy.api import Redu
client = Redu("yourconsumerkey", "yoursecretkey")
```

Adquira o seu PIN visitando a URL retornada por ``cluent.getAuthorizeUrl()`` e inicie o cliente:

```python
print ("Follow this url: {0}".format(client.getAuthorizeUrl()))
pin = raw_input("Enter your pin:")
client.initClient(pin)
```

Teste a autenticação com uma requisição simples, este metódo deve retornar as informações do seu login:

```python
print client.getMe()
```

*Obs*:

Só é preciso pedir o pin uma vez, depois de adquirido basta iniciar o client dessa maneira:

```python
client = Redu("yourconsumerkey", "yoursecretkey", "yourpin")
```

Mais exemplos [aqui](https://github.com/redu/redupy/tree/master/examples).

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