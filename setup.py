from setuptools import setup

def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='yopy',
    description="Zero characters communication for humans.",
    long_description=read('README.rst'),
    version='1.0.2',
    py_modules=['yopy'],
    author='Steven Loria',
    author_email='sloria1@gmail.com',
    url='https://github.com/sloria/yopy',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
        'awesome-slugify',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    entry_points={
        'console_scripts': [
            'yopy = yopy:main'
        ]
    },
)
