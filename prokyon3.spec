Summary:	Qt based MP3 and Ogg manager and tag editor
Summary(pl):	Bazowany na Qt zarz±dca i edytor tagów MP3 i Ogg
Name:		prokyon3
Version:	0.9.2
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/sourceforge/prokyon3/%{name}-%{version}.tar.gz
# Source0-md5:	49e7b2662f4fffc3c366c4fb0ff53d4c
Source1:	%{name}.desktop
URL:		http://prokyon3.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	id3lib-devel >= 3.8
BuildRequires:	libvorbis-devel
BuildRequires:	mysql-devel
BuildRequires:	qt-devel >= 3.1.1
Requires:	qt-plugin-mysql
Requires:	mysql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Prokyon3 is a MP3/Ogg manager and tag editor originally developed for
Linux. It was written in C++ using the Qt3 widget set and the MySQL
database. Prokyon3 can access both MP3 and Ogg files on local as well
as shared network drives.

%description -l pl
Prokyon3 jest zarz±dc± MP3/Ogg i edytorem tagów, oryginalnie
rozwijanym dla Linuksa. Zosta³ napisany w C++, u¿ywa biblioteki Qt3 i
bazy danych MySQL. Mo¿e pracowaæ z plikami MP3 i Ogg zawartymi na
lokalnym dysku, a tak¿e z dzielonymi dyskami sieciowymi.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-qtdir=%{_prefix} \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libs=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/html
%dir %{_datadir}/%{name}/html/manual_one_file
%dir %{_datadir}/%{name}/html/manual_one_file/images
%dir %{_datadir}/%{name}/html/manual_one_file/images/docbook
%dir %{_datadir}/%{name}/images
%{_datadir}/%{name}/html/manual_one_file/index.html
%{_datadir}/%{name}/html/manual_one_file/images/docbook/*.png
%{_datadir}/%{name}/images/*.png
%{_desktopdir}/*.desktop
