%define major	1
%define libxdg	%mklibname xdg-basedir %{major}
%define devname	%mklibname xdg-basedir -d

Summary:	The XDG Base Directory specification defines where files should be looked for
Name:		libxdg-basedir
Version:	1.2.3
Release:	2
Group:		System/Libraries
License:	MIT
Url:		https://github.com/devnev/libxdg-basedir
Source0:	https://github.com/devnev/libxdg-basedir/archive/%{name}-%{version}.tar.gz
#BuildRequires:	doxygen

%description
The XDG Base Directory Specification defines where should user files be looked
for by defining one or more base directories relative in with they should be
located.

This library implements functions to list the directories according to the
specification and provides a few higher-level functions.

%package -n %{libxdg}
Summary:	The XDG Base Directory specification defines where files should be looked for
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libxdg}
The XDG Base Directory Specification defines where should user files be looked
for by defining one or more base directories relative in with they should be
located.

%package -n %{devname}
Summary:	Development Files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Provides:	xdg-basedir-devel = %{version}-%{release}

%description -n %{devname}
Development Files for %{name}.

%prep
%autosetup -p1

%build
./autogen.sh
%configure

%make_build

%install
%make_install

%files -n %{libxdg}
%{_libdir}/libxdg-basedir.so.%{major}*

%files -n %{devname}
%{_includedir}/basedir.h
%{_includedir}/basedir_fs.h
%{_libdir}/libxdg-basedir.so
%{_libdir}/pkgconfig/libxdg-basedir.pc
