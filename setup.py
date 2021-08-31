import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='YourSuperAPI',
    version='0.0.3',
    author='Luke Prior',
    author_email='current.address@unknown.invalid',
    description='Python wrapper for the YourSuper API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LukePrior/PythonYourSuperAPI",
    project_urls={
      "Bug Tracker": "https://github.com/LukePrior/PythonYourSuperAPI/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3",
)