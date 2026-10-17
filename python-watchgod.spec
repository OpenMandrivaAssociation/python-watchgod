Name:		python-watchgod
Version:	1.2.0
Release:	3
Summary:	Transitional package replaced by python-watchfiles
License:	MIT
Group:		Development/Python
URL:		https://github.com/samuelcolvin/watchfiles
BuildArch:	noarch
# python-watchfiles Obsoletes python-watchgod < 1.2.0-2 and Provides
# the old name at 1.2.0-2. Stay above that bound so the extra tests
# can still install this package, and ship no Python modules.
Requires:	python-watchfiles >= 1.2.0-2

%description
python-watchgod has been replaced by python-watchfiles.
This package contains no Python modules. It exists so the
Python 3.14 build is no longer the newest version in the
repository, and so an upgrade pulls in python-watchfiles.

%prep
cat > README << 'EOF'
python-watchgod has been replaced by python-watchfiles.
EOF

%build

%install
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -p README %{buildroot}%{_datadir}/doc/%{name}/README

%files
%{_datadir}/doc/%{name}/README
