from setuptools import setup, find_packages

setup(
    name="morning_greetings",
    version="0.1",
    description="A package for sending personalized Good Morning messages.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'morning_greetings=morning_greetings.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
