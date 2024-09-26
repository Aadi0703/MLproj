from setuptools import setup, find_packages

def get_requirements(filepath):
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
    name="ml_proj",
    version="0.0.1",
    description="ML Project",
    author="Aaditya Ghaisas",
    author_email="aadityaghaisas0703@gmail.com",
    packages=find_packages(),
    license="MIT",
    install_requires=get_requirements("requirements.txt"),
)