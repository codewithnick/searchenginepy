from setuptools import setup, find_packages


setup(
    name='searchenginepy',
    version='0.1.0',
    license='MIT',
    author="Nikhil Singh",
    author_email='nikhilsingh52645@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/codewithnick/searchengine',
    keywords='example project',
    install_requires=[
          'requests',
      ],

)
