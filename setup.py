import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='coinlore',
    version='0.1.7',
    author="CoinLore",
    keywords=['api', 'coinlore', 'cryptocurrency', 'cryptocurrency prices','bitcoin', 'ethereum', 'XRP'],
    author_email="contact@coinlore.com",
    description="Coinlore cryptocurrency api https://www.coinlore.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/coinlore/Python-Cryptocurrency-API-CoinLore",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
