Summary: Help motorically impaired users to use the mouse
Name: mousetweaks
Version: 3.4.1
Release: 1
License: GPLv3+
Group: Accessibility
Url: http://live.gnome.org/Mousetweaks/Home
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gnome-doc-utils)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libpanelapplet-4.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xtst)

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
%configure2_5x \
	--disable-static \
	--enable-pointer-capture \
	--enable-dwell-click

%make

%install
%makeinstall_std
%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS README NEWS TODO
%{_bindir}/dwell-click-applet
%{_bindir}/mousetweaks
%{_bindir}/pointer-capture-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.DwellClickAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.PointerCaptureAppletFactory.service
%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-panel/applets/org.gnome.applets.DwellClickApplet.panel-applet
%{_datadir}/gnome-panel/applets/org.gnome.applets.PointerCaptureApplet.panel-applet
%{_datadir}/%{name}
%{_mandir}/man1/*.1*

