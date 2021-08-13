Name:		qrencode
Version:	4.1.1
Release:	2
Summary:	Compact library for encoding data in a QR Code symbol
License:	LGPLv2+
URL:		https://fukuchi.org/works/qrencode/
Source0:	https://fukuchi.org/works/qrencode/qrencode-%{version}.tar.bz2

BuildRequires:	gcc chrpath libpng-devel SDL-devel autoconf >= 2.69
BuildRequires:  qrencode

Provides:       qrencode-libs
Obsoletes:      qrencode-libs

%description
Libqrencode is a fast and compact library for encoding data in a QR 
Code symbol, a 2D symbology that can be scanned by handy terminals 
such as a mobile phone with CCD. The capacity of QR Code is up to 
7000 digits or 4000 characters and has high robustness.

Libqrencode accepts a string or a list of data chunks then encodes 
in a QR Code symbol as a bitmap array. While other QR Code 
applications generate an image file, using libqrencode allows 
applications to render QR Code symbols from raw bitmap data directly. 
This library also contains a command-line utility outputs QR Code 
images in various formats.

%package        devel
Summary:        Header files for qrencode
Requires:       %{name} = %{version}-%{release}

%description    devel
Header files for qrencode

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoconf
%configure --with-tests
%make_build

%install
%make_install 
%delete_la

chrpath --delete %{buildroot}%{_bindir}/qrencode

%ifnarch riscv64
#Include previous ABI version for temporary binary compatibility
cp -a %{_libdir}/libqrencode.so.3* %{buildroot}%{_libdir}
%endif

%check
pushd ./tests
sh test_all.sh
popd

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README
%{_bindir}/qrencode
%{_libdir}/libqrencode.so.*

%files          devel
%defattr(-,root,root)
%{_includedir}/qrencode.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files          help
%defattr(-,root,root)
%doc NEWS TODO
%{_mandir}/man1/qrencode.1*

%changelog
* Thu Aug 12 2021 lishiyang <lishiyangasdf1113@163.com> - 4.1.1-2
- Path modification error

* Thu Jan 28 2021 jinzhimin <jinzhimin2@huawei.com> - 4.1.1-1
- Upgrade to 4.1.1

* Tue Sep 17 2019 openEuler Buildteam <buildteam@openeuler.org> - 4.0.2-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add previous ABI version for temporary binary compatibility

* Thu Sep 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 4.0.2-1
- Package init
