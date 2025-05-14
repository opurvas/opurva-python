import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(name='opurva',
      version='1.0.5',
      description='sdk for opurva api',
      author='Support',
      author_email='support@opurva.com',
      url='https://github.com/opurvas/opurva-python.git',
      install_requires=['twilio==6.20.0'],
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=setuptools.find_packages(),
      include_package_data=True,
      classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
      ],
      python_requires='>=3.6'
)
