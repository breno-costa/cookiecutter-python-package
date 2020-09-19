from setuptools import setup, find_packages

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

requirements = [
    {%- if cookiecutter.command_line_interface|lower == 'fire' %}'fire',{%- endif %}
]

setup(
    author="{{ cookiecutter.author_name.replace('\"', '\\\"') }}",
    email='{{ cookiecutter.author_email }}',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    name='{{ cookiecutter.project_slug }}',
    description="{{ cookiecutter.project_short_description }}",
    version='{{ cookiecutter.version }}',
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    keywords='{{ cookiecutter.project_slug }}',
    packages=find_packages(
        include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*'],
        exclude=['tests*']
    ),
    install_requires=requirements,
{%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
{%- endif %}
)