Summary:	Text-mode interface for git-core
Summary(pl):	Tekstowy interfejs do git-core
Name:		tig
Version:	0.4
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://jonas.nitro.dk/tig/releases/%{name}-%{version}.tar.gz
# Source0-md5:	fc612d2b7c4551319beb4b5080ef9b90
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

%description -l pl
Tig jest przegl±dark± repozytoriów git-core'a. Dodatkowo mo¿e dzia³aæ
jako pager dla ró¿nych komend gita.

Podczas przegl±dania repozytoriów u¿ywa poleceñ gita i pokazuje log,
statystyki diffa i ró¿nice miêdzy plikami.

U¿ywany jako pager bêdzie kolorowa³ to co otrzyma ze standardowego
wej¶cia.

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
