from setuptools import setup, find_packages

setup(
    name='suprithgames',
    version='0.1.0',
    author='Sai Suprith',
    author_email='Chinnuong.1500@gmail.com',
    description='A collection of terminal-based games. Currently includes Tic Tac Toe with a scoreboard.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sai-suprith',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'tictacsu = suprithgames.tictacsu.cli:play_game',
        ]
    },
    include_package_data=True,
)
