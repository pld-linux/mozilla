#
# Conditional build:
%bcond_with	gtk1	# use GTK+ 1.2.x instead of 2.x.x
%bcond_with	gcc2	# compile using gcc2 to get working macromedia-flash and
			# gcc2-compiled Java plugins on nest and other gcc 3.x systems.
			# WARNING! You have to recompile galeon with gcc2 in
			# order to get it working with this release of mozilla
%bcond_with	ft218	# compile with freetype >= 2.1.8
%bcond_without	gnomevfs	# disable GnomeVFS support

%bcond_without	heimdal	# disable heimdal support
%bcond_without	svg	# disable svg support
#
Summary:	Mozilla - web browser
Summary(es):	Navegador de Internet Mozilla
Summary(pl):	Mozilla - przegl±darka WWW
Summary(pt_BR):	Navegador Mozilla
Summary(ru):	Web browser
Name:		mozilla
Version:	1.7.5
Release:	1
Epoch:		5
License:	Mozilla Public License
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/mozilla/releases/mozilla%{version}/source/%{name}-source-%{version}.tar.bz2
# Source0-md5:	e5994f3e801cd834966367c6a12f8aeb
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}-composer.desktop
Source5:	%{name}-chat.desktop
Source6:	%{name}-jconsole.desktop
Source7:	%{name}-mail.desktop
Source9:	%{name}-terminal.desktop
Source10:	%{name}-venkman.desktop
#Source11:	%{name}-libart.tar.bz2
## Source11-md5:	d6834f4881d5947b4e0540f46b7edfb6
Patch0:		%{name}-pld-homepage.patch
Patch1:		%{name}-nss.patch
Patch2:		%{name}-ldap_nspr_includes.patch
Patch3:		%{name}-ldap-with-nss.patch
Patch4:		%{name}-gfx.patch
Patch5:		%{name}-alpha-gcc3.patch
# http://bugzilla.mozilla.org/show_bug.cgi?id=234035
# http://bugzilla.mozilla.org/attachment.cgi?id=149334&action=view
Patch6:		%{name}-freetype218.patch
URL:		http://www.mozilla.org/
%{?with_gtk1:BuildRequires:	ORBit-devel}
%{?with_svg:BuildRequires:	cairo-devel >= 0.1.17}
%if %{with ft218}
BuildRequires:	freetype-devel >= 1:2.1.8
%else
BuildRequires:	freetype-devel >= 2.1.3
BuildRequires:	freetype-devel < 1:2.1.8
BuildConflicts:	freetype-devel = 2.1.8
%endif
%{?with_gnomevfs:BuildRequires:	gnome-vfs2-devel >= 2.0.0}
%{?with_gtk1:BuildRequires:	gtk+-devel >= 1.2.0}
%{!?with_gtk1:BuildRequires:	gtk+2-devel >= 2:2.2.0}
# for libnegotiateauth
%{?with_heimdal:BuildRequires:	heimdal-devel}
%{!?with_gtk1:BuildRequires:	libIDL-devel >= 0.8.0}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel >= 1:4.6-0.20041030.1
BuildRequires:	nss-devel >= 3.8
%{!?with_gtk1:BuildRequires:	pango-devel >= 1:1.1.0}
BuildRequires:	perl-modules >= 5.6.0
BuildRequires:	pkgconfig
BuildRequires:	xcursor-devel
BuildRequires:	xft-devel >= 2.1-2
BuildRequires:	zip >= 2.1
BuildRequires:	zlib-devel >= 1.0.0
Requires(post,postun):	/sbin/ldconfig
Requires:	nspr >= 1:4.6-0.20041030.1
Requires:	nss >= 3.8
%{?with_gtk1:Provides:	mozilla(gtk1) = %{epoch}:%{version}-%{release}}
%{!?with_gtk1:Provides:	mozilla(gtk2) = %{epoch}:%{version}-%{release}}
Provides:	mozilla-embedded = %{epoch}:%{version}-%{release}
%{?with_gtk1:Provides:	mozilla-embedded(gtk1) = %{epoch}:%{version}-%{release}}
%{!?with_gtk1:Provides:	mozilla-embedded(gtk2) = %{epoch}:%{version}-%{release}}
Obsoletes:	light
Obsoletes:	mozilla-embedded
Obsoletes:	mozilla-irc
Obsoletes:	mozilla-theme-NegativeModern
Obsoletes:	mozilla-theme-gold
Obsoletes:	mozilla-theme-kzilla
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/%{name}/chrome
# mozilla and firefox provide their own versions
%define		_noautoreqdep	libgkgfx.so libgtkxtbin.so libjsj.so libmozjs.so libxpcom.so libxpcom_compat.so

%if %{with gcc2}
%define		__cc		gcc2
%define		__cxx		gcc2
%endif

%define		_gcc_ver	%(%{__cc} -dumpversion | cut -b 1)
%if %{_gcc_ver} == 2
%define		__cxx		"%{__cc}"
%endif

%if %{with gtk1}
%undefine	with_gnomevfs
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
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	mozilla-mail

%description mailnews
Programs for mail and news integrated with browser.

%description mailnews -l pl
Programy pocztowe i obs³uga newsów zintegrowane z przegl±dark±.

%description mailnews -l ru
ëÌÉÅÎÔ ÐÏÞÔÙ É ÎÏ×ÏÓÔÅÊ, ÎÁ ÏÓÎÏ×Å Mozilla. ðÏÄÄÅÒÖÉ×ÁÅÔ IMAP, POP É
NNTP É ÉÍÅÅÔ ÐÒÏÓÔÏÊ ÉÎÔÅÒÆÅÊÓ ÐÏÌØÚÏ×ÁÔÅÌÑ.

%package chat
Summary:	Mozilla Chat - IRC client integrated with Mozilla
Summary(pl):	Mozilla Chat - zintegrowany z Mozill± klient IRC-a
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description chat
Mozilla Chat - IRC client that is integrated with the Mozilla web
browser.

%description chat -l pl
Mozilla Chat - klient IRC-a zintegrowany z przegl±dark± Mozilla.

%package js-debugger
Summary:	JavaScript debugger for use with Mozilla
Summary(pl):	Odpluskwiacz JavaScriptu do u¿ywania z Mozill±
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description js-debugger
JavaScript debugger for use with Mozilla.

%description js-debugger -l pl
Odpluskwiacz JavaScriptu do u¿ywania z Mozill±.

%package dom-inspector
Summary:	A tool for inspecting the DOM of pages in Mozilla
Summary(pl):	Narzêdzie do ogl±dania DOM stron w Mozilli
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description dom-inspector
This is a tool that allows you to inspect the DOM for web pages in
Mozilla. This is of great use to people who are doing Mozilla chrome
development or web page development.

%description dom-inspector -l pl
To narzêdzie pozwala na ogl±danie DOM dla stron WWW w Mozilli. Jest
bardzo przydatne dla ludzi rozwijaj±cych chrome w Mozilli lub
tworz±cych strony WWW.

%package gnomevfs
Summary:	Gnome-VFS module providing support for smb:// URLs
Summary(pl):	Modu³ Gnome-VFS dodaj±cy wsparcie dla URLi smb://
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description gnomevfs
Gnome-VFS module providing support for smb:// URLs.

%description gnomevfs -l pl
Modu³ Gnome-VFS dodaj±cy wsparcie dla URLi smb://.

%package calendar
Summary:	Mozilla calendar
Summary(pl):	Kalendarz Mozilli
Group:		X11/Applications/Networking
Requires(post,postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description calendar
This package contains the calendar application from the Mozilla suite.

%description calendar -l pl
Ten pakiet zawiera kalendarz z zestawu aplikacji Mozilla.

%package devel
Summary:	Headers for developing programs that will use Mozilla
Summary(pl):	Mozilla - pliki nag³ówkowe i biblioteki
Summary(pt_BR):	Arquivos de inclusão para desenvolvimento de programas que usam o Mozilla
Summary(ru):	æÁÊÌÙ, ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÉÓÐÏÌØÚÏ×ÁÎÉÑ ÐÒÏÇÒÁÍÍ, ×ËÌÀÞÁÀÝÉÈ Mozilla
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	nspr-devel >= 1:4.6-0.20041030.1
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
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%{?with_ft218:%patch6 -p0}

%build
BUILD_OFFICIAL="1"; export BUILD_OFFICIAL
MOZILLA_OFFICIAL="1"; export MOZILLA_OFFICIAL
#MOZ_INTERNAL_LIBART_LGPL="1"; export MOZ_INTERNAL_LIBART_LGPL

%if %{_gcc_ver} > 2
CXXFLAGS="-Wno-deprecated"; export CXXFLAGS
%endif
cp -f /usr/share/automake/config.* build/autoconf
cp -f /usr/share/automake/config.* nsprpub/build/autoconf
cp -f /usr/share/automake/config.* directory/c-sdk/config/autoconf
%configure2_13 \
	%{!?debug:--disable-debug} \
	--disable-elf-dynstr-gc \
	--disable-pedantic \
	--disable-tests \
	--enable-calendar \
	--enable-crypto \
	--enable-extensions \
	--enable-ldap \
	--enable-mathml \
	--enable-optimize="%{rpmcflags}" \
	--enable-postscript \
	%{!?debug:--enable-strip} \
	%{?with_svg:--enable-svg} \
	%{?with_svg:--enable-svg-renderer-cairo} \
	%{?with_gtk1:--enable-toolkit-gtk} \
	%{!?with_gtk1:--disable-toolkit-gtk --enable-default-toolkit=gtk2} \
	%{!?with_gnomevfs:--disable-gnomevfs} \
	--enable-xft \
	--enable-xinerama \
	--enable-xprint \
	--disable-xterm-updates \
	--enable-old-abi-compat-wrappers \
	--with-default-mozilla-five-home=%{_libdir}/mozilla \
	--with-pthreads \
	--with-system-jpeg \
	--with-system-nspr \
	--with-system-png \
	--with-system-zlib \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_datadir}/idl} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{chrome,defaults,icons,res,searchplugins,greprefs} \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/{components,plugins} \
	$RPM_BUILD_ROOT{%{_includedir}/%{name},%{_pkgconfigdir}}

# preparing to create register
# remove empty directory trees
rm -fr dist/bin/chrome/{US,chatzilla,classic,comm,content-packs,cview,embed,embed-sample,en-US,en-mac,en-unix,en-win,help,inspector,messenger,modern,pipnss,pippki,toolkit,venkman,xmlterm}
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
ln -sf ../../share/mozilla/greprefs $RPM_BUILD_ROOT%{_libdir}/%{name}/greprefs
ln -sf ../../share/mozilla/icons $RPM_BUILD_ROOT%{_libdir}/%{name}/icons
ln -sf ../../share/mozilla/res $RPM_BUILD_ROOT%{_libdir}/%{name}/res
ln -sf ../../share/mozilla/searchplugins $RPM_BUILD_ROOT%{_libdir}/%{name}/searchplugins

cp -frL dist/bin/chrome/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
cp -frL dist/bin/components/*	$RPM_BUILD_ROOT%{_libdir}/%{name}/components
cp -frL dist/bin/defaults/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
%{?with_gtk1:cp -frL dist/bin/icons/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/icons}
cp -frL dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -frL dist/bin/searchplugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins
cp -frL dist/gre/greprefs/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/greprefs
cp -frL dist/idl/*		$RPM_BUILD_ROOT%{_datadir}/idl
cp -frL dist/include/*		$RPM_BUILD_ROOT%{_includedir}/%{name}
cp -frL dist/public/ldap{,-private} $RPM_BUILD_ROOT%{_includedir}/%{name}

install dist/bin/*.so $RPM_BUILD_ROOT%{_libdir}

ln -s %{_libdir}/libxpcom.so $RPM_BUILD_ROOT%{_libdir}/%{name}/libxpcom.so
ln -s %{_libdir}/libnssckbi.so $RPM_BUILD_ROOT%{_libdir}/%{name}/libnssckbi.so

for f in build/unix/*.pc ; do
	sed -e 's/mozilla-%{version}/mozilla/' $f \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/$(basename $f)
done

sed -e 's,lib/mozilla-%{version},lib,g;s/mozilla-%{version}/mozilla/g' build/unix/mozilla-gtkmozembed.pc \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-gtkmozembed.pc


rm -f $RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-nss.pc $RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-nspr.pc

install %{SOURCE1} %{SOURCE3} %{SOURCE5} %{SOURCE6} %{SOURCE7} \
	%{SOURCE9} %{SOURCE10} $RPM_BUILD_ROOT%{_desktopdir}

install %{SOURCE2}	$RPM_BUILD_ROOT%{_pixmapsdir}

install dist/bin/mozilla-bin $RPM_BUILD_ROOT%{_bindir}
install dist/bin/regchrome $RPM_BUILD_ROOT%{_bindir}
install dist/bin/regxpcom $RPM_BUILD_ROOT%{_bindir}

cp $RPM_BUILD_ROOT%{_chromedir}/installed-chrome.txt \
	$RPM_BUILD_ROOT%{_chromedir}/%{name}-installed-chrome.txt

cat << EOF > $RPM_BUILD_ROOT%{_bindir}/mozilla
#!/bin/sh
# (c) vip at linux.pl, wolf at pld-linux.org

MOZILLA_FIVE_HOME=%{_libdir}/mozilla
if [ "\$1" == "-remote" ]; then
	%{_bindir}/mozilla-bin "\$@"
else
	PING=\`%{_bindir}/mozilla-bin -remote 'ping()' 2>&1 >/dev/null\`
	if [ -n "\$PING" ]; then
		if [ -f "\`pwd\`/\$1" ]; then
			%{_bindir}/mozilla-bin "file://\`pwd\`/\$1"
		else
			%{_bindir}/mozilla-bin "\$@"
		fi
	else
		if [ -z "\$1" ]; then
			%{_bindir}/mozilla-bin -remote 'xfeDoCommand (openBrowser)'
		elif [ "\$1" == "-mail" ]; then
			%{_bindir}/mozilla-bin -remote 'xfeDoCommand (openInbox)'
		elif [ "\$1" == "-compose" ]; then
			%{_bindir}/mozilla-bin -remote 'xfeDoCommand (composeMessage)'
		else
			if [ -f "\`pwd\`/\$1" ]; then
				URL="file://\`pwd\`/\$1"
			else
				URL="\$1"
			fi
			grep browser.tabs.opentabfor.middleclick ~/.mozilla/default/*/prefs.js | grep true > /dev/null
			if [ $? -eq 0 ]; then
				%{_bindir}/mozilla-bin -remote "OpenUrl(\$URL,new-tab)"
			else
				%{_bindir}/mozilla-bin -remote "OpenUrl(\$URL,new-window)"
			fi
		fi
	fi
fi
EOF

cat << EOF > $RPM_BUILD_ROOT%{_sbindir}/mozilla-chrome+xpcom-generate
#!/bin/sh
umask 022
cd %{_datadir}/mozilla/chrome
cat *-installed-chrome.txt > installed-chrome.txt
rm -f chrome.rdf overlayinfo/*/*/*.rdf
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regchrome
exit 0
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
/sbin/ldconfig
if [ "$1" = "1" ]; then
	%{_sbindir}/mozilla-chrome+xpcom-generate
fi

%post mailnews
/sbin/ldconfig
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun mailnews
/sbin/ldconfig
%{_sbindir}/mozilla-chrome+xpcom-generate

%post chat
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun chat
%{_sbindir}/mozilla-chrome+xpcom-generate

%post js-debugger
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun js-debugger
%{_sbindir}/mozilla-chrome+xpcom-generate

%post dom-inspector
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun dom-inspector
%{_sbindir}/mozilla-chrome+xpcom-generate

%post gnomevfs
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun gnomevfs
%{_sbindir}/mozilla-chrome+xpcom-generate

%post calendar
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun calendar
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(744,root,root) %{_sbindir}/mozilla-chrome+xpcom-generate

%dir %{_libdir}/%{name}
%dir %{_chromedir}
%dir %{_libdir}/%{name}/components
%dir %{_libdir}/%{name}/defaults
%dir %{_libdir}/%{name}/greprefs
%dir %{_libdir}/%{name}/icons
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/res
%dir %{_libdir}/%{name}/searchplugins
%dir %{_datadir}/%{name}

%attr(755,root,root) %{_libdir}/libgkgfx.so
%attr(755,root,root) %{_libdir}/libgtkembedmoz.so
%{?with_gtk1:%attr(755,root,root) %{_libdir}/libgtksuperwin.so}
%attr(755,root,root) %{_libdir}/libgtkxtbin.so
%attr(755,root,root) %{_libdir}/libjsj.so
%attr(755,root,root) %{_libdir}/libldap50.so
%attr(755,root,root) %{_libdir}/libprldap50.so
%attr(755,root,root) %{_libdir}/libssldap50.so
%attr(755,root,root) %{_libdir}/libmozjs.so
##%attr(755,root,root) %{_libdir}/libmoz_art_lgpl.so
%attr(755,root,root) %{_libdir}/libxpcom.so
%attr(755,root,root) %{_libdir}/libxpcom_compat.so
%attr(755,root,root) %{_libdir}/libxpistub.so
%attr(755,root,root) %{_libdir}/libxlibrgb.so
%attr(755,root,root) %{_libdir}/%{name}/libxpcom.so
%attr(755,root,root) %{_libdir}/%{name}/libnssckbi.so

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
%attr(755,root,root) %{_libdir}/%{name}/components/libimg*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjar50.so
%attr(755,root,root) %{_libdir}/%{name}/components/libjsd.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmork.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmoz*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libmyspell.so
%attr(755,root,root) %{_libdir}/%{name}/components/libnecko*.so
%{?with_heimdal:%attr(755,root,root) %{_libdir}/%{name}/components/libnegotiateauth.so}
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
%attr(755,root,root) %{_libdir}/%{name}/components/libspellchecker.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtransformiix.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtxmgr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libtypeaheadfind.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuconv.so
%attr(755,root,root) %{_libdir}/%{name}/components/libucv*.so
%attr(755,root,root) %{_libdir}/%{name}/components/libuniversalchardet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwallet.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwalletviewers.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebbrwsr.so
%attr(755,root,root) %{_libdir}/%{name}/components/libwebsrvcs.so
%{?with_gtk1:%attr(755,root,root) %{_libdir}/%{name}/components/libwidget_gtk.so}
%{!?with_gtk1:%attr(755,root,root) %{_libdir}/%{name}/components/libwidget_gtk2.so}
%attr(755,root,root) %{_libdir}/%{name}/components/libx*.so

%{_libdir}/%{name}/components/access*.xpt
%{_libdir}/%{name}/components/appshell.xpt
%{_libdir}/%{name}/components/autocomplete.xpt
%{_libdir}/%{name}/components/autoconfig.xpt
%{_libdir}/%{name}/components/bookmarks.xpt
%{_libdir}/%{name}/components/caps.xpt
%{_libdir}/%{name}/components/chardet.xpt
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
%{?with_svg:%{_libdir}/%{name}/components/gksvgrenderer.xpt}
%{_libdir}/%{name}/components/helperAppDlg.xpt
%{_libdir}/%{name}/components/history.xpt
%{_libdir}/%{name}/components/htmlparser.xpt
%{_libdir}/%{name}/components/imglib2.xpt
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
#%{_libdir}/%{name}/components/plugin.xpt
%{_libdir}/%{name}/components/pref.xpt
%{_libdir}/%{name}/components/prefetch.xpt
%{_libdir}/%{name}/components/prefmigr.xpt
%{_libdir}/%{name}/components/profile.xpt
%{_libdir}/%{name}/components/profilesharingsetup.xpt
%{_libdir}/%{name}/components/progressDlg.xpt
%{_libdir}/%{name}/components/proxyObjInst.xpt
%{_libdir}/%{name}/components/rdf.xpt
%{_libdir}/%{name}/components/related.xpt
%{_libdir}/%{name}/components/search.xpt
%{_libdir}/%{name}/components/shistory.xpt
%{_libdir}/%{name}/components/sidebar.xpt
%{_libdir}/%{name}/components/signonviewer.xpt
%{_libdir}/%{name}/components/spellchecker.xpt
%{_libdir}/%{name}/components/txmgr.xpt
%{_libdir}/%{name}/components/txtsvc.xpt
%{_libdir}/%{name}/components/typeaheadfind.xpt
%{_libdir}/%{name}/components/uconv.xpt
%{_libdir}/%{name}/components/unicharutil.xpt
%{_libdir}/%{name}/components/uriloader.xpt
%{_libdir}/%{name}/components/urlbarhistory.xpt
%{_libdir}/%{name}/components/wallet*.xpt
%{_libdir}/%{name}/components/webBrowser_core.xpt
%{_libdir}/%{name}/components/webbrowserpersist.xpt
%{_libdir}/%{name}/components/webshell_idls.xpt
%{_libdir}/%{name}/components/websrvcs.xpt
%{_libdir}/%{name}/components/widget.xpt
%{_libdir}/%{name}/components/windowds.xpt
%{_libdir}/%{name}/components/windowwatcher.xpt
%{_libdir}/%{name}/components/x*.xpt

# Is this a correct package for these files?
%{_libdir}/%{name}/components/ipcd.xpt
%attr(755,root,root) %{_libdir}/%{name}/components/libipcdc.so
%{!?with_gtk1:%attr(755,root,root) %{_libdir}/%{name}/components/libsystem-pref.so}

%{_libdir}/%{name}/components/jsconsole-clhandler.js
%{_libdir}/%{name}/components/nsCloseAllWindows.js
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

# not *.dat, so check-files can catch any new files
# (and they won't be just silently placed empty in rpm)
%ghost %{_libdir}/%{name}/components/compreg.dat
%ghost %{_libdir}/%{name}/components/xpti.dat

%{_libdir}/%{name}/components/myspell

%dir %{_datadir}/%{name}/chrome
%{_datadir}/%{name}/chrome/US.jar
%{_datadir}/%{name}/chrome/classic.jar
%{_datadir}/%{name}/chrome/comm.jar
%{_datadir}/%{name}/chrome/content-packs.jar
%{_datadir}/%{name}/chrome/cview.jar
%{_datadir}/%{name}/chrome/embed-sample.jar
%{_datadir}/%{name}/chrome/en-US.jar
%{_datadir}/%{name}/chrome/en-unix.jar
%{_datadir}/%{name}/chrome/help.jar
%{_datadir}/%{name}/chrome/layoutdebug.jar
%{_datadir}/%{name}/chrome/modern.jar
%{_datadir}/%{name}/chrome/pipnss.jar
%{_datadir}/%{name}/chrome/pippki.jar
%{?with_svg:%{_datadir}/%{name}/chrome/svg.jar}
%{_datadir}/%{name}/chrome/tasks.jar
%{_datadir}/%{name}/chrome/toolkit.jar

%ghost %{_datadir}/%{name}/chrome/chrome.rdf
%{_datadir}/%{name}/chrome/chromelist.txt
%{_datadir}/%{name}/chrome/icons
%exclude %{_datadir}/%{name}/chrome/icons/default/abcardWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/addressbookWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/calendar-window*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/chatzilla-window*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/messengerWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/msgcomposeWindow*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/venkman-window*.xpm
%exclude %{_datadir}/%{name}/chrome/icons/default/winInspectorMain*.xpm

%dir %{_datadir}/%{name}/chrome/overlayinfo
%dir %{_datadir}/%{name}/chrome/overlayinfo/communicator
%dir %{_datadir}/%{name}/chrome/overlayinfo/communicator/content
%ghost %{_datadir}/%{name}/chrome/overlayinfo/communicator/content/overlays.rdf
%dir %{_datadir}/%{name}/chrome/overlayinfo/editor
%dir %{_datadir}/%{name}/chrome/overlayinfo/editor/content
# chatzilla and messenger entries in editor/content dir
%dir %{_datadir}/%{name}/chrome/overlayinfo/messenger
%dir %{_datadir}/%{name}/chrome/overlayinfo/messenger/content
%ghost %{_datadir}/%{name}/chrome/overlayinfo/messenger/content/overlays.rdf
%dir %{_datadir}/%{name}/chrome/overlayinfo/navigator
%dir %{_datadir}/%{name}/chrome/overlayinfo/navigator/content
%ghost %{_datadir}/%{name}/chrome/overlayinfo/navigator/content/overlays.rdf

%{_datadir}/%{name}/chrome/mozilla-installed-chrome.txt
%ghost %{_datadir}/%{name}/chrome/installed-chrome.txt

%{_datadir}/%{name}/defaults
%{_datadir}/%{name}/greprefs
%exclude %{_datadir}/%{name}/defaults/pref/inspector.js
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/res
%exclude %{_datadir}/%{name}/res/inspector
%{_datadir}/%{name}/searchplugins
%{_datadir}/idl/*

%{_pixmapsdir}/mozilla.png
%{_desktopdir}/mozilla.desktop
%{_desktopdir}/mozilla-composer.desktop
#%{_desktopdir}/mozilla-jconsole.desktop
#%{_desktopdir}/mozilla-terminal.desktop

%files mailnews
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmsgbaseutil.so
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

%{_libdir}/%{name}/components/addrbook.xpt
%{_libdir}/%{name}/components/impComm4xMail.xpt
%{_libdir}/%{name}/components/import.xpt
%{_libdir}/%{name}/components/mailnews.xpt
%{_libdir}/%{name}/components/mailview.xpt
%{_libdir}/%{name}/components/mime.xpt
%{_libdir}/%{name}/components/msg*.xpt

%{_libdir}/%{name}/components/mdn-service.js
%{_libdir}/%{name}/components/nsLDAPPrefsService.js
%{_libdir}/%{name}/components/offlineStartup.js
%{_libdir}/%{name}/components/smime-service.js

%{_datadir}/%{name}/chrome/messenger.jar

%{_datadir}/%{name}/chrome/icons/default/abcardWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/addressbookWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/messengerWindow*.xpm
%{_datadir}/%{name}/chrome/icons/default/msgcomposeWindow*.xpm

%dir %{_datadir}/%{name}/chrome/overlayinfo/cookie
%dir %{_datadir}/%{name}/chrome/overlayinfo/cookie/content
# only chrome://messenger/content/mailPrefsOverlay.xul
%ghost %{_datadir}/%{name}/chrome/overlayinfo/cookie/content/overlays.rdf
%ghost %{_datadir}/%{name}/chrome/overlayinfo/editor/content/overlays.rdf

%{_desktopdir}/mozilla-mail.desktop

%files chat
%defattr(644,root,root,755)
%{_libdir}/%{name}/components/chatzilla-service.js
%{_datadir}/%{name}/chrome/chatzilla.jar
%{_datadir}/%{name}/chrome/icons/default/chatzilla-window*.xpm

%dir %{_datadir}/%{name}/chrome/overlayinfo/browser
%dir %{_datadir}/%{name}/chrome/overlayinfo/browser/content
# only chrome://chatzilla/content/browserOverlay.xul
%ghost %{_datadir}/%{name}/chrome/overlayinfo/browser/content/overlays.rdf
%dir %{_datadir}/%{name}/chrome/overlayinfo/browser/skin
# only chrome://chatzilla/skin/browserOverlay.css
%ghost %{_datadir}/%{name}/chrome/overlayinfo/browser/skin/stylesheets.rdf
%ghost %{_datadir}/%{name}/chrome/overlayinfo/editor/content/overlays.rdf
%dir %{_datadir}/%{name}/chrome/overlayinfo/global
%dir %{_datadir}/%{name}/chrome/overlayinfo/global/skin
# only chrome://chatzilla/skin/browserOverlay.css
%ghost %{_datadir}/%{name}/chrome/overlayinfo/global/skin/stylesheets.rdf

%{_desktopdir}/mozilla-chat.desktop

%files js-debugger
%defattr(644,root,root,755)
%{_libdir}/%{name}/components/venkman-service.js
%{_datadir}/%{name}/chrome/venkman.jar
%{_datadir}/%{name}/chrome/icons/default/venkman-window*.xpm
%{_desktopdir}/mozilla-venkman.desktop

%files dom-inspector
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/components/libinspector.so
%{_libdir}/%{name}/components/inspector.xpt
%{_libdir}/%{name}/components/inspector-cmdline.js
%{_datadir}/%{name}/chrome/inspector.jar
%{_datadir}/%{name}/chrome/icons/default/winInspectorMain*.xpm
%dir %{_datadir}/%{name}/chrome/overlayinfo/inspector
%dir %{_datadir}/%{name}/chrome/overlayinfo/inspector/content
# only chrome://inspector/content/* entries
%ghost %{_datadir}/%{name}/chrome/overlayinfo/inspector/content/overlays.rdf
%{_datadir}/%{name}/defaults/pref/inspector.js
%{_datadir}/%{name}/res/inspector

%if %{with gnomevfs}
%files gnomevfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/components/libnkgnomevfs.so
%endif

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/components/libxpical.so
%{_libdir}/%{name}/components/calendar.xpt
%{_libdir}/%{name}/components/calendarService.js
%{_datadir}/%{name}/chrome/calendar.jar
%{_datadir}/%{name}/chrome/icons/default/calendar-window*.xpm

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*
