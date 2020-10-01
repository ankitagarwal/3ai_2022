import os
import sys
from setuptools import Extension, setup


if sys.version_info[:2] < (3, 7):
    raise RuntimeError("Python version >= 3.7 required.")

with open("README.md", "r") as fh:
    long_description = fh.read()


def generate_extensions() -> list:
    """
        Method to generate cython extensions.
    Returns:
        list: List of extensions.
    """

    root_path = os.path.abspath(os.path.dirname(__file__))

    # Move this to config.
    exclude = ["tests", "__pycache__"]
    extensions = []
    for root, dirs, files in os.walk(root_path + "/lola_tools"):
        # Delete the folders which are not included for packaging.
        [dirs.remove(dir) for dir in list(dirs) if dir in exclude]
        directory = os.path.relpath(root)

        # Create the Extension required the directories.
        extension = Extension(directory.replace(os.sep, ".") + ".*", [os.path.join(directory, '*.py')])
        extensions.append(extension)

    return extensions


setup(
    ext_modules=generate_extensions(),
    name="baby_skynet",
    version="1.0",
    author="Arnold",
    author_email="arnold@has.to.come",
    description="A package for reaching Transcendence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ankitagarwal/pycon_2020",
    license="GPL3",
    packages=[],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: LINUX",
        "Operating System :: Apple :: MacOS",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    platforms=["Windows", "Linux", "MacOS"],
    test_suite="pytest",
    python_requires='>=3.7',
    data_files=[
        ('baby-skynet', ['README.md']),
        ('baby-skynet', ['requirements.txt']),
    ],
)
