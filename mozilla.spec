#
# Conditional build:
# _with_gtk1		- use gtk+ 1.2.x instead of 2.x.x
# _with_gcc2		- compile using gcc2 to get working flash and Sun Java plugins
#			  on nest and other gcc 3.x systems. WARNING! You have to
#			  recompile galeon with gcc2 in order to get it working with
#			  this release of mozilla
#
Summary:	Mozilla - web browser
Summary(es):	Navegador de Internet Mozilla
Summary(pl):	Mozilla - przegl±darka WWW
Summary(pt_BR):	Navegador Mozilla
Summary(ru):	Web browser
Name:		mozilla
Version:	1.4b
Release:	0.2
Epoch:		3
License:	Mozilla Public License
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla/releases/mozilla%{version}/src/%{name}-source-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Source4:	%{name}-addressbook.desktop
Source5:	%{name}-chat.desktop
Source6:	%{name}-jconsole.desktop
Source7:	%{name}-mail.desktop
Source8:	%{name}-news.desktop
Source9:	%{name}-terminal.desktop
Source10:	%{name}-venkman.desktop
Patch0:		%{name}-pld-homepage.patch
Patch2:		%{name}-nss.patch
Patch3:		%{name}-ldap_nspr_includes.patch
Patch5:		%{name}-ldap-with-nss.patch
Patch6:		%{name}-gfx.patch
URL:		http://www.mozilla.org/
%{?_with_gtk1:BuildRequires:	ORBit-devel}
BuildRequires:	Xft-devel >= 2.1-2
BuildRequires:	autoconf
BuildRequires:	freetype-devel >= 2.1.3
%{?_with_gtk1:BuildRequires:	gtk+-devel}
%{!?_with_gtk1:BuildRequires:  gtk+2-devel >= 2.2.0}
%{!?_with_gtk1:BuildRequires:  pkgconfig}
%{!?_with_gtk1:BuildRequires:  libIDL-devel}
%{!?_with_gtk1:BuildRequires:  freetype-devel >= 2.1.3}
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel >= 1.0.4
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	nss-devel >= 3.7.3
BuildRequires:	nspr-devel >= 4.3-2.20030517
BuildRequires:	perl-modules >= 5.6.0
BuildRequires:	zip >= 2.1
Provides:	mozilla-embedded = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	nss >= 3.7.3
Obsoletes:	mozilla-embedded
Obsoletes:	mozilla-irc

%define		_chromedir	%{_libdir}/%{name}/chrome

%if%{?_with_gcc2:1}%{!?_with_gcc2:0}
%define		__cc		gcc2
%define		__cxx		gcc2
%endif

%define		_gcc_ver	%(%{__cc} -dumpversion | cut -b 1)
%if %{_gcc_ver} == 2
%define		__cxx		"%{__cc}"
%endif

%description
Mozilla is an open-source web browser, designed for standards
compliance, performance and portability.

%description -l es
Mozilla es un navegador de Internet que se basa en una versión inicial
de Netscape Communicator. Este software está en desarrollo, por lo
cual todavía es inestable.

%description -l pl
Mozilla jest potê¿n± graficzn± przegl±dark± WWW, która jest nastêpc±
Netscape Navigatora.

%description -l pt_BR
O Mozilla é um web browser baseado numa versão inicial do Netscape
Communicator. Este software está em fase de desenvolvimento, portanto,
ainda não estável.

%description -l ru
Mozilla - ÐÏÌÎÏÆÕÎËÃÉÏÎÁÌØÎÙÊ web-browser Ó ÏÔËÒÙÔÙÍÉ ÉÓÈÏÄÎÙÍÉ
ÔÅËÓÔÁÍÉ, ÒÁÚÒÁÂÏÔÁÎÎÙÊ ÄÌÑ ÍÁËÓÉÍÁÌØÎÏÇÏ ÓÏÏÔ×ÅÓÔ×ÉÑ ÓÔÁÎÄÁÒÔÁÍ,
ÍÁËÓÍÉÍÁÌØÎÏÊ ÐÅÒÅÎÏÓÉÍÏÓÔÉ É ÓËÏÒÏÓÔÉ ÒÁÂÏÔÙ

%package mailnews
Summary:	Mozilla - programs for mail and news
Summary(pl):	Mozilla - programy do poczty i newsów
Summary(ru):	ðÏÞÔÏ×ÁÑ ÓÉÓÔÅÍÁ ÎÁ ÏÓÎÏ×Å Mozilla
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}
Obsoletes:	mozilla-mail

%description mailnews
Programs for mail and news integrated with browser.

%description mailnews -l pl
Programy pocztowe i obs³uga newsów zintegrowane z przegl±dark±.

%description mailnews -l ru
ëÌÉÅÎÔ ÐÏÞÔÙ É ÎÏ×ÏÓÔÅÊ, ÎÁ ÏÓÎÏ×Å Mozilla. ðÏÄÄÅÒÖÉ×ÁÅÔ IMAP, POP É
NNTP É ÉÍÅÅÔ ÐÒÏÓÔÏÊ ÉÎÔÅÒÆÅÊÓ ÐÏÌØÚÏ×ÁÔÅÌÑ.

%package devel
Summary:	Headers for developing programs that will use Mozilla
Summary(pl):	Mozilla - pliki nag³ówkowe i biblioteki
Summary(pt_BR):	Arquivos de inclusão para desenvolvimento de programas que usam o Mozilla
Summary(ru):	æÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÉÓÐÏÌØÚÏ×ÁÎÉÑ ÐÒÏÇÒÁÍÍ, ×ËÌÀÞÁÀÝÉÈ Mozilla
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	nspr-devel
Provides:	mozilla-embedded-devel = %{version}
Obsoletes:	mozilla-embedded-devel

%description devel
Mozilla development package.

%description devel -l pl
Biblioteki i pliki nag³ówkowe.

%description devel -l pt_BR
Arquivos de inclusão para desenvolvimento de programas que usam o
Mozilla.

%description devel -l ru
úÁÇÏÌÏ×ÏÞÎÙÅ ÆÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ ÐÒÏÇÒÁÍÍ, ÉÓÐÅÏÌØÚÕÀÝÉÈ
Mozilla

%prep
%setup -q -n mozilla
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1

%build
BUILD_OFFICIAL="1"; export BUILD_OFFICIAL
MOZILLA_OFFICIAL="1"; export MOZILLA_OFFICIAL

MOZ_INTERNAL_LIBART_LGPL="x"
export MOZ_INTERNAL_LIBART_LGPL

%if %{_gcc_ver} > 2
CXXFLAGS="-Wno-deprecated"; export CXXFLAGS
%endif

%configure2_13 \
	--disable-debug \
	--disable-dtd-debug \
	--disable-elf-dynstr-gc \
	--disable-pedantic \
	--disable-short-wchar \
	--disable-tests \
	--enable-crypto \
	--enable-extensions \
	--enable-ldap \
	--enable-mathml \
	--enable-new-cache \
	--enable-optimize="%{rpmcflags}" \
	--enable-postscript \
	--enable-strip-libs \
	--enable-svg \
	%{?_with_gtk1:--enable-toolkit-gtk} \
	%{!?_with_gtk1:--disable-toolkit-gtk --enable-default-toolkit=gtk2} \
	--enable-xft \
	--enable-xinerama \
	--enable-xprint \
	--enable-xsl \
	--disable-xterm-updates \
	--enable-old-abi-compat-wrappers \
	--with-default-mozilla-five-home=%{_libdir}/mozilla \
	--with-system-nspr \
	--with-pthreads \
	--with-system-jpeg \
	--with-system-mng \
	--with-system-png \
	--with-system-zlib \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/idl,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_applnkdir}/Network/{Communications,Mail,Misc,News,WWW} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{chrome,defaults,icons,res,searchplugins} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/{components,plugins} \
	$RPM_BUILD_ROOT{%{_includedir}/%{name},%{_pkgconfigdir}}

# preparing to create register
rm -fr dist/bin/chrome/{US,chatzilla,classic,comm,content-packs,embed,en-US,en-unix,en-win,help,inspector,messenger,modern,pipnss,pippki,toolkit,xmlterm}
echo "skin,install,select,classic/1.0"	>> dist/bin/chrome/installed-chrome.txt
echo "locale,install,select,en-US"	>> dist/bin/chrome/installed-chrome.txt

# creating and installing register
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regxpcom
LD_LIBRARY_PATH="dist/bin" MOZILLA_FIVE_HOME="dist/bin" dist/bin/regchrome
#install dist/bin/component.reg $RPM_BUILD_ROOT%{_libdir}/%{name}

ln -sf ../../share/mozilla/chrome $RPM_BUILD_ROOT%{_chromedir}
ln -sf ../../share/mozilla/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -sf ../../share/mozilla/icons $RPM_BUILD_ROOT%{_libdir}/%{name}/icons
ln -sf ../../share/mozilla/res $RPM_BUILD_ROOT%{_libdir}/%{name}/res
ln -sf ../../share/mozilla/searchplugins $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins

cp -frL dist/bin/chrome/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
cp -frL dist/bin/components/*	$RPM_BUILD_ROOT%{_libdir}/%{name}/components
cp -frL dist/bin/defaults/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
%{?_with_gtk1:cp -frL dist/bin/icons/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/icons}
cp -frL dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -frL dist/bin/searchplugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins
cp -frL dist/idl/*		$RPM_BUILD_ROOT%{_datadir}/idl
cp -frL dist/include/*		$RPM_BUILD_ROOT%{_includedir}/%{name}
cp -frL dist/public/ldap{,-private} $RPM_BUILD_ROOT%{_includedir}/%{name}

install dist/bin/*.so $RPM_BUILD_ROOT%{_libdir}

ln -s %{_libdir}/libxpcom.so $RPM_BUILD_ROOT%{_libdir}/%{name}/libxpcom.so

for f in build/unix/*.pc ; do
	sed -e 's/mozilla-%{version}/mozilla/' $f \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/$(basename $f)
done

sed -e 's,lib/mozilla-%{version},lib,g;s/mozilla-%{version}/mozilla/g' build/unix/mozilla-gtkmozembed.pc \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-gtkmozembed.pc

		
sed -e 's|/mozilla-%{version}||' build/unix/mozilla-nspr.pc \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-nspr.pc

install %{SOURCE1}	$RPM_BUILD_ROOT%{_applnkdir}/Network/WWW
install %{SOURCE4}	$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install %{SOURCE5}	$RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install %{SOURCE6}	$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install %{SOURCE7}	$RPM_BUILD_ROOT%{_applnkdir}/Network/Mail
install %{SOURCE8}	$RPM_BUILD_ROOT%{_applnkdir}/Network/News
install %{SOURCE9}	$RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install %{SOURCE10}	$RPM_BUILD_ROOT%{_applnkdir}/Network/Misc
install %{SOURCE2}	$RPM_BUILD_ROOT%{_pixmapsdir}

install dist/bin/mozilla-bin $RPM_BUILD_ROOT%{_bindir}/mozilla
install dist/bin/regchrome $RPM_BUILD_ROOT%{_bindir}
install dist/bin/regxpcom $RPM_BUILD_ROOT%{_bindir}

cp $RPM_BUILD_ROOT%{_chromedir}/installed-chrome.txt \
	$RPM_BUILD_ROOT%{_chromedir}/%{name}-installed-chrome.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom

cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%postun	-p /sbin/ldconfig

%post mailnews
/sbin/ldconfig
umask 022
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom

%postun mailnews -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/%{name}
%dir %{_chromedir}
%dir %{_libdir}/%{name}/components
%dir %{_libdir}/%{name}/defaults
%dir %{_libdir}/%{name}/icons
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/res
%dir %{_libdir}/%{name}/searchplugins
%dir %{_datadir}/%{name}

#%ghost %{_libdir}/%{name}/component.reg
%attr(755,root,root) %{_libdir}/libgkgfx.so
%attr(755,root,root) %{_libdir}/libgtkembedmoz.so
%{?_with_gtk1:%attr(755,root,root) %{_libdir}/libgtksuperwin.so}
%attr(755,root,root) %{_libdir}/libgtkxtbin.so
%attr(755,root,root) %{_libdir}/libjsj.so
%attr(755,root,root) %{_libdir}/libldap50.so
%attr(755,root,root) %{_libdir}/libprldap50.so
%attr(755,root,root) %{_libdir}/libssldap50.so
%attr(755,root,root) %{_libdir}/libmozjs.so
#%attr(755,root,root) %{_libdir}/libmozpango.so
#%attr(755,root,root) %{_libdir}/libmozpango-thaix.so
%attr(755,root,root) %{_libdir}/libmoz_art_lgpl.so
#%attr(755,root,root) %{_libdir}/libnullplugin.so
%attr(755,root,root) %{_libdir}/libxpcom.so
%attr(755,root,root) %{_libdir}/libxpcom_compat.so
%attr(755,root,root) %{_libdir}/libxpistub.so
%attr(755,root,root) %{_libdir}/libxlibrgb.so
%attr(755,root,root) %{_libdir}/%{name}/libxpcom.so
%attr(755,root,root) %{_libdir}/%{name}/components/libaccess*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libappcomps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libautoconfig.so

%attr(755,root,root) %{_libdir}/%{name}/components/libcaps.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libchardet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libchrome.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcomposer.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcookie.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libctl.so
%attr(755,root,root) %{_libdir}/%{name}/components/libdocshell.so
%attr(755,root,root) %{_libdir}/%{name}/components/libeditor.so
%attr(755,root,root) %{_libdir}/%{name}/components/libembedcomponents.so
%attr(755,root,root) %{_libdir}/%{name}/components/libfileview.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgfx*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgk*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libhtmlpars.so
%attr(755,root,root) %{_libdir}/%{name}/components/libi18n.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libiiextras.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimg*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libinspector.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjar50.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsd.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsdom.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libjsloader.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libjsurl.so
#%attr(755,root,root) %{_libdir}/%{name}/components/liblwbrk.so

%attr(755,root,root) %{_libdir}/%{name}/components/libmork.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmoz*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnecko*.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libnkcache.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnkdatetime.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnkfinger.so
%attr(755,root,root) %{_libdir}/%{name}/components/libns*.so
%attr(755,root,root) %{_libdir}/%{name}/components/liboji.so
%attr(755,root,root) %{_libdir}/%{name}/components/libp3p.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpipboot.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpipnss.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpippki.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpref.so
%attr(755,root,root) %{_libdir}/%{name}/components/libprofile.so
%attr(755,root,root) %{_libdir}/%{name}/components/librdf.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libregviewer.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libshistory.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libstrres.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtransformiix.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtxmgr.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libtxtsvc.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtypeaheadfind.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuconv.so
%attr(755,root,root) %{_libdir}/%{name}/components/libucv*.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libunicharutil.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuniversalchardet.so
#%attr(755,root,root) %{_libdir}/%{name}/components/liburiloader.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwallet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwalletviewers.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebbrwsr.so
%{?_with_gtk1:%attr(755,root,root) %{_libdir}/%{name}/components/libwidget_gtk.so}
%{!?_with_gtk1:%attr(755,root,root) %{_libdir}/%{name}/components/libwidget_gtk2.so}
%attr(755,root,root) %{_libdir}/%{name}/components/libx*.so

%{_libdir}/%{name}/components/access*.xpt
%{_libdir}/%{name}/components/appshell.xpt
%{_libdir}/%{name}/components/autocomplete.xpt
%{_libdir}/%{name}/components/autoconfig.xpt
%{_libdir}/%{name}/components/bookmarks.xpt
%{_libdir}/%{name}/components/caps.xpt
%{_libdir}/%{name}/components/chardet.xpt
%{_libdir}/%{name}/components/chrome.xpt
%{_libdir}/%{name}/components/commandhandler.xpt
%{_libdir}/%{name}/components/composer.xpt
%{_libdir}/%{name}/components/content*.xpt
%{_libdir}/%{name}/components/cookie.xpt
%{_libdir}/%{name}/components/directory.xpt
%{_libdir}/%{name}/components/docshell.xpt
%{_libdir}/%{name}/components/dom*.xpt
%{_libdir}/%{name}/components/downloadmanager.xpt
%{_libdir}/%{name}/components/editor.xpt
%{_libdir}/%{name}/components/embed_base.xpt
%{_libdir}/%{name}/components/exthandler.xpt
%{_libdir}/%{name}/components/find.xpt
%{_libdir}/%{name}/components/filepicker.xpt
%{_libdir}/%{name}/components/gfx*.xpt
%{_libdir}/%{name}/components/helperAppDlg.xpt
%{_libdir}/%{name}/components/history.xpt
%{_libdir}/%{name}/components/htmlparser.xpt
#%{_libdir}/%{name}/components/iiextras.xpt
%{_libdir}/%{name}/components/imglib2.xpt
%{_libdir}/%{name}/components/inspector.xpt
%{_libdir}/%{name}/components/intl.xpt
%{_libdir}/%{name}/components/jar.xpt
%{_libdir}/%{name}/components/js*.xpt
%{_libdir}/%{name}/components/layout*.xpt
%{_libdir}/%{name}/components/locale.xpt
%{_libdir}/%{name}/components/lwbrk.xpt
%{_libdir}/%{name}/components/mimetype.xpt
%{_libdir}/%{name}/components/moz*.xpt
%{_libdir}/%{name}/components/necko*.xpt
%{_libdir}/%{name}/components/oji.xpt
%{_libdir}/%{name}/components/p3p.xpt
%{_libdir}/%{name}/components/pipboot.xpt
%{_libdir}/%{name}/components/pipnss.xpt
%{_libdir}/%{name}/components/pippki.xpt
%{_libdir}/%{name}/components/plugin.xpt
%{_libdir}/%{name}/components/pref.xpt
%{_libdir}/%{name}/components/prefetch.xpt
%{_libdir}/%{name}/components/prefmigr.xpt
%{_libdir}/%{name}/components/profile.xpt
%{_libdir}/%{name}/components/progressDlg.xpt
%{_libdir}/%{name}/components/proxyObjInst.xpt
%{_libdir}/%{name}/components/rdf.xpt
#%{_libdir}/%{name}/components/regviewer.xpt
%{_libdir}/%{name}/components/related.xpt
%{_libdir}/%{name}/components/search.xpt
%{_libdir}/%{name}/components/shistory.xpt
%{_libdir}/%{name}/components/sidebar.xpt
%{_libdir}/%{name}/components/signonviewer.xpt
%{_libdir}/%{name}/components/timebomb.xpt
#%%{_libdir}/%{name}/components/transformiix.xpt
%{_libdir}/%{name}/components/txmgr.xpt
%{_libdir}/%{name}/components/txtsvc.xpt
%{_libdir}/%{name}/components/typeaheadfind.xpt
%{_libdir}/%{name}/components/uconv.xpt
%{_libdir}/%{name}/components/unicharutil.xpt
%{_libdir}/%{name}/components/uriloader.xpt
%{_libdir}/%{name}/components/urlbarhistory.xpt
%{_libdir}/%{name}/components/util.xpt
%{_libdir}/%{name}/components/wallet*.xpt
%{_libdir}/%{name}/components/webBrowser_core.xpt
%{_libdir}/%{name}/components/webbrowserpersist.xpt
%{_libdir}/%{name}/components/webshell_idls.xpt
%{_libdir}/%{name}/components/widget.xpt
%{_libdir}/%{name}/components/windowds.xpt
%{_libdir}/%{name}/components/windowwatcher.xpt
%{_libdir}/%{name}/components/x*.xpt

# Is this a correct package for these files?
%{_libdir}/%{name}/components/ipcd.xpt
%{_libdir}/%{name}/components/profilesharingsetup.xpt
%{_libdir}/%{name}/components/transmngr.xpt
%{_libdir}/%{name}/components/ucnative.xpt
%{_libdir}/%{name}/components/websrvcs.xpt
%{_libdir}/%{name}/components/libipcdc.so
%{_libdir}/%{name}/components/libsystem-pref.so
%{_libdir}/%{name}/components/libtransmngr_client.so
%{_libdir}/%{name}/components/libwebsrvcs.so

#%%{_libdir}/*.js
%{_libdir}/%{name}/components/*.js
%config %verify(not size mtime md5) %{_libdir}/%{name}/components/*.dat

%dir %{_datadir}/%{name}/chrome
%{_datadir}/%{name}/chrome/[!i]*
%{_datadir}/%{name}/chrome/i[!n]*
%{_datadir}/%{name}/chrome/ins[!t]*
%ghost %{_datadir}/%{name}/chrome/installed-chrome.txt

%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/res
%{_datadir}/%{name}/searchplugins
%{_datadir}/idl/*

%{_pixmapsdir}/mozilla.png
%{_applnkdir}/Network/WWW/mozilla.desktop
%{_applnkdir}/Network/Misc/mozilla-jconsole.desktop
%{_applnkdir}/Network/Communications/mozilla-chat.desktop
%{_applnkdir}/Network/Communications/mozilla-terminal.desktop
%{_applnkdir}/Network/Misc/mozilla-venkman.desktop

##########################################
################ mailnews ################
##########################################
%files mailnews
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmsgbaseutil.so
#%attr(755,root,root) %{_libdir}/%{name}/components/libabsyncsvc.so
%attr(755,root,root) %{_libdir}/%{name}/components/libaddrbook.so
%attr(755,root,root) %{_libdir}/%{name}/components/libbayesflt.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimpText.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimpComm4xMail.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimport.so
%attr(755,root,root) %{_libdir}/%{name}/components/liblocalmail.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmailnews.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmailview.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmimeemitter.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmime.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmsg*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libvcard.so

#%{_libdir}/%{name}/components/absync.xpt
%{_libdir}/%{name}/components/addrbook.xpt
%{_libdir}/%{name}/components/impComm4xMail.xpt
%{_libdir}/%{name}/components/import.xpt
%{_libdir}/%{name}/components/mailnews.xpt
%{_libdir}/%{name}/components/mailview.xpt
%{_libdir}/%{name}/components/mime.xpt
%{_libdir}/%{name}/components/msg*.xpt

%{_applnkdir}/Network/Misc/mozilla-addressbook.desktop
%{_applnkdir}/Network/Mail/mozilla-mail.desktop
%{_applnkdir}/Network/News/mozilla-news.desktop

#######################################
################ devel ################
#######################################
%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*
