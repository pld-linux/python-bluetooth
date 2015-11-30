%define		realname PyBluez
Summary:	Python API for Bluetooth resources
Summary(pl.UTF-8):	API Pythona do obsługi urządzeń Bluetooth
Name:		python-bluetooth
Version:	0.18
Release:	5
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://pybluez.googlecode.com/files/%{realname}-%{version}.tar.gz
# Source0-md5:	be8c8ce615c3189fda1aaf3d568314b2
URL:		http://code.google.com/p/pybluez/
BuildRequires:	bluez-libs-devel
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
Obsoletes:	python-pybluez <= 0.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyBluez is an effort to create Python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create
Bluetooth applications.

%description -l pl.UTF-8
PyBluez to próba stworzenia pythonowej obudowy dla zasobów systemowych
Bluetooth w celu umożliwienia programistom Pythona łatwego i szybkiego
tworzenia aplikacji Bluetooth.

%prep
%setup -q -n %{realname}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{py_sitedir}/%{realname}-%{version}-py*.egg-info
%dir %{py_sitedir}/bluetooth
%{py_sitedir}/bluetooth/*.py[co]
%attr(755,root,root) %{py_sitedir}/bluetooth/_bluetooth.so
