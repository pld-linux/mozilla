%define ver		5.0
%define rel		SeaMonkey_M3_BRANCH_19990323
%define prefix	/usr
%define tmp		/builds/tmp

Summary:	Mozilla Mozilla
Name:		mozilla
Version:	%ver
Release:	%rel
Copyright:	NPL
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Source:		mozilla-%{ver}-%{rel}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
Packager:	Ramiro Estrugo <ramiro@netscape.com>
URL:		http://www.mozilla.org/projects/newlayout/
Provides:	mozilla
Requires:	nspr gtk+ >= 1.1.13 nspr-pthreads >= 3.1

%description
Mozilla

%package devel
Summary:	Mozilla development crap
Group:		X11/Development/Libraries
#Requires:	mozilla nspr-devel

#Obsoletes: libnspr-devel
#Conflicts: libnspr-userthreads-devel

%description devel
Mozilla development libs and headers

%prep
%setup -n mozilla

%build
./configure \
			--with-pthreads \
			--enable-toolkit=gtk \
			--disable-build-nspr \
			--enable-debug \
			--with-insure=no

make

%install
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib/mozilla/bin
mkdir -p $RPM_BUILD_ROOT%{prefix}/include/mozilla
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib/mozilla/idl
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib/mozilla/components
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib/mozilla/res
mkdir -p $RPM_BUILD_ROOT%{_bindir}

cp -rpv dist/bin/components/*.so $RPM_BUILD_ROOT%{prefix}/lib/mozilla/components
cp -rpv dist/bin/res/* $RPM_BUILD_ROOT%{prefix}/lib/mozilla/res
cp -rpv dist/bin/*.so $RPM_BUILD_ROOT%{prefix}/lib
cp -rpv dist/include/* $RPM_BUILD_ROOT%{prefix}/include/mozilla
cp -rpv dist/idl/* $RPM_BUILD_ROOT%{prefix}/lib/mozilla/idl
cp -rpv dist/lib/*.a $RPM_BUILD_ROOT%{prefix}/lib
cp -rpv dist/bin/apprunner $RPM_BUILD_ROOT%{prefix}/lib/mozilla/bin
cp -rpv dist/bin/viewer $RPM_BUILD_ROOT%{prefix}/lib/mozilla/bin
cp -rpv dist/bin/vreg $RPM_BUILD_ROOT%{prefix}/lib/mozilla/bin

cp -rpv build/mozilla-viewer.sh $RPM_BUILD_ROOT%{_bindir}/mozilla-viewer
cp -rpv build/mozilla-apprunner.sh $RPM_BUILD_ROOT%{_bindir}/mozilla-apprunner

%clean
rm -rf $RPM_BUILD_ROOT

%post

#if grep "/usr/mozilla/lib" /etc/ld.so.conf > /dev/null 2>&1
#then
#	:
#else
#	echo "/usr/mozilla/lib" >> /etc/ld.so.conf
#fi
#
#/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%attr(-,root,root)

%{prefix}/lib/mozilla/components/*
%{prefix}/lib/*.so
%{prefix}/lib/mozilla/bin/*
%{prefix}/lib/mozilla/res/*
%attr(755,root,root)%{_bindir}/mozilla-viewer
%attr(755,root,root)%{_bindir}/mozilla-apprunner

%files devel
%attr(-,root,root)

%{prefix}/lib/*.a
%{prefix}/include/mozilla/*
%{prefix}/lib/mozilla/idl/*
