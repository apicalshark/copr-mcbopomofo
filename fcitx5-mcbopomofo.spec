%undefine _hardened_build
%define __global_cflags %nil
%define __global_cxxflags %nil
%define __global_fflags %nil
%define __global_fcflags %nil
%define __global_ldflags %nil

Name: fcitx5-mcbopomofo
Version: 2.9.1
Release: 1
License: MIT
Summary:  McBopomofo for fcitx5
URL: https://github.com/openvanilla/fcitx5-mcbopomofo
Source0: %{url}/archive/refs/tags/%{version}/fcitx5-mcbopomofo-%{version}.tar.gz

BuildRequires: git
BuildRequires: gcc g++
BuildRequires: fcitx5
BuildRequires: fcitx5-configtool
BuildRequires: fcitx5-devel
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: fmt-devel
BuildRequires: libicu-devel
BuildRequires: json-c-devel
BuildRequires: ninja-build
BuildRequires: clang-tools-extra

Requires: fcitx5 fcitx5-configtool fcitx5-gtk4 fcitx5-gtk3 fcitx5-gtk


%description
McBopomofo for fcitx5.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir build
pushd build
cmake ../ -GNinja -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DENABLE_CLANG_TIDY=On
ninja
popd

%install
pushd build
DESTDIR=$RPM_BUILD_ROOT ninja install
popd

%files
%{_libdir}/fcitx5/mcbopomofo.so
%{_datadir}/fcitx5/addon/mcbopomofo.conf
%{_datadir}/fcitx5/data/*
%{_datadir}/fcitx5/inputmethod/mcbopomofo.conf
%{_datadir}/fcitx5/inputmethod/mcbopomofo-plain.conf
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/locale/*/LC_MESSAGES/fcitx5-mcbopomofo.mo
%{_metainfodir}/org.fcitx.Fcitx5.Addon.McBopomofo.metainfo.xml

%changelog
%autochangelog
