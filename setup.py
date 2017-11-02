from setuptools import setup

setup(name='scholar',
      version='0.1.0',
      description='Get Google Scholar results',
      url='https://github.com/maenu/scholar.py',
      author='Christian Kreibich',
      author_email='',
      license='BSD',
      packages=['scholar'],
      install_requires=[
          'beautifulsoup4',
      ],
      scripts=['scholar/scholar.py'],
      zip_safe=False)