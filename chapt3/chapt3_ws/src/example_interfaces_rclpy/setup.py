from setuptools import find_packages, setup

package_name = 'example_interfaces_rclpy'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fishros',
    maintainer_email='fishros@foxmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'example_interfaces_control_02 = example_interfaces_rclpy.example_interfaces_control_02:main',
          'example_interfaces_robot_02 = example_interfaces_rclpy.example_interfaces_robot_02:main'
        ],
    },
)
