import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/deylahm/Desktop/ros2 (copy)/install/holonomic_robot'
