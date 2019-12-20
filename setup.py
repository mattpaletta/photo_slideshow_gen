try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

requirements = []
with open('requirements-freeze.txt', "r") as requirements_file:
    for line in requirements_file:
        requirements.append(line.strip())

setup(
    name = "photo-slideshow-gen",
    version = "0.0.1",
    url = 'https://github.com/mattpaletta/photo-slideshow-gen',
    packages = find_packages(),
    include_package_data = True,
    install_requires = requirements,
    author = "Matthew Paletta",
    author_email = "mattpaletta@gmail.com",
    description = "Utility to generate a slideshow from a folder of images.",
    license = "BSD",
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications',
    ],
    entry_points={
        'console_scripts': [
            'photo_slideshow = slideshow.__main__:main',
        ]
    },
    package_data={'slideshow': ['haarcascades/haarcascade_frontalface_alt.xml', 'haarcascades/haarcascade_profileface.xml', 'haarcascades/haarcascade_fullbody.xml']},
)
