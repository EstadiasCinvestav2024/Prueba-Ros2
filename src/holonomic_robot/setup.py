from setuptools import setup 

 

package_name = 'holonomic_robot' 

 

setup( 

    name=package_name, 

    version='0.0.0', 

    packages=[package_name], 

    data_files=[ 

        ('share/ament_index/resource_index/packages', 

            ['resource/' + package_name]), 

        ('share/' + package_name, ['package.xml']), 

        ('share/' + package_name + '/launch', launch_files), 
        ('share/' + package_name + '/urdf', ['urdf/holonomic_robot.urdf']),
        ('share/' + package_name + '/config', ['config/nav2_params.yaml']),  # Incluye tus archivos .yaml aquí
        ('share/' + package_name + '/scripts', ['scripts/navigate_robot.py']),


    ], 

    install_requires=['setuptools'], 

    zip_safe=True, 

    maintainer='deylahm', 

    maintainer_email='deylahm@todo.todo', 

    description='TODO: Package description', 

    license='TODO: License declaration', 

    tests_require=['pytest'], 

    entry_points={ 

        'console_scripts': [ 


        ], 

    }, 

) 