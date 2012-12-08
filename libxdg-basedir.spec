%define major 1
%define libxdg %mklibname xdg-basedir %{major}
%define libdev %mklibname xdg-basedir -d
%define libdevstatic %mklibname xdg-basedir -d -s

Name:		libxdg-basedir
Version:	1.1.1
Release:	%mkrel 1
Summary:	The XDG Base Directory specification defines where files should be looked for
Group:		System/Libraries
License:	MIT
URL:		https://www.ohloh.net/p/libxdg-basedir
Source0:	http://n.ethz.ch/~nevillm/download/libxdg-basedir/libxdg-basedir-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}-build

BuildRequires:	doxygen

%description
The XDG Base Directory Specification defines where should user files be looked
for by defining one or more base directories relative in with they should be
located.

This library implements functions to list the directories according to the
specification and provides a few higher-level functions.

#------------------------------------------------------------------------------
%package -n %{libxdg}
Summary:	The XDG Base Directory specification defines where files should be looked for
Group:		System/Libraries
Provides:	%{name} = %{version}

%description -n %{libxdg}
The XDG Base Directory Specification defines where should user files be looked
for by defining one or more base directories relative in with they should be
located
#------------------------------------------------------------------------------
%package -n %{libdev}
Summary:	Development Files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}
Provides:	xdg-basedir-devel = %{version}-%{release}

%description -n %{libdev}
Development Files for %{name}

%files -n %{libdev}
%defattr(-,root,root,-)
%_includedir/basedir.h
%_includedir/basedir_fs.h
%_libdir/libxdg-basedir.so
%_libdir/pkgconfig/libxdg-basedir.pc
#------------------------------------------------------------------------------
%package -n %{libdevstatic}
Summary:	Static development files for %{name}
Group:		Development/Other
Requires:	%{libdev} = %{version}
Provides:	libxdg-basedir-static-devel = %{version}-%{release}

%description -n %{libdevstatic}
Static development files for %{name}

%files -n %{libdevstatic}
%defattr(-,root,root,-)
%_libdir/libxdg-basedir.a
#------------------------------------------------------------------------------
%prep
%setup -q -n libxdg-basedir-%{version}

%build
%configure2_5x

%make


%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libxdg} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libxdg} -p /sbin/ldconfig
%endif

%files -n %{libxdg}
%defattr(-,root,root,-)
%_libdir/libxdg-basedir.so.1
%_libdir/libxdg-basedir.so.1.1.0


%changelog
* Sun Aug 08 2010 Rémy Clouard <shikamaru@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 567673
- bump release
- fix file list

* Sat Sep 19 2009 Rémy Clouard <shikamaru@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 444660
- bump release

* Thu May 21 2009 Rémy Clouard <shikamaru@mandriva.org> 1.0.1-1mdv2010.0
+ Revision: 378432
- new upstream release

* Sat May 16 2009 Rémy Clouard <shikamaru@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 376492
- fix static provides?\195
- fix major
- import libxdg-basedir


