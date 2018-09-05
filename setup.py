from setuptools import setup

setup(name='signed_clustering',
      version='0.1.0',
      description='A package for clustering signed networks',
      long_description=open('README.txt').read(),
      author='Peter Davies, Aldo Glielmo',
      author_email='p.w.davies@warwick.ac.uk, aldo.glielmo@kcl.ac.uk',
      packages=['SigNet'],
      install_requires=['numpy','scipy','scikit-learn','cvxpy'],
      zip_safe=False)