Summary: Mapbox GL Native Qt version
Name: qmapboxgl
Version: 1.1.0
Release: 1%{?dist}
License: Open Source
Group: Libraries/Geosciences
URL: https://github.com/mapbox/mapbox-gl-native

Source: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: opt-gcc6 gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

#Requires: proj

%description
A library for embedding interactive, customizable vector maps into native applications on multiple platforms.
It takes stylesheets that conform to the Mapbox Style Specification, applies them to vector tiles that
conform to the Mapbox Vector Tile Specification, and renders them using OpenGL. Mapbox GL JS is the WebGL-based
counterpart, designed for use on the Web.

%prep
%setup -q -n %{name}-%{version}/mapbox-gl-native

%build
cp ../mapbox-gl-native-lib.pro .

%qmake5 mapbox-gl-native-lib.pro \
    VERSION='%{version}-%{release}'


%{__make} CXX=/opt/gcc6/bin/g++ CC=/opt/gcc6/bin/gcc LINK=/opt/gcc6/bin/g++ %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%qmake5_install

%clean
%{__rm} -rf %{buildroot}

%pre

%files
%defattr(-, root, root, 0755)
%{_libdir}/libqmapboxgl.a
%{_includedir}/qt5/mbgl
%{_includedir}/qt5/Q*Mapbox*
%{_includedir}/qt5/qmapbox*

%changelog
* Sat Sep 9 2017 rinigus <rinigus.git@gmail.com> - 1.1.0-1
- initial packaging release for SFOS
