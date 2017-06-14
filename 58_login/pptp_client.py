import win32ras
vpn_name='vpn'
ip_address="zzzh.8866.org"
username="a1365"
password="1"
class PPTPDial:
    def __init__(self,ip_address,username,password):
        self.ip_address=ip_address
        self.username=self.username
        self.password=self.password

    def connect(self):

        pid, ret = win32ras.Dial(None, None, (vpn_name, ip_address, "", username, password, ""), None)
print pid,ret
re=win32ras.HangUp(pid)
print re