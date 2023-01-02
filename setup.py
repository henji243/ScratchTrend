from setuptools import setup
import scratchtrend

NAME = "scratchtrend"
DESCRIPTION = "ScratchTrend: Get Popular Projects from scratch"
AUTHOR = "ujex_256(henji243)"
URL = "https://github.com/henji243/ScratchTrend"

LICENSE = "MIT"
VERSION = scratchtrend.__version__

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

PYTHON_REQUIRES = ">=3.6"
INSTALL_REQUIRES = [
    "selenium>=4.3.0",
    "beautifulsoup4>=4.10.0",
]
EXTRAS_REQUIRE = ["chromedriver-binary>=100.0.4896.20.0"]
PACKAGES = ["scratchtrend"]

CLASSIFIERS = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: Japanese",
    "Natural Language :: English",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Internet",
]

setup(
    name=NAME,
    version=VERSION,
    license=LICENSE,
    author=AUTHOR,
    maintainer=AUTHOR,
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type="text/markdown",
    url=URL,
    download_url=URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=PACKAGES,
    classifiers=CLASSIFIERS
)
