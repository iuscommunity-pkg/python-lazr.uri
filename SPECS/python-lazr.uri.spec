%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

#python major version
%{expand: %%define pyver %(%{__python} -c 'import sys;print(sys.version[0:3])')}

Name:		python-lazr.uri
Version:	1.0.2
Release:	1.ius%{?dist}
Summary:	A self-contained, easily reusable library for parsing, manipulating, and generating URIs.

Group:		Applicatons/System
License:	GPLv3
URL:		https://launchpad.net/lazr.uri	
Source0:	http://launchpad.net/lazr.uri/trunk/1.0.2/+download/lazr.uri-%{version}.tar.gz

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python, python-setuptools
Requires:	python

%description
A self-contained, easily reusable library for parsing, manipulating, and generating URIs.

%prep
%setup -q -n lazr.uri-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 \
		    --skip-build \
	     --root %{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc PKG-INFO README.txt HACKING.txt COPYING.txt 
%{python_sitelib}/lazr.uri-%{version}-py%{pyver}.egg-info/
%{python_sitelib}/lazr.uri-%{version}-py%{pyver}-nspkg.pth/
%{python_sitelib}/lazr/uri/


%changelog
* Fri Jun 10 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.2-1.ius
- Initial spec
