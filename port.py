import os
import socket
import urllib.request
from urllib import request
class port(object):
    '''
    classdocs
    '''
    def __init__(self):
        pass

    def IsOpen(self,ip,port):

        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((ip,int(port)))
            s.shutdown(2)
            print('%d is open' % port)
            return True
        except:
            print('%d is down' % port)
            return False

    def open_web(self,url):
        response = request.urlopen(url)

if __name__ == '__main__':
    TC=port()
    url="http://10.1.107.72/webapi/open/wmkhvcWzgcMWbXWCoLvU2sbbY3xYZ8F91zUimLRbwZliW7SM"
    TC.open_web(url)
    port_list=[22,8243,8080]
    # print(type(port_list))
    for i in port_list:
        # print(i)
        TC.IsOpen('10.1.107.72',i)


