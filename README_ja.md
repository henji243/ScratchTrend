<div align="center"><img src="https://user-images.githubusercontent.com/105550500/197376654-a36e55d0-35ac-42c8-aed5-23e9a48c04fd.jpg" /></div>

# ScratchTrend: Scratchから人気作品を取得。
[![PyPI](https://img.shields.io/badge/PyPI-dummy?style=for-the-badge&logo=pypi&labelColor=gray&color=red)](https://pypi.org/project/scratchtrend/)
[![GitHub](https://img.shields.io/badge/GitHub-dummy?style=for-the-badge&logo=github&labelColor=gray&color=blue)](https://github.com/henji243/ScratchTrend)

[![License](https://img.shields.io/github/license/henji243/ScratchTrend)](https://github.com/henji243/ScratchTrend)
[![Downloads](https://img.shields.io/pypi/dd/scratchtrend?color=%2383ccd2&label=PyPI%20Downloads&logo=PyPI&logoColor=%2383ccd2)](https://pypi.org/project/scratchtrend)

ScratchTrendは、https://scratch.mit.edu/explore から、人気の作品を取得します。
<br />
<span style="color:red;">**(このライブラリはScratch財団とは無関係です。)**</span>
<br /><br />
# 使い方
## インストール
ターミナル
```sh
$ pip install scratchtrend
```
インポート
```python
import scratchtrend as sct
from scratchtrend.select import Lang, Sort
```
**必須ライブラリ・アプリ**
- Selenium
- BeautifulSoup
- GoogleChrome

**推奨ライブラリ**
- chromedriver_binary
- webdriver_manager

上記のどれか一つがインストールされていると、ChromeDriverのパスを自動で通してくれます。
<br /><br />

## 準備
```python
sct.CHROMEDRIVER_PATH = "chromedriverのパス"
```
もし推奨ライブラリのいずれかが入っていない場合はここで指定することができます。
(インストールされていればこれは無視されます。)


```python
# example
data = sct.connect(Lang.JAPANESE, Sort.POPULAR)
```
指定できる言語の一覧はLanguages.mdに書いてあります。
```connect()```メソッドで、言語、並び替えを指定してください。<br />
並び替えは以下の通りです:
| 指定内容 | 並び替え |
| ------- | ------- |
| Sort.TRENDING | 傾向 |
| Sort.POPULAR | 人気 |
| Sort.RECENT | 最近 |
<br />

## メソッド
(まだ開発途中のため、ショボいです)
```python
data.get_by_page()  # ページを指定して取得
data.get_by_num()  # 順位を指定して取得
```
```get_by_page()```メソッドはstart引数からend引数のページの作品を取得します。必ず start&lt;endとなるようにしてください。<br />
```get_by_num()```メソッドはstart引数からend引数の順位の作品を取得します。こちらもstart&lt;endとなるようにしてください。
##### "順位"という言い方には少し語弊があります。良い言い方があったらIssuesまでお願いします。
<br />

**返り値**
```python
# 見やすくするため整形しています。
[
    {
        'title': '作品のタイトル',
        'id': "作品のID"
    },
    {
        'title': 'タイトル',
        'id': "ID"
    }
]
```
このようにリスト内辞書で返されます。
<br /><br />
# デモ
<a href="https://youtu.be/P-7ia4hHtjY" target="_blank"><img src="https://user-images.githubusercontent.com/105550500/198833200-901bc950-6799-4ec0-852a-8a1af70ee87f.png" /></a>


# その他
## ライセンス
ScratchTrendはMITライセンスです。
## クレジット
- ロゴは<a href="https://www.designevo.com/jp/" title="無料オンラインロゴメーカー">DesignEvo</a> を使用しました。
- [Selenium](https://github.com/SeleniumHQ/selenium)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [GoogleChrome](https://chrome.com/)

## 連絡
もしバグを発見した場合は、[Issue](https://github.com/henji243/ScratchTrend/issues)または[Scratch](https://scratch.mit.edu/projects/753404201/)まで。
