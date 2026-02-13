from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bsb-Inquiry",
    version="1.0.0",
    author="BLACK SPAMMER BD",
    author_email="githubshawpon@gmail.com",
    description="A professional web security testing toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shawpon2/bsb-Inquiry",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests",
        "beautifulsoup4",
        "colorama"
    ],
    entry_points={
        "console_scripts": [
            "sp = bsb_Inquiry.cli:main",
        ],
    },
    include_package_data=True,
)
