%define upstream_name	 Net-Dict
%define upstream_version 2.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A perl client for accessing network dictionary servers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Net/Net-Dict-%{upstream_version}.tar.gz

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

%changelog
* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.70.0-1mdv2010.0
+ Revision: 407811
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.07-7mdv2009.0
+ Revision: 258008
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.07-6mdv2009.0
+ Revision: 246061
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.07-4mdv2008.1
+ Revision: 140692
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 2.07-4mdv2008.0
+ Revision: 25292
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.07-3mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Fri Feb 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.07-2mdk
- Rebuild
- Disable tests, obsolete

* Wed Sep 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.07-1mdk
- Initial MDK release.


