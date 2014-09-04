from setuptools import setup, find_packages

version = "0.0.0"

long_description = ""
try:
    long_description=file('README.md').read()
except Exception:
    pass

license = ""
try:
    license=file('LICENSE').read()
except Exception:
    pass


setup(
    name = 'usbbd',
    version = version,
    description = 'USB BackDoor',
    author = 'Pablo Saavedra',
    author_email = 'saavedra.pablo@gmail.com',
    url = 'http://github.com/ataka-team/usbbd',
    packages = find_packages(),
    package_data={
    },
    scripts=[
        "tools/usbbd",
        "tools/usbbd-make-package",
        "tools/usbbd-make-template",
    ],
    zip_safe=False,
    install_requires=[
    ],
    data_files=[
        ('/usr/share/doc/usbbd/', ['cfg/usbbd.cfg.example']),
    #     ('/etc/init.d', ['init-script'])
    ],

    download_url= 'https://github.com/ataka-team/usbbd/zipball/master',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=long_description,
    license=license,
    keywords = "python usb backdoor",
)
