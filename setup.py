import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jiale0709",                     
    version="0.0.9",                      
    author="Jia Le",                  
    description="Jia Le's Python Library",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),   
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                     
    python_requires='>=3.6',                
    py_modules=["jiale0709"],            
    package_dir={'':'jiale0709/src'},   
    install_requires=[]                     
)