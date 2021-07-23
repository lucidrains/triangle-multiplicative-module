from setuptools import setup, find_packages

setup(
  name = 'triangle-multiplicative-module',
  packages = find_packages(),
  version = '0.0.2',
  license='MIT',
  description = 'Triangle Multiplicative Module',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/triangle-multiplicative-module',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'protein folding'
  ],
  install_requires=[
    'einops>=0.3',
    'torch>=1.7'
  ],
  setup_requires=[
    'pytest-runner',
  ],
  tests_require=[
    'pytest'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
