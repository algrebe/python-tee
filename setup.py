from setuptools import setup, find_packages

version = '0.0.1'
setup(
    name="tee",
    version=version,
    description="Python library to tee stderr/stdout temporarily",
    long_description="Python library to tee stderr/stdout temporarily",
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
