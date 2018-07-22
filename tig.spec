Summary:	Text-mode interface for git-core
Summary(pl.UTF-8):	Tekstowy interfejs do git-core
Name:		tig
Version:	2.4.0
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	https://github.com/jonas/tig/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ae8fce41b1ba26ef2306bde9135c52dd
URL:		https://jonas.github.io/tig/
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n bash-completion-tig
This package provides bash-completion for tig.

%description -n bash-completion-tig -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla tiga.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} %{rpmldflags} -I/usr/include/ncursesw"
export CFLAGS
LIBS=-ltinfow %configure
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%{__make} install install-doc-man \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir} \
	prefix=%{_prefix}
	sysconfdir=%{_sysconfdir}

# bash completion
cp -a contrib/tig-completion.bash $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tigrc
%attr(755,root,root) %{_bindir}/tig
#%attr(755,root,root) %{_bindir}/test-graph
%{_mandir}/man1/tig.1*
%{_mandir}/man5/tigrc.5*
%{_mandir}/man7/tigmanual.7*

%files -n bash-completion-tig
%defattr(644,root,root,755)
%{_sysconfdir}/bash_completion.d/tig-completion.bash
