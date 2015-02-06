%define upstream_name	 Net-Dict
%define upstream_version 2.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A perl client for accessing network dictionary servers



License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

# both packages provide /usr/bin/dict
Conflicts:	dictd-client

%description
Net::Dict is a perl class for looking up words and their definitions on network
dictionary servers. It provides a simple client API for the DICT network
protocol.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%install
%makeinstall_std

%files
%doc README examples
%{perl_vendorlib}/Net/*
%{_mandir}/*/*
%{_bindir}/dict
%{_bindir}/tkdict




