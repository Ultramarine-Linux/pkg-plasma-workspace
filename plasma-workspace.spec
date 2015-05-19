# Enable bootstrap when building plasma-workspace on a new repo
# or arch where there's no package that would provide plasmashell
#%define bootstrap 1

Name:           plasma-workspace
Version:        5.3.0
Release:        6%{?dist}
Summary:        Plasma workspace, applications and applets
License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/plasma-workspace

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

# This goes to PAM
Source10:       kde
# upstream startkde.kde, minus stuff we don't want or need, plus a minor bit of customization --rex
Source11:       startkde.cmake
# Desktop file for Fedora Twenty Two look-and-feel package
Source12:       metadata.desktop

## downstream Patches
Patch10:        plasma-workspace-5.3.0-konsole-in-contextmenu.patch
Patch11:        plasma-workspace-5.3.0-set-fedora-default-look-and-feel.patch

## upstreamable Patches

## upstream Patches

## master branch Patches

# udev
BuildRequires:  zlib-devel
BuildRequires:  dbusmenu-qt5-devel
BuildRequires:  libGL-devel
BuildRequires:  mesa-libGLES-devel
#BuildRequires:  wayland-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXau-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-devel
BuildRequires:  glib2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  python-devel
BuildRequires:  boost-devel
#BuildRequires:  akonadi-qt5-devel
#BuildRequires:  kdepimlibs-devel
BuildRequires:  libusb-devel
BuildRequires:  libbsd-devel
BuildRequires:  pam-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  pciutils-devel
%ifnarch s390 s390x
BuildRequires:  libraw1394-devel
%endif
BuildRequires:  gpsd-devel

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  phonon-qt5-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-krunner-devel
BuildRequires:  kf5-kjsembed-devel
BuildRequires:  kf5-knotifyconfig-devel
BuildRequires:  kf5-kdesu-devel
BuildRequires:  kf5-knewstuff-devel
BuildRequires:  kf5-kwallet-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  kf5-threadweaver-devel
BuildRequires:  kf5-ktexteditor-devel
BuildRequires:  kf5-kdeclarative-devel
BuildRequires:  kf5-plasma-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kdewebkit-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kglobalaccel-devel >= 5.7
BuildRequires:  kf5-networkmanager-qt-devel
BuildRequires:  kf5-kxmlrpcclient-devel

BuildRequires:  kf5-ksysguard-devel
BuildRequires:  kf5-kscreen-devel
BuildRequires:  kf5-baloo-devel

BuildRequires:  kf5-kwayland-devel
BuildRequires:  libwayland-client-devel >= 1.3.0
BuildRequires:  libwayland-server-devel >= 1.3.0

BuildRequires:  kwin-devel

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

# Optional
BuildRequires:  kf5-kactivities-devel


# HACK: Should be kf5-kactivities-runtime, but that conflicts with kactivities,
# so we requre KDE4 KActivities (it's dbus runtime dep, so no problem)
Requires:       kactivities
Requires:       kf5-kinit
Requires:       kf5-kded
Requires:       kf5-kdoctools
#Requires:       kde5-runtime
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtgraphicaleffects
Requires:       kf5-filesystem
Requires:       kf5-baloo
Requires:       kf5-kglobalaccel >= 5.7
# for translations mostly, can drop for plasma-5.3 (#1208947) -- rex
Requires:       kf5-kxmlrpcclient >= 5.8
Requires:       khotkeys

# Without the platformtheme plugins we get broken fonts
Requires:       kf5-frameworkintegration

# For krunner
Requires:       plasma-milou

# Power management
Requires:       powerdevil

# startkde
Requires:       coreutils
Requires:       dbus-x11
Requires:       socat
Requires:       xmessage
Requires:       qt5-qttools

Requires:       xorg-x11-utils
Requires:       xorg-x11-server-utils

Requires:       kde-settings-plasma
Requires:       f22-kde-theme >= 22.2

Requires:       systemd

# SysTray support for Qt 4 apps
Requires:       sni-qt

# Oxygen
Requires:       oxygen-icon-theme
Requires:       oxygen-sound-theme
Requires:       oxygen-fonts

# PolicyKit authentication agent
Requires:        polkit-kde

# Require any plasmashell (plasma-desktop provides plasmashell(desktop))
%if 0%{?bootstrap}
Provides:       plasmashell = %{version}
%else
Requires:       plasmashell >= %{version}
%endif

%description
Plasma 5 libraries and runtime components


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation and user manuals for %{name}

%description    doc
Documentation and user manuals for %{name}.


%prep
%autosetup -p1

mv startkde/startkde.cmake startkde/startkde.cmake.orig
install -m644 -p %{SOURCE11} startkde/startkde.cmake

# omit conflicts with kf5-kxmlrpcclient-5.8
rm -fv po/*/libkxmlrpcclient5.po


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

chrpath --delete %{buildroot}/%{_kf5_qtplugindir}/phonon_platform/kde.so

# Create Fedora Twenty Two look and feel package from the Breeze one
cp -r %{buildroot}/%{_datadir}/plasma/look-and-feel/{org.kde.breeze.desktop,org.fedoraproject.fedora.twenty.two}
install -m 0644 %{SOURCE12} %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.two/metadata.desktop
install -m 0644 %{SOURCE12} %{buildroot}%{_datadir}/kservices5/plasma-lookandfeel-org.fedoraproject.fedora.twenty.two.desktop
## We need to remove original background which will be replaced by Fedora one from f22-kde-theme
rm -f %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.two/contents/components/artwork/background.png
rm -f %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.two/contents/previews/{lockscreen.png,preview.png,splash.png}

# Make kcheckpass work
install -m455 -p -D %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/kde
%find_lang plasmaworkspace5 --with-qt --with-kde --all-name


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/{plasma-windowed,org.kde.klipper}.desktop


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f plasmaworkspace5.lang
%{_kf5_bindir}/*
%{_kf5_libdir}/*.so.*
%{_kf5_libdir}/libkdeinit5_*.so
%{_kf5_qtplugindir}/plasma/dataengine/*.so
%{_kf5_qtplugindir}/plasma/packagestructure/*.so
%{_kf5_qtplugindir}/*.so
%{_kf5_qtplugindir}/phonon_platform/kde.so
%{_kf5_qtplugindir}/kpackage/packagestructure/*.so
%{_kf5_qmldir}/org/kde/*
%{_libexecdir}/*
%{_kf5_datadir}/ksmserver
%{_kf5_datadir}/ksplash
%{_kf5_datadir}/plasma/plasmoids
%{_kf5_datadir}/plasma/services
%{_kf5_datadir}/plasma/shareprovider
%{_kf5_datadir}/plasma/wallpapers
%{_kf5_datadir}/plasma/look-and-feel
%{_kf5_datadir}/plasma/kcms
%{_kf5_datadir}/solid
%{_kf5_datadir}/kstyle
%{_kf5_datadir}/drkonqi/debuggers/external/*
%{_kf5_datadir}/drkonqi/debuggers/internal/*
%{_kf5_datadir}/drkonqi/mappings
%{_kf5_datadir}/drkonqi/pics/*.png
%{_kf5_datadir}/kconf_update/*
%{_sysconfdir}/xdg/*.knsrc
%{_sysconfdir}/xdg/taskmanagerrulesrc
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/desktop-directories/*.directory
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/interfaces/*.xml
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/*.protocol
%{_kf5_datadir}/kservices5/kded/*.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/knotifications5/*.notifyrc
%{_kf5_datadir}/config.kcfg/*
%{_datadir}/applications/*.desktop
%{_datadir}/sddm/themes/breeze
%{_datadir}/xsessions/plasma.desktop

# PAM
%config %{_sysconfdir}/pam.d/kde

%files doc
%{_datadir}/doc/HTML/*/*

%files devel
%{_libdir}/libweather_ion.so
%{_libdir}/libtaskmanager.so
%{_libdir}/libplasma-geolocation-interface.so
%{_libdir}/libkworkspace5.so
%{_includedir}/*
%{_libdir}/cmake/KRunnerAppDBusInterface
%{_libdir}/cmake/KSMServerDBusInterface
%{_libdir}/cmake/LibKWorkspace
%{_libdir}/cmake/LibTaskManager
%{_libdir}/cmake/ScreenSaverDBusInterface

# TODO split to subpackages
# - KCM (?)
# - plasmoids
# - icons
# - individual tools


%changelog
* Tue May 19 2015 Jan Grulich <jgrulich@redhat.com> - 5.3.0-6
- copy Breeze look-and-feel package also as Fedora Twenty Two look-and-feel package

* Mon May 18 2015 Jan Grulich <jgrulich@redhat.com> - 5.3.0-5
- set default look and feel theme to Fedora Twenty Two

* Tue May 05 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-4
- backport patch form kde-workspace to add Konsole into shell context menu
- re-enable fix-update-scripts.patch

* Wed Apr 29 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-3
- Disable bootstrap

* Wed Apr 29 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-2
- Requires plasmashell (virtual provides for packages that provide Plasma shells, like plasma-desktop)

* Mon Apr 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- Plasma 5.3.0

* Wed Apr 22 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.95-1
- Plasma 5.2.95

* Wed Apr 15 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.2-6
- Requires: kde-settings-plasma (#1197709)

* Sat Apr 04 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.2-5
- conflicts with kf5-kxmlrpcclient (#1208947)

* Tue Mar 31 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.2-4
- Requires: khotkeys (#1207079)

* Mon Mar 30 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.2-3
- backport fix for update scripts

* Wed Mar 25 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.2-2
- Lockscreen: Password field does not have focus (kde#344823)

* Fri Mar 20 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.2-1
- Plasma 5.2.2

* Mon Mar 16 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.2.1-6
- revert Requires: plasma-desktop (dep should be the other way around)
- drop Obsoletes: kde-workspace (leave for plasma-desktop)
- Requires: polkit-kde

* Sun Mar 15 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-5
- Requires: -sddm (#1201034), +plasma-desktop

* Fri Mar 06 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-4
- rebuild (gpsd)

* Tue Mar 03 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-3
- use our own startkde.cmake

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-2
- Rebuild (GCC 5)

* Tue Feb 24 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-1
- Plasma 5.2.1

* Wed Feb 18 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.2.0-8
- (Build)Requires: kf5-kglobalaccel(-devel) >= 5.7
- drop ksyncdbusenv.patch workaround
- .spec cosmetics

* Wed Feb 11 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-7
- "Could not sync environment to dbus." (startkde) (#1191171)

* Mon Feb 09 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-6
- Revert the previous change

* Mon Feb 09 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-5
- Provides/Obsoletes: kdeclassic-cursor-theme

* Sun Feb 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-4
- Requires: powerdevil, oxygen-sound-theme

* Thu Jan 29 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-3
- Requires: plasma-milou (for krunner)

* Thu Jan 29 2015 Dan Horák <dan[at]danny.cz> - 5.2.0-2
- no FireWire on s390(x)

* Mon Jan 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- Plasma 5.2.0

* Wed Jan 14 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.95-3.beta
- Requires: kf5-frameworkintegration (provides platformtheme plugin)

* Wed Jan 14 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.95-2.beta
- BR: kf5-kscreen-devel (renamed)

* Tue Jan 13 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.95-1.beta
- Plasma 5.1.95 Beta

* Mon Jan 12 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.2-5
- Add upstream patch to make ksyncdbusenv work with dbus-1.8.14

* Fri Jan 09 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.2-4
- Requires: qt5-qttools (for dbus-qt5)

* Wed Jan 07 2015 Jan Grulich <jgrulich@redhat.com> - 5.1.2-3
- Omit "5" from pkg summary
  Drop config macro for files installed to /etc/xdg
  Move /usr/share/dbus-1/interfaces/*.xml stuff to main package
  Validate .desktop files
  look for qdbus-qt5 in startkde instead of qdbus

* Mon Jan 05 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.2-2
- add upstream patch to fix black screen on start

* Wed Dec 17 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.2-1
- Plasma 5.1.2

* Fri Nov 28 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.1-2
- Apply upstream patch to build against new version of KScreen

* Fri Nov 07 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.1-1
- Plasma 5.1.1

* Tue Oct 14 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0.1-1
- Plasma 5.1.0.1

* Thu Oct 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- Plasma 5.1.0

* Tue Sep 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.2-1
- Plasma 5.0.2

* Tue Sep 02 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.1-3
- Make sure we get oxygen-icon-theme and oxyge-icons installed

* Fri Aug 29 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.1-2
- Add upstream patch to fix generated path in plasma.desktop

* Sun Aug 10 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.1-1
- Plasma 5.0.1

* Wed Aug 06 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-7
- Add more Obsoletes to make upgrade from KDE 4 smooth
- Add sni-qt to Requires so that Qt 4 apps are working with Plasma 5 systray
- Requires kde-settings

* Thu Jul 24 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-4
- Add patch to fix build-time generated paths

* Thu Jul 24 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-3
- Use relative BIN_INSTALL_DIR so that built-in paths are correctly generated

* Thu Jul 24 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-2
- Fix /usr//usr/ in generated files

* Wed Jul 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- Plasma 5.0.0

* Tue May 20 2014 Daniel Vrátil <dvratil@redhat.com> - 4.96.0-6.20140519gita85f5bc
- Add LIBEXEC_PATH to kde5 profile to fix drkonqi lookup
- Fix install 

* Mon May 19 2014 Daniel Vrátil <dvratil@redhat.com> - 4.96.0-3.20140519gita85f5bc
- Update to latest git snapshot
- Add PAM file
- Add profile.d entry

* Fri Apr 25 2014 Daniel Vrátil <dvratil@redhat.com> - 4.95.0-1.20140425git7c97c92
- Initial version of kde5-plasma-workspace
