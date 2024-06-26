#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Devel
%define		pnam	Size
Summary:	Devel::Size - finding the memory usage of Perl variables
Summary(pl.UTF-8):	Devel::Size - określanie zużycia pamięci przez zmienne Perla
Name:		perl-Devel-Size
Version:	0.84
Release:	2
# same as perl itself (as stated in COPYRIGHT section of pod)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4978c07f54a730b16a705e074d7685e3
URL:		https://metacpan.org/dist/Devel-Size
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module figures out the real sizes of Perl variables in bytes.
Call functions with a reference to the variable you want the size
of.  If the variable is a plain scalar it returns the size of
the scalar.  If the variable is a hash or an array, use a reference
when calling.

%description -l pl.UTF-8
Ten moduł oblicza prawdziwe rozmiary zmiennych perlowych w bajtach.
Wystarczy wywołać funkcję z referencją do zmiennej, której rozmiar
chce się poznać. Jeśli zmienna jest skalarem, zwraca rozmiar skalara.
Jeśli zmienna jest haszem lub tablicą, należy użyć referencji przy
wywołaniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%doc CHANGES
%{perl_vendorarch}/Devel/Size.pm
%dir %{perl_vendorarch}/auto/Devel/Size
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/Size/Size.so
%{_mandir}/man3/Devel::Size.3pm*
