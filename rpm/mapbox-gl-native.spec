Summary: Mapbox GL Native Qt version
Name: qmapboxgl
Version: 1.5.0
Release: 3%{?dist}
License: Open Source
Group: Libraries/Geosciences
URL: https://github.com/mapbox/mapbox-gl-native

Source: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  cmake
BuildRequires:  opt-gcc gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(icu-uc)

#Requires: proj

%description
A library for embedding interactive, customizable vector maps into native applications on multiple platforms.
It takes stylesheets that conform to the Mapbox Style Specification, applies them to vector tiles that
conform to the Mapbox Vector Tile Specification, and renders them using OpenGL. Mapbox GL JS is the WebGL-based
counterpart, designed for use on the Web.

%package devel
Summary:        Development files for %{name}
License:        Open Source
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers for %{name}.

%prep
%setup -q -n %{name}-%{version}/mapbox-gl-native

%build
CXX=/opt/gcc/bin/g++
CC=/opt/gcc/bin/gcc
LINK=/opt/gcc/bin/g++
LDFLAGS=-L/opt/gcc6/lib -static-libstdc++
%cmake -DCMAKE_C_COMPILER=/opt/gcc/bin/gcc -DCMAKE_CXX_COMPILER=/opt/gcc/bin/g++ -DMBGL_WITH_QT=ON -DBUILD_WARNING_AS_ERROR=OFF -DCMAKE_INSTALL_PREFIX:PATH=/usr -DMBGL_WITH_QT_HEADLESS=OFF -DMBGL_WITH_QT_TEST=OFF -DMBGL_WITH_QT_DEMO=OFF .
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%files
%defattr(-, root, root, 0755)
%{_libdir}/libqmapboxgl.*

%files devel
%{_includedir}/mbgl
%{_includedir}/qt5/Q*Mapbox*
%{_includedir}/qt5/qmapbox*

%changelog
* Sat Mar 10 2018 rinigus <rinigus.git@gmail.com> - 1.3.0-1
- update to the current upstream version

* Sat Sep 9 2017 rinigus <rinigus.git@gmail.com> - 1.1.0-1
- initial packaging release for SFOS
