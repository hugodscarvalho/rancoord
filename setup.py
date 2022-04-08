import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rancoord",                    
    version="0.0.1",                       
    author="Hugo Carvalho",                    
    description="RanCoord is a Python package for random sampling of geographic coordinates.",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),   
    url="https://github.com/hugodscarvalho/rancoord",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                     
    py_modules=["rancoord"],
    keywords=['coordinates', 'random', 'generation', 'sampling', 'python', 'geographic coordinates', 'geocoder'],
    package_dir={"": "src/rancoord"},             
    install_requires=[
        'Shapely>=1.8.1',
        'geopy>=2.2.0',
        'XlsxWriter>=3.0.3'
    ]                 
)