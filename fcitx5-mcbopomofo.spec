%global   debug_package %{nil}
%undefine _enable_debug_packages

Name:    fcitx5-mcbopomofo
Version: 3.0
Release: 1
License: MIT
Summary: McBopomofo for fcitx5
URL:     https://github.com/openvanilla/fcitx5-mcbopomofo
Source0: %{url}/archive/refs/tags/%{version}/fcitx5-mcbopomofo-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(Fcitx5Core)
BuildRequires:  pkgconfig(Fcitx5Module)
BuildRequires:  pkgconfig(Fcitx5Utils)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(json-c)

Requires:       fcitx5
Requires:       fcitx5-configtool
Requires:       fcitx5-gtk
Requires:       fcitx5-qt

%description
McBopomofo for fcitx5

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
    -GNinja \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DENABLE_TEST=Off
%cmake_build

%install
%cmake_install
chmod a+x %{buildroot}/%{_datadir}/fcitx5/data/mcbopomofo-add-phrase-hook.sh

%files
%{_libdir}/fcitx5/mcbopomofo.so
%{_datadir}/fcitx5/addon/mcbopomofo.conf
%{_datadir}/fcitx5/data/mcbopomofo-add-phrase-hook.sh
%{_datadir}/fcitx5/data/mcbopomofo-associated-phrases-v2.txt
%{_datadir}/fcitx5/data/mcbopomofo-bpmfvs-pua.txt
%{_datadir}/fcitx5/data/mcbopomofo-bpmfvs-variants.txt
%{_datadir}/fcitx5/data/mcbopomofo-data-plain-bpmf.txt
%{_datadir}/fcitx5/data/mcbopomofo-data.txt
%{_datadir}/fcitx5/data/mcbopomofo-dictionary-service.json
%{_datadir}/fcitx5/inputmethod/mcbopomofo.conf
%{_datadir}/fcitx5/inputmethod/mcbopomofo-plain.conf
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/locale/*/LC_MESSAGES/fcitx5-mcbopomofo.mo
%{_metainfodir}/org.fcitx.Fcitx5.Addon.McBopomofo.metainfo.xml

%changelog
%autochangelog
