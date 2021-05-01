from setuptools import find_packages, setup

setup(
    name='django-ebhealthcheck',
    version='2.0.0',
    license='BSD',
    author='Sam Kingston',
    author_email='sjkingo88@gmail.com',
    description='Django app to add an instance\'s public IP to ALLOWED_HOSTS for Elastic Beanstalk\'s health check system',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sjkingo/django-ebhealthcheck',
    install_requires=['requests'],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
