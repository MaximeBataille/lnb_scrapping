import os
from pkg_resources import parse_requirements
from setuptools import find_packages, setup


here = os.path.abspath(os.path.dirname(__file__))
package_name = "sia_data_quality"

with open(os.path.join(here, "requirements.txt"), "r") as f:
    REQUIRED = [
        str(req) for req in parse_requirements(f) if req.name != "python"
    ]

EXTRAS = {}  
extras = []  # todo walk through folders and add the 'all'
for extra in extras:
    rel_path = f'{package_name}/requirements.txt' if extra == 'all' else f'{package_name}/{extra}/requirements.txt'
    path = os.path.join(here, rel_path)
    with open(path, 'r') as f:
        EXTRAS[extra] = [str(req) for req in parse_requirements(f) if str(req) not in REQUIRED]



with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=package_name,
    license="MIT",
    version="0.0.1",
    author="Maxime Bataille",
    author_email="maximebataille95@gmail.com",
    description="Data scrapping of the French basketball league",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaximeBataille/scrapping_pro_b",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=REQUIRED,
    include_package_data=True,
    packages=find_packages(where="src"),
    python_requires=">=3.7.7",
)
