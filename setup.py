from distutils.core import setup

from sklearn2pmml import __license__, __version__

setup(
    name = "sklearn2pmml",
    version = __version__,
    description = "Python library for converting Scikit-Learn models to PMML",
    author = "Villu Ruusmann",
    author_email = "villu.ruusmann@gmail.com",
    license = __license__,
    packages = [
        "sklearn2pmml",
        "sklearn2pmml.resources"
    ],
    package_data = {
        "sklearn2pmml.resources" : ["*.jar"]
    },
    install_requires = [
        "scikit-learn>=0.16.0",
        "sklearn_pandas>=0.0.10"
    ]
)