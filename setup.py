from setuptools import setup

setup(
    name="QDgym",
    url="https://gitlab.doc.ic.ac.uk/AIRL/students_projects/2019-2020/olle_nilsson/QDgym",
    author="Olle Nilsson",
    author_email="olle.nilsson19@imperial.ac.uk",
    packages=["QDgym"],
    install_requires=["gym", "pybullet", "numpy"],
    package_data={"QDgym":["assets/*"]},
    version="0.1",
    license="MIT",
    description="QD version of gym",   
)
