Summary:	Text-mode interface for git-core
Summary(pl.UTF-8):	Tekstowy interfejs do git-core
Name:		tig
Version:	0.5
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://jonas.nitro.dk/tig/releases/%{name}-%{version}.tar.gz
# Source0-md5:	fab4a728d13b8eb0643a1f5c26c0b8c9
Patch0:		%{name}-ncurses.patch
URL:		http://jonas.nitro.dk/tig/
BuildRequires:	asciidoc
BuildRequires:	ncurses-devel
Requires:	git-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tig is a git-core repository browser that additionally can act as a
pager for output from various git commands.

When browsing repositories, it uses the underlying git commands to
present the user with various views, such as summarized revision log
and showing the commit with the log message, diffstat, and the diff.

Using it as a pager, it will display input from stdin and colorize it.

%description -l pl.UTF-8
Tig jest przeglądarką repozytoriów git-core'a. Dodatkowo może działać
jako pager dla różnych komend gita.

Podczas przeglądania repozytoriów używa poleceń gita i pokazuje log,
statystyki diffa i różnice między plikami.

Używany jako pager będzie kolorował to co otrzyma ze standardowego
wejścia.

%prep
%setup -q
%patch0 -p1

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

install tig.1 $RPM_BUILD_ROOT%{_mandir}/man1
install tigrc.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO *.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
