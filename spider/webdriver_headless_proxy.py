#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:webdriver_headless_proxy.py
#time:2019/4/24 上午11:07
# _*_ coding:utf‐8 _*

from selenium import webdriver

# ---chrome
chrome_executable_path = r"E:\Program Files (x86)\wyhdriver\chromedriver.exe"
PROXY = "http://10.18.97.76:3128"

if __name__ == '__main__':


    # 配置项目
    # Create a copy of desired capabilities object.
    # 在windows系统:chrome driver 默认使用的是IE代理设置。而例如Firefox可以自行配置proxy
    desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
    # Change the proxy properties of that copy.
    desired_capabilities['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "noProxy": None,
        "proxyType": "MANUAL",
        "class": "org.openqa.selenium.Proxy",
        "autodetect": False
    }

    # 创建的新实例驱动
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(executable_path=chrome_executable_path,chrome_options=options,desired_capabilities=desired_capabilities)

    # 尝试访问登陆页面
    for neti in range(0, 3):
        SUCCESS = True
        try:
            driver.get('http://www.baidu.com')
            driver.implicitly_wait(3)  # wait seconds 等待页面加载
        except Exception as e:
            SUCCESS = False
            print(e)
            continue
        if SUCCESS:
            break
    print(driver.page_source)
    print("--finish--")
    driver.quit()
    exit(0)

'''webdriver+headless+proxy'''
# https://www.jianshu.com/p/a92dd9a824ec
# https://blog.csdn.net/guduyishuai/article/details/78988793
# https://blog.csdn.net/weixin_39847926/article/details/82190341
# https://www.cnblogs.com/zhang-pengcheng/p/6081007.html
# https://blog.csdn.net/duzilonglove/article/details/78517429
# https://stackoverflow.com/questions/48979520/chrome-headless-proxy-server
# https://www.cnblogs.com/rookies/p/6119786.html
# https://blog.csdn.net/weixin_42156283/article/details/84978904
# https://blog.csdn.net/qq_37059367/article/details/82943755
# https://blog.csdn.net/jane1229/article/details/83719431
# https://www.cnblogs.com/fhjy/p/9762908.html

'''browsermobproxy'''
# https://blog.csdn.net/zhanghs11/article/details/80487030
# https://www.cnblogs.com/lhfcws/p/6594038.html

# from selenium import webdriver
#
# PROXY = "proxy_host:proxy:port"
# options = webdriver.ChromeOptions()
# desired_capabilities = options.to_capabilities()
# desired_capabilities['proxy'] = {
# "httpProxy":PROXY,
# "ftpProxy":PROXY,
# "sslProxy":PROXY,
# "noProxy":None,
# "proxyType":"MANUAL",
# "class":"org.openqa.selenium.Proxy",
# "autodetect":False
# }
# driver = webdriver.Chrome(desired_capabilities = desired_capabilities)