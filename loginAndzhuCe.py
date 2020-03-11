from locust import HttpLocust,Locust, TaskSet, task
import time
import queue
from requests_toolbelt import MultipartEncoder
import sys
sys.path.append("F:/myTestFile/TestObject/YouTime")
from yunqianbao.single.publicData import PublicDataClass
from yunqianbao.single.userMobile import user_mobile




class LoginAndZhuCe(TaskSet):

    def on_start(self):
        self.header ={
            "Connection":"keep-alive",
            "app-type":"android", #android
            "mobile-unid":str(int(round(time.time() * 100000))),
            "app-version":"5.4.91",
            "mobile-type":"HUAWEIALP-TL00(8.0.0)",
            "mobile-system":"android8.0.0",
            "device-tokens": "",  #AkWsVNSPMcwhC6nAXITHbPyrv0YgG5nt1T0B8n79-lrN
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; ALP-TL00 Build/HUAWEIALP-TL00)",
            "Content-Type":	"application/x-www-form-urlencoded",
        }
        self.apikey="djakdgkadgkafddadfjaddgbadsbfhbdashbgfadssfhbh"
        self.sfz_path = "F:/myTestFile/TestObject/YouTime/yunqianbao/static/shenfenzheng.txt"
        # self.publicData = PublicDataClass(self)
        # self.login_res = self.publicData.login(self.apikey,self.header)  #登录
        # is_safe = self.publicData.index(self.apikey,self.header,self.login_res)  #获取首页
        # self.publicData.setMiBao(self.apikey, self.header,self.login_res,is_safe) # 设置密保
        # self.publicData.shiMing(self.apikey,self.header,self.login_res,self.sfz_path) #实名认证
        # taskdata = self.publicData.getTask(self.apikey,self.header,self.login_res) #获取任务
        # if taskdata["type"] == 3:
        #     print("{}==需要去后台审核通过实名认证".format(self.login_res))


    # @task(1)   
    def userlogin(self):
        PublicDataClass(self).login(self.apikey,self.header)



    # @task(1)   
    def zhuCeUser(self,url,zc_data,header):
        PublicDataClass(self).zhuceUser(self.apikey,self.header)


    
    


class WebsiteUser(HttpLocust):
    task_set = LoginAndZhuCe
    min_wait = 600
    max_wait = 1000
    host = "https://tyqbapi.bankft.com/"
    # host = "http://dev.api.bankft.com/"
    
    # users = queryUsers() #多个用户
    mobile = user_mobile()
    users = []
    for i in range(mobile["start"],mobile["end"]): #(15001200238,15001200239): #
        users.append(i)
    queueData = queue.Queue()
    for userItem in users:
        queueData.put_nowait(userItem)   