from setuptools import setup

setup(name='library1',
      version='0.1',
      description='What the module does',
      url='https://github.com/kirigaikabuto/PythonLibraryExample',
      author='KirigaiKabuto',
      author_email='tleugazy98@gmail.com',
      license='MIT',
      packages=['library1'],
      install_requires=['numpy>=1.11',
                        'matplotlib>=1.5'])