# pkg-mapbox-gl-native

Originally, this package provided RPM packaging scripts of Mapbox GL
Native for Sailfish. It can also be used for install QMapboxGL native
as a library on desktop systems. 

For Sailfish, see OBS for example use. For Linux dekstop, instructions
are below.

This branch uses regular Qt HTTP client, as opposed to `sfos` branch
which is based on curl.

## Requirements

This package requires C++14 compiler, see Mapbox GL Native
requirements

## Linux desktop

Clone the repository:

```
git clone --recursive https://github.com/rinigus/pkg-mapbox-gl-native.git
```

Get to the repository folder:

```
cd pkg-mapbox-gl-native
```

Add link to PRO file:

```
ln -s ../mapbox-gl-native-lib.pro mapbox-gl-native
```

Make and change into build directory:
```
mkdir build && cd build
```

Generate Makefile:
```
qmake ../mapbox-gl-native/mapbox-gl-native-lib.pro
```

Compile
```
make -j4
```
and install
```
sudo make install
```
