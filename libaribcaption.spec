Summary:	Portable ARIB STD-B24 Caption Decoder/Renderer
Summary(pl.UTF-8):	Przenośny dekoder/renderer napisów ARIB STD-B24
Name:		libaribcaption
Version:	1.1.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/xqq/libaribcaption/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6315ebaf84c538654c0c69cd8fa0c8f3
URL:		https://github.com/xqq/libaribcaption/
BuildRequires:	cmake >= 3.11
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	libstdc++-devel >= 6:7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portable caption decoder/renderer for handling ARIB STD-B24 based TV
broadcast captions.

%description -l pl.UTF-8
Przenośny dekoder/renderer napisów obsługujący napisy telewizyjne ARIB
STD-B24.

%package devel
Summary:	Header files for aribcaption library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki aribcaption
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:7

%description devel
Header files for aribcaption library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki aribcaption.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%lang(ja) %doc README_ja.md
%attr(755,root,root) %{_libdir}/libaribcaption.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/aribcaption
%{_pkgconfigdir}/libaribcaption.pc
%{_libdir}/cmake/aribcaption
