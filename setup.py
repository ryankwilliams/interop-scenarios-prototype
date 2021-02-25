import os
import importlib
from setuptools import setup, find_packages

# get scenario name
__scenario__ = os.getenv("SCENARIO")
if __scenario__ is None:
    raise SystemError("SCENARIO is undefined, do not know how to proceed. A scenario is required!")

# get scenario module
scenario_module = importlib.import_module(__scenario__)


# Get scenario version
scenario_version = getattr(scenario_module, "scenario_version")
scenario_dependencies = getattr(scenario_module, "scenario_dependencies")


def package_files(directory=__scenario__, install_directory=__scenario__):
    """Determine the data files to include when the scenario is installed.

    :param directory: the base directory where all files reside
    :param install_directory: the directory where files are installed into
    :return: a list of tuples (install_dir, [base directory path])
    """
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        if path != directory:
            install_path = os.path.join(install_directory, path.split('/', 1)[-1])
        else:
            install_path = install_directory

        for filename in filenames:
            paths.append((install_path, [os.path.join(path, filename)]))
    return paths

setup(
    name=__scenario__,
    version=scenario_version,
    author="Author",
    author_email="author@somedomain.com",
    url="https://github.com/ryankwilliams/interop-scenarios-prototype",
    packages=find_packages(),
    data_files=package_files(),
    python_requires="~=3.6",
    install_requires=[
        "teflo"
    ] + scenario_dependencies,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License"
    ]
)
