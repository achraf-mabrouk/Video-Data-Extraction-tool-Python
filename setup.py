from pip._vendor.idna import package_data
from setuptools import setup

setup(
    name='multimedia_data_mining_V2.1',
    version='1.0',
    packages=['GUI', 'Model', 'Database', 'SearchAPIs'],
    url='',
    license='',
    author='Achraf Mabrouk',
    author_email='mab.achraf95@gmail.com',
    description='this is an application for video data mining for research purposes realised in term of end project studies',
    install_requires=['PyQt5', 'youtube_dl', 'cv2', 'requests', 'gtts', 'PIL'],
    package_data={'Database': ['multimedia_content_mining.db']},
)
