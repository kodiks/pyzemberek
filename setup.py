import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

files = ["zemberek/bin/zemberek-full-0.17.1.jar"]

setuptools.setup(
    name="pyzemberek",
    version="0.0.2",
    author="Yavuz Kömeçoğlu",
    author_email="yavuz.komecoglu@kodiks.com",
    description="Python implementation of the Turkish NLP library Zemberek.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kodiks/pyzemberek",
    packages=setuptools.find_packages(),
    package_data = {'bin' : files },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=["Cython", "pyjnius"]
)
