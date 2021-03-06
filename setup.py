import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cli-IOTNinja", # Replace with your own username
    version="0.0.1",
    author="Ali Azizi",
    author_email="aliazizi.79a@gmail.com",
    description="IOTNinja client side",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NinjaGeeks/cli-python-IOTNinja.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)