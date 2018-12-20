#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mojolicious
Version  : 8.10
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojolicious-8.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojolicious-8.10.tar.gz
Summary  : 'Real-time web framework'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Mojolicious-bin = %{version}-%{release}
Requires: perl-Mojolicious-license = %{version}-%{release}
Requires: perl-Mojolicious-man = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
<p align="center">
<a href="https://mojolicious.org">
<img src="https://raw.github.com/mojolicious/mojo/master/lib/Mojolicious/resources/public/mojo/logo.png?raw=true" style="margin: 0 auto;">
</a>
</p>

%package bin
Summary: bin components for the perl-Mojolicious package.
Group: Binaries
Requires: perl-Mojolicious-license = %{version}-%{release}
Requires: perl-Mojolicious-man = %{version}-%{release}

%description bin
bin components for the perl-Mojolicious package.


%package dev
Summary: dev components for the perl-Mojolicious package.
Group: Development
Requires: perl-Mojolicious-bin = %{version}-%{release}
Provides: perl-Mojolicious-devel = %{version}-%{release}

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


%prep
%setup -q -n Mojolicious-8.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mojolicious
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Mojolicious/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Mojo.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Asset.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Asset/File.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Asset/Memory.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Base.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/ByteStream.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Cache.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Collection.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Content.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Content/MultiPart.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Content/Single.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Cookie.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Cookie/Request.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Cookie/Response.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/DOM.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/DOM/CSS.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/DOM/HTML.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Date.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/DynamicMethods.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/EventEmitter.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Exception.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/File.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Headers.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/HelloWorld.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Home.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/IOLoop.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/IOLoop/Client.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/IOLoop/Delay.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/IOLoop/Server.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/IOLoop/Stream.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/IOLoop/Subprocess.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/IOLoop/TLS.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/IOLoop/resources/server.crt
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/IOLoop/resources/server.key
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/JSON.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/JSON/Pointer.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Loader.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Log.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Message.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Message/Request.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Message/Response.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Parameters.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Path.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Promise.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Reactor.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Reactor/EV.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Reactor/Poll.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Server.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Server/CGI.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Server/Daemon.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Server/Hypnotoad.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Server/Morbo.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Server/Morbo/Backend.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Server/Morbo/Backend/Poll.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Server/PSGI.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Server/Prefork.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Template.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Transaction.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Transaction/HTTP.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Transaction/WebSocket.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/URL.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Upload.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/UserAgent.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/UserAgent/CookieJar.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/UserAgent/Proxy.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/UserAgent/Server.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/UserAgent/Transactor.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/Util.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/WebSocket.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/Author/cpanify.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/Author/generate.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/Author/generate/app.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/Author/generate/lite_app.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/Author/generate/makefile.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/Author/generate/plugin.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/Author/inflate.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/cgi.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/daemon.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/eval.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/get.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/prefork.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/psgi.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/routes.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Command/version.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Commands.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Controller.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Guides.pod
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Guides/Contributing.pod
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Guides/Cookbook.pod
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Guides/FAQ.pod
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Guides/Growing.pod
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Guides/Rendering.pod
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Guides/Routing.pod
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Guides/Testing.pod
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Guides/Tutorial.pod
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Lite.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Plugin.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Plugin/Config.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Plugin/DefaultHelpers.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Plugin/EPLRenderer.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Plugin/EPRenderer.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Plugin/HeaderCondition.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Plugin/JSONConfig.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Plugin/Mount.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Plugin/PODRenderer.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Plugin/TagHelpers.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Plugins.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Renderer.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Routes.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Routes/Match.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Routes/Pattern.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Routes/Route.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Sessions.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Static.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Types.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Validator.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/Validator/Validation.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/favicon.ico
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/failraptor.png
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/jquery/jquery.js
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/logo-black-2x.png
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/logo-black.png
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/logo-white-2x.png
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/logo-white.png
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/logo.png
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/noraptor.png
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/notfound.png
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/pinstripe-dark.png
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/pinstripe-light.png
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/prettify/prettify-mojo-dark.css
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/public/mojo/prettify/run_prettify.js
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/templates/mojo/debug.html.ep
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/templates/mojo/exception.html.ep
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/templates/mojo/menubar.html.ep
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/templates/mojo/not_found.html.ep
/usr/lib/perl5/vendor_perl/5.28.1/Mojolicious/resources/templates/mojo/perldoc.html.ep
/usr/lib/perl5/vendor_perl/5.28.1/Test/Mojo.pm
/usr/lib/perl5/vendor_perl/5.28.1/ojo.pm

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
/usr/share/man/man3/Mojo::IOLoop::Delay.3
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
/usr/share/man/man3/Mojolicious::Plugin::PODRenderer.3
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
/usr/share/package-licenses/perl-Mojolicious/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/hypnotoad.1
/usr/share/man/man1/mojo.1
/usr/share/man/man1/morbo.1
