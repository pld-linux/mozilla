Summary:	Mozilla - web browser
Summary(pl):	Mozilla - przegl±darka WWW
Name:		mozilla
Version:	5.M15
Release:	1
License:	NPL
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	ftp://ftp.mozilla.org/pub/mozilla/releases/m15/src/%{name}-source-M15.tar.bz2
Source1:	mozilla.sh
Source2:	mozilla-icon.png
Source3:	mozilla.desktop
URL:		http://www.mozilla.org/projects/newlayout/
BuildRequires:	libstdc++-devel
BuildRequires:	gtk+-devel
BuildRequires:	glib-devel
BuildRequires:	ORBit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Mozilla is an open-source web browser, designed for standards
compliance, performance and portability. 

%description -l pl
Mozilla jest potê¿n± graficzn± przegl±dark± WWW, która jest
nastêpc± Netscape Navigatora.

%package devel
Summary:	Mozilla development crap
Summary(pl):	Mozilla - pliki nag³ówkowe i biblioteki
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Mozilla development libs and headers

%description -l pl devel
Biblioteki i pliki nag³ówkowe s³u¿±ce programowaniu.

%prep
%setup -q -n mozilla

%build
CFLAGS="$RPM_OPT_FLAGS" ; export CFLAGS
CXXFLAGS="$RPM_OPT_FLAGS" ; export CXXFLAGS
LDFLAGS="-s" ; export LDFLAGS
%configure \
	--with-pthreads \
	--enable-toolkit=gtk \
	--enable-x11-shm \
	--enable-optimize \
	--enable-strip-libs \
	--with-extensions \
	--disable-dtd-debug \
	--disable-debug \
	--disable-tests \
	--with-x \
	--with-jpeg \
	--with-zlib \
	--with-png \
	--disable-mailnews

make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_datadir}/{idl,pixmaps,applnk/Internet} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{chrome,defaults,res,icons} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/{components,plugins} \
	$RPM_BUILD_ROOT%{_includedir}

ln -s ../../share/mozilla/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -s ../../share/mozilla/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -s ../../share/mozilla/res $RPM_BUILD_ROOT%{_libdir}/%{name}/res
ln -s ../../share/mozilla/icons $RPM_BUILD_ROOT%{_libdir}/%{name}/icons

cp -fr dist/bin/chrome/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
cp -fr dist/bin/defaults/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
cp -fr dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -fr dist/bin/icons/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/icons
cp -fr dist/bin/components/*	$RPM_BUILD_ROOT%{_libdir}/%{name}/components
cp -fr dist/idl/*		$RPM_BUILD_ROOT%{_datadir}/idl
#cp -fr dist/include/gtkmozilla.h $RPM_BUILD_ROOT%{_includedir}

#install dist/lib/libgtkmozilla.{so.0.*,la} $RPM_BUILD_ROOT%{_libdir}
install dist/bin/*.so		$RPM_BUILD_ROOT%{_libdir}

# creating and installing register
LD_LIBRARY_PATH="dist/bin" \
MOZILLA_FIVE_HOME="dist/bin" \
    dist/bin/regxpcom
install dist/bin/component.reg $RPM_BUILD_ROOT%{_libdir}/%{name}

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/mozilla
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/applnk/Internet

install dist/bin/mozilla-bin $RPM_BUILD_ROOT%{_bindir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/%{name}/components/*.so \
	$RPM_BUILD_ROOT%{_libdir}/*.so* || :

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%attr(755,root,root) %{_libdir}/*.so*

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/components
%{_libdir}/%{name}/component.reg
%attr(755,root,root) %{_libdir}/%{name}/components/*.so
%{_libdir}/%{name}/components/*.xpt
%{_libdir}/%{name}/components/*.js
%{_libdir}/%{name}/plugins
%{_libdir}/%{name}/chrome
%{_libdir}/%{name}/defaults
%{_libdir}/%{name}/res
%{_libdir}/%{name}/icons

%{_datadir}/%{name}
%{_datadir}/pixmaps/mozilla-icon.png
%{_datadir}/applnk/Internet/mozilla.desktop

%files devel
%defattr(644,root,root,755)
#%{_libdir}/lib*.la
#%{_includedir}/*
%{_datadir}/idl/*
