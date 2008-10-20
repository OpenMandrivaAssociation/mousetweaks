%define name mousetweaks
%define version 2.24.1
%define release %mkrel 1

Summary: Help motorically impaired users to use the mouse
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
License: GPLv3+
Group: Accessibility
Url: http://live.gnome.org/Mousetweaks/Home
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libGConf2-devel
BuildRequires: gtk+2-devel
BuildRequires: libglade2.0-devel
BuildRequires: gnome-panel-devel
BuildRequires: at-spi-devel
BuildRequires: dbus-glib-devel
BuildRequires: libgnomeui2-devel
BuildRequires: libxtst-devel
BuildRequires: intltool
BuildRequires: gnome-doc-utils >= 0.3.2


%description
The Mousetweaks package provides mouse accessibility enhancements for 
the GNOME desktop. These enhancements are:

1. It offers a way to perform the various clicks without using any 
hardware button.

2. It allows users to perform a right click by doing a click&hold 
of the left mousebutton. (For a left-handed mouse user, the termes 
left and right have to be inverted.) 

3. It provides an applet that the user can install on a panel. This
applet creates an area on the panel into which the pointer can 
be captured until the user releases it with a predefined button
and modifier combination.

The options can be accessed through the Accessibility tab of the
Mouse Preferences of GNOME Control Center or through command-line.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot} %name.lang
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
%find_lang %name --with-gnome
for omf in %buildroot%_datadir/omf/*/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done


%clean
rm -rf %{buildroot}

%define schemas mousetweaks pointer-capture-applet
%if %mdvver < 200900
%post
%post_install_gconf_schemas %schemas
%endif

%preun
%preun_uninstall_gconf_schemas %schemas

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS TODO
%_sysconfdir/gconf/schemas/mousetweaks.schemas
%_sysconfdir/gconf/schemas/pointer-capture-applet.schemas
%_bindir/dwell-click-applet
%_bindir/mousetweaks
%_bindir/pointer-capture-applet
%_libdir/bonobo/servers/*.server
%dir %_datadir/omf/%name
%_datadir/omf/%name/%name-C.omf
%_mandir/man1/*.1*
%_datadir/%name

