build() {
cd cpp
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$PREFIX -DPYTHON_EXECUTABLE=$(command -v python) ..
cmake --build . --config Release
}
