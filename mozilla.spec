Summary:	Mozilla
Name:		mozilla
Version:	0.M13
Release:	1
Copyright:	NPL
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Source:		%{name}-source-M13.tar.bz2
URL:		http://www.mozilla.org/projects/newlayout/
BuildRequires:	gtk+-devel
BuildRequires:	glib-devel
BuildRequires:	ORBit-devel
Requires:	gtk+ >= 1.2.0
Requires:	glib >= 1.2.0
Requires:	ORBit >= 0.5.0
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Mozilla

%package devel
Summary:	Mozilla development crap
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Mozilla development libs and headers

%prep
%setup -q -n mozilla

%build
CFLAGS="$RPM_OPT_FLAGS" ; export CFLAGS
CXXFLAGS="$RPM_OPT_FLAGS" ; export CXXFLAGS
LDFLAGS="-s" ; export LDFLAGS
./configure \
	--with-pthreads \
	--enable-toolkit=gtk \
	--enable-x11-shm \
	--enable-optimize \
	--enable-strip-libs \
	--with-extensions \
	--disable-dtd-debug \
	--disable-debug \
	--disable-tests \
	--with-jpeg \
	--with-zlib \
	--with-png \
	--disable-mailnews

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/mozilla/idl,%{_includedir},%{_bindir}}

cp -rp dist/bin/* $RPM_BUILD_ROOT/%{_libdir}/mozilla/
cp -rp dist/include/gtkmozilla.h $RPM_BUILD_ROOT%{_includedir}/
cp -rp dist/lib/libgtkmozilla.{so.0.0.0,la} $RPM_BUILD_ROOT%{_libdir}/
cp -rp dist/idl/* $RPM_BUILD_ROOT/%{_libdir}/mozilla/idl/

rm -rf $RPM_BUILD_ROOT/%{_libdir}/mozilla/*{Test,test}*

ln -sf %{_libdir}/mozilla/mozilla $RPM_BUILD_ROOT%{_bindir}/mozilla
(cd $RPM_BUILD_ROOT%{_libdir} ; ln -s libgtkmozilla.so.0.0.0 libgtkmozilla.so)

perl -p -i -e "s|^dist_bin.*|dist_bin=%{_libdir}/mozilla/|" \
	$RPM_BUILD_ROOT%{_libdir}/mozilla/mozilla

perl -p -i -e 's|^MOZILLA_BIN.*|MOZILLA_BIN=\"\$dist_bin/mozilla-bin\"|' \
	$RPM_BUILD_ROOT%{_libdir}/mozilla/mozilla

perl -p -i -e "s|^MOZ_DIST_BIN.*|MOZ_DIST_BIN=\"%{_libdir}/mozilla/\"|" \
	$RPM_BUILD_ROOT%{_libdir}/mozilla/run-mozilla.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
cd %{_libdir}/mozilla ; LD_LIBRARY_PATH=. ./regxpcom

%preun
rm -f %{_libdir}/mozilla/component.reg

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/mozilla
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/plugins
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/mozilla/chrome
%{_libdir}/mozilla/components/*.xpt
%attr(755,root,root) %{_libdir}/mozilla/components/*.so
%{_libdir}/mozilla/defaults
%{_libdir}/mozilla/res
%attr(755,root,root) %{_libdir}/mozilla/*.so
%attr(755,root,root) %{_libdir}/mozilla/*mozilla*
%attr(755,root,root) %{_libdir}/mozilla/*reg*
%attr(755,root,root) %{_libdir}/mozilla/xp*
%attr(755,root,root) %{_libdir}/mozilla/*browser
%attr(755,root,root) %{_libdir}/mozilla/nsinstall

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_libdir}/mozilla/idl
