import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="character-model-python",
    version="0.1.0",
    author="ccthomas",
    author_email="ccthom94@gmail.com",
    description="Python Character Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/places-and-characters/character-models-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ]
)
