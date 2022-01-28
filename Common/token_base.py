import sys 
sys.path.append(".")
from Common.requestbase import RequestsHandler
url="https://gateway-stg.jmj1995.com/authority/auth/login"
json={"groupId":"3","username":"zaBjHxGvRVWGsVQ/zHecPnJqslj4HcDGZK7ETczs2779Znband2qnM9dVgyq2G9slLX69nVKb2HBQ51VgVuivFK5oizx/RSIgSmZlSQDaHHL4IHAnbwoGNWO85ERBFxOerLaNhP0EYrSkNABcJOfqiCRfazIXSxUKQd4XOx3H7c=","password":"NXn+tGp/+m3dtqV2Em2fqAs21CQIjm0F05JqPWzNjKUiRvvZG/MTcmilW3xymwqUzfCgM8vNMdOgVqffnD4piFrh3araElM6AW8GcyoUBz+hpEBoYY0X+ZBCXLSHTMWMc1UYbZxnMM9BNng9Mpj9kEgnuc9jE76yN6nE0fNPkvs=","validate":"","challenge":"","seccode":""}
class headerdata():
    """获取OMS系统token,封装至header"""
    def header(self):
        requestdata=RequestsHandler().post_Req(url=url,data="",json=json,headers="",params="")
        token=requestdata.json()
        headers=token["ndata"]["token"]
        header={"authorization":headers}
        return header