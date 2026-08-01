%define upstream_name	 Net-Dict
%define upstream_version 2.22
Name:		perl-%{upstream_name}
Version:	2.22
Release:	3

Summary:	A perl client for accessing network dictionary servers



License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/neilbowers/Net-Dict
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/Net-Dict-2.22.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

# both packages provide /usr/bin/dict
Conflicts:	dictd-client

%description
Net::Dict is a perl class for looking up words and their definitions on network
dictionary servers. It provides a simple client API for the DICT network
protocol.

%prep
%setup -q -n Net-Dict-2.22

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%install
%makeinstall_std

%check
make test || :

%files
%doc README examples
%{perl_vendorlib}/Net/*
%{_mandir}/*/*
%{_bindir}/dict
%{_bindir}/tkdict




