from distutils.core import setup

setup(
    name = "sklearn2pmml",    
    description = "Python library for converting Scikit-Learn models to PMML",
    author = "Villu Ruusmann",
    author_email = "villu.ruusmann@gmail.com",
    packages = [
        "sklearn2pmml",
        "sklearn2pmml.resources"
    ],
    package_data = {
        "sklearn2pmml.resources" : ["*.jar"]
    },
    install_requires = [
        "scikit-learn>=0.16.0",
        "sklearn-pandas>=0.0.10"
    ]
)
