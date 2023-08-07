from setuptools import setup

setup(
    name='google_cse_scraper',
    version='1.0',
    packages=['google_cse_scraper'],
    install_requires=[
        'requests',
        # Add any other dependencies your project needs
    ],
    entry_points={
        'console_scripts': [
            'google_cse_scraper = google_cse_scraper.__main__:main',
        ],
    },
)
