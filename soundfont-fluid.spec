Summary:	Fluid (R3) - General Midi soundfont by Frank Wen
Name:		soundfont-fluid
Version:	3.1
Release:	1
License:	MIT
Group:		Applications
Source0:	fluid-soundfont_%{version}.tar.gz
Obsoletes:	fluid-soundfont
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fluid (R3) - General Midi soundfont by Frank Wen.

%prep
%setup -qn fluid-soundfont-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/soundfonts
install *.sf2 $RPM_BUILD_ROOT%{_datadir}/soundfonts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/soundfonts/*
