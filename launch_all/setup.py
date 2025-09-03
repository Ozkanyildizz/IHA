from setuptools import setup
import os
from glob import glob

package_name = 'launch_all'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ozkan',
    maintainer_email='yildizozkan6541@gmail.com',
    description='Launch file to start multiple packages',
    license='Apache-2.0',
    entry_points={},
)

