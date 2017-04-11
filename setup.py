from setuptools import setup, find_packages
import os

HERE = os.path.abspath(os.path.dirname(__file__))
def get_long_description():
    dirs = [ HERE ]
    if os.getenv("TRAVIS"):
        dirs.append(os.getenv("TRAVIS_BUILD_DIR"))

    long_description = ""

    for d in dirs:
        rst_readme = os.path.join(d, "README.rst")
        if not os.path.exists(rst_readme):
            continue

        with open(rst_readme) as fp:
            long_description = fp.read()
            return long_description

    return long_description

long_description = get_long_description()

version = '0.0.2'
setup(
    name="tee",
    version=version,
    description="Python library to tee stderr/stdout temporarily",
    long_description=long_description,
    keywords='tee',
    author='Anthony Rebello',
    author_email="rebello.anthony@gmail.com",
    url="https://github.com/algrebe/python-tee",
    download_url="https://github.com/algrebe/python-tee/tarball/%s" % version,
    license='MIT License',
    package_dir={'tee': 'tee'},
    packages=find_packages('.', exclude=['tests*']),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ]
)
