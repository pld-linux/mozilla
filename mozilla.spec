Summary:	Mozilla - web browser
Summary(pl):	Mozilla - przegl±darka WWW
Name:		mozilla
Version:	5.M16
Release:	1
License:	NPL
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	ftp://ftp.mozilla.org/pub/mozilla/releases/m16/src/%{name}-source-M16.tar.bz2
Source1:	mozilla.sh
Source2:	mozilla.desktop
Patch0:		mozilla-themes.patch
URL:		http://www.mozilla.org/projects/newlayout/
BuildRequires:	libstdc++-devel
BuildRequires:	libjpeg-devel
BuildRequires:	gtk+-devel
BuildRequires:	ORBit-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Mozilla is an open-source web browser, designed for standards compliance,
performance and portability.

%description -l pl
Mozilla jest potê¿n± graficzn± przegl±dark± WWW, która jest nastêpc±
Netscape Navigatora.

%package mailnews
Summary:	Mozilla - programs for mail and news
Summary(pl):	Mozilla - programy do poczty i newsów
Group:		X11/Applications/Networking
Group(pl):	X11/Aplikacje/Sieciowe
Requires:	%{name} = %{version}

%description mailnews
Programs for mail and news integrated with browser.

%description -l pl mailnews
Programy pocztowe i newsów zintegrowane z przegl±dark±.

%package devel
Summary:	Mozilla development crap
Summary(pl):	Mozilla - pliki nag³ówkowe i biblioteki
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	%{name}-mailnews = %{version}

%description devel
Mozilla development libs and headers.

%description -l pl devel
Biblioteki i pliki nag³ówkowe s³u¿±ce programowaniu.

%prep
%setup -q -n mozilla
%patch0 -p1

%build
CXXFLAGS="-fno-rtti -fno-exceptions"
MOZ_OPTIMIZE_FLAGS="$RPM_OPT_FLAGS"
LDFLAGS="-s"
export CXXFLAGS MOZ_OPTIMIZE_FLAGS LDFLAGS
%configure \
	--with-pthreads \
	--enable-optimize \
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
	--with-png

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Network/WWW} \
	$RPM_BUILD_ROOT%{_datadir}/{idl,pixmaps} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{chrome,defaults,res,icons,searchplugins} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/{components,plugins} \
	$RPM_BUILD_ROOT%{_includedir}

cat dist/bin/defaults/pref/all.js \
	| sed -e 's/http:\/\/www.mozilla.org\/projects\/seamonkey\/release-notes\//http:\/\/www.pld.org.pl\//g' \
	> dist/bin/defaults/pref/all.js.new
mv -f dist/bin/defaults/pref/all.js.new dist/bin/defaults/pref/all.js

# creating and installing register
LD_LIBRARY_PATH="dist/bin" \
MOZILLA_FIVE_HOME="dist/bin" \
dist/bin/regxpcom

install dist/bin/component.reg $RPM_BUILD_ROOT%{_libdir}/%{name}

# discussion feature: it's need to create some files (skin overview and others)
#LD_LIBRARY_PATH="dist/bin" \
#MOZILLA_FIVE_HOME="dist/bin" \
#dist/bin/mozilla-bin &
#sleep 20

ln -s ../../share/mozilla/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -s ../../share/mozilla/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -s ../../share/mozilla/res $RPM_BUILD_ROOT%{_libdir}/%{name}/res
ln -s ../../share/mozilla/icons $RPM_BUILD_ROOT%{_libdir}/%{name}/icons
ln -s ../../share/mozilla/searchplugins $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins

cp -fr dist/bin/chrome/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
cp -fr dist/bin/defaults/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
cp -fr dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -fr dist/bin/icons/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/icons
cp -fr dist/bin/searchplugins/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins
cp -fr dist/bin/components/*	$RPM_BUILD_ROOT%{_libdir}/%{name}/components
cp -fr dist/idl/*		$RPM_BUILD_ROOT%{_datadir}/idl
#cp -fr dist/include/gtkmozilla.h $RPM_BUILD_ROOT%{_includedir}

#install dist/lib/libgtkmozilla.{so.0.*,la} $RPM_BUILD_ROOT%{_libdir}
install dist/bin/*.so		$RPM_BUILD_ROOT%{_libdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/mozilla
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
cp -fr dist/bin/icons/mozicon16.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/mozilla-icon.xpm

install dist/bin/mozilla-bin $RPM_BUILD_ROOT%{_bindir}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/%{name}/components/*.so \
	$RPM_BUILD_ROOT%{_libdir}/*.so* || :

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post   mailnews -p /sbin/ldconfig
%postun mailnews -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/chrome
%dir %{_libdir}/%{name}/components
%dir %{_libdir}/%{name}/defaults
%dir %{_libdir}/%{name}/icons
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/res
%dir %{_libdir}/%{name}/searchplugins
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/chrome
%dir %{_datadir}/%{name}/chrome/packages

%{_libdir}/%{name}/component.reg
%attr(755,root,root) %{_libdir}/libcmt.so
%attr(755,root,root) %{_libdir}/libdocshell.so
%attr(755,root,root) %{_libdir}/libgtkembedmoz.so
%attr(755,root,root) %{_libdir}/libgtksuperwin.so
%attr(755,root,root) %{_libdir}/libgtkxtbin.so
%attr(755,root,root) %{_libdir}/libjsdom.so
%attr(755,root,root) %{_libdir}/libjsj.so
%attr(755,root,root) %{_libdir}/libmozjs.so
%attr(755,root,root) %{_libdir}/libnspr4.so
%attr(755,root,root) %{_libdir}/libplc4.so
%attr(755,root,root) %{_libdir}/libplds4.so
%attr(755,root,root) %{_libdir}/libprotocol.so
%attr(755,root,root) %{_libdir}/libraptorgfx.so
%attr(755,root,root) %{_libdir}/libraptorplugin.so
%attr(755,root,root) %{_libdir}/libraptorwebwidget.so
%attr(755,root,root) %{_libdir}/libxpcom.so
%attr(755,root,root) %{_libdir}/libxpistub.so

%attr(755,root,root) %{_libdir}/%{name}/components/libautocomplete.so
%attr(755,root,root) %{_libdir}/%{name}/components/libbookmarks.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcaps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libchardet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libchrome.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcookie.so
%attr(755,root,root) %{_libdir}/%{name}/components/libdirectory.so
%attr(755,root,root) %{_libdir}/%{name}/components/libeditor.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgfx_gtk.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgfxps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libhistory.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjar50.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsloader.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsurl.so
%attr(755,root,root) %{_libdir}/%{name}/components/liblwbrk.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmork.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmozbrwsr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmozfind.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmozucth.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmozxfer.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnecko*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libns*.so
%attr(755,root,root) %{_libdir}/%{name}/components/liboji.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpref.so
%attr(755,root,root) %{_libdir}/%{name}/components/libprofile.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpsmglue.so
%attr(755,root,root) %{_libdir}/%{name}/components/libraptor*.so
%attr(755,root,root) %{_libdir}/%{name}/components/librdf.so
%attr(755,root,root) %{_libdir}/%{name}/components/libregviewer.so
%attr(755,root,root) %{_libdir}/%{name}/components/librelated.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsample.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsearch.so
%attr(755,root,root) %{_libdir}/%{name}/components/libshistory.so
%attr(755,root,root) %{_libdir}/%{name}/components/libstrres.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtbmb.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtimer_gtk.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtxmgr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtxtsvc.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuconv.so
%attr(755,root,root) %{_libdir}/%{name}/components/libucv*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libunicharutil.so
%attr(755,root,root) %{_libdir}/%{name}/components/liburiloader.so
%attr(755,root,root) %{_libdir}/%{name}/components/liburlbarhistory.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwallet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwalletviewers.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebbrwsr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwidget_gtk.so
%attr(755,root,root) %{_libdir}/%{name}/components/libxmlterm.so
%attr(755,root,root) %{_libdir}/%{name}/components/libxpconnect.so
%attr(755,root,root) %{_libdir}/%{name}/components/libxpinstall.so

%{_libdir}/%{name}/components/appshell.xpt
%{_libdir}/%{name}/components/autocomplete.xpt
%{_libdir}/%{name}/components/bookmarks.xpt
%{_libdir}/%{name}/components/caps.xpt
%{_libdir}/%{name}/components/chrome.xpt
%{_libdir}/%{name}/components/cookieviewer.xpt
%{_libdir}/%{name}/components/directory.xpt
%{_libdir}/%{name}/components/docshell.xpt
%{_libdir}/%{name}/components/dom.xpt
%{_libdir}/%{name}/components/editor.xpt
%{_libdir}/%{name}/components/gfx.xpt
%{_libdir}/%{name}/components/history.xpt
%{_libdir}/%{name}/components/intl.xpt
%{_libdir}/%{name}/components/jar.xpt
%{_libdir}/%{name}/components/jsurl.xpt
%{_libdir}/%{name}/components/layout*.xpt
%{_libdir}/%{name}/components/locale.xpt
%{_libdir}/%{name}/components/mimetype.xpt
%{_libdir}/%{name}/components/moz*.xpt
%{_libdir}/%{name}/components/necko*.xpt
%{_libdir}/%{name}/components/oji.xpt
%{_libdir}/%{name}/components/pref.xpt
%{_libdir}/%{name}/components/prefmigr.xpt
%{_libdir}/%{name}/components/profile.xpt
%{_libdir}/%{name}/components/proxyObjInst.xpt
%{_libdir}/%{name}/components/psmglue.xpt
%{_libdir}/%{name}/components/rdf.xpt
%{_libdir}/%{name}/components/regviewer.xpt
%{_libdir}/%{name}/components/related.xpt
%{_libdir}/%{name}/components/remote.xpt
%{_libdir}/%{name}/components/sample.xpt
%{_libdir}/%{name}/components/search.xpt
%{_libdir}/%{name}/components/shistory.xpt
%{_libdir}/%{name}/components/sidebar.xpt
%{_libdir}/%{name}/components/signonviewer.xpt
%{_libdir}/%{name}/components/tbmb.xpt
%{_libdir}/%{name}/components/txmgr.xpt
%{_libdir}/%{name}/components/uconv.xpt
%{_libdir}/%{name}/components/unicharutil.xpt
%{_libdir}/%{name}/components/uriloader.xpt
%{_libdir}/%{name}/components/urlbarhistory.xpt
%{_libdir}/%{name}/components/util.xpt
%{_libdir}/%{name}/components/wallet*.xpt
%{_libdir}/%{name}/components/webBrowser*.xpt
%{_libdir}/%{name}/components/widget.xpt
%{_libdir}/%{name}/components/xml*.xpt
%{_libdir}/%{name}/components/xp*.xpt

%{_libdir}/%{name}/components/*.js
%{_libdir}/%{name}/components/*.dat

%{_datadir}/%{name}/chrome/locales
%{_datadir}/%{name}/chrome/packages/chatzilla
%{_datadir}/%{name}/chrome/packages/core
%{_datadir}/%{name}/chrome/packages/widget-toolkit
%{_datadir}/%{name}/chrome/packages/xmlterm
%{_datadir}/%{name}/chrome/skins
# some discussion files
#%{_datadir}/%{name}/chrome/overlayinfo
#%{_datadir}/%{name}/chrome/*.rdf

%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/res
%{_datadir}/%{name}/searchplugins

%{_datadir}/pixmaps/mozilla-icon.xpm
%{_applnkdir}/Network/WWW/mozilla.desktop

##########################################
################ mailnews ################
##########################################
%files mailnews
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmsgbaseutil.so

%attr(755,root,root) %{_libdir}/%{name}/components/libabsyncsvc.so
%attr(755,root,root) %{_libdir}/%{name}/components/libaddrbook.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimport.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimpText.so
%attr(755,root,root) %{_libdir}/%{name}/components/liblocalmail.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmailnews.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmime.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmimeemitter.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmsg*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsigned.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsmime.so
%attr(755,root,root) %{_libdir}/%{name}/components/libvcard.so

%{_libdir}/%{name}/components/absync.xpt
%{_libdir}/%{name}/components/addrbook.xpt
%{_libdir}/%{name}/components/import.xpt
%{_libdir}/%{name}/components/mailnews.xpt
%{_libdir}/%{name}/components/mime.xpt
%{_libdir}/%{name}/components/msg*.xpt

%{_datadir}/%{name}/chrome/packages/messenger

#######################################
################ devel ################
#######################################
%files devel
%defattr(644,root,root,755)
#%{_libdir}/lib*.la
#%{_includedir}/*
%{_datadir}/idl/*
