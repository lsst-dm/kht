build() {
cd cpp
mkdir build
cd build
CFLAGS="-I$CONDA_PREFIX/include/eigen3 $CFLAGS"
CXXFLAGS="-I$CONDA_PREFIX/include/eigen3 $CXXFLAGS"
cmake -DCMAKE_INSTALL_PREFIX=$PREFIX -DPYTHON_EXECUTABLE=$(command -v python) ..
cmake --build . --config Release
}
