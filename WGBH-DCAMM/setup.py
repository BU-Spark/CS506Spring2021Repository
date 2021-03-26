from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

tests_require = [
    'pytest',
    'pytest-cov',
    'testfixtures',
    'scipy',
    'matplotlib',
    'cycler',
    'joblib',
    'kiwisolver',
    'matplotlib',
    'nltk',
    'numpy',
    'pandas',
    'Pillow',
    'pyparsing',
    'python-dateutil',
    'pytz',
    'scikit-learn',
    'scipy',
    'seaborn',
    'six',
    'sklearn',
    'threadpoolctl',
    'tox',
    'wheel',
    'PyPDF2',
    'tabula-py',
    'camelot-py'
]

setup(
  name='WGBH',
  packages=['tests','src','src.parsers'],
  version='0.0.1',
  description='Run WGBH Transform',
  entry_points={
    'console_scripts': ['wgbh=wgbh.cli:main'],
  },
  install_requires=[],
  python_requires='>=3.9, <4',
  setup_requires=['pytest-runner'],
  tests_require=tests_require,
  extras_require={
    'test': tests_require,
  },
  long_description=long_description,
  long_description_content_type="text/markdown",
  license="Apache License 2.0",
  include_package_data=True,
  classifiers=[
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
