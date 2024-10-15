from setuptools import setup, find_packages

setup(
    name="morning_greetings",
    version="0.1",
    description="A package for sending personalized Good Morning messages.",
    author="Terje Saltskår",
    author_email="Terjesemail@example.com",
    packages=find_packages(where="."),  # Finds all packages in the current directory
    install_requires=[
        "schedule" 
    ],
    entry_points={
        'console_scripts': [
            'morning_greetings=morning_greetings.main:schedule_morning_greetings',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)