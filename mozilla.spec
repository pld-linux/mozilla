Summary:	Mozilla - web browser
Summary(es):	Navegador de Internet Mozilla
Summary(pl):	Mozilla - przegl±darka WWW
Summary(pt_BR):	Navegador Mozilla
Summary(ru):	Web browser
Name:		mozilla
Version:	1.2.1
Release:	3
Epoch:		2
License:	Mozilla Public License
Group:		X11/Applications/Networking
Source0:	ftp://ftp.mozilla.org/pub/mozilla/releases/mozilla%{version}/src/%{name}-source-%{version}.tar.bz2
# Source0-md5:	58c37a29ef2fae2939f5be116abec32a
Source1:	%{name}.desktop
Source2:	%{name}.png
Source4:	%{name}-addressbook.desktop
Source5:	%{name}-chat.desktop
Source6:	%{name}-jconsole.desktop
Source7:	%{name}-mail.desktop
Source8:	%{name}-news.desktop
Source9:	%{name}-terminal.desktop
Source10:	%{name}-venkman.desktop
Source11:	http://dl.sourceforge.net/mozillapl/Lang-PL-Build-ID-%{version}.xpi
# Source11-md5:	ff815e9e9a5b2b2184a46ce0ab3dd94e
Source12:	http://dl.sourceforge.net/mozillapl/Reg-PL-Build-ID-%{version}.xpi
# Source12-md5:	251dc06cc99b6b9d55bf66af743a34d4
Source13:	lang_pl-installed-chrome.txt
Source14:	%{name}-antialiasing-howto.txt
Patch0:		%{name}-pld-homepage.patch
Patch1:		%{name}-nss.patch
Patch2:		%{name}-ldap_nspr_includes.patch
Patch3:		%{name}-ldap-with-nss.patch
Patch4:		%{name}-gfx.patch
Patch5:		%{name}-alpha-gcc3.patch
Patch6:		%{name}-64bit.patch
#Patch5:		%{name}-gtk2.patch
URL:		http://www.mozilla.org/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	freetype-devel >= 2.1.3
BuildRequires:	gtk+-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel >= 1.0.4
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	nss-devel >= 3.6
BuildRequires:	nspr-devel >= 4.2.2-2
BuildRequires:	perl-modules >= 5.6.0
BuildRequires:	unzip
BuildRequires:	zip >= 2.1
Requires(post,postun):	/sbin/ldconfig
Requires:	nss >= 3.6
Provides:	mozilla(gtk1) = %{epoch}:%{version}-%{release}
Provides:	mozilla-embedded = %{epoch}:%{version}-%{release}
Provides:	mozilla-embedded(gtk1) = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	mozilla-Lang-PL
Obsoletes:	mozilla-embedded
Obsoletes:	mozilla-irc
Obsoletes:	mozilla-theme-NegativeModern
Obsoletes:	mozilla-theme-gold
Obsoletes:	mozilla-theme-kzilla

%define		_chromedir	%{_libdir}/%{name}/chrome
%define		_prefix		/usr/X11R6

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
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	%{name} = %{epoch}:%{version}
Requires:	%{name} = %{epoch}:%{version}
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
Requires:	%{name} = %{epoch}:%{version}
Requires:	nspr-devel
Provides:	mozilla-embedded-devel = %{epoch}:%{version}-%{release}
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%ifarch alpha sparc64
%patch6 -p1
%endif
#%patch5 -p0

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
	--enable-toolkit-gtk \
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
# remove empty directory trees
rm -fr dist/bin/chrome/{US,chatzilla,classic,comm,content-packs,cview,embed,embed-sample,en-US,en-mac,en-unix,en-win,forms,help,inspector,messenger,modern,pipnss,pippki,toolkit,venkman,xmlterm}
# non-unix
rm -f dist/bin/chrome/en-{mac,win}.jar
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
cp -frL dist/bin/icons/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/icons
cp -frL dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -frL dist/bin/searchplugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins
cp -frL dist/idl/*		$RPM_BUILD_ROOT%{_datadir}/idl
cp -frL dist/include/*		$RPM_BUILD_ROOT%{_includedir}/%{name}
cp -frL dist/public/ldap{,-private} $RPM_BUILD_ROOT%{_includedir}/%{name}

install dist/bin/*.so $RPM_BUILD_ROOT%{_libdir}

for f in build/unix/*.pc ; do
	sed -e 's/%{name}-%{version}/%{name}/' $f \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/$(basename $f)
done

sed -e 's,lib/%{name}-%{version},lib,g;s/%{name}-%{version}/%{name}/g' build/unix/mozilla-gtkmozembed.pc \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-gtkmozembed.pc

		
sed -e 's|/%{name}-%{version}||' build/unix/mozilla-nspr.pc \
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

cp %{SOURCE14} .

# pl-stuff:
unzip %{SOURCE11} -d $RPM_BUILD_ROOT%{_libdir}
unzip -n %{SOURCE12} -d $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT%{_libdir}/bin/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv $RPM_BUILD_ROOT%{_libdir}/bin/searchplugins/* $RPM_BUILD_ROOT%{_libdir}/mozilla/searchplugins
install %{SOURCE13} $RPM_BUILD_ROOT%{_chromedir}/lang_pl-installed-chrome.txt
cd $RPM_BUILD_ROOT%{_chromedir}
unzip PL.jar
zip -r PL.jar locale
rm -rf locale

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom

cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%postun
/sbin/ldconfig
if [ "$1" = "2" ]; then
	umask 022
	rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat
	MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom
fi

%post mailnews
/sbin/ldconfig
umask 022
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom

%postun mailnews
/sbin/ldconfig
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

%doc %{name}-antialiasing-howto.txt

%dir %{_libdir}/%{name}
%dir %{_chromedir}
%dir %{_libdir}/%{name}/components
%dir %{_libdir}/%{name}/defaults
%dir %{_libdir}/%{name}/icons
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/res
%dir %{_libdir}/%{name}/searchplugins
%dir %{_datadir}/%{name}

%attr(755,root,root) %{_libdir}/libgkgfx.so
%attr(755,root,root) %{_libdir}/libgtkembedmoz.so
%attr(755,root,root) %{_libdir}/libgtksuperwin.so
%attr(755,root,root) %{_libdir}/libgtkxtbin.so
%attr(755,root,root) %{_libdir}/libjsj.so
%attr(755,root,root) %{_libdir}/libldap50.so
%attr(755,root,root) %{_libdir}/libprldap50.so
%attr(755,root,root) %{_libdir}/libssldap50.so
%attr(755,root,root) %{_libdir}/libmozjs.so
%attr(755,root,root) %{_libdir}/libmoz_art_lgpl.so
%attr(755,root,root) %{_libdir}/libnullplugin.so
%attr(755,root,root) %{_libdir}/libxpcom.so
%attr(755,root,root) %{_libdir}/libxpistub.so
%attr(755,root,root) %{_libdir}/libxlibrgb.so

%attr(755,root,root) %{_libdir}/%{name}/components/libaccess*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libappcomps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libautoconfig.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcaps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libchrome.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcomposer.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcookie.so
%attr(755,root,root) %{_libdir}/%{name}/components/libdocshell.so
%attr(755,root,root) %{_libdir}/%{name}/components/libeditor.so
%attr(755,root,root) %{_libdir}/%{name}/components/libembedcomponents.so
%attr(755,root,root) %{_libdir}/%{name}/components/libfileview.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgfx*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgk*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libhtmlpars.so
%attr(755,root,root) %{_libdir}/%{name}/components/libi18n.so
%attr(755,root,root) %{_libdir}/%{name}/components/libiiextras.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimg*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libinspector.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjar50.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsd.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsdom.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsurl.so

%attr(755,root,root) %{_libdir}/%{name}/components/libmork.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmoz*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnecko*.so
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
%attr(755,root,root) %{_libdir}/%{name}/components/libregviewer.so
%attr(755,root,root) %{_libdir}/%{name}/components/libshistory.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtransformiix.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtxmgr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtypeaheadfind.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuconv.so
%attr(755,root,root) %{_libdir}/%{name}/components/libucv*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuniversalchardet.so
%attr(755,root,root) %{_libdir}/%{name}/components/liburiloader.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwallet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwalletviewers.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebbrwsr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwidget_gtk.so
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
%{_libdir}/%{name}/components/iiextras.xpt
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
%{_libdir}/%{name}/components/regviewer.xpt
%{_libdir}/%{name}/components/related.xpt
%{_libdir}/%{name}/components/search.xpt
%{_libdir}/%{name}/components/shistory.xpt
%{_libdir}/%{name}/components/sidebar.xpt
%{_libdir}/%{name}/components/signonviewer.xpt
%{_libdir}/%{name}/components/timebomb.xpt
%{_libdir}/%{name}/components/txmgr.xpt
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

%{_libdir}/install.js
%{_libdir}/%{name}/components/chatzilla-service.js
%{_libdir}/%{name}/components/jsconsole-clhandler.js
%{_libdir}/%{name}/components/nsDictionary.js
%{_libdir}/%{name}/components/nsDownloadProgressListener.js
%{_libdir}/%{name}/components/nsFilePicker.js
%{_libdir}/%{name}/components/nsHelperAppDlg.js
%{_libdir}/%{name}/components/nsInterfaceInfoToIDL.js
%{_libdir}/%{name}/components/nsKillAll.js
%{_libdir}/%{name}/components/nsProgressDialog.js
%{_libdir}/%{name}/components/nsProxyAutoConfig.js
%{_libdir}/%{name}/components/nsResetPref.js
%{_libdir}/%{name}/components/nsSidebar.js
%{_libdir}/%{name}/components/nsUpdateNotifier.js
%{_libdir}/%{name}/components/nsXmlRpcClient.js
%{_libdir}/%{name}/components/venkman-service.js
%{_libdir}/%{name}/components/xmlterm-service.js

# not *.dat, so check-files can catch any new files
# (and they won't be just silently placed empty in rpm)
%ghost %{_libdir}/%{name}/components/compreg.dat
%ghost %{_libdir}/%{name}/components/xpti.dat

%dir %{_datadir}/%{name}/chrome

%{_datadir}/%{name}/chrome/US.jar
%{_datadir}/%{name}/chrome/chatzilla.jar
%{_datadir}/%{name}/chrome/classic.jar
%{_datadir}/%{name}/chrome/comm.jar
%{_datadir}/%{name}/chrome/content-packs.jar
%{_datadir}/%{name}/chrome/cview.jar
%{_datadir}/%{name}/chrome/embed-sample.jar
%{_datadir}/%{name}/chrome/en-US.jar
%{_datadir}/%{name}/chrome/en-unix.jar
%{_datadir}/%{name}/chrome/forms.jar
%{_datadir}/%{name}/chrome/help.jar
%{_datadir}/%{name}/chrome/inspector.jar
%{_datadir}/%{name}/chrome/modern.jar
%{_datadir}/%{name}/chrome/pipnss.jar
%{_datadir}/%{name}/chrome/pippki.jar
%{_datadir}/%{name}/chrome/toolkit.jar
%{_datadir}/%{name}/chrome/venkman.jar
%{_datadir}/%{name}/chrome/xmlterm.jar

# some *.rdf files are broken in 1.2.1, so it must stay here...
# bringing non-working Messenger window to base mozilla :/
%{_datadir}/%{name}/chrome/messenger.jar

%{_datadir}/%{name}/chrome/chrome.rdf
%{_datadir}/%{name}/chrome/chromelist.txt
%{_datadir}/%{name}/chrome/icons
%exclude %{_datadir}/%{name}/chrome/icons/default/abcardWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/addressbookWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/messengerWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/msgcomposeWindow*.xpm

%{_datadir}/%{name}/chrome/overlayinfo
%{_datadir}/%{name}/chrome/mozilla-installed-chrome.txt
%ghost %{_datadir}/%{name}/chrome/installed-chrome.txt

%lang(pl) %{_datadir}/%{name}/chrome/lang_pl-installed-chrome.txt
%lang(pl) %{_datadir}/%{name}/chrome/PL.jar
%lang(pl) %{_datadir}/%{name}/chrome/pl-PL.jar
%lang(pl) %{_datadir}/%{name}/chrome/pl-unix.jar

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

%attr(755,root,root) %{_libdir}/%{name}/components/libabsyncsvc.so
%attr(755,root,root) %{_libdir}/%{name}/components/libaddrbook.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimpText.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimpComm4xMail.so
%attr(755,root,root) %{_libdir}/%{name}/components/libimport.so
%attr(755,root,root) %{_libdir}/%{name}/components/liblocalmail.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmailnews.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmimeemitter.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmime.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmsg*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libvcard.so

%{_libdir}/%{name}/components/absync.xpt
%{_libdir}/%{name}/components/addrbook.xpt
%{_libdir}/%{name}/components/impComm4xMail.xpt
%{_libdir}/%{name}/components/import.xpt
%{_libdir}/%{name}/components/mailnews.xpt
%{_libdir}/%{name}/components/mime.xpt
%{_libdir}/%{name}/components/msg*.xpt

%{_libdir}/%{name}/components/mdn-service.js
%{_libdir}/%{name}/components/nsLDAPPrefsService.js
%{_libdir}/%{name}/components/smime-service.js

# should belong here, but see above
#%{_datadir}/%{name}/chrome/messenger.jar

%{_datadir}/%{name}/chrome/icons/default/abcardWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/addressbookWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/messengerWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/msgcomposeWindow*.xpm

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
