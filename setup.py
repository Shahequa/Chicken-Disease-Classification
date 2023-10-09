import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_descripton = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classifiaction"
AUTHOR_USER_NAME = "Shahequa"
SRC_REPO = "ChickenDiseaseClassifiaction"
AUTHOR_EMAIL = "tsmodabbera017@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A small python app for CNN app.",
    long_description= long_descripton,
    long_descripton_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src")

)