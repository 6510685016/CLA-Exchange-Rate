from setuptools import setup, find_packages

setup(
    name="cli-app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'requests',
        'typer',
        'fastapi',
    ],
    entry_points={
        'console_scripts': [
            'cli-exc = cli_app.main:app',  
        ],
    },
)
