from setuptools import setup, find_packages

setup(
    name="prompt-engineering-examples",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=2.6.0",
        "python-dotenv>=1.0.0",
    ],
    python_requires=">=3.10",
)
