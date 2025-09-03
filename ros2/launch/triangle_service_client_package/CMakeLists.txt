cmake_minimum_required(VERSION 3.5)
project(triangle_service_client_package)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Custom srv tanımla
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/TriangleCalc.srv"
)

ament_export_dependencies(rosidl_default_runtime)

ament_python_install_package(${PROJECT_NAME})
install(PROGRAMS ${PROJECT_NAME}/triangle_service.py
  RENAME triangle_service
  DESTINATION lib/${PROJECT_NAME})

install(PROGRAMS ${PROJECT_NAME}/triangle_client.py
  RENAME triangle_client
  DESTINATION lib/${PROJECT_NAME})
ament_package()
