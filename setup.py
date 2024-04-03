from setuptools import setup, find_packages

setup(
    name="my_package",  # This is the name of your package
    version="0.1",  # The initial release version
    packages=find_packages(where='src'),  # This function automatically finds all packages in the 'src' directory.
    package_dir={'': 'src'},  # This specifies that the packages are located under the 'src' directory.

    # Here we specify dependencies. These are external packages that your project depends on.
    # These packages will be installed automatically when installing your package.
    install_requires=[
        # For this project, there are no dependencies, but typically it would look like this:
        # 'numpy', 'pandas', etc.
    ],

    entry_points={
            "console_scripts": [
                f"cmd = my_package.main:main",
            ]
    },

    # Metadata for your project
    author="Cedric Anover",
    author_email="ca20110820@gmail.com",
    description="Session 10 Activities",
    license="MIT",
    keywords="project git github devops ci cd",
    url="https://github.com/ca20110820/MyProject",  # project home page
)

# With this setup.py in place, you can install your project in another environment with pip:
# pip install .
# The '.' means that setup.py is in the current directory
