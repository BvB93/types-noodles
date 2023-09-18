from setuptools import setup

setup(
    name="types-noodles",
    version="0.3.4",
    description="Typing stubs for noodles",
    long_description="Typing stubs for noodles\n\n",
    long_description_content_type="text/x-rst",
    author="Bas van Beek",
    url="https://github.com/BvB93/types-noodles",
    install_requires=[],
    packages=["noodles-stubs"],
    package_data={"noodles-stubs": ["py.typed", "**/*.pyi"]},
    license="Apache-2.0 license",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Typing :: Stubs Only",
    ]
)
