%global plugin_name matrix

%global commit0 f26edd53ff81b21530d06e687ae223e15a015d79
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date 20180927

Name: purple-%{plugin_name}
Version: 0
Release: 12.%{date}git%{shortcommit0}%{?dist}
Summary: Matrix plugin for libpurple

License: GPLv2+
URL: https://github.com/matrix-org/purple-matrix
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

# Pull request sent: https://github.com/matrix-org/purple-matrix/pull/49
Patch0: 0001-Respect-target-CFLAGS.patch

BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(purple)
BuildRequires: http-parser-devel
BuildRequires: libgcrypt-devel
BuildRequires: libolm-devel
BuildRequires: gcc

%package -n pidgin-%{plugin_name}
Summary: Adds pixmaps, icons and smileys for Matrix protocol
BuildArch: noarch
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pidgin

%description
Adds support for Matrix to Pidgin, Adium, Finch and other libpurple
based messengers.

%description -n pidgin-%{plugin_name}
Adds pixmaps, icons and smileys for Matrix protocol implemented by
purple-matrix.

%prep
%autosetup -n %{name}-%{commit0}

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md CHANGES.md AUTHORS.rst CONTRIBUTING.rst
%{_libdir}/purple-2/lib%{plugin_name}.so

%files -n pidgin-%{plugin_name}
%{_datadir}/pixmaps/pidgin/protocols/*/%{plugin_name}.png

%changelog
* Sat Jan 05 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 0-12.20180927gitf26edd5
- Rebuilt due to libolm update.

* Wed Nov 21 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-11.20180927gitf26edd5
- Updated to latest snapshot.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20180325git49ea988
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 04 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-9.20180325git49ea988
- Updated to latest snapshot.

* Sun Feb 25 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0-8.20180224gitca2f214
- Updated to latest snapshot.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20170902gitf4ab172
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-6.20170902gitf4ab172
- Updated to latest snapshot.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20170530gitbe53d53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20170530gitbe53d53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-3.20170530gitbe53d53
- Small fixes.

* Thu Jun 22 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-2.20170530gitbe53d53
- Small fixes.

* Thu Jun 22 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0-1.20170530gitbe53d53
- First SPEC release.
