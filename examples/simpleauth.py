from redupy.api import Redu
if __name__ == '__main__':

    client = Redu("yourconsumerkey",
        "yoursecretkey")
    #ou voce pode passar o pin diretamente
    #client = Redu("yourconsumerkey", "yoursecretkey", "yourpin")
    #note que assim o initclient ja eh chamado diretamente
    print ("Follow this url: {0}".format(client.getAuthorizeUrl()))
    pin = raw_input("Enter your pin:")
    client.initClient(pin)
    print client.getMe()
