from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import chromedriver_binary

from .select import Lang, Sort
from math import ceil


class ScratchTrendData:
    """Use Selenium to retrieve popular works in Scratch.
    Args:
        lang (Lang): Language
        mode (Sort): Mode of acquisition
        visible_window (bool): Either put it in headless mode.
    """

    def __init__(self, lang: str, mode: str, visible_window: bool):
        self.__cookie = {"name": "scratchlanguage", "value": lang}
        self.mode = mode
        self._visible_window = visible_window

    def __setup(self):
        """Run Chrome."""
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        if self._visible_window:
            options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)
        driver.get("https://scratch.mit.edu/explore/projects/all")
        driver.add_cookie(self.__cookie)
        driver.get(f"https://scratch.mit.edu/explore/projects/all/{self.mode}")

        self.__wait_by_css(driver, "#projectBox>div>div>div:nth-child(16)>div>div>a")

        return driver

    def __wait_by_css(self, driver: webdriver.Chrome, element: str) -> None:
        wait = WebDriverWait(driver, 15)
        ec = EC.presence_of_element_located((By.CSS_SELECTOR, element))
        wait.until(ec)

    def get_by_rank(self, start: int, end: int) -> list:
        """Obtain by specifying the rank.

        Args:
            start (int): First page to retrieve
            end (int): Last page to retrieve

        Raises:
            ValueError: When start>end

        Returns:
            list[dict]: Acquisition Result
        """

        if start > end:
            raise ValueError("The start argument should be smaller than the end argument.")
        driver = self.__setup()

        # 指定された順位が1Pより下のときの処理
        if end - start >= 17:
            for _ in range(ceil((end - start) / 16)):
                driver.find_element(By.XPATH, '//*[@id="projectBox"]/button').click()

        soup = BeautifulSoup(driver.page_source, "html.parser")
        trend = list()

        for i in range(start, end):
            selector = f"#projectBox>div>div>div:nth-of-type({i})>div>div>a"
            if i % 17 == 0:
                driver.find_element(By.XPATH, '//*[@id="projectBox"]/button').click()

                self.__wait_by_css(driver, selector)
                soup = BeautifulSoup(driver.page_source, "html.parser")

            # CSSセレクタで選択し、タイトルとIDを抽出
            found = soup.select_one(selector)
            project_data = {
                "title": found.text,
                "id": int(found.attrs["href"].replace("/", "").replace("projects", ""))
            }
            trend.append(project_data)
        return trend

    def get_by_page(self, start: int, end: int) -> list[dict]:
        """Specify and retrieve the page.

        Args:
            start (int): First page to retrieve
            end (int): Last page to retrieve

        Raises:
            ValueError: When start>end

        Returns:
            list[dict]: Acquisition Result
        """

        if start > end:
            raise ValueError("The start argument should be smaller than the end argument.")

        driver = self.__setup()
        # 指定されたページが2P以上なら表示させる
        if start >= 2:
            for _ in range(start - 1):
                driver.find_element(By.XPATH, '//*[@id="projectBox"]/button').click()

        soup = BeautifulSoup(driver.page_source, "html.parser")
        trend = list()

        for i in range((start - 1) * 16 + 1, end * 16 + 1):
            selector = f"#projectBox>div>div>div:nth-of-type({i})>div>div>a"
            if i % 16 == 0:
                driver.find_element(By.XPATH, '//*[@id="projectBox"]/button').click()

                self.__wait_by_css(driver, selector.replace(str(i), str(i + 1)))
                soup = BeautifulSoup(driver.page_source, "html.parser")

            # CSSセレクタで選択し、タイトルとIDを抽出
            found = soup.select_one(selector)
            project_data = {
                "title": found.text,
                "id": int(found.attrs["href"].replace("/", "").replace("projects", "")),
            }
            trend.append(project_data)

        return trend


def connect(lang: Lang, sort: Sort, visible_window: bool = True):
    return ScratchTrendData(lang, sort, visible_window)
