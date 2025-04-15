from setuptools import setup, find_packages

setup(
    name="PackageA",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author="Your Name",
    author_email="your_email@example.com",
    description="A short description of your package",
    # long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your_package",  # if hosted on GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)