from setuptools import setup, find_packages

setup(
    name="sudoku",
    version="0.1",
    packages=find_packages(),
    install_requires=["numpy", "math", "random", "copy"],
    author="Tiago Bica",
    author_email="tiago.bica@gmail.com",
    description="Sudoku game tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tfbica/sudoku",
    license="MIT",
)
