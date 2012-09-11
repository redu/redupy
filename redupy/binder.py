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

            data = m(path, params=self.url_arg,
                data=self.payload_arg)
            retorno = None

            if self.payload_type:
                if not data:
                    raise Exception("Empty response content!, probally a 404 error")
                json = simplejson.loads(data, encoding="UTF-8")
                tipo = getattr(self.api.model_factory, self.payload_type)
                retorno = tipo()
                if isinstance(json, list):
                    retorno = []
                    for dct in json:
                        elem = tipo()
                        elem.parse(dct)
                        retorno.append(elem)
                else:
                    retorno.parse(json)

            return retorno

    def _call(api, **kargs):
        method = APIMethod(api, kargs)
        return method.execute()

    return _call
