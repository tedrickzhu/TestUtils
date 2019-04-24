#encoding=utf-8
#author:Tedrick
#software:Pycharm
#file:webdriver_headless_proxy.py
#time:2019/4/24 上午11:07
# _*_ coding:utf‐8 _*

'''
@描述：chrome -headless with proxy -- baidu
@作者：wuyanhui
@版本：V1.0
@创建时间：2017/11/15 16:47
'''

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
