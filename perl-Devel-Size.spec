#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	Size
Summary:	Devel::Size - finding the memory usage of Perl variables
Summary(pl):	Devel::Size - okre¶lanie zu¿ycia pamiêci przez zmienne Perla
Name:		perl-Devel-Size
Version:	0.64
Release:	0.1
# same as perl itself (as stated in COPYRIGHT section of pod)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d200be2102275c77e2e3bb18ac6914b4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module figures out the real sizes of Perl variables in bytes.
Call functions with a reference to the variable you want the size
of.  If the variable is a plain scalar it returns the size of
the scalar.  If the variable is a hash or an array, use a reference
when calling.

%description -l pl
Ten modu³ oblicza prawdziwe rozmiary zmiennych perlowych w bajtach.
Wystarczy wywo³aæ funkcjê z referencj± do zmiennej, której rozmiar
chce siê poznaæ. Je¶li zmienna jest skalarem, zwraca rozmiar skalara.
Je¶li zmienna jest haszem lub tablic±, nale¿y u¿yæ referencji przy
wywo³aniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Devel/Size.pm
%dir %{perl_vendorarch}/auto/Devel/Size
%{perl_vendorarch}/auto/Devel/Size/Size.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/Size/Size.so
%{_mandir}/man3/*
