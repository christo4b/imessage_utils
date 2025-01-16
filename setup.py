from setuptools import setup, find_packages

setup(
    name="imessage_utils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
    author="Chris Bassano",
    author_email="chrisbassano@gmail.com",
    description="Python interface for sending messages via macOS Messages app",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/christo4b/imessage_utils",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License 2.0",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)