from distutils.core import setup

setup(
    name="redupy",
    packages=["redupy"],
    version="0.0.9",
    description="Wrapper for redu api",
    long_description=open("README.markdown").read(),
    author="Igor Calabria",
    author_email="igor@redu.com.br",
    url="https://github.com/redu/redupy/",
    keywords=["web", "REST API", "redu"],
    install_requires=["simplejson>=2.6.1", "rauth>=0.4.14", "requests>=0.13.6"],
    classifiers=["Programming Language :: Python",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 2 - Pre-Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules"]
)
