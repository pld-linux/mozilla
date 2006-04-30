#
# Conditional build:
%bcond_with	gtk1	# use GTK+ 1.2.x instead of 2.x.x
%bcond_with	gcc2	# compile using gcc2 to get working macromedia-flash and
			# gcc2-compiled Java plugins on nest and other gcc 3.x systems.
			# WARNING! You have to recompile galeon with gcc2 in
			# order to get it working with this release of mozilla
%bcond_without	ft218	# compile with freetype < 2.1.8
%bcond_without	gnomevfs	# disable GnomeVFS support

%bcond_without	heimdal	# disable heimdal support
%bcond_with	svg	# enable svg support
#
Summary:	Mozilla - web browser
Summary(es):	Navegador de Internet Mozilla
Summary(pl):	Mozilla - przegl±darka WWW
Summary(pt_BR):	Navegador Mozilla
Summary(ru):	Web browser
Name:		mozilla
Version:	1.7.13
Release:	1.1
Epoch:		5
License:	Mozilla Public License
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/mozilla/releases/mozilla%{version}/source/%{name}-%{version}-source.tar.bz2
# Source0-md5:	eb0683207f7668319c65e403d04bfc41
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}-composer.desktop
Source5:	%{name}-chat.desktop
Source6:	%{name}-jconsole.desktop
Source7:	%{name}-mail.desktop
Source9:	%{name}-terminal.desktop
Source10:	%{name}-venkman.desktop
Source11:	http://www.mozilla-enigmail.org/downloads/src/ipc-1.1.3.tar.gz
# Source11-md5:	64ba4c6e3b52568468c4f6680ec7e679
Source12:	http://www.mozilla-enigmail.org/downloads/src/enigmail-0.93.0.tar.gz
# Source12-md5:	cb7126705924cb7f0de205b4ff4e28b4
#Source13:	%{name}-libart.tar.bz2
## Source13-md5:	d6834f4881d5947b4e0540f46b7edfb6
Patch0:		%{name}-pld-homepage.patch
Patch1:		%{name}-nss.patch
Patch2:		%{name}-ldap_nspr_includes.patch
Patch3:		%{name}-ldap-with-nss.patch
Patch4:		%{name}-gfx.patch
Patch5:		%{name}-alpha-gcc3.patch
# http://bugzilla.mozilla.org/show_bug.cgi?id=234035
# http://bugzilla.mozilla.org/attachment.cgi?id=149334&action=view
Patch6:		%{name}-freetype218.patch
Patch7:		%{name}-cairo.patch
Patch8:		%{name}-gcc-bugs.patch
Patch9:		%{name}-nspr.patch
Patch10:	firefox-1.0-gcc4-compile.patch
Patch11:	%{name}-enigmail-makemake.patch
Patch12:	%{name}-lib_path.patch
URL:		http://www.mozilla.org/
BuildRequires:	/bin/csh
BuildRequires:	/bin/ex
BuildRequires:	automake
BuildRequires:	tar >= 1:1.15.1
%{?with_gtk1:BuildRequires:	ORBit-devel}
# TODO: https://bugzilla.mozilla.org/show_bug.cgi?id=296463
%{?with_svg:BuildRequires:	cairo-devel >= 0.3.0}
%{?with_svg:BuildRequires:	cairo-devel < 0.5.0}
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
%{?with_heimdal:BuildRequires:	heimdal-devel >= 0.7}
%{!?with_gtk1:BuildRequires:	libIDL-devel >= 0.8.0}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 1.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	nspr-devel >= 1:4.6-2
BuildRequires:	nss-devel >= 3.9.4-1
%{!?with_gtk1:BuildRequires:	pango-devel >= 1:1.1.0}
BuildRequires:	perl-modules >= 5.6.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xcursor-devel
BuildRequires:	xft-devel >= 2.1-2
BuildRequires:	tar >= 1:1.15.1
BuildRequires:	zip >= 2.1
BuildRequires:	zlib-devel >= 1.0.0
Requires(post,postun):	/sbin/ldconfig
%{?with_svg:Requires:	cairo >= 0.3.0}
%{?with_svg:Requires:	cairo < 0.5.0}
Requires:	nspr >= 1:4.6-2
Requires:	nss >= 3.9.4-1
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
%{?with_gtk1:Provides:	mozilla(gtk1) = %{epoch}:%{version}-%{release}}
%{!?with_gtk1:Provides:	mozilla(gtk2) = %{epoch}:%{version}-%{release}}
Provides:	mozilla-embedded = %{epoch}:%{version}-%{release}
%{?with_gtk1:Provides:	mozilla-embedded(gtk1) = %{epoch}:%{version}-%{release}}
%{!?with_gtk1:Provides:	mozilla-embedded(gtk2) = %{epoch}:%{version}-%{release}}
Provides:	wwwbrowser
Obsoletes:	light
Obsoletes:	mozilla-embedded
Obsoletes:	mozilla-irc
Obsoletes:	mozilla-theme-NegativeModern
Obsoletes:	mozilla-theme-gold
Obsoletes:	mozilla-theme-kzilla
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%define		_mozilladir	%{_libdir}/%{name}
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

%package libs
Summary:	mozilla shared libraries
Summary(pl):	Biblioteki wspó³dzielone mozilli
Group:		Libraries

%description libs
mozilla shared libraries.

%description libs -l pl
Biblioteki wspó³dzielone mozilli.

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

%package addon-enigmail
Summary:	Enigmail - PGP/GPG support for Mozilla
Summary(pl):	Enigmail - obs³uga PGP/GPG dla Mozilli
Group:		X11/Applications/Networking
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	%{name}-mailnews = %{epoch}:%{version}-%{release}
Requires:	%{name}-mailnews = %{epoch}:%{version}-%{release}

%description addon-enigmail
Enigmail is an extension to the mail client of Mozilla / Netscape and
Mozilla Thunderbird which allows users to access the authentication and
encryption features provided by GnuPG.

%description addon-enigmail -l pl
Rozszerzenie Mozilla Mail dla Mozilla Mail. Pozwala na ³atwe korzystanie
z dobrodziejstw GnuPG.

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
Requires:	nspr-devel >= 1:4.6-2
Provides:	mozilla-embedded-devel = %{epoch}:%{version}-%{release}
Obsoletes:	mozilla-embedded-devel
Obsoletes:	mozilla-firefox-devel

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
%setup -q -c -T
tar jxf %{SOURCE0} --strip-components=1

cd extensions
tar xvfz %{SOURCE11}
tar xvfz %{SOURCE12}
cd ..

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%{?with_ft218:%patch6 -p0}
%patch7 -p1
%patch8 -p0
%patch9 -p1
%patch10 -p0
%patch11 -p1
%patch12 -p1

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
	%{?with_svg:--enable-svg --enable-svg-renderer-cairo} \
	%{?with_gtk1:--enable-toolkit-gtk} \
	%{!?with_gtk1:--disable-toolkit-gtk --enable-default-toolkit=gtk2} \
	%{!?with_gnomevfs:--disable-gnomevfs} \
	--enable-xft \
	--enable-xinerama \
	--enable-xprint \
	--disable-xterm-updates \
	--enable-old-abi-compat-wrappers \
	--with-default-mozilla-five-home=%{_mozilladir} \
	--with-pthreads \
	--with-system-jpeg \
	--with-system-nspr \
	--with-system-png \
	--with-system-zlib \
	--with-x

%{__make}

cd extensions/ipc
./makemake -r
%{__make}
cd ../enigmail
./makemake -r
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_datadir}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/{chrome,defaults,icons,res,searchplugins,greprefs} \
	$RPM_BUILD_ROOT%{_mozilladir}/{components,plugins} \
	$RPM_BUILD_ROOT{%{_includedir}/%{name}/idl,%{_pkgconfigdir}}

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
#install dist/bin/component.reg $RPM_BUILD_ROOT%{_mozilladir}

ln -sf ../../share/mozilla/chrome $RPM_BUILD_ROOT%{_chromedir}
ln -sf ../../share/mozilla/defaults $RPM_BUILD_ROOT%{_mozilladir}/defaults
ln -sf ../../share/mozilla/greprefs $RPM_BUILD_ROOT%{_mozilladir}/greprefs
ln -sf ../../share/mozilla/icons $RPM_BUILD_ROOT%{_mozilladir}/icons
ln -sf ../../share/mozilla/res $RPM_BUILD_ROOT%{_mozilladir}/res
ln -sf ../../share/mozilla/searchplugins $RPM_BUILD_ROOT%{_mozilladir}/searchplugins

cp -frL dist/bin/chrome/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/chrome
cp -frL dist/bin/components/*	$RPM_BUILD_ROOT%{_mozilladir}/components
cp -frL dist/bin/defaults/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/defaults
%{?with_gtk1:cp -frL dist/bin/icons/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/icons}
cp -frL dist/bin/res/*		$RPM_BUILD_ROOT%{_datadir}/%{name}/res
cp -frL dist/bin/searchplugins/* $RPM_BUILD_ROOT%{_datadir}/%{name}/searchplugins
cp -frL dist/gre/greprefs/*	$RPM_BUILD_ROOT%{_datadir}/%{name}/greprefs
cp -frL dist/idl/*		$RPM_BUILD_ROOT%{_includedir}/%{name}/idl
cp -frL dist/include/*		$RPM_BUILD_ROOT%{_includedir}/%{name}
cp -frL dist/public/ldap{,-private} $RPM_BUILD_ROOT%{_includedir}/%{name}

install dist/bin/*.so $RPM_BUILD_ROOT%{_mozilladir}

ln -s %{_libdir}/libnssckbi.so $RPM_BUILD_ROOT%{_mozilladir}/libnssckbi.so

for f in build/unix/*.pc ; do
	sed -e 's/mozilla-%{version}/mozilla/' $f \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/$(basename $f)
done

sed -e 's,lib/mozilla-%{version},lib,g;s/mozilla-%{version}/mozilla/g' build/unix/mozilla-gtkmozembed.pc \
		> $RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-gtkmozembed.pc

sed -i -e 's#mozilla-nspr =.*#mozilla-nspr#g' -e 's#mozilla-nss =.*#mozilla-nss#g' $RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc

# add includir/dom to Cflags, for openvrml.spec, perhaps others
sed -i -e '/Cflags:/{/{includedir}\/dom/!s,$, -I${includedir}/dom,}' $RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-plugin.pc

rm -f $RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-nss.pc $RPM_BUILD_ROOT%{_pkgconfigdir}/mozilla-nspr.pc

install %{SOURCE1} %{SOURCE3} %{SOURCE5} %{SOURCE6} %{SOURCE7} \
	%{SOURCE9} %{SOURCE10} $RPM_BUILD_ROOT%{_desktopdir}

install %{SOURCE2}	$RPM_BUILD_ROOT%{_pixmapsdir}

install dist/bin/mozilla-bin $RPM_BUILD_ROOT%{_mozilladir}
install dist/bin/regchrome $RPM_BUILD_ROOT%{_mozilladir}
install dist/bin/regxpcom $RPM_BUILD_ROOT%{_mozilladir}
install dist/bin/xpidl $RPM_BUILD_ROOT%{_mozilladir}
install dist/bin/regchrome $RPM_BUILD_ROOT%{_bindir}
install dist/bin/regxpcom $RPM_BUILD_ROOT%{_bindir}
install dist/bin/xpidl $RPM_BUILD_ROOT%{_bindir}

cp $RPM_BUILD_ROOT%{_chromedir}/installed-chrome.txt \
	$RPM_BUILD_ROOT%{_chromedir}/%{name}-installed-chrome.txt

cat << 'EOF' > $RPM_BUILD_ROOT%{_bindir}/mozilla
#!/bin/sh
# (c) vip at linux.pl, wolf at pld-linux.org

LD_LIBRARY_PATH=%{_mozilladir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export LD_LIBRARY_PATH

MOZILLA_FIVE_HOME=%{_mozilladir}
if [ "$1" == "-remote" ]; then
	%{_mozilladir}/mozilla-bin "$@"
else
	PING=`%{_mozilladir}/mozilla-bin -remote 'ping()' 2>&1 >/dev/null`
	if [ -n "$PING" ]; then
		if [ -f "`pwd`/$1" ]; then
			%{_mozilladir}/mozilla-bin "file://`pwd`/$1"
		else
			%{_mozilladir}/mozilla-bin "$@"
		fi
	else
		if [ -z "$1" ]; then
			%{_mozilladir}/mozilla-bin -remote 'xfeDoCommand (openBrowser)'
		elif [ "$1" == "-mail" ]; then
			%{_mozilladir}/mozilla-bin -remote 'xfeDoCommand (openInbox)'
		elif [ "$1" == "-compose" ]; then
			%{_mozilladir}/mozilla-bin -remote 'xfeDoCommand (composeMessage)'
		else
			echo $1 | grep -q "^-" > /dev/null
			if [ $? -eq 0 ]; then
				%{_mozilladir}/mozilla-bin "$@"
			else
				if [ -f "`pwd`/$1" ]; then
					URL="file://`pwd`/$1"
				else
					URL="$1"
				fi
				grep browser.tabs.opentabfor.middleclick ~/.mozilla/default/*/prefs.js | grep true > /dev/null
				if [ $? -eq 0 ]; then
					%{_mozilladir}/mozilla-bin -remote "OpenUrl($URL,new-tab)"
				else
					%{_mozilladir}/mozilla-bin -remote "OpenUrl($URL,new-window)"
				fi
			fi
		fi
	fi
fi
EOF

cat << 'EOF' > $RPM_BUILD_ROOT%{_sbindir}/mozilla-chrome+xpcom-generate
#!/bin/sh
umask 022
cd %{_datadir}/mozilla/chrome
cat *-installed-chrome.txt > installed-chrome.txt
rm -f chrome.rdf overlayinfo/*/*/*.rdf
rm -f %{_mozilladir}/components/{compreg,xpti}.dat

LD_LIBRARY_PATH=%{_mozilladir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export LD_LIBRARY_PATH

MOZILLA_FIVE_HOME=%{_mozilladir} %{_mozilladir}/regxpcom
MOZILLA_FIVE_HOME=%{_mozilladir} %{_mozilladir}/regchrome
exit 0
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
if [ "$1" = "1" ]; then
	%{_sbindir}/mozilla-chrome+xpcom-generate
fi

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post mailnews
/sbin/ldconfig
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun mailnews
/sbin/ldconfig
%{_sbindir}/mozilla-chrome+xpcom-generate

%post addon-enigmail
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun addon-enigmail
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
%attr(755,root,root) %{_bindir}/mozilla
%attr(744,root,root) %{_sbindir}/mozilla-chrome+xpcom-generate

%dir %{_mozilladir}
%dir %{_chromedir}
%dir %{_mozilladir}/components
%dir %{_mozilladir}/defaults
%dir %{_mozilladir}/greprefs
%dir %{_mozilladir}/icons
%dir %{_mozilladir}/plugins
%dir %{_mozilladir}/res
%dir %{_mozilladir}/searchplugins
%dir %{_datadir}/%{name}

%attr(755,root,root) %{_mozilladir}/mozilla-bin
%attr(755,root,root) %{_mozilladir}/reg*
%attr(755,root,root) %{_mozilladir}/xpidl

%attr(755,root,root) %{_mozilladir}/libxpcom.so
%attr(755,root,root) %{_mozilladir}/libnssckbi.so

%attr(755,root,root) %{_mozilladir}/components/libaccess*.so
%attr(755,root,root) %{_mozilladir}/components/libappcomps.so
%attr(755,root,root) %{_mozilladir}/components/libautoconfig.so
%attr(755,root,root) %{_mozilladir}/components/libcaps.so
%attr(755,root,root) %{_mozilladir}/components/libchrome.so
%attr(755,root,root) %{_mozilladir}/components/libcomposer.so
%attr(755,root,root) %{_mozilladir}/components/libcookie.so
%attr(755,root,root) %{_mozilladir}/components/libdocshell.so
%attr(755,root,root) %{_mozilladir}/components/libeditor.so
%attr(755,root,root) %{_mozilladir}/components/libembedcomponents.so
%attr(755,root,root) %{_mozilladir}/components/libfileview.so
%attr(755,root,root) %{_mozilladir}/components/libgfx*.so
%attr(755,root,root) %{_mozilladir}/components/libgk*.so
%attr(755,root,root) %{_mozilladir}/components/libhtmlpars.so
%attr(755,root,root) %{_mozilladir}/components/libi18n.so
%attr(755,root,root) %{_mozilladir}/components/libimg*.so
%attr(755,root,root) %{_mozilladir}/components/libjar50.so
%attr(755,root,root) %{_mozilladir}/components/libjsd.so
%attr(755,root,root) %{_mozilladir}/components/libmork.so
%attr(755,root,root) %{_mozilladir}/components/libmoz*.so
%attr(755,root,root) %{_mozilladir}/components/libmyspell.so
%attr(755,root,root) %{_mozilladir}/components/libnecko*.so
%{?with_heimdal:%attr(755,root,root) %{_mozilladir}/components/libnegotiateauth.so}
%attr(755,root,root) %{_mozilladir}/components/libnkdatetime.so
%attr(755,root,root) %{_mozilladir}/components/libnkfinger.so
%attr(755,root,root) %{_mozilladir}/components/libns*.so
%attr(755,root,root) %{_mozilladir}/components/liboji.so
%attr(755,root,root) %{_mozilladir}/components/libp3p.so
%attr(755,root,root) %{_mozilladir}/components/libpipboot.so
%attr(755,root,root) %{_mozilladir}/components/libpipnss.so
%attr(755,root,root) %{_mozilladir}/components/libpippki.so
%attr(755,root,root) %{_mozilladir}/components/libpref.so
%attr(755,root,root) %{_mozilladir}/components/libprofile.so
%attr(755,root,root) %{_mozilladir}/components/librdf.so
%attr(755,root,root) %{_mozilladir}/components/libspellchecker.so
%attr(755,root,root) %{_mozilladir}/components/libtransformiix.so
%attr(755,root,root) %{_mozilladir}/components/libtxmgr.so
%attr(755,root,root) %{_mozilladir}/components/libtypeaheadfind.so
%attr(755,root,root) %{_mozilladir}/components/libuconv.so
%attr(755,root,root) %{_mozilladir}/components/libucv*.so
%attr(755,root,root) %{_mozilladir}/components/libuniversalchardet.so
%attr(755,root,root) %{_mozilladir}/components/libwallet.so
%attr(755,root,root) %{_mozilladir}/components/libwalletviewers.so
%attr(755,root,root) %{_mozilladir}/components/libwebbrwsr.so
%attr(755,root,root) %{_mozilladir}/components/libwebsrvcs.so
%{?with_gtk1:%attr(755,root,root) %{_mozilladir}/components/libwidget_gtk.so}
%{!?with_gtk1:%attr(755,root,root) %{_mozilladir}/components/libwidget_gtk2.so}
%attr(755,root,root) %{_mozilladir}/components/libx*.so

%{_mozilladir}/components/access*.xpt
%{_mozilladir}/components/appshell.xpt
%{_mozilladir}/components/autocomplete.xpt
%{_mozilladir}/components/autoconfig.xpt
%{_mozilladir}/components/bookmarks.xpt
%{_mozilladir}/components/caps.xpt
%{_mozilladir}/components/chardet.xpt
%{_mozilladir}/components/commandhandler.xpt
%{_mozilladir}/components/composer.xpt
%{_mozilladir}/components/content*.xpt
%{_mozilladir}/components/cookie.xpt
%{_mozilladir}/components/directory.xpt
%{_mozilladir}/components/docshell.xpt
%{_mozilladir}/components/dom*.xpt
%{_mozilladir}/components/downloadmanager.xpt
%{_mozilladir}/components/editor.xpt
%{_mozilladir}/components/embed_base.xpt
%{_mozilladir}/components/exthandler.xpt
%{_mozilladir}/components/find.xpt
%{_mozilladir}/components/filepicker.xpt
%{_mozilladir}/components/gfx*.xpt
%{?with_svg:%{_mozilladir}/components/gksvgrenderer.xpt}
%{_mozilladir}/components/helperAppDlg.xpt
%{_mozilladir}/components/history.xpt
%{_mozilladir}/components/htmlparser.xpt
%{_mozilladir}/components/imglib2.xpt
%{_mozilladir}/components/intl.xpt
%{_mozilladir}/components/jar.xpt
%{_mozilladir}/components/js*.xpt
%{_mozilladir}/components/layout*.xpt
%{_mozilladir}/components/locale.xpt
%{_mozilladir}/components/lwbrk.xpt
%{_mozilladir}/components/mimetype.xpt
%{_mozilladir}/components/moz*.xpt
%{_mozilladir}/components/necko*.xpt
%{_mozilladir}/components/oji.xpt
%{_mozilladir}/components/p3p.xpt
%{_mozilladir}/components/pipboot.xpt
%{_mozilladir}/components/pipnss.xpt
%{_mozilladir}/components/pippki.xpt
#%{_mozilladir}/components/plugin.xpt
%{_mozilladir}/components/pref.xpt
%{_mozilladir}/components/prefetch.xpt
%{_mozilladir}/components/prefmigr.xpt
%{_mozilladir}/components/profile.xpt
%{_mozilladir}/components/profilesharingsetup.xpt
%{_mozilladir}/components/progressDlg.xpt
%{_mozilladir}/components/proxyObjInst.xpt
%{_mozilladir}/components/rdf.xpt
%{_mozilladir}/components/related.xpt
%{_mozilladir}/components/search.xpt
%{_mozilladir}/components/shistory.xpt
%{_mozilladir}/components/sidebar.xpt
%{_mozilladir}/components/signonviewer.xpt
%{_mozilladir}/components/spellchecker.xpt
%{_mozilladir}/components/txmgr.xpt
%{_mozilladir}/components/txtsvc.xpt
%{_mozilladir}/components/typeaheadfind.xpt
%{_mozilladir}/components/uconv.xpt
%{_mozilladir}/components/unicharutil.xpt
%{_mozilladir}/components/uriloader.xpt
%{_mozilladir}/components/urlbarhistory.xpt
%{_mozilladir}/components/wallet*.xpt
%{_mozilladir}/components/webBrowser_core.xpt
%{_mozilladir}/components/webbrowserpersist.xpt
%{_mozilladir}/components/webshell_idls.xpt
%{_mozilladir}/components/websrvcs.xpt
%{_mozilladir}/components/widget.xpt
%{_mozilladir}/components/windowds.xpt
%{_mozilladir}/components/windowwatcher.xpt
%{_mozilladir}/components/x*.xpt

# Is this a correct package for these files?
%{_mozilladir}/components/ipcd.xpt
%attr(755,root,root) %{_mozilladir}/components/libipcdc.so
%{!?with_gtk1:%attr(755,root,root) %{_mozilladir}/components/libsystem-pref.so}

%{_mozilladir}/components/jsconsole-clhandler.js
%{_mozilladir}/components/nsCloseAllWindows.js
%{_mozilladir}/components/nsDictionary.js
%{_mozilladir}/components/nsDownloadProgressListener.js
%{_mozilladir}/components/nsFilePicker.js
%{_mozilladir}/components/nsHelperAppDlg.js
%{_mozilladir}/components/nsInterfaceInfoToIDL.js
%{_mozilladir}/components/nsKillAll.js
%{_mozilladir}/components/nsProgressDialog.js
%{_mozilladir}/components/nsProxyAutoConfig.js
%{_mozilladir}/components/nsResetPref.js
%{_mozilladir}/components/nsSidebar.js
%{_mozilladir}/components/nsUpdateNotifier.js
%{_mozilladir}/components/nsXmlRpcClient.js

# not *.dat, so check-files can catch any new files
# (and they won't be just silently placed empty in rpm)
%ghost %{_mozilladir}/components/compreg.dat
%ghost %{_mozilladir}/components/xpti.dat

%{_mozilladir}/components/myspell

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

%{_pixmapsdir}/mozilla.png
%{_desktopdir}/mozilla.desktop
%{_desktopdir}/mozilla-composer.desktop
#%{_desktopdir}/mozilla-jconsole.desktop
#%{_desktopdir}/mozilla-terminal.desktop

%files libs
%defattr(644,root,root,755)
# libxpcom.so used by mozillaplug-in
# probably should add more if more packages require
%attr(755,root,root) %{_mozilladir}/libxpcom.so
%attr(755,root,root) %{_mozilladir}/libxpcom_compat.so

# add rest too
%attr(755,root,root) %{_mozilladir}/libgkgfx.so
%attr(755,root,root) %{_mozilladir}/libgtkembedmoz.so
%{?with_gtk1:%attr(755,root,root) %{_mozilladir}/libgtksuperwin.so}
%attr(755,root,root) %{_mozilladir}/libgtkxtbin.so
%attr(755,root,root) %{_mozilladir}/libjsj.so
%attr(755,root,root) %{_mozilladir}/libldap50.so
%attr(755,root,root) %{_mozilladir}/libprldap50.so
%attr(755,root,root) %{_mozilladir}/libssldap50.so
%attr(755,root,root) %{_mozilladir}/libmozjs.so
##%attr(755,root,root) %{_mozilladir}/libmoz_art_lgpl.so
%attr(755,root,root) %{_mozilladir}/libxpistub.so
%attr(755,root,root) %{_mozilladir}/libxlibrgb.so


%files mailnews
%defattr(644,root,root,755)
%attr(755,root,root) %{_mozilladir}/libmsgbaseutil.so
%attr(755,root,root) %{_mozilladir}/components/libaddrbook.so
%attr(755,root,root) %{_mozilladir}/components/libbayesflt.so
%attr(755,root,root) %{_mozilladir}/components/libimpText.so
%attr(755,root,root) %{_mozilladir}/components/libimpComm4xMail.so
%attr(755,root,root) %{_mozilladir}/components/libimport.so
%attr(755,root,root) %{_mozilladir}/components/liblocalmail.so
%attr(755,root,root) %{_mozilladir}/components/libmailnews.so
%attr(755,root,root) %{_mozilladir}/components/libmailview.so
%attr(755,root,root) %{_mozilladir}/components/libmimeemitter.so
%attr(755,root,root) %{_mozilladir}/components/libmime.so
%attr(755,root,root) %{_mozilladir}/components/libmsg*.so
%attr(755,root,root) %{_mozilladir}/components/libvcard.so

%{_mozilladir}/components/addrbook.xpt
%{_mozilladir}/components/impComm4xMail.xpt
%{_mozilladir}/components/import.xpt
%{_mozilladir}/components/mailnews.xpt
%{_mozilladir}/components/mailview.xpt
%{_mozilladir}/components/mime.xpt
%{_mozilladir}/components/msg*.xpt

%{_mozilladir}/components/mdn-service.js
%{_mozilladir}/components/nsLDAPPrefsService.js
%{_mozilladir}/components/offlineStartup.js
%{_mozilladir}/components/smime-service.js

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

%files addon-enigmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_mozilladir}/components/libenigmime.so
%{_mozilladir}/components/enigmail.xpt
%{_mozilladir}/components/enigmime.xpt
%{_mozilladir}/components/ipc.xpt
%{_mozilladir}/components/enigmail.js
%{_mozilladir}/components/enigprefs-service.js
%{_datadir}/%{name}/chrome/enigmail-en-US.jar
%{_datadir}/%{name}/chrome/enigmail-skin-tbird.jar
%{_datadir}/%{name}/chrome/enigmail-skin.jar
%{_datadir}/%{name}/chrome/enigmail.jar
%{_datadir}/%{name}/chrome/enigmime.jar
%dir %{_datadir}/%{name}/chrome/overlayinfo/global
%ghost %{_datadir}/%{name}/chrome/overlayinfo/global/content/overlays.rdf

%files chat
%defattr(644,root,root,755)
%{_mozilladir}/components/chatzilla-service.js
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
%{_mozilladir}/components/venkman-service.js
%{_datadir}/%{name}/chrome/venkman.jar
%{_datadir}/%{name}/chrome/icons/default/venkman-window*.xpm
%{_desktopdir}/mozilla-venkman.desktop

%files dom-inspector
%defattr(644,root,root,755)
%attr(755,root,root) %{_mozilladir}/components/libinspector.so
%{_mozilladir}/components/inspector.xpt
%{_mozilladir}/components/inspector-cmdline.js
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
%attr(755,root,root) %{_mozilladir}/components/libnkgnomevfs.so
%endif

%files calendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_mozilladir}/components/libxpical.so
%{_mozilladir}/components/calendar.xpt
%{_mozilladir}/components/calendarService.js
%{_datadir}/%{name}/chrome/calendar.jar
%{_datadir}/%{name}/chrome/icons/default/calendar-window*.xpm

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*
%attr(755,root,root) %{_bindir}/reg*
%attr(755,root,root) %{_bindir}/xpidl
