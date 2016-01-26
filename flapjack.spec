Summary:	Intelligent, scalable, distributed monitoring notification system
Name:		flapjack
Version:	1.6.0
Release:	0.1
License:	MIT
Group:		Networking
Source0:	https://github.com/flapjack/flapjack/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	95ae6e534c277be34638b06bff9c6940
URL:		http://flapjack.io/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	sed >= 4.0
Requires:	ruby-activesupport
Requires:	ruby-blather < 0.9
Requires:	ruby-blather >= 0.8.3
Requires:	ruby-chronic
Requires:	ruby-chronic_duration
Requires:	ruby-dante = 0.2.0
Requires:	ruby-em-hiredis
Requires:	ruby-em-http-request
Requires:	ruby-em-synchrony < 1.1
Requires:	ruby-em-synchrony >= 1.0.2
Requires:	ruby-eventmachine < 1.1
Requires:	ruby-eventmachine >= 1.0.0
Requires:	ruby-gli = 2.12.0
Requires:	ruby-hiredis
Requires:	ruby-ice_cube
Requires:	ruby-mail
Requires:	ruby-nexmo = 2.0.0
Requires:	ruby-nokogiri = 1.6.2.1
Requires:	ruby-oj >= 2.9.0
Requires:	ruby-rack-fiber_pool
Requires:	ruby-rake
Requires:	ruby-rbtrace
Requires:	ruby-redis < 3.1
Requires:	ruby-redis >= 3.0.6
Requires:	ruby-sinatra
Requires:	ruby-terminal-table
Requires:	ruby-thin < 1.7
Requires:	ruby-thin >= 1.6.1
Requires:	ruby-tzinfo
Requires:	ruby-tzinfo-data
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flapjack is a distributed monitoring notification system that provides
a scalable method for processing streams of events from Nagios and
deciding who should be notified.

%prep
%setup -q
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# make gemspec self-contained
ruby -r rubygems -e 'spec = eval(File.read("%{name}.gemspec"))
	File.open("%{name}-%{version}.gemspec", "w") do |file|
	file.puts spec.to_ruby_for_cache
end'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flapjack
%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}
%{ruby_specdir}/%{name}-%{version}.gemspec
