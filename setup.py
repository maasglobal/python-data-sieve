import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data-sieve",
    version="0.0.1",
    author="Brylie Christopher Oxley",
    author_email="brylie.oxley@maas.global",
    description="A small package to separate wanted from unwanted data properties.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maasglobal/python-data-sieve",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="" >= 3.6",
)
