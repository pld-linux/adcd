Summary:	Text mode CD player for Linux
Summary(pl.UTF-8):	Odtwarzacz płyt CD dla Linuksa
Name:		adcd
Version:	0.9
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://savannah.nongnu.org/download/adcd/%{name}-%{version}.tar.bz2
# Source0-md5:	3915678b9f9d0abbcfa35aff86335d25
URL:		http://www.nongnu.org/adcd/adcd.html
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adcd is a text mode CD player for Linux. It features all the functions
expected in a compact disc player, including playing selected tracks,
random playing, and continuous playing.

%description -l pl.UTF-8
Adcd jest działającym w trybie tekstowym odtwarzaczem płyt CD dla
Linuksa. Posiada wszystkie funkcje, jakich można się spodziewać po
odtwarzaczu płyt kompaktowych, włączając w to odtwarzanie wybranych
bądź losowych ścieżek czy ciągłe odtwarzanie.

%prep
%setup -q
# fix ncurses.h path
%{__sed} -i -e 's,ncurses.h,ncurses/ncurses.h,g' player.cc
# add missing library
%{__sed} -i -e '/^#include <vector>$/a#include <cstdlib>' main.cc

%build
# not autoconf-generated
./configure \
	--prefix=%{_prefix}
%{__make} 
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags} -lncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix="%{_prefix}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%lang(es) %doc LEEME
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
