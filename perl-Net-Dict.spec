%define module	Net-Dict
%define name	perl-%{module}
%define version	2.07
%define	release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A perl client for accessing network dictionary servers
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
# both packages provide /usr/bin/dict
Conflicts:	dictd-client

%description
Net::Dict is a perl class for looking up words and their definitions on network
dictionary servers. It provides a simple client API for the DICT network
protocol.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README examples
%{perl_vendorlib}/Net/*
%{_mandir}/*/*
%{_bindir}/dict
%{_bindir}/tkdict

