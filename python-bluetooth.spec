%define		realname PyBluez
Summary:	Python API for Bluetooth resources
Name:		python-bluetooth
Version:	0.15
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://pybluez.googlecode.com/files/%{realname}-%{version}.tar.gz
# Source0-md5:	104ad743d4bc999796ceff4f39d1003a
URL:		http://code.google.com/p/pybluez/
BuildRequires:	bluez-libs-devel
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Obsoletes:	python-pybluez <= 0.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyBluez is an effort to create python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create
Bluetooth applications.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/%{realname}-%{version}-py*.egg-info
%dir %{py_sitedir}/bluetooth
%{py_sitedir}/bluetooth/*.py[co]
%attr(755,root,root) %{py_sitedir}/bluetooth/_bluetooth.so
