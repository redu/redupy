import simplejson


def bind_api(**config):

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

        def build_params(self):
            tempDict = {}
            for param in self.querry_params:
                if self.kargs.get(param):
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

    def _call(api, **kargs):
        method = APIMethod(api, kargs)
        return method.execute()
    #CODIGO PARA GERAR A DCOUMENTACAO
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
