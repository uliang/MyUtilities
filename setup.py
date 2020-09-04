import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tidbits", 
    version="0.0.1", 
    author="Tang U-Liang", 
    author_email="uliang6482@gmail.com", 
    description="Utility functions and classes",
    long_description_content_type="text/markdown", 
    packages=setuptools.find_packages(), 
    url="https://github.com/uliang/MyUtilities",
    classifiers=[
        "Programming Language :: Python :: 3", 
        "License :: MIT License", 
        "Operating System :: MacOS"
    ], 
    python_requires=">=3.8"
    
)    