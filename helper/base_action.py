import requests
import json

class BaseAction():
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
        self.hostUrl = 'hostUrl'

    def get(self, url, params):
        try:
            response = requests.get(url=self.hostUrl, params=params, headers=self.headers)
            rsp_json = response.json()
            status_code = response.status_code
            print("get请求结果为{}".format(rsp_json))
        except BaseException as e:
            print("get请求错误，错误原因：{}".format(e))

    def post(self, url, data):
 
        json = json.dumps(data)
        try:
            response = requests.post(url=url, json=json, headers=self.headers)
            rsp_json = response.json()
            status_code = response.status_code
            print("post请求结果为{}".format(rsp_json))
        except BaseException as e:
            print("post请求错误，错误原因：{}".format(e))

    def put(self,url,data):
        pass
    
    def delete(self,url,params):
        pass
    
    def patch(self, url, data):
        pass


