Summary:	Intelligent, scalable, distributed monitoring notification system
Name:		flapjack
Version:	1.6.0
Release:	0.1
License:	MIT
Group:		Networking
Source0:	https://github.com/flapjack/flapjack/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	95ae6e534c277be34638b06bff9c6940
URL:		http://flapjack.io/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flapjack is a distributed monitoring notification system that provides
a scalable method for processing streams of events from Nagios and
deciding who should be notified.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
