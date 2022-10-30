from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import chromedriver_binary

from .select import Lang, Sort
from math import ceil


class ScratchTrend(object):
    """Use Selenium to retrieve popular works in Scratch.
    Args:
        lang (Lang): Language
        mode (Sort): Mode of acquisition
        hide (bool): Headless mode
    """

    def __init__(self, lang: str, mode: str, hide: bool):
        self.__cookie = {"name": "scratchlanguage", "value": lang}
        self._mode = mode
        self._hide = hide

    def __setup(self):
        """Chromeの起動などをします。
        Run Chrome.
        """

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        if self._hide:
            options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)
        driver.get("https://scratch.mit.edu/explore/projects/all")
        driver.add_cookie(self.__cookie)
        driver.get(f"https://scratch.mit.edu/explore/projects/all/{self._mode}")

        self.__wait_css(driver, "#projectBox>div>div>div:nth-child(16)>div>div>a")

        return driver

    def __wait_css(self, driver: webdriver.Chrome, element: str):
        wait = WebDriverWait(driver, 15)
        ec = EC.presence_of_element_located((By.CSS_SELECTOR, element))
        wait.until(ec)

    def get_by_num(self, start: int, end: int) -> list:
        """順位を指定して取得します。

        Args:
            start (int): 最初の順位
            end (int): 最後の順位

        Raises:
            ValueError: start>end の時

        Returns:
            list[dict]: リスト内辞書
        """

        if start > end:
            raise ValueError("start引数はend引数より小さくしてください。")
        driver = self.__setup()

        # 指定された順位が1Pより下のときの処理
        if end - start >= 17:
            for _ in range(ceil((end - start) / 16)):
                driver.find_element(
                    By.XPATH, '//*[@id="projectBox"]/button').click()

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        trend = list()

        for i in range(start, end):
            selector = f"#projectBox>div>div>div:nth-of-type({i})>div>div>a"
            if i % 17 == 0:
                driver.find_element(
                    By.XPATH, '//*[@id="projectBox"]/button').click()

                self.__wait_css(driver, selector)
                soup = BeautifulSoup(driver.page_source, 'html.parser')

            # CSSセレクタで選択し、タイトルとIDを抽出
            found = soup.select_one(selector)
            project_data = {
                'title': found.text,
                'id': int(found.attrs['href'].replace('/', '').replace('projects', ''))
                }
            trend.append(project_data)

        return trend

    def get_by_page(self, start: int, end: int) -> list:
        """ページを指定して取得します。

        Args:
            start (int): 最初のページ
            end (int): 最後のページ

        Raises:
            ValueError: start>end の時

        Returns:
            list[dict]: リスト内辞書
        """

        if start > end:
            raise ValueError("start引数はend引数より小さくしてください。")

        driver = self.__setup()
        # 指定されたページが2P以上なら表示させる
        if start >= 2:
            for _ in range(start - 1):
                driver.find_element(
                    By.XPATH, '//*[@id="projectBox"]/button').click()

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        trend = list()

        for i in range((start - 1) * 16 + 1, end * 16 + 1):
            selector = f"#projectBox>div>div>div:nth-of-type({i})>div>div>a"
            if i % 16 == 0:
                driver.find_element(
                    By.XPATH, '//*[@id="projectBox"]/button').click()

                self.__wait_css(driver, selector.replace(str(i), str(i+1)))
                soup = BeautifulSoup(driver.page_source, 'html.parser')

            # CSSセレクタで選択し、タイトルとIDを抽出
            found = soup.select_one(selector)
            project_data = {
                'title': found.text,
                'id': int(found.attrs['href'].replace('/', '').replace('projects', ''))
                }
            trend.append(project_data)

        return trend

def connect(lang: Lang, sort: Sort, hide: bool = True):
    return ScratchTrend(lang, sort, hide)
