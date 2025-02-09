from setuptools import setup, find_packages

setup(
    name="django-success-response",
    version="1.1.1",
    description="Django app for customizing response",
    author="Quvonchbek Bobojonov",
    author_email="hi@moorfo.uz",
    url="https://github.com/QuvonchbekBobojonov/django-success-response",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=[],
    license="MIT",
    license_files=[
        "LICENSE",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Framework :: Django",
    ],
)
