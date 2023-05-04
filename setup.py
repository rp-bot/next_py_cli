from setuptools import setup, find_packages

setup(
    name="nextpy",
    version="0.0.2",
    author="rp-bot",
    author_email="prathamvadhulas@gmail.com",
    description=("Python program that automates creating a nextjs app "),
    long_description="jkshfdgvkhjfsdbvkjh",
    long_description_content_type="text/markdown",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'nextpy=nextpy.default_app:main',
        ],
    },
)
