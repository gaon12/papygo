from setuptools import setup, find_packages

setup(
    name="papygo",
    version="1.0.1",
    author="Jeong Gaon",
    author_email="gokirito12@gmail.com",
    description="A simple library for translating using the NAVER Papago API",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gaon12/papygo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.6',
    install_requires=[
        "urllib3>=1.25.3",
    ],
)
