Summary:	Text-mode interface for git-core
Summary(pl.UTF-8):	Tekstowy interfejs do git-core
Name:		tig
Version:	0.15
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://jonas.nitro.dk/tig/releases/%{name}-%{version}.tar.gz
# Source0-md5:	8f373a99823f6db241b66642075657d3
URL:		http://jonas.nitro.dk/tig/
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

%package -n bash-completion-tig
Summary:	bash-completion for tig
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla tiga
Group:		Applications/Shells
Requires:	bash-completion

%description -n bash-completion-tig
This package provides bash-completion for tig.

%description -n bash-completion-tig -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla tiga.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmldflags} -I/usr/include/ncursesw" \
	LDLIBS=-lncursesw

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%{__make} install install-doc-man \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir} \
	prefix=%{_prefix}

# bash completion
install contrib/tig-completion.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README TODO *.html contrib/tigrc
%attr(755,root,root) %{_bindir}/tig
%{_mandir}/man*/*

%files -n bash-completion-tig
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/tig-completion.bash
