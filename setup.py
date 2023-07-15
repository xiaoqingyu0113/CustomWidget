from setuptools import setup, find_packages

setup(
    name='customwidget',
    version='1.0.0',
    author='Qingyu Xiao',
    author_email='xiaoqingyu0113@gmail.com',
    description='Some morden widgets based on PyQt 6',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xiaoqingyu0113/CustomWidget.git',
    packages=find_packages(include=['customwidget']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='PyQt6, Widgets',
    install_requires=[
        # Add any dependencies required by your package here
        'pyqt6',
    ],
    # entry_points={
    #     'console_scripts': [
    #         'your_command=your_package.module:main',
    #     ],
    # },
)