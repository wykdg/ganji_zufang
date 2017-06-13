import PyV8
import rsa
import binascii
class Enerypt_58:
    def __init__(self,e,m):
        # PyV8.JSEngine
        # self.ctxt=PyV8.JSContext()
        # self.ctxt.enter()
        self.e=e
        self.m=m
        # with open("deal.js") as jsfile:

            # self.ctxt.eval(jsfile.read())
    def energy(self,msg):
        with PyV8.JSLocker():
            with PyV8.JSContext() as ctex:
                with open("deal.js") as jsfile:
                    ctex.eval(jsfile.read())
                    encrypt_pwd = ctex.eval('encryptString("%s","%s","%s")' % (msg, self.e, self.m))
            print encrypt_pwd


        return encrypt_pwd
        #
        # rsaPublickey = int(self.m, 16)
        # key = rsa.PublicKey(rsaPublickey, 65537)
        # message = msg
        # passwd = rsa.encrypt(message, key)
        # passwd = binascii.b2a_hex(passwd)
        # return passwd

if __name__=='__main__':
    msg = '1411093458382123123123'
    e='010001'
    m='008baf14121377fc76eaf7794b8a8af17085628c3590df47e6534574efcfd81ef8635fcdc67d141c15f51649a89533df0db839331e30b8f8e4440ebf7ccbcc494f4ba18e9f492534b8aafc1b1057429ac851d3d9eb66e86fce1b04527c7b95a2431b07ea277cde2365876e2733325df04389a9d891c5d36b7bc752140db74cb69f'

    s=Enerypt_58(e,m)
    # for i in range(100):
    print s.energy(msg)



    # rsaPublickey = int(m, 16)
    # key = rsa.PublicKey(rsaPublickey, 65537)
    # message = msg
    # passwd = rsa.encrypt(message, key)
    # passwd = binascii.b2a_hex(passwd)
    # print passwd