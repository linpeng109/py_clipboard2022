from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from py_config import ConfigFactory
from py_logging import LoggerFactory

'''
控制Chrome浏览器
'''


class ChromClient:
    # 初始化
    def __init__(self, config, logger) -> None:
        self.config = config
        self.logger = logger
    
    # 打开指定网址
    def open_url(self, url: str):
        # chrome配置
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "excludeSwitches", ['enable-automation', 'enable-logging'])
        chrome_options.add_experimental_option('detach', True)
        chrome_options.headless = False

        # 获取执行文件路径
        executable_path = self.config.get('robots', 'chrome_driver')
        self.service = Service(executable_path=executable_path)  # , port=9222
        self.chrome = webdriver.Chrome(
            chrome_options=chrome_options, service=self.service)
        self.logger.debug(url)

        # 打开url
        script_str = "window.open('%s','_self','toolbar=yes, location=yes, directories=no, status=no, menubar=yes, scrollbars=yes,  resizable=no, copyhistory=yes, width=400, height=400') " % url
        self.chrome.execute_script(script_str)

        # 关闭service
        self.service.stop()


if __name__ == '__main__':
    #     # 初始化配置
    config = ConfigFactory(config_file='py_clipboard.ini').get_config()
    logger = LoggerFactory(config_factory=config).get_logger()
    chrome_client = ChromClient(config=config, logger=logger)
    chrome_client.open_url(url=r'https://www.sina.com.cn')
