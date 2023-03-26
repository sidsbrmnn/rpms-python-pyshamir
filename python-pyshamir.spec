%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname pyshamir

Name:           python-%{srcname}
Version:        1.0.1
Release:        %autorelease
Summary:        Python port of Shamir's secret sharing
License:        MIT
URL:            https://github.com/konidev20/%{srcname}
Source0:        https://github.com/konidev20/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
Python port of Shamir's secret sharing (SSS) from HashiCorp Vault.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Python port of Shamir's secret sharing (SSS) from HashiCorp Vault.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%check
%{__python3} -m unittest discover -p 'test_*.py'


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
%autochangelog
