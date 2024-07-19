import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/deylahm/Desktop/Simulacion Rotbot/Prueba-Ros2/install/occupancy_grid_demo'
