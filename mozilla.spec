#
# Conditional build:
# _with_gdkxft
# _with_gtk2
# _without_PL

Summary:	Mozilla - web browser
Summary(es):	Navegador de Internet Mozilla
Summary(pl):	Mozilla - przegl�darka WWW
Summary(pt_BR):	Navegador Mozilla
Summary(ru):	Web browser
Name:		mozilla
Version:	1.0.2
Release:	2
Epoch:		2
License:	GPL
Group:		X11/Applications/Networking
Source0:	ftp://ftp.mozilla.org/pub/mozilla/releases/mozilla%{version}/src/%{name}-source-%{version}.tar.bz2
# Source0-md5:	faddffb99f6566771e3accc0043e49a5
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}-libart.tar.bz2
Source4:	%{name}-addressbook.desktop
Source5:	%{name}-chat.desktop
Source6:	%{name}-jconsole.desktop
Source7:	%{name}-mail.desktop
Source8:	%{name}-news.desktop
Source9:	%{name}-terminal.desktop
Source10:	%{name}-venkman.desktop
Source11:	ftp://ftp.sourceforge.net/pub/sourceforge/mozillapl/Lang-PL-Build-ID-%{version}.xpi
# Source11-md5:	c9a595e50f245cba407813e01d34bd9f
Source12:	ftp://ftp.sourceforge.net/pub/sourceforge/mozillapl/Reg-PL-Build-ID-%{version}.xpi
# Source12-md5:	9fcf4fabb73b618a60b4a1bd7fc40602
Source13:	http://free.of.pl/a/adgor/lang_pl-installed-chrome.txt
# Source13-md5:	72ec9f5cdd03be565cf585a8db713154
Source14:	%{name}-antialiasing-howto.txt
Patch0:		%{name}-pld-homepage.patch
Patch1:		%{name}-gdkxft.patch
Patch2:		%{name}-nss.patch
Patch3:		%{name}-ldap_nspr_includes.patch
Patch4:		http://people.redhat.com/blizzard/mozilla/gtk2_embedding/2002-04-11/gtk2_embed.patch
Patch5:		http://people.redhat.com/blizzard/mozilla/gtk2_embedding/2002-04-11/gtk2_widget.patch
Patch6:		%{name}-pld-homepage-PL.patch
Patch7:		%{name}-ldap-with-nss.patch
URL:		http://www.mozilla.org/projects/newlayout/
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	freetype-devel >= 2.0.9
%{!?_with_gtk2:BuildRequires:	gtk+-devel}
%{?_with_gtk2:BuildRequires:	gtk+2-devel >= 2.0.2}
%{?_with_gtk2:BuildRequires:	pkgconfig}
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel >= 1.0.4
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	nss-devel >= 3.6-1
BuildRequires:	nspr-devel >= 4.2.2-2
BuildRequires:	perl-modules >= 5.6.0
%{!?_without_PL:BuildRequires: unzip}
BuildRequires:	zip >= 2.1
Provides:	mozilla-embedded = %{version}
%{?_with_gdkxft:Requires:	gdkxft}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	nss >= 3.6-1
Obsoletes:	mozilla-embedded
Obsoletes:	mozilla-irc
%{!?_without_PL:Conflicts: mozilla-Lang-PL}

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_chromedir	%{_libdir}/%{name}/chrome

%define		_gcc_ver	%(%{__cc} -dumpversion | cut -b 1)
%if %{_gcc_ver} == 2
%define		__cxx		"%{__cc}"
%endif

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

%description -l ru
Mozilla - ������������������� web-browser � ��������� ���������
��������, ������������� ��� ������������� ����������� ����������,
������������� ������������� � �������� ������

%package mailnews
Summary:	Mozilla - programs for mail and news
Summary(pl):	Mozilla - programy do poczty i news�w
Summary(ru):	�������� ������� �� ������ Mozilla
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}
Obsoletes:	mozilla-mail

%description mailnews
Programs for mail and news integrated with browser.

%description mailnews -l pl
Programy pocztowe i obs�uga news�w zintegrowane z przegl�dark�.

%description mailnews -l ru
������ ����� � ��������, �� ������ Mozilla. ������������ IMAP, POP �
NNTP � ����� ������� ��������� ������������.

%package devel
Summary:	Headers for developing programs that will use Mozilla
Summary(pl):	Mozilla - pliki nag��wkowe i biblioteki
Summary(pt_BR):	Arquivos de inclus�o para desenvolvimento de programas que usam o Mozilla
Summary(ru):	�����, ����������� ��� ������������� ��������, ���������� Mozilla
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	nspr-devel
Provides:	mozilla-embedded-devel = %{version}
Obsoletes:	mozilla-embedded-devel

%description devel
Mozilla development package.

%description devel -l pl
Biblioteki i pliki nag��wkowe.

%description devel -l pt_BR
Arquivos de inclus�o para desenvolvimento de programas que usam o
Mozilla.

%description devel -l ru
������������ �����, ����������� ��� ���������� ��������, �������������
Mozilla

%prep
%setup -q -a 3 -n mozilla
%patch0 -p1
%{?_with_gdkxft:%patch1 -p1}
%patch2 -p1
%patch3 -p1
%{?_with_gtk2:%patch4 -p1}
%{?_with_gtk2:%patch5 -p1}
%patch7 -p1

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
	%{!?_with_gtk2:--enable-toolkit-gtk} \
	%{?_with_gtk2:--disable-toolkit-gtk --enable-default-toolkit=gtk2} \
	--enable-xinerama \
	--enable-xprint \
	--enable-xsl \
	--disable-xterm-updates \
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
install dist/bin/component.reg $RPM_BUILD_ROOT%{_libdir}/%{name}

ln -sf ../../share/mozilla/chrome $RPM_BUILD_ROOT%{_chromedir}
ln -sf ../../share/mozilla/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults
ln -sf ../../share/mozilla/icons $RPM_BUILD_ROOT%{_libdir}/%{name}/icons
ln -sf ../../share/mozilla/res $RPM_BUILD_ROOT%{_libdir}/%{name}/res
ln -sf ../../share/mozilla/searchplugins $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins

cp -frL dist/bin/chrome/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
cp -frL dist/bin/components/*	$RPM_BUILD_ROOT%{_libdir}/%{name}/components
cp -frL dist/bin/defaults/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
%{!?_with_gtk2:cp -frL dist/bin/icons/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/icons}
cp -frL dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -frL dist/bin/searchplugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins
cp -frL dist/idl/*		$RPM_BUILD_ROOT%{_datadir}/idl
cp -frL dist/include/*		$RPM_BUILD_ROOT%{_includedir}/%{name}
cp -frL dist/public/ldap{,-private} $RPM_BUILD_ROOT%{_includedir}/%{name}

install dist/bin/*.so $RPM_BUILD_ROOT%{_libdir}

install build/unix/*.pc $RPM_BUILD_ROOT%{_pkgconfigdir}

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

%if %{!?_without_PL:1}%{?_without_PL:0}
unzip %{SOURCE11} -d $RPM_BUILD_ROOT%{_libdir}
unzip -n %{SOURCE12} -d $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT%{_libdir}/bin/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv $RPM_BUILD_ROOT%{_libdir}/bin/searchplugins/* $RPM_BUILD_ROOT%{_libdir}/mozilla/searchplugins
install %{SOURCE13} $RPM_BUILD_ROOT%{_chromedir}
cd $RPM_BUILD_ROOT%{_chromedir}
unzip PL.jar
patch -p0  < %{PATCH6}
zip -r PL.jar locale
rm -rf locale
cd -
%endif

cp %{SOURCE14} .

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
rm -f %{_libdir}/mozilla/component.reg
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom

cd %{_chromedir}
cat *-installed-chrome.txt >installed-chrome.txt

%postun	-p /sbin/ldconfig

%post mailnews
/sbin/ldconfig
umask 022
rm -f %{_libdir}/mozilla/component.reg
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom

%postun mailnews -p /sbin/ldconfig

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

%ghost %{_libdir}/%{name}/component.reg
%attr(755,root,root) %{_libdir}/libgkgfx.so
%attr(755,root,root) %{_libdir}/libgtkembedmoz.so
%{!?_with_gtk2:%attr(755,root,root) %{_libdir}/libgtksuperwin.so}
%{!?_with_gtk2:%attr(755,root,root) %{_libdir}/libgtkxtbin.so}
%attr(755,root,root) %{_libdir}/libjsj.so
%attr(755,root,root) %{_libdir}/libldap50.so
%attr(755,root,root) %{_libdir}/libprldap50.so
%attr(755,root,root) %{_libdir}/libssldap50.so
%attr(755,root,root) %{_libdir}/libmozjs.so
%attr(755,root,root) %{_libdir}/libmozpango.so
%attr(755,root,root) %{_libdir}/libmozpango-thaix.so
%attr(755,root,root) %{_libdir}/libmoz_art_lgpl.so
%{!?_with_gtk2:%attr(755,root,root) %{_libdir}/libnullplugin.so}
%attr(755,root,root) %{_libdir}/libxpcom.so
%attr(755,root,root) %{_libdir}/libxpistub.so
%attr(755,root,root) %{_libdir}/libxlibrgb.so

%attr(755,root,root) %{_libdir}/%{name}/components/libaccess*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libappcomps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libautoconfig.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcaps.so
%attr(755,root,root) %{_libdir}/%{name}/components/libchardet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libchrome.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcomposer.so
%attr(755,root,root) %{_libdir}/%{name}/components/libcookie.so
%attr(755,root,root) %{_libdir}/%{name}/components/libctl.so
%attr(755,root,root) %{_libdir}/%{name}/components/libdocshell.so
%attr(755,root,root) %{_libdir}/%{name}/components/libeditor.so
%attr(755,root,root) %{_libdir}/%{name}/components/libembedcomponents.so
%attr(755,root,root) %{_libdir}/%{name}/components/libfileview.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgfx*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libgk*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libhtmlpars.so
%attr(755,root,root) %{_libdir}/%{name}/components/libiiextras.so
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
%attr(755,root,root) %{_libdir}/%{name}/components/libp3p.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpipboot.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpipnss.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpippki.so
%attr(755,root,root) %{_libdir}/%{name}/components/libpref.so
%attr(755,root,root) %{_libdir}/%{name}/components/libprofile.so
%attr(755,root,root) %{_libdir}/%{name}/components/librdf.so
%attr(755,root,root) %{_libdir}/%{name}/components/libregviewer.so
%attr(755,root,root) %{_libdir}/%{name}/components/libshistory.so
%attr(755,root,root) %{_libdir}/%{name}/components/libstrres.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtransformiix.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtxmgr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtxtsvc.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuconv.so
%attr(755,root,root) %{_libdir}/%{name}/components/libucv*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libunicharutil.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuniversalchardet.so
%attr(755,root,root) %{_libdir}/%{name}/components/liburiloader.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwallet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwalletviewers.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebbrwsr.so
%{!?_with_gtk2:%attr(755,root,root) %{_libdir}/%{name}/components/libwidget_gtk.so}
%{?_with_gtk2:%attr(755,root,root) %{_libdir}/%{name}/components/libwidget_gtk2.so}
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
%{_libdir}/%{name}/components/transformiix.xpt
%{_libdir}/%{name}/components/txmgr.xpt
%{_libdir}/%{name}/components/txtsvc.xpt
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
%{_libdir}/%{name}/components/windowwatcher.xpt
%{_libdir}/%{name}/components/x*.xpt

%{_libdir}/%{name}/components/*.js
%{_libdir}/%{name}/components/*.dat

%dir %{_datadir}/%{name}/chrome
%{_datadir}/%{name}/chrome/[!lpP]*
%{_datadir}/%{name}/chrome/pipnss.jar
%{_datadir}/%{name}/chrome/pippki.jar
%{!?_without_PL:%lang(pl) %{_datadir}/%{name}/chrome/lang_pl-installed-chrome.txt}
%{!?_without_PL:%lang(pl) %{_datadir}/%{name}/chrome/PL.jar}
%{!?_without_PL:%lang(pl) %{_datadir}/%{name}/chrome/pl-PL.jar}
%{!?_without_PL:%lang(pl) %{_datadir}/%{name}/chrome/pl-unix.jar}

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
