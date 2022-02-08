# -*- coding: utf-8 -*-
import sys 
sys.path.append(".")
from Common.requestbase import RequestsHandler
url="https://gateway-stg.datousoft.com/authority/auth/login"
json={"groupId":"3","username":"TRtsH2z2egXgbqWAIOTsJBf7E+Z/nA17u7HoVWtUqBIQP3PXpTeNuxcIm2rHTBkpnuCplP+CR/CkjzNFC2oMTKzMgXJWSu97e0qqLOV+Sm8VqntO0HMC0gTlQkHzJ33LLA4x12fDEGJnLcaznG16eCYlZPgssGvazAPGvOO7Wqk=","password":"rlSCBdDGZAeGyaN7qlTWWEsZN0r8dlD7y81u2Waq2IyyUJfIZZ9A8Iua0eJpViQOeEOUQgk4L/5SaZtRQrfv3iJG2ryuw+zv8FX+DS6CY/kkZwmq6jnebMDCeaUhcBkbS+6g3vOM9Q0fCR/5yPLOJ5SQlYAnyL+pd66NSlFkh4M=","validate":'',"challenge":'',"seccode":''}
class headerdata():
    """获取OMS系统token,封装至header"""
    def header(self):
        requestdata=RequestsHandler().post_Req(url=url,data="",json=json,headers="",params="")
        token=requestdata.json()
        headers=token["ndata"]["token"]
        header={"authorization":headers}
        return header