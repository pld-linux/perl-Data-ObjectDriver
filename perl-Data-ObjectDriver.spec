#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Data
%define	pnam	ObjectDriver
Summary:	Data::ObjectDriver - Simple, transparent data interface, with caching
#Summary(pl.UTF-8):	
Name:		perl-Data-ObjectDriver
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ff9a34c466b0e200b14b56e1aec8bcbf
URL:		http://search.cpan.org/dist/Data-ObjectDriver/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Class::Trigger)
BuildRequires:	perl-DBI
BuildRequires:	perl(Test::Exception)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::ObjectDriver is an object relational mapper, meaning that it maps
object-oriented design concepts onto a relational database.

It's inspired by, and descended from, the MT::ObjectDriver classes in
Six Apart's Movable Type and TypePad weblogging products. But it adds in
caching and partitioning layers, allowing you to spread data across multiple
physical databases, without your application code needing to know where the
data is stored.

It's currently considered ALPHA code. The API is largely fixed, but may seen
some small changes in the future. For what it's worth, the likeliest area
for changes are in the syntax for the search method, and would most
likely not break much in the way of backwards compatibility.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/*.pm
%{perl_vendorlib}/Data/ObjectDriver
%{_mandir}/man3/*
