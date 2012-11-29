# -*- coding: latin-1 -*-
import simplejson

# Helper para construir os metódos de chamada de api, recebe os parâmetros de
# configuração na forma de um dicionario e retorna um metódo baseado nesses
# parâmetros.
#
# Configurações possíveis:
#
# path - A url parcial do recurso com um formatador no lugar do id.
#        Por exemplo: 'users/{0}'.
#
# method - O verbo da requisicao html: 'get', 'post', 'put' ou 'delete'.
#
# querry_params - Lista de strings que representa os nomes dos parâmetros que
#                 são aceitos via querry string, por exemplo:
#                 ['type', 'page'].
#
# payload_params - Lista de strings que representa os nomes dos parâmetros que
#                  são aceitos na payload da requisição, por exemplo:
#                  ['name', 'description'].
#
# payload_type - Uma String que representa o tipo de recurso retornado,
#
# send_type - Uma String que representa o tipo de recurso enviado


def bind_api(**config):

    # Classe dinâmica que representa um metódo de requisição da api
    class APIMethod(object):

        path = config['path']
        payload_type = config.get('payload_type', None)
        method = config.get('method', 'get')
        querry_params = config.get('querry_params', [])
        payload_params = config.get('payload_params', [])
        send_type = config.get('send_type', payload_type)

        def __init__(self, api, kargs):
            self.api = api
            self.kargs = kargs
            self.build_params()

        # Constrói os argumentos da requisição, tanto o payload quanto o
        # querry-string
        def build_params(self):
            tempDict = {}
            for param in self.querry_params:
                if self.kargs.get(param):  # Se o parametro foi passado
                    tempDict[param] = self.kargs[param]
            self.url_arg = tempDict
            tempDict = {}
            for param in self.payload_params:
                if self.kargs.get(param):
                    tempDict[param] = self.kargs[param]
            if not tempDict == {}:
                tempDict = {self.send_type: tempDict}
            self.payload_arg = simplejson.dumps(tempDict)

        def execute(self):
            path = self.api.base_url + self.path
            path = path.format(self.kargs.get('id', ''))
            m = getattr(self.api.client, self.method)

            response = m(path, params=self.url_arg,
                data=self.payload_arg)

            response.raise_for_status()
            data = response.content
            if self.payload_type:
                json = simplejson.loads(data, encoding="UTF-8")
                tipo = getattr(self.api.model_factory, self.payload_type)
                retorno = tipo()
                if isinstance(json, list):
                    retorno = []
                    for dct in json:
                        elem = tipo()
                        elem.parse(dct, self.api.model_factory)
                        retorno.append(elem)
                else:
                    retorno.parse(json, self.api.model_factory)

            return retorno

    # Metódo retornado pelo bind_api, vai receber os argumentos que foram
    # definidos pelo binder via o **kargs e api é o argumento implicito(self) da
    # classe que definir esse metódo
    def _call(api, **kargs):
        method = APIMethod(api, kargs)
        return method.execute()

    # Codigo para gerar o help dinamico
    required_args = config.get('payload_params', [])
    url = config.get('path')
    if"{0}" in url:
        required_args.append('id')
    optional_args = config.get('querry_params', [])
    return_type = config.get('payload_type', None)

    _call.__doc__ = """Argumentos obrigatorios: {0}
    Argumentos Opicionais: {1}
    Retorna: {2}""".format(required_args,
        optional_args, return_type)

    return _call
