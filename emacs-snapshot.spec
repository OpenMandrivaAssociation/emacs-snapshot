%define _localstatedir /var/lib

Summary:	GNU Emacs text editor with X11 support

Name:		emacs-snapshot
Version:	23.1.93
Release:	%mkrel 1
License:	GPLv3+
Group:		Editors
URL:		http://www.gnu.org/software/emacs/

Source0:	ftp://alpha.gnu.org/gnu/emacs/pretest/emacs-%{version}.tar.gz
Source2:	gnu-mini.png
Source3:	gnu-normal.png
Source4:	gnu-large.png
Source5:	emacs-config

Patch1: 	emacs-20.5-loadup.patch
Patch3: 	emacs-23.0.94-ia64-1.patch
Patch5:		emacs-23.0.94-bzip2.patch
Patch6:		emacs-snapshot-same-etc-DOC-for-all.patch
Patch7:		emacs-22.0.90-rpath.patch
Patch9:		emacs-22.0.90-force-sendmail-program.patch

Patch20:	emacs-20.4-ppc-config.patch
Patch21:	emacs-20.4-ppc.patch
Patch22:	emacs-21.1-omit-nocombreloc-ppc.patch

Patch100:	emacs-23.0.94-infofix.patch
Patch101:	emacs-23.1.92-version.patch
Patch103:	emacs-23.0.94-x86_64.patch
Patch104:	emacs-22.3-hide-toolbar.patch
Patch111:	emacs-23.1.92-ispell-dictionaries-list-iso-8859-15.patch
Patch114:	emacs-23.0.94-ppc64.patch
Patch115:	emacs-23.0.94-lzma-support.patch
Patch116:	emacs-22.3-fix-str-fmt.patch
# Fix Gtk menus not being updated
# From http://emacsbugs.donarmstrong.com/cgi-bin/bugreport.cgi?bug=4122
Patch117:	emacs-23.1.92-gtk-menus.patch

BuildRoot:	%_tmppath/%name-root
BuildRequires:	libxaw-devel
BuildRequires:	Xaw3d-devel
BuildRequires:	x11-server-common
BuildRequires:	libx11-devel
BuildRequires:	gcc
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	ncurses-devel
BuildRequires:	libungif-devel
BuildRequires:  texinfo
BuildRequires:	xpm-devel
BuildRequires:	gtk+2-devel

Requires(preun): update-alternatives
Requires(post):  update-alternatives

Requires:	emacs-snapshot-common = %version
Provides:	emacs = %{version}-%{release}
Provides:	emacs-bin emacs-gtk

Conflicts:	emacs < %{version}-%{release}
Obsoletes:	emacs-gtk <= 22.3
Obsoletes:	emacs-X11 < 22.0.50
Provides:	emacs-X11 < 22.0.50

%description
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor. 

This package provides an emacs binary with support for X Windows. 

%package el
Summary:	GNU Emacs Lisp source files
Group:		Editors
Requires:	emacs-snapshot-common = %version
Conflicts:	emacs-el

%description el
The emacs-snapshot-el package contains the emacs elisp sources for
many of the elisp programs included with the main Emacs text editor
package.

You need to install this package only if you intend to modify any of
the Emacs packages or see some elisp examples.

%package doc
Summary:	GNU Emacs documentation
Group:		Editors
Requires:	emacs-snapshot-common = %version
Conflicts:	emacs-doc

%description doc
Documentation for GNU Emacs.

%package leim
Summary:	GNU Emacs Lisp code for international input methods
Group:		Editors
Requires:	emacs-snapshot-common = %version
Conflicts:	emacs-leim 

%description leim
This package contains Emacs Lisp code for input methods for various
international character scripts.

%package nox
Summary:	GNU Emacs text editor without support for X11
Group:		Editors
Requires:	emacs-snapshot-common = %version
Provides:	emacs-bin

Conflicts:	emacs-nox

Requires(preun): update-alternatives
Requires(post):  update-alternatives

%description nox
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor. 

This package provides an emacs binary with no X Windows support for
running on a terminal.

%package common
Summary:	Common files for GNU Emacs
Group:		Editors
Requires:	emacs-snapshot-common = %version

Obsoletes:	gnus-emacs < 5.13.0
Provides:	gnus-emacs = 5.13.0

Obsoletes:	emacs-cedet < 1.0-0.pre7
Provides:	emacs-cedet = 1.0-0.pre7

Conflicts:	emacs-speedbar < 1.0
Provides:	emacs-speedbar = 1.0

Obsoletes:	emacs-tramp < 2.1.18-pre
Provides:	emacs-tramp = 2.1.18-pre

Obsoletes:	emacs-url
Provides:	emacs-url

# (Lev) This doesn't look correct:
Obsoletes:	emacs-pcomplete <= 2.4.2
Provides:	emacs-pcomplete = 1.1.1

Obsoletes:	eshell-emacs <= 2.4.2
Provides:	eshell-emacs = 2.4.2

Obsoletes:	emacs-easypg < 1.0.0
Provides:	emacs-easypg = 1.0.0

Obsoletes:	emacs-erc < 5.3
Provides:	emacs-erc = 5.3

Conflicts:	emacs-common

# conflicts due to %%_bindir/{b2m,etags,rcs-checkin}
Conflicts: xemacs-extras

%description common
Emacs is a powerful, customizable, self-documenting, modeless text
editor. Emacs contains special code editing features, a scripting
language (elisp), and the capability to read mail, news, and more
without leaving the editor. 

This package contains all of the common files needed by emacs-snapshot
or emacs-snapshot-nox

%prep

%setup -q -n emacs-%{version}

%__perl -p -i -e 's/ctags/gctags/g' etc/etags.1

%patch1 -p1 -b .loadup
%patch3 -p1 -b .ia64-2
%patch5 -p1 -b .bzip2
%patch6 -p1
%patch7 -p1 -b .rpath
%patch9 -p1 -b .sendmail-program

%ifarch ppc
%patch20 -p1
%patch21 -p1
%patch22 -p1
%endif

%patch100 -p1
%patch101 -p1 -b .version
%patch103 -p1 -b .x86_64
%patch104 -p1 -b .toolbar
%patch111 -p1
%patch114 -p1 -b .ppc
%patch115 -p1 -z .lzma-support
%patch116 -p0 -b .str
%patch117 -p0 -b .gtkmenus

%build
autoreconf -fi

PUREDEF="-DNCURSES_OSPEED_T"
XPUREDEF="-DNCURSES_OSPEED_T"
CONFOPTS="--prefix=%{_prefix} --libexecdir=%{_libdir} --sharedstatedir=/var --with-pop --mandir=%{_mandir} --infodir=%{_infodir}"

export CFLAGS="$RPM_OPT_FLAGS $PUREDEF -fno-zero-initialized-in-bss"

./configure ${CONFOPTS} --with-x=no ${RPM_ARCH}-mandrake-linux --libdir=%_libdir
%make bootstrap

%make distclean
# Build binary without X support
./configure ${CONFOPTS} --with-x=no ${RPM_ARCH}-mandrake-linux --libdir=%_libdir
%make
mv src/emacs src/nox-emacs

%make distclean
# Build binary with X support
./configure ${CONFOPTS} --with-x-toolkit ${RPM_ARCH}-mandrake-linux --libdir=%_libdir
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr

PATH=$PATH:/sbin
ARCHDIR=${RPM_ARCH}-mandrake-linux
%old_makeinstall sharedstatedir=%{buildroot}/var

rm -f %{buildroot}%_bindir/emacs
rm -f %{buildroot}%{_infodir}/dir
rm %{buildroot}%{_libdir}/emacs/%version/%_arch-mandrake-linux/fakemail

# remove sun specific stuff
rm -f %{buildroot}%{_datadir}/emacs/%{version}/etc/{emacstool.1,emacs.1,ctags.1,etags.1,sex.6}

# rename ctags to gctags
mv %{buildroot}%{_mandir}/man1/ctags.1 %{buildroot}%{_mandir}/man1/gctags.1
mv %{buildroot}%{_bindir}/ctags %{buildroot}%{_bindir}/gctags

# is that needed?
install -d %{buildroot}%{_libdir}/emacs/site-lisp

mkdir -p %{buildroot}%{_sysconfdir}/emacs
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/emacs/site-start.el
(cd %{buildroot}%{_datadir}/emacs/%{version}/lisp; ln -s ../../../../..%{_sysconfdir}/emacs/site-start.el site-start.el)

install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d


install -m755 src/nox-emacs %{buildroot}%{_bindir}/emacs-nox
chmod -t %{buildroot}%{_bindir}/emacs*

# create file lists

#
# emacs-doc file list
#
# 3.22MB of docs from emacs-common to emacs-doc to reduce size (tutorials, news, postscript files, ...)
# NB: etc/ps-prin{0,1}.ps are needed by ps-print
find %{buildroot}%{_datadir}/emacs/%version/etc/ -type f | \
  egrep 'TUTORIAL\.|NEWS|ONEWS|.ps$'|fgrep -v /etc/ps-prin | \
  sed "s^%{buildroot}^^" > doc-filelist

#
# emacs-el file list
#

# take every .el and .el.gz which have a corresponding .elc
find %{buildroot}%{_datadir}/emacs -name '*.el' -o -name '*.el.gz' | \
  grep -v /leim/ | while read I; do
  f=`basename $I .gz`
  f=`basename $f .el`
  if [ -e `dirname $I`/$f.elc ]; then
    echo $I | sed "s^%{buildroot}^^"
  fi
done > el-filelist

#
# emacs-common file list
#

# everything not in previous filelists, and remove a few things listed in %files
find %{buildroot}%{_datadir}/emacs/%version -type f -print -o -type d -printf "%%%%dir %%p\n" | \
  grep -v /leim/ | sed "s^%{buildroot}^^" > common-filelist.raw
while read I; do
  grep -qxF $I doc-filelist el-filelist || echo $I
done < common-filelist.raw > common-filelist

find %{buildroot}%{_libdir}/emacs -type f -print -o -type d -printf "%%%%dir %%p\n" | \
  egrep -v 'movemail$|update-game-score$' | sed "s^%{buildroot}^^" >> common-filelist


%define info_files ada-mode auth autotype calc ccmode cl dbus dired-x ebrowse ede ediff edt efaq eieio eintr elisp emacs emacs-mime epa erc eshell eudc flymake forms gnus idlwave info mairix-el message mh-e newsticker nxml-mode org pcl-cvs pgg rcirc reftex remember sasl sc semantic ses sieve smtpmail speedbar tramp url vip viper widget woman
have_info_files=$(echo $(ls %{buildroot}%{_infodir} | egrep -v -- '-[0-9]+$' | sort))

[ "$have_info_files" = "%info_files" ] || {
  echo "you must modify the spec file, %%info_files should be: $have_info_files"
  exit 1
}


%clean
rm -rf %{buildroot}

%post common
# --section="GNU Emacs"
for f in %info_files; do  %_install_info $f
done
:

%preun
for f in %info_files; do  %_remove_install_info $f
done
:

%post nox
update-alternatives --install %_bindir/emacs emacs %_bindir/emacs-nox 10

[[ ! -f %_bindir/emacs ]] && update-alternatives --auto emacs
:

%postun nox
[[ ! -f %_bindir/emacs-nox ]] && \
    /usr/sbin/update-alternatives --remove emacs %_bindir/emacs-nox
:

%post
/usr/sbin/update-alternatives --install %_bindir/emacs emacs %_bindir/emacs-%version 21

%if %mdkversion < 200900
%{update_menus}
%endif

%postun
%if %mdkversion < 200900
%{clean_menus}
%endif

[[ ! -f %{_bindir}/emacs-%{version} ]] && \
    /usr/sbin/update-alternatives --remove emacs %{_bindir}/emacs-%{version}|| :

%files -f common-filelist common
%defattr(-,root,root)
%doc BUGS README src/COPYING
%{_localstatedir}/games/emacs
%dir %{_sysconfdir}/emacs/site-start.d
%dir %{_sysconfdir}/emacs
%config(noreplace) %{_sysconfdir}/emacs/site-start.el
%dir %{_datadir}/emacs
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/%version/lisp/site-start.el
%attr(2755,root,mail) %{_libdir}/emacs/%version/%_arch-mandrake-linux/movemail
%attr(4755,games,root) %{_libdir}/emacs/%version/%_arch-mandrake-linux/update-game-score
%{_bindir}/b2m
%{_bindir}/emacsclient
%{_bindir}/etags
%{_bindir}/ebrowse
%{_bindir}/grep-changelog
%{_bindir}/gctags
%{_bindir}/rcs-checkin
%{_mandir}/*/*
%{_infodir}/*

%files -f doc-filelist doc
%defattr(-,root,root)

%files -f el-filelist el
%defattr(-,root,root)
%doc src/COPYING
%{_datadir}/emacs/%{version}/site-lisp/subdirs.el
%{_datadir}/emacs/site-lisp/subdirs.el
%{_datadir}/emacs/%{version}/leim/ja-dic/*.el.gz
%{_datadir}/emacs/%{version}/leim/quail/*.el.gz

%files leim
%defattr(-,root,root)
%doc src/COPYING
%{_datadir}/emacs/%{version}/leim/leim-list.el
%dir %{_datadir}/emacs/%{version}/leim/ja-dic
%{_datadir}/emacs/%{version}/leim/ja-dic/*.elc
%dir %{_datadir}/emacs/%{version}/leim/quail
%{_datadir}/emacs/%{version}/leim/quail/*.elc

%files nox
%defattr(-,root,root)
%doc src/COPYING
%{_bindir}/emacs-nox

%files
%defattr(-,root,root)
%doc src/COPYING
%{_bindir}/emacs-%{version}
%{_datadir}/applications/emacs.desktop
%{_iconsdir}/hicolor/*/apps/emacs*.png
%{_iconsdir}/hicolor/scalable/apps/emacs.svg
%{_iconsdir}/hicolor/scalable/mimetypes/emacs-document.svg
