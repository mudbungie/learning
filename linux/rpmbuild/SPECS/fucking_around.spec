Name:           fucking_around
Version:        0.0.1
Release:        1%{?dist}
Summary:        just learning

License:        WTFPL
Source0:        %{name}-%{version}.tar.gz

%description


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%{_bindir}/%{name}
%doc add-docs-here



%changelog
* Wed Jan 18 2023 mudbungie <mudbungie@gmail.com>
- 
