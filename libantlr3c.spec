%define major	3
%define devname	%mklibname -d antlr3c
%define debug_package %nil

Summary:	Library for accessing antlr
Name:		libantlr3c
Version:	3.4
Release:	3
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.antlr3.org
Source0:	http://www.antlr3.org/download/C/libantlr3c-3.4.tar.gz

%description
C runtime for the ANTLR parsing library.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	antlr3c-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%prep
%setup -q
autoreconf -fiv

%build
%setup_compile_flags
%configure \
	--disable-static \
%ifarch x86_64 aarch64
	--enable-64bit \
%endif
	--enable-examples-build

%make

%install
%makeinstall_std

%files -n %{devname}
%{_libdir}/libantlr3c.so
%{_includedir}/*.h
