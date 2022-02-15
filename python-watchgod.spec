%define module watchgod

Summary:	A simple, modern file watching and code reload in python
Name:		python-%{module}
Version:	0.7
Release:	1
License:	Expat
Url:		https://github.com/samuelcolvin/watchgod
Group:		Development/Languages/Python
Source:		https://files.pythonhosted.org/packages/source/w/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)

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
%{python_sitelib}/*

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

