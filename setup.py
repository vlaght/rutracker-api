import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rutracker-api-vlaght",
    version="0.0.1",
    author="Vlad Boyko",
    author_email="v1aght@ya.ru",
    description="Fork of rutracker-api by raitonoberu",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vlaght/rutracker-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
