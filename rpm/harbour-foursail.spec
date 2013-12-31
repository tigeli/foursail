# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-foursail

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Simple foursquare client with basic functions.
Version:    0.2
Release:    1
Group:      Qt/Qt
License:    BSD Licence
URL:        https://gitorious.org/foursail
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-foursail.yaml
Requires:   qt5-qtdeclarative-import-location
Requires:   qt5-qtdeclarative-import-positioning
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(sailfishapp) >= 0.0.10
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
The application is an native Foursquare(r) client for Sailfish OS. 

It have just basic features such as:
- Browsing of nearby venues
- Checkin with a shout, and sharing to Facebook and Twitter.
- Quick checkin via Press and Hold.
- Browsing of recent friend checkins.
- Shows most recent chekin at the Cover Page.

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
/usr/share/icons/hicolor/86x86/apps
/usr/share/applications
/usr/share/harbour-foursail
/usr/bin
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/qml
%{_bindir}
# >> files
# << files
