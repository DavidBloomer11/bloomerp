from setuptools import find_packages, setup


setup(
    name="Bloomerp",
    version="0.1.9",
    packages=find_packages(),
    include_package_data=True,
    license="MIT License",
    description="Bloomerp is an open-source Business Management Software framework that lets you create fully functional business management applications just by defining your Django database models.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/davidbloomer11/Bloomerp",
    website="https://bloomerp.io",
    author="David Bloomer",
    author_email="bloomer.david@outlook.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests>=2.0.0',
        'djangorestframework>=3.12.0',
        'django-htmx>=1.0.0',
        'django-formtools>=2.3',
        'Pillow>=8.0.0',
        'psycopg2==2.9.9',
        'django-crispy-forms>=2.2',
        'django-filter>=24.3',
        'crispy-bootstrap5==2024.2',
        'xhtml2pdf>=0.2.16',
        'pandas>=2.0.0',
        'openpyxl>=3.1.5',
        'openai>=1.54.1',
        'plotly>=5.0.0',
        'PyPDF2>=3.0.1'
    ],
    extras_require={
        'images': ['Pillow>=8.0.0'],
    },
)