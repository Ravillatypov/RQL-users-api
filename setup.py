from setuptools import setup

setup(
    name='django-rql-users-api',
    version='0.1',
    description=('Django-rql-users-api is a simple Django application'),
    long_description='',
    author='Ravil Latypov',
    author_email='ravillatypo12@gmail.com',
    url='https://github.com/Ravillatypov/RQL-users-api',
    packages=['rql_users_api'],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.4',
    install_requires=[
        'Django>=2.0',
        'djangorestframework>=3.9.0',
        'pyrql>=0.4.1'
    ],
    entry_points={
        'console_scripts': [
            'django-rql-users-api = rql_users_api.manage:run',
        ],
    },

)
