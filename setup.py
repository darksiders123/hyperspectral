import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spectramap",
    version="0.6.0.0",
    author="Juan David Muñoz-Bolaños",
    author_email="jmunozbolanos@gmail.com",
    description="Hyperspectral package for spectroscopists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MicroscopeMaestro/spectramap",
    project_urls={
        "Bug Tracker": "https://github.com/MicroscopeMaestro/spectramap",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	"Intended Audience :: Science/Research",
	"Development Status :: 3 - Alpha",
	"Topic :: Software Development :: Bug Tracking"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=["scikit-learn", "scipy", "numpy"],
<<<<<<< HEAD
)
=======
)
>>>>>>> 6ab45c2fddb988b7cd9850654b54d21260d226b3
