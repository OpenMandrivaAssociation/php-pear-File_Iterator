%define  upstream_name File_Iterator

Summary:	FilterIterator implementation that filters files based on a list of suffixes
Name:		php-pear-%{upstream_name}
Version:	1.3.0
Release:	4
License:	BSD
Group:		Development/PHP
URL:		http://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/File_Iterator-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear >= 1:1.9.4
Requires:	php-channel-phpunit
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
Suggests:	php-pear-PHPUnit >= 3.6.3

%description
PHPUnit is a regression testing framework used by the developer who implements
unit tests in PHP.

This package provides FilterIterator implementation that filters files based
on a list of suffixes for PHPUnit.

%prep

%setup -q -c 
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/ChangeLog.markdown
%doc %{upstream_name}-%{version}/LICENSE
%doc %{upstream_name}-%{version}/README.markdown
%{_datadir}/pear/File/Iterator
%{_datadir}/pear/File/*.php
%{_datadir}/pear/packages/File_Iterator.xml



%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2012.0
+ Revision: 741977
- fix major breakage by careless packager

* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1
+ Revision: 730867
- import php-pear-File_Iterator


* Wed Nov 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdv2010.2
- initial Mandriva package
