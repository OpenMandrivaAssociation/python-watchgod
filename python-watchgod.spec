%define module watchgod

Summary:	A simple, modern file watching and code reload in python
Name:		python-%{module}
Version:	0.8.2
Release:	3
License:	Expat
Url:		https://github.com/samuelcolvin/watchgod
Group:		Development/Languages/Python
Source0:		https://files.pythonhosted.org/packages/source/w/%{module}/%{module}-%{version}.tar.gz
Patch0:     relax-anyio-deps.patch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(pip)

BuildArch:	noarch

%description
watchgod is a simple, modern file watching and code reload in python.

(watchgod is inspired by watchdog, hence the name, but tries to fix some of
the frustrations I found with watchdog, namely: separate approaches for each
OS, an inelegant approach to concurrency using threading, challenges around
debouncing changes and bugs which weren't being fixed)

%files
%license LICENSE
%doc README.md
%{_bindir}/%{module}
%{python_sitelib}/watchgod-%{version}-py*.*.egg-info
%{python_sitelib}/watchgod/

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version} -p1

%build
%py_build

%install
%py_install

