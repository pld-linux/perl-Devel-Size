#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Size
Summary:	Devel::Size - finding the memory usage of Perl variables
Summary(pl):	Devel::Size - okre¶lanie zu¿ycia pamiêci przez zmienne Perla
Name:		perl-Devel-Size
Version:	0.58
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3043357cff650863b00cb54e511e38f0
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
Jesli zmienna jest haszem lub tablic±, nale¿y u¿yæ referencji przy
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
