from setuptools import setup

setup(
    name="QDgym",
    url="https://github.com/ollenilsson19/QDgym",
    author="Olle Nilsson",
    author_email="olle.nilsson19@imperial.ac.uk",
    packages=["QDgym"],
    install_requires=["gym", "pybullet", "numpy"],
    package_data={"QDgym":["assets/*"]},
    version="0.1",
    license="MIT",
    description="QD version of gym",   
)
