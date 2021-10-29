from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'jupylint',
    version = '0.1.0',
    license='MIT',
    description = 'A tool to run pylint on Jupyter notebooks',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Edmund Goodman',
    author_email = 'egoodman3141@gmail.com',
    url = 'https://github.com/EdmundGoodman/Jupyter_Pylinter',
    download_url = 'https://github.com/EdmundGoodman/Jupyter_Pylinter/archive/refs/tags/v0.1.0.tar.gz',
    packages=find_packages(),
    keywords = ['Jupyter', 'Pylint', 'linter'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
