import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_NAME = "Thorus-Slughorm"
SRC_REPO ="textSummarizer"
AUTHOR_EMAIL = "tanishdogra6794@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for NLP app",
    Long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{SRC_REPO}",
    project_urls={"Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")     
    
)