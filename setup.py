from setuptools import setup, find_packages
import os

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='cv32e41p_diwall',
    version='1.0.0',
    description='Description of your package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mohamed EL BOUAZZATI',
    author_email='mohamed.el-bouazzati@univ-ubs.fr',  # Add your email address
    url='https://github.com/mohamedElbouazzati/cv32e41p_diwall.git',
    download_url='https://github.com/mohamedElbouazzati/cv32e41p_diwall/archive/refs/tags/v1.0.0.tar.gz',
    packages=find_packages(),
    include_package_data = True,
    python_requires='~=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='CV32E41P + Diwall',
    license='MIT',  # Add your license type
    project_urls={  # Add relevant project URLs
        'Documentation': 'https://github.com/mohamedElbouazzati/cv32e41p_diwall/wiki',
        'Source': 'https://github.com/mohamedElbouazzati/cv32e41p_diwall',
        'Tracker': 'https://github.com/mohamedElbouazzati/cv32e41p_diwall/issues',
    },
)
