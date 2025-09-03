from setuptools import setup

package_name = 'pub_sub_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
        'subscriber = pub_sub_package.subscriber:main',
        'publisher = pub_sub_package.publisher:main',
    ],
},
)
