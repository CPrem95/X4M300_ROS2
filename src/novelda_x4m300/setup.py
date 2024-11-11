from setuptools import find_packages, setup
import os # for launch
from glob import glob # for launch

package_name = 'novelda_x4m300'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.py')),
        (os.path.join('share', package_name), glob('launch/*.launch')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
        (os.path.join('share', package_name, package_name, 'scripts/python35/pymoduleconnector/moduleconnectorwrapper'), glob('*.so')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arms',
    maintainer_email='charithprem@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'uwbTalker = novelda_x4m300.scripts.readUWB:main',
        	'uwbListener = novelda_x4m300.scripts.plotUWB:main',
        	'test = novelda_x4m300.scripts.publisher:main',
        ],
    },
)
