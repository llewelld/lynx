Name:           lynx
Version:        2.9.0dev.12
Release:        1
Summary:        Lynx is the text web browser
Url:            https://lynx.invisible-island.net/lynx.html
Source0:        %{name}-%{version}.tar.bz2
License:        GPLv2
BuildRequires:  autoconf
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)

%description
Lynx is the text web browser.

%package docs
Summary: Lynx documentation package

%description docs
Documentation for Lynx - Lynx is the text web browser.

%prep
%autosetup -n %{name}-%{version}/lynx2.9.0dev.12

%build
%configure \
    --with-ssl \
    --with-screen=ncurses

%make_build

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/lynx
%{_sysconfdir}/lynx.cfg
%{_sysconfdir}/lynx.lss

%files docs
%defattr(-,root,root)
%{_datadir}/man/man1/lynx.1.gz

