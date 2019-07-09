import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="onlaw_api_client",
    version="0.1.2",
    author="Onlaw",
    author_email="jens@onlaw.dk",
    description="client for api.onlaw.dk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Onlaw/onlaw_api_client",
    packages=setuptools.find_packages(exclude=("tests")),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
