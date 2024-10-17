Name:		sourceinstall-gtk
Summary:	GUI front end for sourceinstall
Version:	2.5
Release:	%{mkrel 2}
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
URL:		https://www.gnu.org/software/sourceinstall 
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:	GPLv3+
BuildRequires:	libsrcinst-devel
BuildRequires:	gtk2-devel
BuildRequires:	imagemagick

%description
For an experienced user, sourceinstall provides a way to centralize source
installation, keep track of already installed packages and their relevant 
files, check installations for consistency, and have enhanced uninstallation.
sourceinstall-gtk is a GUI front end for sourceinstall.

%prep 
%setup -q

%build 
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
install -m 0644 images/icon48x48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32 images/icon48x48.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 images/icon48x48.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

# menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=GNU Source Installer
Comment=Install software from source code
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Settings;PackageManager;
EOF

%find_lang %{name}

%clean 
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,0755) 
%doc AUTHORS ChangeLog
%{_bindir}/%{name}
%{_mandir}/*/*
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.5-2mdv2010.0
+ Revision: 445166
- rebuild

* Thu Nov 06 2008 Adam Williamson <awilliamson@mandriva.org> 2.5-1mdv2009.1
+ Revision: 300356
- import sourceinstall-gtk


