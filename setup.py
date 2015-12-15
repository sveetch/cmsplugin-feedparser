from setuptools import setup, find_packages

setup(
    name='cmsplugin-feedparser',
    version=__import__('cmsplugin_feedparser').__version__,
    description=__import__('cmsplugin_feedparser').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='sveetch@gmail.com',
    url='https://github.com/sveetch/cmsplugin-feedparser',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.6',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'django-cms>=3.0.1',
        'django-feedparser>=0.2.0',
    ],
    include_package_data=True,
    zip_safe=False
)