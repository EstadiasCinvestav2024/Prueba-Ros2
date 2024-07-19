from setuptools import setup 

  

package_name = 'occupancy_grid_demo' 

  

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

    maintainer='deylahm', 

    maintainer_email='deylahm@todo.todo', 

    description='Paquete para publicar una rejilla de ocupación', 

    license='TODO: License declaration', 

    tests_require=['pytest'], 

    entry_points={ 

        'console_scripts': [ 

            'occupancy_grid_publisher = occupancy_grid_demo.occupancy_grid_publisher:main' 

        ], 

    }, 

) 