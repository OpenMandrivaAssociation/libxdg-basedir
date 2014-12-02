%define major	1
%define libxdg	%mklibname xdg-basedir %{major}
%define devname	%mklibname xdg-basedir -d

Summary:	The XDG Base Directory specification defines where files should be looked for
Name:		libxdg-basedir
Version:	1.2.0
Release:	1
Group:		System/Libraries
License:	MIT
Url:		https://www.ohloh.net/p/libxdg-basedir
Source0:	http://n.ethz.ch/~nevillm/download/libxdg-basedir/libxdg-basedir-%{version}.tar.gz
BuildRequires:	doxygen

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
%setup -q

%build
%configure

%make

%install
%makeinstall_std

%files -n %{libxdg}
%{_libdir}/libxdg-basedir.so.%{major}*

%files -n %{devname}
%{_includedir}/basedir.h
%{_includedir}/basedir_fs.h
%{_libdir}/libxdg-basedir.so
%{_libdir}/pkgconfig/libxdg-basedir.pc

