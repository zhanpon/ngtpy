cmake_minimum_required(VERSION 3.15...3.19)

project(ngtpy VERSION "0.1.1")

if(SKBUILD)
  # Scikit-Build does not add your site-packages to the search path
  # automatically, so we need to add it _or_ the pybind11 specific directory
  # here.
  execute_process(
    COMMAND "${PYTHON_EXECUTABLE}" -c
            "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE _tmp_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE COMMAND_ECHO STDOUT)
  list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")
endif()

# Enable this option if you want to build wheels for PyPI
if(PORTABLE_WHEEL)
  set(NGT_MARCH_NATIVE_DISABLED, ON)
  set(NGT_AVX_DISABLED ON)
else()
  add_compile_options(-Ofast -march=native -DNDEBUG)
endif()

add_subdirectory(extern/NGT EXCLUDE_FROM_ALL)

find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(_ngtpy MODULE src/ngtpy/_ngtpy.cpp)

find_package(OpenMP REQUIRED)
target_link_libraries(_ngtpy PUBLIC OpenMP::OpenMP_CXX)

target_link_libraries(_ngtpy PUBLIC ngtstatic)
target_include_directories(_ngtpy PUBLIC extern/NGT/lib PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/extern/NGT/lib)

install(TARGETS _ngtpy DESTINATION .)
