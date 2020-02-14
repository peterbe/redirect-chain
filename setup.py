from os import path

from setuptools import setup


_here = path.dirname(__file__)

setup(
    name="redirect-chain",
    version="0.1.0",
    description="Shows the redirect chain of a URL from start to end",
    long_description=open(path.join(_here, "README.md")).read(),
    long_description_content_type='text/markdown',
    author="Peter Bengtsson",
    author_email="mail@peterbe.com",
    license="MIT",
    py_modules=["main"],
    entry_points={"console_scripts": ["redirect-chain = main:main"]},
    url="https://github.com/peterbe/redirect-chain",
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=["requests"],
    tests_require=[],
    setup_requires=[],
    extras_require={},
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords=[],
)
