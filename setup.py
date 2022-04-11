import setuptools

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README_PYPI.md").read_text()

setuptools.setup(
    name="rancoord",                    
    version="0.0.1", 
    author_email="hugodanielsilvacarvalho.hc@gmail.com",                      
    author="Hugo Carvalho",
    description="RanCoord is a Python package for random sampling of geographic coordinates.",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),   
    url="https://github.com/hugodscarvalho/rancoord",
    License="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                     
    py_modules=["rancoord"],
    keywords=['coordinates', 'random', 'generation', 'sampling', 'python', 'geographic coordinates', 'geocoder', 'distance-matrix'],
    package_dir={"": "src/rancoord"},             
    install_requires=[
        'Shapely>=1.8.1',
        'geopy>=2.2.0',
        'XlsxWriter>=3.0.3',
        'requests>=2.27.1',
        'numpy>=1.22.3',
        'folium>=0.12.1',
    ]                 
)