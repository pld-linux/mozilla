#
# Conditional build:
# _with_clearmenu
#
Summary:	Mozilla - web browser
Summary(es):	Navegador de Internet Mozilla
Summary(pl):	Mozilla - przegl�darka WWW
Summary(pt_BR):	Navegador Mozilla
Name:		mozilla
Version:	0.9.6
Release:	3
Epoch:		1
License:	GPL
# Mirror0:	ftp://sunsite.icm.edu.pl/pub/mozilla/mozilla/releases/mozilla%{version}/src/%{name}-source-%{version}.tar.bz2
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	ftp://ftp.mozilla.org/pub/mozilla/releases/mozilla%{version}/src/%{name}-source-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-navigator-overlay-menu.patch
Patch1:		%{name}-taskbar-no%{name}.patch
Patch2:		%{name}-pld-homepage.patch
URL:		http://www.mozilla.org/projects/newlayout/
BuildRequires:	libstdc++-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	gtk+-devel
BuildRequires:	ORBit-devel
BuildRequires:	nspr-devel
BuildRequires:	fileutils
BuildRequires:	zip >= 2.1
BuildRequires:	perl-modules >= 5.6.0
BuildRequires:	autoconf
Provides:	mozilla-embedded
Obsoletes:	mozilla-embedded
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Mozilla is an open-source web browser, designed for standards
compliance, performance and portability.

%description -l es
Mozilla es un navegador de Internet que se basa en una versi�n inicial
de Netscape Communicator. Este software est� en desarrollo, por lo
cual todav�a es inestable.

%description -l pl
Mozilla jest pot�n� graficzn� przegl�dark� WWW, kt�ra jest nast�pc�
Netscape Navigatora.

%description -l pt_BR
O Mozilla � um web browser baseado numa vers�o inicial do Netscape
Communicator. Este software est� em fase de desenvolvimento, portanto,
ainda n�o est�vel.

%package mailnews
Summary:	Mozilla - programs for mail and news
Summary(pl):	Mozilla - programy do poczty i news�w
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Requires:	%{name} = %{version}

%description mailnews
Programs for mail and news integrated with browser.

%description -l pl mailnews
Programy pocztowe i news�w zintegrowane z przegl�dark�.

%package devel
Summary:	Mozilla development crap
Summary(es):	Headers for developing programs that will use Mozilla
Summary(pl):	Mozilla - pliki nag��wkowe i biblioteki
Summary(pt_BR):	Arquivos de inclus�o para desenvolvimento de programas que usam o Mozilla
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/����������/����������
Group(uk):	X11/��������/��̦�����
Requires:	%{name} = %{version}
Provides:	mozilla-embedded-devel
Obsoletes:	mozilla-embedded-devel

%description devel
Mozilla development libs and headers.

%description -l es devel
Development package for Mozilla.

%description -l pl devel
Biblioteki i pliki nag��wkowe s�u��ce programowaniu.

%description -l pt_BR devel
Arquivos de inclus�o para desenvolvimento de programas que usam o
Mozilla.

%prep
%setup -q -n mozilla
%{!?_without_clearmenu:%patch0 -p1}
%{!?_without_clearmenu:%patch1 -p1}
%patch2 -p1

%build
BUILD_OFFICIAL="1"; export BUILD_OFFICIAL

%configure2_13 \
	--with-default-mozilla-five-home=%{_libdir}/mozilla \
	--with-nspr-prefix="/usr" \
	--enable-optimize="%{rpmcflags}" \
	--with-pthreads \
	--enable-toolkit=gtk \
	--enable-strip-libs \
	--enable-new-cache \
	--enable-mathml \
	--enable-svg \
	--enable-ldap \
	--enable-xsl \
	--enable-xinerama \
	--disable-elf-dynstr-gc \
	--enable-crypto \
	--with-extensions \
	--disable-dtd-debug \
	--disable-debug \
	--disable-tests \
	--disable-pedantic \
	--disable-short-wchar \
	--with-x \
	--with-jpeg \
	--with-zlib \
	--with-png \
	--with-mng \
	--with-xprint

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Network/WWW} \
	$RPM_BUILD_ROOT%{_datadir}/{idl,pixmaps} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{chrome,defaults,dtd,icons,res,searchplugins} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/{components,plugins} \
	$RPM_BUILD_ROOT%{_includedir}/%{name}

# preparing to create register
rm -fr dist/bin/chrome/{US,chatzilla,classic,comm,content-packs,embed,en-US,en-unix,en-win,help,inspector,messenger,modern,pipnss,pippki,toolkit,xmlterm}
echo "skin,install,select,classic/1.0"	>> dist/bin/chrome/installed-chrome.txt
echo "locale,install,select,en-US"	>> dist/bin/chrome/installed-chrome.txt

# creating and installing register
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regxpcom
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regchrome
install dist/bin/component.reg $RPM_BUILD_ROOT%{_libdir}/%{name}

ln -sf ../../share/mozilla/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/chrome
ln -sf ../../share/mozilla/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -sf ../../share/mozilla/dtd $RPM_BUILD_ROOT%{_libdir}/%{name}/dtd
ln -sf ../../share/mozilla/icons $RPM_BUILD_ROOT%{_libdir}/%{name}/icons
ln -sf ../../share/mozilla/res $RPM_BUILD_ROOT%{_libdir}/%{name}/res
ln -sf ../../share/mozilla/searchplugins $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins

cp -frL dist/bin/chrome/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
cp -frL dist/bin/components/*	$RPM_BUILD_ROOT%{_libdir}/%{name}/components
cp -frL dist/bin/defaults/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
cp -frL dist/bin/dtd/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/dtd
cp -frL dist/bin/icons/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/icons
cp -frL dist/bin/plugins/*	$RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
cp -frL dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -frL dist/bin/searchplugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins
cp -frL dist/idl/*		$RPM_BUILD_ROOT%{_datadir}/idl
cp -frL dist/include/*		$RPM_BUILD_ROOT%{_includedir}/%{name}

install dist/bin/*.so		$RPM_BUILD_ROOT%{_libdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

install dist/bin/mozilla-bin $RPM_BUILD_ROOT%{_bindir}/mozilla
install dist/bin/regchrome $RPM_BUILD_ROOT%{_bindir}
install dist/bin/regxpcom $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post 
/sbin/ldconfig
umask 022
rm -f %{_libdir}/mozilla/component.reg
MOZILLA_FIVE_HOME=%{_libdir}/mozilla regxpcom

%postun	-p /sbin/ldconfig

%post   mailnews 
/sbin/ldconfig
umask 022
rm -f %{_libdir}/mozilla/component.reg
MOZILLA_FIVE_HOME=%{_libdir}/mozilla regxpcom

%postun mailnews -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/chrome
%dir %{_libdir}/%{name}/components
%dir %{_libdir}/%{name}/defaults
%dir %{_libdir}/%{name}/dtd
%dir %{_libdir}/%{name}/icons
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/res
%dir %{_libdir}/%{name}/searchplugins
%dir %{_datadir}/%{name}

%ghost %{_libdir}/%{name}/component.reg
%attr(755,root,root) %{_libdir}/libgkgfx.so
%attr(755,root,root) %{_libdir}/libgtkembedmoz.so
%attr(755,root,root) %{_libdir}/libgtksuperwin.so
%attr(755,root,root) %{_libdir}/libgtkxtbin.so
%attr(755,root,root) %{_libdir}/libjsj.so
%attr(755,root,root) %{_libdir}/liblber40.so
%attr(755,root,root) %{_libdir}/libldap40.so
%attr(755,root,root) %{_libdir}/libmozjs.so
%attr(755,root,root) %{_libdir}/libmozpango.so
%attr(755,root,root) %{_libdir}/libmozpango-thaix.so
%attr(755,root,root) %{_libdir}/libnssckbi.so
%attr(755,root,root) %{_libdir}/libnullplugin.so
%attr(755,root,root) %{_libdir}/libxpcom.so
%attr(755,root,root) %{_libdir}/libxpistub.so
%attr(755,root,root) %{_libdir}/libxlibrgb.so

%attr(755,root,root) %{_libdir}/%{name}/plugins/libnullplugin.so

%attr(755,root,root) %{_libdir}/%{name}/components/libaccess*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libappcomps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcaps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libchardet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libchrome.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcomposer.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcookie.so
%attr(755,root,root) %{_libdir}/%{name}/components/libctl.so
%attr(755,root,root) %{_libdir}/%{name}/components/libdocshell.so
%attr(755,root,root) %{_libdir}/%{name}/components/libeditor.so
%attr(755,root,root) %{_libdir}/%{name}/components/libembedcomponents.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgfx*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgk*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libhtmlpars.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimg*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libinspector.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjar50.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsd.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsdom.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsloader.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsurl.so
%attr(755,root,root) %{_libdir}/%{name}/components/liblwbrk.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmork.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmoz*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnecko*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnkcache.so
%attr(755,root,root) %{_libdir}/%{name}/components/libns*.so
%attr(755,root,root) %{_libdir}/%{name}/components/liboji.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpipnss.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpippki.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpref.so
%attr(755,root,root) %{_libdir}/%{name}/components/libprofile.so
%attr(755,root,root) %{_libdir}/%{name}/components/librdf.so
%attr(755,root,root) %{_libdir}/%{name}/components/libregviewer.so
%attr(755,root,root) %{_libdir}/%{name}/components/libshistory.so
%attr(755,root,root) %{_libdir}/%{name}/components/libsmimestb.so
%attr(755,root,root) %{_libdir}/%{name}/components/libstrres.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtimer_gtk.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtransformiix.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtxmgr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtxtsvc.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuconv.so
%attr(755,root,root) %{_libdir}/%{name}/components/libucv*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libunicharutil.so
%attr(755,root,root) %{_libdir}/%{name}/components/liburiloader.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwallet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwalletviewers.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebbrwsr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwidget_gtk.so
%attr(755,root,root) %{_libdir}/%{name}/components/libx*.so

%{_libdir}/%{name}/components/access*.xpt
%{_libdir}/%{name}/components/appshell.xpt
%{_libdir}/%{name}/components/autocomplete.xpt
%{_libdir}/%{name}/components/bookmarks.xpt
%{_libdir}/%{name}/components/caps.xpt
%{_libdir}/%{name}/components/chardet.xpt
%{_libdir}/%{name}/components/chrome.xpt
%{_libdir}/%{name}/components/content_base.xpt
%{_libdir}/%{name}/components/content_xsl.xpt
%{_libdir}/%{name}/components/cookie.xpt
%{_libdir}/%{name}/components/directory.xpt
%{_libdir}/%{name}/components/docshell.xpt
%{_libdir}/%{name}/components/dom*.xpt
%{_libdir}/%{name}/components/editor.xpt
%{_libdir}/%{name}/components/embed_base.xpt
%{_libdir}/%{name}/components/exthandler.xpt
%{_libdir}/%{name}/components/find.xpt
%{_libdir}/%{name}/components/gfx*.xpt
%{_libdir}/%{name}/components/helperAppDlg.xpt
%{_libdir}/%{name}/components/history.xpt
%{_libdir}/%{name}/components/imglib2.xpt
%{_libdir}/%{name}/components/inspector.xpt
%{_libdir}/%{name}/components/intl.xpt
%{_libdir}/%{name}/components/jar.xpt
%{_libdir}/%{name}/components/js*.xpt
%{_libdir}/%{name}/components/layout*.xpt
%{_libdir}/%{name}/components/locale.xpt
%{_libdir}/%{name}/components/mimetype.xpt
%{_libdir}/%{name}/components/moz*.xpt
%{_libdir}/%{name}/components/necko*.xpt
%{_libdir}/%{name}/components/oji.xpt
%{_libdir}/%{name}/components/pipnss.xpt
%{_libdir}/%{name}/components/pippki.xpt
%{_libdir}/%{name}/components/plugin.xpt
%{_libdir}/%{name}/components/pref.xpt
%{_libdir}/%{name}/components/prefmigr.xpt
%{_libdir}/%{name}/components/profile.xpt
%{_libdir}/%{name}/components/proxyObjInst.xpt
%{_libdir}/%{name}/components/rdf.xpt
%{_libdir}/%{name}/components/regviewer.xpt
%{_libdir}/%{name}/components/related.xpt
%{_libdir}/%{name}/components/search.xpt
%{_libdir}/%{name}/components/shistory.xpt
%{_libdir}/%{name}/components/sidebar.xpt
%{_libdir}/%{name}/components/signonviewer.xpt
%{_libdir}/%{name}/components/transformiix.xpt
%{_libdir}/%{name}/components/txmgr.xpt
%{_libdir}/%{name}/components/txtsvc.xpt
%{_libdir}/%{name}/components/uconv.xpt
%{_libdir}/%{name}/components/unicharutil.xpt
%{_libdir}/%{name}/components/uriloader.xpt
%{_libdir}/%{name}/components/urlbarhistory.xpt
%{_libdir}/%{name}/components/util.xpt
%{_libdir}/%{name}/components/wallet*.xpt
%{_libdir}/%{name}/components/webBrowser*.xpt
%{_libdir}/%{name}/components/webbrowserpersist.xpt
%{_libdir}/%{name}/components/webshell_idls.xpt
%{_libdir}/%{name}/components/widget.xpt
%{_libdir}/%{name}/components/windowwatcher.xpt
%{_libdir}/%{name}/components/x*.xpt

%{_libdir}/%{name}/components/*.js
%{_libdir}/%{name}/components/*.dat

%{_datadir}/%{name}/chrome
%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/res
%{_datadir}/%{name}/searchplugins
%{_datadir}/%{name}/dtd

%{_pixmapsdir}/mozilla.png
%{_applnkdir}/Network/WWW/mozilla.desktop

##########################################
################ mailnews ################
##########################################
%files mailnews
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmsgbaseutil.so

%attr(755,root,root) %{_libdir}/%{name}/components/libabsyncsvc.so
%attr(755,root,root) %{_libdir}/%{name}/components/libaddrbook.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimpText.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimport.so
%attr(755,root,root) %{_libdir}/%{name}/components/liblocalmail.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmailnews.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmimeemitter.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmime.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmsg*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libvcard.so

%{_libdir}/%{name}/components/absync.xpt
%{_libdir}/%{name}/components/addrbook.xpt
%{_libdir}/%{name}/components/import.xpt
%{_libdir}/%{name}/components/mailnews.xpt
%{_libdir}/%{name}/components/mime.xpt
%{_libdir}/%{name}/components/msg*.xpt

#######################################
################ devel ################
#######################################
%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_datadir}/idl/*
