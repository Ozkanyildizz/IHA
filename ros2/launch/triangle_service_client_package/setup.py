from setuptools import setup

package_name = 'triangle_service_client_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/srv', ['srv/TriangleCalc.srv']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='ROS2 üçgen hesaplama servisi',
    license='MIT',
    entry_points={
        'console_scripts': [
            'triangle_service = triangle_service_client_package.triangle_service:main',
            'triangle_client = triangle_service_client_package.triangle_client:main',
        ],
    },
)
