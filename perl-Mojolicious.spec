#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 5424026
#
Name     : perl-Mojolicious
Version  : 9.39
Release  : 135
URL      : https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojolicious-9.39.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojolicious-9.39.tar.gz
Summary  : 'Real-time web framework'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Mojolicious-bin = %{version}-%{release}
Requires: perl-Mojolicious-license = %{version}-%{release}
Requires: perl-Mojolicious-man = %{version}-%{release}
Requires: perl-Mojolicious-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Digest::MD5)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<p align="center">
<a href="https://mojolicious.org">
<img src="https://raw.github.com/mojolicious/mojo/main/lib/Mojolicious/resources/public/mojo/logo.png?raw=true" style="margin: 0 auto;">
</a>
</p>

%package bin
Summary: bin components for the perl-Mojolicious package.
Group: Binaries
Requires: perl-Mojolicious-license = %{version}-%{release}

%description bin
bin components for the perl-Mojolicious package.


%package dev
Summary: dev components for the perl-Mojolicious package.
Group: Development
Requires: perl-Mojolicious-bin = %{version}-%{release}
Provides: perl-Mojolicious-devel = %{version}-%{release}
Requires: perl-Mojolicious = %{version}-%{release}

%description dev
dev components for the perl-Mojolicious package.


%package license
Summary: license components for the perl-Mojolicious package.
Group: Default

%description license
license components for the perl-Mojolicious package.


%package man
Summary: man components for the perl-Mojolicious package.
Group: Default

%description man
man components for the perl-Mojolicious package.


%package perl
Summary: perl components for the perl-Mojolicious package.
Group: Default
Requires: perl-Mojolicious = %{version}-%{release}

%description perl
perl components for the perl-Mojolicious package.


%prep
%setup -q -n Mojolicious-9.39
cd %{_builddir}/Mojolicious-9.39
pushd ..
cp -a Mojolicious-9.39 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mojolicious
cp %{_builddir}/Mojolicious-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Mojolicious/2f8018a02043ed1a43f032379e036bb6b88265f2 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hypnotoad
/usr/bin/mojo
/usr/bin/morbo

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mojo.3
/usr/share/man/man3/Mojo::Asset.3
/usr/share/man/man3/Mojo::Asset::File.3
/usr/share/man/man3/Mojo::Asset::Memory.3
/usr/share/man/man3/Mojo::Base.3
/usr/share/man/man3/Mojo::BaseUtil.3
/usr/share/man/man3/Mojo::ByteStream.3
/usr/share/man/man3/Mojo::Cache.3
/usr/share/man/man3/Mojo::Collection.3
/usr/share/man/man3/Mojo::Content.3
/usr/share/man/man3/Mojo::Content::MultiPart.3
/usr/share/man/man3/Mojo::Content::Single.3
/usr/share/man/man3/Mojo::Cookie.3
/usr/share/man/man3/Mojo::Cookie::Request.3
/usr/share/man/man3/Mojo::Cookie::Response.3
/usr/share/man/man3/Mojo::DOM.3
/usr/share/man/man3/Mojo::DOM::CSS.3
/usr/share/man/man3/Mojo::DOM::HTML.3
/usr/share/man/man3/Mojo::Date.3
/usr/share/man/man3/Mojo::DynamicMethods.3
/usr/share/man/man3/Mojo::EventEmitter.3
/usr/share/man/man3/Mojo::Exception.3
/usr/share/man/man3/Mojo::File.3
/usr/share/man/man3/Mojo::Headers.3
/usr/share/man/man3/Mojo::HelloWorld.3
/usr/share/man/man3/Mojo::Home.3
/usr/share/man/man3/Mojo::IOLoop.3
/usr/share/man/man3/Mojo::IOLoop::Client.3
/usr/share/man/man3/Mojo::IOLoop::Server.3
/usr/share/man/man3/Mojo::IOLoop::Stream.3
/usr/share/man/man3/Mojo::IOLoop::Subprocess.3
/usr/share/man/man3/Mojo::IOLoop::TLS.3
/usr/share/man/man3/Mojo::JSON.3
/usr/share/man/man3/Mojo::JSON::Pointer.3
/usr/share/man/man3/Mojo::Loader.3
/usr/share/man/man3/Mojo::Log.3
/usr/share/man/man3/Mojo::Message.3
/usr/share/man/man3/Mojo::Message::Request.3
/usr/share/man/man3/Mojo::Message::Response.3
/usr/share/man/man3/Mojo::Parameters.3
/usr/share/man/man3/Mojo::Path.3
/usr/share/man/man3/Mojo::Promise.3
/usr/share/man/man3/Mojo::Reactor.3
/usr/share/man/man3/Mojo::Reactor::EV.3
/usr/share/man/man3/Mojo::Reactor::Poll.3
/usr/share/man/man3/Mojo::Server.3
/usr/share/man/man3/Mojo::Server::CGI.3
/usr/share/man/man3/Mojo::Server::Daemon.3
/usr/share/man/man3/Mojo::Server::Hypnotoad.3
/usr/share/man/man3/Mojo::Server::Morbo.3
/usr/share/man/man3/Mojo::Server::Morbo::Backend.3
/usr/share/man/man3/Mojo::Server::Morbo::Backend::Poll.3
/usr/share/man/man3/Mojo::Server::PSGI.3
/usr/share/man/man3/Mojo::Server::Prefork.3
/usr/share/man/man3/Mojo::Template.3
/usr/share/man/man3/Mojo::Transaction.3
/usr/share/man/man3/Mojo::Transaction::HTTP.3
/usr/share/man/man3/Mojo::Transaction::WebSocket.3
/usr/share/man/man3/Mojo::URL.3
/usr/share/man/man3/Mojo::Upload.3
/usr/share/man/man3/Mojo::UserAgent.3
/usr/share/man/man3/Mojo::UserAgent::CookieJar.3
/usr/share/man/man3/Mojo::UserAgent::Proxy.3
/usr/share/man/man3/Mojo::UserAgent::Server.3
/usr/share/man/man3/Mojo::UserAgent::Transactor.3
/usr/share/man/man3/Mojo::Util.3
/usr/share/man/man3/Mojo::WebSocket.3
/usr/share/man/man3/Mojolicious.3
/usr/share/man/man3/Mojolicious::Command.3
/usr/share/man/man3/Mojolicious::Command::Author::cpanify.3
/usr/share/man/man3/Mojolicious::Command::Author::generate.3
/usr/share/man/man3/Mojolicious::Command::Author::generate::app.3
/usr/share/man/man3/Mojolicious::Command::Author::generate::dockerfile.3
/usr/share/man/man3/Mojolicious::Command::Author::generate::lite_app.3
/usr/share/man/man3/Mojolicious::Command::Author::generate::makefile.3
/usr/share/man/man3/Mojolicious::Command::Author::generate::plugin.3
/usr/share/man/man3/Mojolicious::Command::Author::inflate.3
/usr/share/man/man3/Mojolicious::Command::cgi.3
/usr/share/man/man3/Mojolicious::Command::daemon.3
/usr/share/man/man3/Mojolicious::Command::eval.3
/usr/share/man/man3/Mojolicious::Command::get.3
/usr/share/man/man3/Mojolicious::Command::prefork.3
/usr/share/man/man3/Mojolicious::Command::psgi.3
/usr/share/man/man3/Mojolicious::Command::routes.3
/usr/share/man/man3/Mojolicious::Command::version.3
/usr/share/man/man3/Mojolicious::Commands.3
/usr/share/man/man3/Mojolicious::Controller.3
/usr/share/man/man3/Mojolicious::Guides.3
/usr/share/man/man3/Mojolicious::Guides::Contributing.3
/usr/share/man/man3/Mojolicious::Guides::Cookbook.3
/usr/share/man/man3/Mojolicious::Guides::FAQ.3
/usr/share/man/man3/Mojolicious::Guides::Growing.3
/usr/share/man/man3/Mojolicious::Guides::Rendering.3
/usr/share/man/man3/Mojolicious::Guides::Routing.3
/usr/share/man/man3/Mojolicious::Guides::Testing.3
/usr/share/man/man3/Mojolicious::Guides::Tutorial.3
/usr/share/man/man3/Mojolicious::Lite.3
/usr/share/man/man3/Mojolicious::Plugin.3
/usr/share/man/man3/Mojolicious::Plugin::Config.3
/usr/share/man/man3/Mojolicious::Plugin::DefaultHelpers.3
/usr/share/man/man3/Mojolicious::Plugin::EPLRenderer.3
/usr/share/man/man3/Mojolicious::Plugin::EPRenderer.3
/usr/share/man/man3/Mojolicious::Plugin::HeaderCondition.3
/usr/share/man/man3/Mojolicious::Plugin::JSONConfig.3
/usr/share/man/man3/Mojolicious::Plugin::Mount.3
/usr/share/man/man3/Mojolicious::Plugin::NotYAMLConfig.3
/usr/share/man/man3/Mojolicious::Plugin::TagHelpers.3
/usr/share/man/man3/Mojolicious::Plugins.3
/usr/share/man/man3/Mojolicious::Renderer.3
/usr/share/man/man3/Mojolicious::Routes.3
/usr/share/man/man3/Mojolicious::Routes::Match.3
/usr/share/man/man3/Mojolicious::Routes::Pattern.3
/usr/share/man/man3/Mojolicious::Routes::Route.3
/usr/share/man/man3/Mojolicious::Sessions.3
/usr/share/man/man3/Mojolicious::Static.3
/usr/share/man/man3/Mojolicious::Types.3
/usr/share/man/man3/Mojolicious::Validator.3
/usr/share/man/man3/Mojolicious::Validator::Validation.3
/usr/share/man/man3/Test::Mojo.3
/usr/share/man/man3/ojo.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Mojolicious/2f8018a02043ed1a43f032379e036bb6b88265f2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/hypnotoad.1
/usr/share/man/man1/mojo.1
/usr/share/man/man1/morbo.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
