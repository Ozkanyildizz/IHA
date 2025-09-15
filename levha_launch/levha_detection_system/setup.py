from setuptools import setup

package_name = 'levha_detection_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/srv', ['srv/LevhaList.srv']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ozkan',
    maintainer_email='yildizozkan6541@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = levha_detection_system.server:main',
            'client = levha_detection_system.client:main',
            'subscriber = levha_detection_system.subscriber:main',
        ],
    },
)
