Summary:	Text mode CD player for Linux
Summary(pl):	Odtwarzacz p³yt CD dla Linuksa
Name:		adcd
Version:	0.4
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://savannah.nongnu.org/download/adcd/%{name}-%{version}.tar.bz2
# Source0-md5:	9e373050efdb19929cd477bb5ee22160
URL:		http://www.nongnu.org/adcd/adcd.html
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adcd is a text mode CD player for Linux. It features all the functions
expected in a compact disc player, including playing selected tracks,
random playing, and continuous playing.

%description -l pl
Adcd jest dzia³aj±cym w trybie tekstowym odtwarzaczem p³yt CD dla
Linuksa. Posiada wszystkie funkcje, jakich mo¿na siê spodziewaæ po
odtwarzaczu p³yt kompaktowych, w³±czaj±c w to odtwarzanie wybranych
b±d¼ losowych ¶cie¿ek czy ci±g³e odtwarzanie.

%prep
%setup -q

%build
%{__make} \
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
%doc ChangeLog LEEME README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
