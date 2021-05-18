from setuptools import setup

setup(
    name="QDgym",
    url="https://github.com/ollenilsson19/QDgym",
    author="Olle Nilsson",
    author_email="olle.nilsson19@imperial.ac.uk",
    packages=["QDgym"],
    install_requires=["gym==0.15.4", "pybullet==3.0.8", "numpy==1.19.5"],
    package_data={"QDgym":["assets/*"]},
    version="0.1",
    license="MIT",
    description="QDgym",   
)
