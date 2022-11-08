# -*- coding: utf-8 -*-
"""
This module contains the tool of plone.recipe.filestorage
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


version = '0.7'

long_description = (
        'Detailed Documentation\n'
        '**********************\n'
        + '\n' +
        read('README.rst')
        + '\n' +
        'Change history\n'
        '**************\n'
        + '\n' +
        read('CHANGES.txt')
        + '\n' +
        'Contributors\n'
        '************\n'
        + '\n' +
        read('CONTRIBUTORS.txt')
)
entry_point = 'plone.recipe.filestorage:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}

tests_require = ['zope.testing', 'manuel']

setup(name='plone.recipe.filestorage',
      version=version,
      description="This recipe aids the creation and management of multiple Zope 5 filestorages.",
      long_description=long_description,
      classifiers=[
          'Framework :: Buildout',
          'Framework :: Zope5',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python :: 3.6',
          'License :: OSI Approved :: Zope Public License',
      ],
      keywords='buildout zope zeo zodb mountpoint filestorage',
      author='Albert Ormazabal',
      author_email='aormazabal@tda.ad',
      url='https://github.com/aormazabal/plone.recipe.filestorage',
      download_url='https://github.com/aormazabal/plone.recipe.filestorage/archive/refs/tags/0.7.tar.gz',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout',
                        'plone.recipe.zope2instance',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(test=tests_require),
      test_suite='plone.recipe.filestorage.tests.test_docs.test_suite',
      entry_points=entry_points,
      )
