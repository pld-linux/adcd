Summary:	Text mode CD player for Linux
Summary(pl.UTF-8):	Odtwarzacz płyt CD dla Linuksa
Name:		adcd
Version:	1.10
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://download.savannah.gnu.org/releases/adcd/%{name}-%{version}.tar.lz
# Source0-md5:	b8e7cb8416701b1ee536b50140e52600
URL:		http://www.nongnu.org/adcd/adcd.html
BuildRequires:	libstdc++-devel >= 5:3.3
BuildRequires:	lzip
BuildRequires:	ncurses-devel >= 5
BuildRequires:	tar >= 1:1.22
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

%build
# not autoconf-generated
./configure \
	CXX="%{__cxx}" \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses" \
	CXXFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}" \
	--prefix=%{_prefix}

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix="%{_prefix}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%lang(es) %doc LEEME
%attr(755,root,root) %{_bindir}/adcd
%{_mandir}/man1/adcd.1*
