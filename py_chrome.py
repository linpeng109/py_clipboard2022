from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from py_config import ConfigFactory
from py_logging import LoggerFactory


class ChromClient:
    def __init__(self, config, logger) -> None:
        self.config = config
        self.logger = logger

    def open_url(self, url: str):
        # chrome配置
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "excludeSwitches", ['enable-automation', 'enable-logging'])
        chrome_options.add_experimental_option('detach', True)
        chrome_options.headless = False

        # 获取执行文件路径
        executable_path = config.get('robots', 'chrome_driver')
        service = Service(executable_path=executable_path)
        chrome = webdriver.Chrome(options=chrome_options, service=service)

        # 打开url
        url = r'http://www.sina.com.cn'
        script_str = "window.open('%s','_self','toolbar=yes, location=yes, directories=no, status=no, menubar=yes, scrollbars=yes,  resizable=no, copyhistory=yes, width=400, height=400')" % url
        chrome.execute_script(script_str)

        # 关闭service
        service.stop()


if __name__ == '__main__':
    # 初始化配置
    config = ConfigFactory(config_file='py_clipboard.ini').get_config()
    logger = LoggerFactory(config_factory=config).get_logger()

    chrome_client = ChromClient(config=config, logger=logger)
    chrome_client.open_url('http://www.sina.com.cn')
