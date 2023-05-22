from setuptools import setup, find_packages

setup(
    name="nextpy",
    version="1.0.1",
    author="Pratham Vadhulas",
    description=("Python CLI that automates creating a nextjs app"),
    long_description="""The Next.js App is created with a CLI. This wrapper is a Python program that helps you create a new Next.js app with less hassle. Say goodbye to boilerplate code, and hello to a clean start. Just enter your project name and the CLI will do the rest.""",
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
