# Define (as 1) to enable bootstrap when building plasma-workspace on a new
# repo or arch where there's no package that would provide plasmashell
#define bootstrap 1

%global kf5_version 5.25.0

Name:    plasma-workspace
Summary: Plasma workspace, applications and applets
Version: 5.7.4
Release: 2%{?dist}

License: GPLv2+
URL:     https://quickgit.kde.org/?p=%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

%global majmin_ver %(echo %{version} | cut -d. -f1,2)

# This goes to PAM
# TODO: this should arguably be in kde-settings with the other pam-related configs
Source10:       kde
# Desktop file for Fedora Twenty Two/Three look-and-feel package
Source12:       twenty.two.desktop
Source13:       twenty.three.desktop

## downstream Patches
Patch10:        plasma-workspace-5.6.1-konsole-in-contextmenu.patch
Patch11:        plasma-workspace-5.3.0-set-fedora-default-look-and-feel.patch
# remove stuff we don't want or need, plus a minor bit of customization --rex
Patch12:        startkde.patch
Patch13:        startplasmacompositor.patch
# revert (semi) regresssion wrt systray icon sizes, http://bugs.kde.org/365570
Patch14:        plasma-workspace-5.7.4-systray_iconSizes.patch
# default to folderview (instead of desktop) containment, see also
# https://mail.kde.org/pipermail/distributions/2016-July/000133.html
# and example,
# https://github.com/notmart/artwork-lnf-netrunner-core/blob/master/usr/share/plasma/look-and-feel/org.kde.netrunner-core.desktop/contents/defaults
Patch15:        plasma-workspace-5.7.3-folderview_layout.patch

## upstreamable Patches
# (yum) debuginfo-install improvements
Patch1:         kde-runtime-4.9.0-installdbgsymbols.patch
# dnf debuginfo-install
Patch2:         plasma-workspace-5.6.4-installdbgsymbols.patch

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
# can remove when kf5-ki18n-5.24.0-2 lands
BuildRequires:  python
BuildRequires:  boost-devel
BuildRequires:  libusb-devel
BuildRequires:  libbsd-devel
BuildRequires:  pam-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  pciutils-devel
%ifnarch s390 s390x
BuildRequires:  libraw1394-devel
%endif
BuildRequires:  gpsd-devel
BuildRequires:  libqalculate-devel
%if 0%{?fedora} > 23
%global kf5_pim 1
BuildRequires:  kf5-kholidays-devel
%endif
%if 0%{?prison}
BuildRequires:  kf5-prison-devel
%endif

BuildRequires:  qt5-qtbase-devel >= 5.6.1
## todo: document why this is needed -- rex
#BuildRequires:  qt5-qtbase-private-devel
#{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  phonon-qt5-devel

BuildRequires:  kf5-rpm-macros >= %{kf5_version}
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-baloo-devel >= %{kf5_version}
BuildRequires:  kf5-kcmutils-devel >= %{kf5_version}
BuildRequires:  kf5-kcrash-devel >= %{kf5_version}
BuildRequires:  kf5-kdeclarative-devel >= %{kf5_version}
BuildRequires:  kf5-kdelibs4support-devel >= %{kf5_version}
BuildRequires:  kf5-kdesu-devel >= %{kf5_version}
BuildRequires:  kf5-kdewebkit-devel >= %{kf5_version}
BuildRequires:  kf5-kdoctools-devel >= %{kf5_version}
BuildRequires:  kf5-kglobalaccel-devel >= %{kf5_version}
BuildRequires:  kf5-kidletime-devel >= %{kf5_version}
BuildRequires:  kf5-kinit-devel >= %{kf5_version}
BuildRequires:  kf5-kjsembed-devel >= %{kf5_version}
BuildRequires:  kf5-knewstuff-devel >= %{kf5_version}
BuildRequires:  kf5-knotifyconfig-devel >= %{kf5_version}
BuildRequires:  kf5-krunner-devel >= %{kf5_version}
BuildRequires:  kf5-ktexteditor-devel >= %{kf5_version}
BuildRequires:  kf5-ktextwidgets-devel >= %{kf5_version}
BuildRequires:  kf5-kwallet-devel >= %{kf5_version}
BuildRequires:  kf5-kxmlrpcclient-devel >= %{kf5_version}
BuildRequires:  kf5-networkmanager-qt-devel >= %{kf5_version}
BuildRequires:  kf5-plasma-devel >= %{kf5_version}
BuildRequires:  kf5-threadweaver-devel >= %{kf5_version}

BuildRequires:  kf5-ksysguard-devel >= %{majmin_ver}
BuildRequires:  kf5-kwayland-devel >= %{kf5_version}
BuildRequires:  libwayland-client-devel >= 1.3.0
BuildRequires:  libwayland-server-devel >= 1.3.0
BuildRequires:  libkscreen-qt5-devel >= %{majmin_ver}
BuildRequires:  kscreenlocker-devel >= %{majmin_ver}

BuildRequires:  kwin-devel >= %{majmin_ver}

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

# Optional
BuildRequires:  kf5-kactivities-devel

# when kded_desktopnotifier.so moved here
Conflicts:      kio-extras < 5.4.0

%if 0%{?fedora} > 21
Recommends:     %{name}-drkonqi = %{version}-%{release}
Recommends:     %{name}-geolocation = %{version}-%{release}
Suggests:       imsettings-qt
%else
Requires:       %{name}-drkonqi = %{version}-%{release}
Requires:       %{name}-geolocation = %{version}-%{release}
%endif

Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libkworkspace5%{?_isa} = %{version}-%{release}

# for libkdeinit5_*
%{?kf5_kinit_requires}
Requires:       kactivitymanagerd >= %{majmin_ver}
Requires:       khotkeys >= %{majmin_ver}
Requires:       kf5-kded
Requires:       kf5-kdoctools
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtgraphicaleffects
Requires:       kf5-filesystem
Requires:       kf5-baloo
Requires:       kf5-kglobalaccel >= 5.7
Requires:       kf5-kxmlrpcclient

# The new volume control for PulseAudio
%if 0%{?fedora} > 22
Requires:       plasma-pa
%endif

# Without the platformtheme plugins we get broken fonts
Requires:       kf5-frameworkintegration

# For krunner
Requires:       plasma-milou >= %{majmin_ver}

# Power management
Requires:       powerdevil >= %{majmin_ver}

# startkde
Requires:       coreutils
Requires:       dbus-x11
Requires:       socat
Requires:       xmessage
Requires:       qt5-qttools

Requires:       xorg-x11-utils
Requires:       xorg-x11-server-utils

Requires:       kde-settings-plasma

# Default look-and-feel theme
%if 0%{?fedora} > 21
Provides:       f22-kde-theme-core = %{version}-%{release}
%endif
%if 0%{?fedora} > 22
Provides:       f23-kde-theme-core = %{version}-%{release}
%endif
%if 0%{?fedora} == 22
Requires:       f22-kde-theme >= 22.2
%global default_lookandfeel org.fedoraproject.fedora.twenty.two
%endif
%if 0%{?fedora} == 23
Requires:       f23-kde-theme
%global default_lookandfeel org.fedoraproject.fedora.twenty.three
%endif
%if 0%{?fedora} > 23
Requires:       f24-kde-theme-core
%global         f24_kde_theme_core 1
%global default_lookandfeel org.fedoraproject.fedora.twenty.four
%endif
%if ! 0%{?default_lookandfeel:1}
Requires:       desktop-backgrounds-compat
%endif

Requires:       systemd

%if 0%{?fedora} < 23
# SysTray support for Qt 4 apps
Requires:       sni-qt%{?_isa}

# kde(4) platform plugin
Requires:       kde-platform-plugin%{?_isa}
%endif

# Oxygen
# TODO: review if oxygen-fonts, oxygen-icon-theme are still needed (I suspect not) -- rex
Requires:       oxygen-icon-theme
Requires:       oxygen-sound-theme >= %{majmin_ver}
Requires:       oxygen-fonts

# PolicyKit authentication agent
Requires:        polkit-kde >= %{majmin_ver}

# Require any plasmashell (plasma-desktop provides plasmashell(desktop))
%if 0%{?bootstrap}
Provides:       plasmashell = %{version}
%else
# Note: We should require >= %%{version}, but that creates a circular dependency
# at build time of plasma-desktop, because it provides the needed dependency, but
# also needs plasma-workspace to build. So for now the dependency is unversioned.
Requires:       plasmashell >= %{majmin_ver}
%endif

# when -common, libkworkspace5 was split out
Obsoletes:      plasma-workspace < 5.4.2-2

# deprecate/replace kde-runtime-kuiserver, http://bugzilla.redhat.com/1249157
Obsoletes:      kde-runtime-kuiserver < 1:15.08.2
Provides:       kuiserver = %{version}-%{release}

%if 0%{?fedora} && 0%{?fedora} < 23
# (hopefully temporary) workaround for dnf Obsoletes bug
# https://bugzilla.redhat.com/show_bug.cgi?id=1260394
Requires: sddm-breeze = %{version}-%{release}
%endif

# upgrade path, when sddm-breeze was split out
Obsoletes: plasma-workspace < 5.3.2-8

# digitalclock applet
%if ! 0%{?bootstrap}
BuildRequires: pkgconfig(iso-codes)
%endif
Requires: iso-codes

%description
Plasma 5 libraries and runtime components

%package common
Summary: Common files for %{name}
%description common
%{name}.

%package -n libkworkspace5
Summary: Runtime libkworkspace5 library
# when spilt occurred
Obsoletes: plasma-workspace < 5.4.2-2
Requires:  %{name}-common = %{version}-%{release}
%description -n libkworkspace5
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
# when split out
Obsoletes: plasma-workspace < 5.4.2-2
## omit dep on main pkg for now, means we can avoid pulling in a
## huge amount of deps (including kde4) into buildroot -- rex
#Requires:  %%{name}%%{?_isa} = %%{version}-%%{release}
Requires:  %{name}-common = %{version}-%{release}
%description libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libkworkspace5%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation and user manuals for %{name}
License:        GFDL
# switch to noarch
Obsoletes:      plasma-workspace-doc < 5.3.1-2
Requires:       %{name}-common = %{version}-%{release}
BuildArch: noarch
%description    doc
Documentation and user manuals for %{name}.

%package drkonqi
Summary: DrKonqi crash handler for KF5/Plasma5
# when split out
Obsoletes: plasma-workspace < 5.4.2-2
Requires: %{name} = %{version}-%{release}
Requires: %{name}-common = %{version}-%{release}
%if 0%{?fedora} > 23
Requires: dnf-command(debuginfo-install)
%else
# owner of debuginfo-install
Requires: yum-utils
%endif
## not needed, since we already ensure other dependencies (debuginfo-install, konsole)
#Requires: kdialog
Requires: konsole5
Requires: polkit
# owner of setsebool
Requires(post): policycoreutils
%description drkonqi
%{summary}.

%package geolocation
Summary: Plasma5 geolocation components
# when split out
Obsoletes: plasma-workspace < 5.4.2-2
Requires: %{name}-geolocation-libs%{?_isa} = %{version}-%{release}
%description geolocation
%{summary}.

%package geolocation-libs
Summary: Plasma5 geolocation runtime libraries
Requires: %{name}-common = %{version}-%{release}
Requires: %{name}-geolocation = %{version}-%{release}
%description geolocation-libs
%{summary}.

%package -n sddm-breeze
Summary:        SDDM breeze theme
# upgrade path, when sddm-breeze was split out
Obsoletes: plasma-workspace < 5.3.2-8
Requires:       kf5-plasma
# QML imports:
# org.kde.plasma.workspace.components
# org.kde.plasma.workspace.keyboardlayout
Requires:       %{name} = %{version}-%{release}
# /usr/share/backgrounds/default.png
Requires:       desktop-backgrounds-compat
BuildArch: noarch
%description -n sddm-breeze
%{summary}.

%package wayland
Summary:        Wayland support for Plasma
Requires:       %{name} = %{version}-%{release}
Requires:       kwin-wayland >= %{version}
Requires:       kwayland-integration%{?_isa} >= %{majmin_ver}
Requires:       xorg-x11-server-Xwayland
Requires:       qt5-qtwayland%{?_isa}
# startplasmacompositor deps
Requires:       qt5-qttools
%description wayland
%{summary}.

%package -n f24-kde-theme-core
Summary:  Core and Inherited theme elements
Requires: %{name} = %{version}-%{release}
Requires: f24-kde-theme
%description -n f24-kde-theme-core
%{summary}.


%prep
%setup -q

## upstream patches
%if 0%{?fedora} > 23
# dnf debuginfo-install
%patch2 -p1 -b .installdgbsymbols
%else
# (yum) debuginfo-install
%patch1 -p1 -b .installdbgsymbols
%endif
%patch10 -p1 -b .konsole-in-contextmenu
%if 0%{?default_lookandfeel:1}
%patch11 -p1 -b .set-fedora-default-look-and-feel
sed -i -e "s|@DEFAULT_LOOKANDFEEL@|%{?default_lookandfeel}%{!?default_lookandfeel:org.kde.breeze.desktop}|g" \
  shell/packageplugins/lookandfeel/lookandfeel.cpp
%endif
%patch12 -p1 -b .startkde
%patch13 -p1 -b .startplasmacompositor
%patch14 -p1
%patch15 -p1

# highlight the use of wayland
sed -i.plasmawayland -e "s|Plasma|Plasma (Wayland)|g" plasmawayland.desktop.cmake


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

chrpath --delete %{buildroot}%{_kf5_qtplugindir}/phonon_platform/kde.so

#if 0%{?fedora} > 21
%if 0
# Create Fedora Twenty Two look and feel package from the Breeze one
cp -r %{buildroot}%{_datadir}/plasma/look-and-feel/{org.kde.breeze.desktop,org.fedoraproject.fedora.twenty.two}
install -m 0644 %{SOURCE12} %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.two/metadata.desktop
install -m 0644 %{SOURCE12} %{buildroot}%{_datadir}/kservices5/plasma-lookandfeel-org.fedoraproject.fedora.twenty.two.desktop
## We need to remove original background which will be replaced by Fedora one from f22-kde-theme
rm -fv %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.two/contents/components/artwork/background.png
rm -fv %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.two/contents/previews/{lockscreen.png,preview.png,splash.png}
%endif

%if 0%{?fedora} > 22
# Create Fedora Twenty Three look and feel package from the Breeze one
cp -r %{buildroot}%{_datadir}/plasma/look-and-feel/{org.kde.breeze.desktop,org.fedoraproject.fedora.twenty.three}
install -m 0644 %{SOURCE13} %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.three/metadata.desktop
install -m 0644 %{SOURCE13} %{buildroot}%{_datadir}/kservices5/plasma-lookandfeel-org.fedoraproject.fedora.twenty.three.desktop
## We need to remove original background which will be replaced by Fedora one from f23-kde-theme
rm -fv %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.three/contents/components/artwork/background.png
rm -fv %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.three/contents/previews/{lockscreen.png,preview.png,splash.png}
%endif

%if 0%{?f24_kde_theme_core}
# Create Fedora Twenty Three look and feel package from the Breeze one
cp -r %{buildroot}%{_datadir}/plasma/look-and-feel/{org.kde.breeze.desktop,org.fedoraproject.fedora.twenty.four}
# remove items that will be provided by f24-kde-theme
rm -fv %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.four/metadata.desktop
rm -fv %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.four/contents/components/artwork/background.png
rm -fv %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.four/contents/previews/{lockscreen.png,preview.png,splash.png}
%endif

# make fedora-breeze sddm theme variant.  FIXME/TODO: corrected preview screenshot
cp -alf %{buildroot}%{_datadir}/sddm/themes/breeze/ \
        %{buildroot}%{_datadir}/sddm/themes/01-breeze-fedora
ln -sf  %{_datadir}/backgrounds/default.png \
        %{buildroot}%{_datadir}/sddm/themes/01-breeze-fedora/components/artwork/background.png

# Make kcheckpass work
install -m644 -p -D %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/kde

# installdbgsymbols script
install -p -D -m755 drkonqi/doc/examples/installdbgsymbols_fedora.sh \
  %{buildroot}%{_libexecdir}/installdbgsymbols.sh

# revert klipper autostart: https://quickgit.kde.org/?p=plasma-workspace.git&a=commit&h=fc439f63e122cd6d668fb75cf71a5b361da0b10d
# https://bugzilla.redhat.com/show_bug.cgi?id=1361765
# https://bugs.kde.org/show_bug.cgi?id=366277
sed -i -e 's|^NotShowIn=KDE;|OnlyShowIn=KDE;|' \
  %{buildroot}%{_sysconfdir}/xdg/autostart/org.kde.klipper.desktop


%find_lang all --with-qt --all-name
grep drkonqi.mo all.lang > drkonqi.lang
grep libkworkspace.mo all.lang > libkworkspace5.lang
grep libtaskmanager.mo all.lang > libs.lang
# any translations not used elsewhere, include in main pkg
cat *.lang | sort | uniq -u > %{name}.lang


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/{plasma-windowed,org.kde.klipper}.desktop


%files common
%license COPYING
%license COPYING.LIB

%files -f %{name}.lang
%{_kf5_bindir}/kcheckrunning
%{_kf5_bindir}/kcminit
%{_kf5_bindir}/kcminit_startup
%{_kf5_bindir}/kdostartupconfig5
%{_kf5_bindir}/klipper
%{_kf5_bindir}/krunner
%{_kf5_bindir}/ksmserver
%{_kf5_bindir}/ksplashqml
%{_kf5_bindir}/kstartupconfig5
%{_kf5_bindir}/kuiserver5
%{_kf5_bindir}/plasmashell
%{_kf5_bindir}/plasmawindowed
%{_kf5_bindir}/startkde
%{_kf5_bindir}/systemmonitor
%{_kf5_bindir}/xembedsniproxy
%{_kf5_libdir}/libkdeinit5_*.so
%{_kf5_qmldir}/org/kde/*
%{_libexecdir}/ksyncdbusenv
%{_kf5_datadir}/ksmserver/
%{_kf5_datadir}/ksplash/
%{_kf5_datadir}/plasma/plasmoids/
%{_kf5_datadir}/plasma/services/
%{_kf5_datadir}/plasma/shareprovider/
%{_kf5_datadir}/plasma/wallpapers/
%dir %{_kf5_datadir}/plasma/look-and-feel/
%{_kf5_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/
#if 0%{?fedora} > 21
%if 0
%{_kf5_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.two/
%endif
%if 0%{?fedora} > 22
%{_kf5_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.three/
%endif
%{_kf5_datadir}/solid/
%{_kf5_datadir}/kstyle/
%{_sysconfdir}/xdg/*.knsrc
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/desktop-directories/*.directory
%{_datadir}/dbus-1/services/*.service
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/kservices5/*.protocol
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_datadir}/knotifications5/*.notifyrc
%{_kf5_datadir}/config.kcfg/*
%{_kf5_datadir}/kio_desktop/
%{_kf5_metainfodir}/*.xml
%{_datadir}/applications/org.kde.klipper.desktop
%{_datadir}/applications/plasma-windowed.desktop
%{_datadir}/xsessions/plasma.desktop
# PAM
%config(noreplace) %{_sysconfdir}/pam.d/kde
%exclude %{_kf5_datadir}/kservices5/plasma-dataengine-geolocation.desktop
%exclude %{_kf5_datadir}/kservices5/plasma-geolocation-gps.desktop
%exclude %{_kf5_datadir}/kservices5/plasma-geolocation-ip.desktop
%exclude %{_kf5_datadir}/kservicetypes5/plasma-geolocationprovider.desktop

%files doc
%license COPYING.DOC
%lang(ca) %{_docdir}/HTML/ca/klipper/
%lang(cs) %{_docdir}/HTML/cs/kcontrol/screenlocker/
%lang(en) %{_docdir}/HTML/en/klipper/
%lang(en) %{_docdir}/HTML/en/kcontrol/screenlocker/
#lang(de) %{_docdir}/HTML/de/klipper/

%post -n libkworkspace5 -p /sbin/ldconfig
%postun -n libkworkspace5 -p /sbin/ldconfig

%files -n libkworkspace5 -f libkworkspace5.lang
%{_libdir}/libkworkspace5.so.5*

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs -f libs.lang
%{_sysconfdir}/xdg/legacytaskmanagerrulesrc
%{_sysconfdir}/xdg/taskmanagerrulesrc
%{_libdir}/liblegacytaskmanager.so.5
%{_libdir}/liblegacytaskmanager.so.%{version}
%{_libdir}/libtaskmanager.so.6
%{_libdir}/libtaskmanager.so.%{version}
%{_libdir}/libweather_ion.so.7*
# multilib'able plugins
%{_kf5_qtplugindir}/plasma/applets/
%{_kf5_qtplugindir}/plasma/dataengine/
%{_kf5_qtplugindir}/plasma/packagestructure/
%if 0%{?kf5_pim}
%{_kf5_qtplugindir}/plasmacalendarplugins/
%endif
%{_kf5_qtplugindir}/*.so
%exclude %{_kf5_qtplugindir}/plasma-geolocation-gps.so
%exclude %{_kf5_qtplugindir}/plasma-geolocation-ip.so
%exclude %{_kf5_qtplugindir}/plasma/dataengine/plasma_engine_geolocation.so
%dir %{_kf5_qtplugindir}/phonon_platform/
%{_kf5_qtplugindir}/phonon_platform/kde.so
%{_kf5_qtplugindir}/kpackage/packagestructure/*.so
%{_kf5_plugindir}/kio/desktop.so
%{_kf5_plugindir}/kded/*.so

%files geolocation
%{_kf5_qtplugindir}/plasma-geolocation-gps.so
%{_kf5_qtplugindir}/plasma-geolocation-ip.so
%{_kf5_qtplugindir}/plasma/dataengine/plasma_engine_geolocation.so
%{_kf5_datadir}/kservices5/plasma-dataengine-geolocation.desktop
%{_kf5_datadir}/kservices5/plasma-geolocation-gps.desktop
%{_kf5_datadir}/kservices5/plasma-geolocation-ip.desktop
%{_kf5_datadir}/kservicetypes5/plasma-geolocationprovider.desktop

%post geolocation-libs -p /sbin/ldconfig
%postun geolocation-libs -p /sbin/ldconfig

%files geolocation-libs
%{_libdir}/libplasma-geolocation-interface.so.5*

%files devel
%{_libdir}/libweather_ion.so
%{_libdir}/liblegacytaskmanager.so
%{_libdir}/libtaskmanager.so
%{_libdir}/libplasma-geolocation-interface.so
%{_libdir}/libkworkspace5.so
%dir %{_includedir}/plasma/
%{_includedir}/plasma/weather/
%{_includedir}/kworkspace5/
%{_includedir}/plasma/geolocation/
%{_includedir}/legacytaskmanager/
%{_includedir}/taskmanager/
%{_libdir}/cmake/KRunnerAppDBusInterface/
%{_libdir}/cmake/KSMServerDBusInterface/
%{_libdir}/cmake/LibKWorkspace/
%{_libdir}/cmake/LibLegacyTaskManager/
%{_libdir}/cmake/LibTaskManager/
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/kdevappwizard/templates/ion-dataengine.tar.bz2

%post drkonqi
# make DrKonqi work by default by taming SELinux enough (suggested by dwalsh)
# if KDE_DEBUG is set, DrKonqi is disabled, so do nothing
# if it is unset (or empty), check if deny_ptrace is already disabled
# if not, disable it
if [ -z "$KDE_DEBUG" ] ; then
  if [ "`getsebool deny_ptrace 2>/dev/null`" == 'deny_ptrace --> on' ] ; then
    setsebool -P deny_ptrace off &> /dev/null || :
  fi
fi

%files drkonqi -f drkonqi.lang
%{_libexecdir}/drkonqi
%{_kf5_datadir}/drkonqi/
%{_libexecdir}/installdbgsymbols.sh

%files -n sddm-breeze
%{_datadir}/sddm/themes/breeze/
%{_datadir}/sddm/themes/01-breeze-fedora/

%files wayland
%{_kf5_bindir}/startplasmacompositor
%{_libexecdir}/startplasma
%{_datadir}/wayland-sessions/plasmawayland.desktop

%if 0%{?f24_kde_theme_core}
%files -n f24-kde-theme-core
%{_kf5_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.four/
%endif


%changelog
* Fri Sep 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.4-2
- drop support for f22 (plasma theme)

* Tue Aug 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.4-1
- 5.7.4

* Tue Aug 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.3-2
- adapt to upstream looknfeel/default-layout changes
- BR: iso-codes (technically only runtime dep, but can't hurt)

* Tue Aug 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.3-1
- 5.7.3

* Sat Jul 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.2-3
- klipper autostart: OnlyShowIn=KDE (#1361765,kde#366277)

* Mon Jul 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.2-2
- -drkonqi: -Requires: kdialog
- remove BR: qt5-qtbase-private-devel until we can properly document why it is needed

* Tue Jul 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.2-1
- 5.7.2

* Tue Jul 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-3
- BR: qt5-qtbase-private-devel

* Thu Jul 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-2
- BR: kf5-kholidays-devel
- revert recent upstream systray icon resize (kde#365570)

* Tue Jul 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-1
- 5.7.1

* Thu Jun 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.0-1
- 5.7.0

* Mon Jun 27 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.95-3
- kwaylad-integration is part of plasma, not kf5

* Sun Jun 26 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.95-2
- bump Qt5 dep

* Sat Jun 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.95-1
- 5.6.95

* Fri Jun 24 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.5-2
- Suggests: imsettings-qt (#1349743)

* Tue Jun 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.5-1
- 5.6.5

* Sun Jun 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.4-3
- -drkonqi: support 'dnf debuginfo-install' (f24+)
- -drkonqi: Requires: kdialog konsole5 dnf-command(debuginfo-install) (f24+)

* Thu May 26 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.4-2
- backport 5.6 branch fixes

* Sat May 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.4-1
- 5.6.4

* Thu May 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.3-5
- /etc/pam.d/kde is executable (#1335500)

* Sun May 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.3-4
- -libs: omit geolocation plugins

* Sat Apr 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.3-3
- own phonon_platform plugin dir
- -libs: move multilib'able plugins here

* Wed Apr 27 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.3-2
- Some processes (kuiserver) are left running after exiting KDE (#348123)

* Tue Apr 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.3-1
- 5.6.3

* Sat Apr 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.2-1
- 5.6.2

* Fri Apr 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.1-2
- de-bootstrap

* Fri Apr 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.6.1-1
- Plasma-5.6.1 (bootstrap)

* Wed Mar 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.5.5-10
- f24-kde-theme-core: fix conflict with f24-kde-theme
- f24-kde-theme-core: add dep to/from plasma-workspace
- -wayland: s/plasma-workspace/%%name/

* Wed Mar 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.5.5-9
- enable f24-kde-theme default looknfeel (f24+)

* Mon Mar 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.5.5-8
- f24-kde-theme-core subpkg (readying for f24-kde-theme)

* Mon Mar 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.5.5-7
- Provides: f23-kde-theme-core

* Mon Mar 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.5.5-6
- generic theming for f24+

* Mon Mar 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.5.5-5
- drop Requires: sddm-breeze for f23+ (workaround for bug #1261034)

* Fri Mar 11 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.5-4
- f23+: -Requires: sni-qt kde-platform-plugin (use rich/soft deps elsewhere)

* Mon Mar 07 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.5-3
- backport "Avoid blocking DBus calls in SNI startup" (kde#359611)

* Thu Mar 03 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.5-2
- Upstream respun tarball

* Wed Mar 02 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.5-1
- Plasma 5.5.5

* Mon Feb 29 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.4-6
- Requires: iso-codes (digitalclock applet)

* Mon Feb 29 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.4-5
- pull in some 5.5 branch fixes

* Mon Feb 22 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.4-4
- -wayland: Requires: xorg-x11-server-Xwayland

* Tue Feb 09 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.4-3
- backport xembedsniproxy fixes

* Thu Feb 04 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.4-2
- backport systray applets not shown workaround (kde#352055)

* Wed Jan 27 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.4-1
- Plasma 5.5.4

* Mon Jan 25 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.3-6
- pull in upstream fixes (notifications/xembedsniproxy)

* Mon Jan 11 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.3-5
- -wayland: Requires: qt5-qtools (for qdbus-qt5)

* Mon Jan 11 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.5.3-4
- startplasmacompositor.patch (#1297418)
- disable bootstrap

* Sun Jan 10 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.3-3
- drop hacked klipper/prison support (until we have kf5-prison available properly)

* Sat Jan 09 2016 Rex Dieter <rdieter@fedoraproject.org> 5.5.3-2
- pull in upstream fixes (notifications,xembedsniproxy)

* Thu Jan 07 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.3-1
- Plasma 5.5.3

* Thu Dec 31 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.5.2-2
- use %%majmin_ver for most plasma-related deps
- tighten plugin deps using %%_isa
- update URL

* Thu Dec 31 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.5.2-1
- 5.5.2

* Fri Dec 18 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.1-1
- Plasma 5.5.1

* Tue Dec 15 2015 Than Ngo <than@redhat.com> - 5.5.0-5
- enable bootstrap for secondary arch

* Mon Dec 14 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.0-4
- proper upstream fix for #356415 (review #126331)

* Sun Dec 13 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.5.0-3
- latest upstream fixes (#1291100)
- revert commit causing regression'ish kde #356415
- drop kwayland-integration from main pkg (only in -wayland subpkg)

* Sat Dec 05 2015 Daniel Vrátil <dvraitl@fedoraproject.org> - 5.5.0-2
- remove version dependency on oxygen-fonts, because it's not being released anymore

* Thu Dec 03 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.0-1
- Plasma 5.5.0

* Wed Nov 25 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.4.95-1
- Plasma 5.4.95

* Tue Nov 17 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.3-4
- Unhelpful summary/description for drkonqi packages (#1282810)

* Mon Nov 16 2015 Jan Grulich <jgrulich@redhat.com> - 5.4.3-3
- Fix changing of visibility for system tray entries
  Resolves: kdebz#355404

* Wed Nov 11 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.3-2
- refresh xembedsniproxy support (#1280457)

* Thu Nov 05 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.4.3-1
- Plasma 5.4.3

* Tue Nov 03 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.4.2-8
- make klipper/prison support f24+ only (for now)
- backport xembed-sni-proxy

* Tue Oct 20 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-7
- klipper: prison (qrcode) support

* Wed Oct 14 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-6
- rev startkde.patch drop dbus launch (kde#352251)

* Mon Oct 12 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-5
- Obsoletes: kde-runtime-kuiserver (#1249157), Provides: kuiserver

* Mon Oct 05 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-4
- startkde: don't try to source things in a subshell, don't munge XDG_DATA_DIRS needlessly

* Sun Oct 04 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.2-3
- consistently use %%{majmin_ver} macro for other plasma5-related deps

* Sat Oct 03 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.4.2-2
- .spec cosmetics, use %%license
- -common, -drkonqi, -libs, libkworkspace5 subpkgs
- -geolocation subpkg (#1222097)
- -drkonqi: include installdbgsymbols.sh

* Thu Oct 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.4.2-1
- 5.4.2

* Thu Oct 01 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-6
- try tightened plasmashell dep (loosened in plasma-desktop)

* Fri Sep 25 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-5
- relax kf5-kxmlrpcclient dep (and drop related hacks), tighten khotkeys

* Tue Sep 15 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-4
- Requires: sddm-breeze unconditionally (#1260394)

* Sat Sep 12 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-3
- tighten build deps

* Sat Sep 12 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-2
- Requires: sddm-breeze, (hopefully) temporary workaround for dnf Obsoletes bug (#1260394, f22)

* Fri Sep 11 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-1
- de-bootstrap

* Wed Sep 09 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.4.1-0.1
- 5.4.1, enable bootstrap

* Fri Sep 04 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-7
- Conflicts: kio-extras < 5.4.0

* Wed Sep 02 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-6.1
- make plasma-pa f23+ only

* Tue Sep 01 2015 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-6
- Try rebuilding against new baloo

* Wed Aug 26 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.0-5
- versioned kf5-related build deps

* Tue Aug 25 2015 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-4
- Disable bootstrap

* Tue Aug 25 2015 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-3
- Re-enable plasma-pa and kwayland-integration dependencies

* Sat Aug 22 2015 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-2
- Temporarily disable plasma-pa and kwayland-integration until the packages are reviewed

* Fri Aug 21 2015 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-1
- Plasma 5.4.0

* Thu Aug 20 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.95-4
- use patch for startkde.cmake, remove redundant prison dependency

* Thu Aug 13 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.95-1
- Plasma 5.3.95

* Tue Aug 11 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.3.2-11
- Provides: f23-kde-theme-core (and f22-kde-theme-core)
- default_lookandfeel org.fedoraproject.fedora.twenty.three (f23+)

* Thu Aug 06 2015 Rex Dieter <rdieter@fedoraproject.org> 5.3.2-10
- prep fedora.twenty.three plasma theme

* Thu Aug 06 2015 Rex Dieter <rdieter@fedoraproject.org> 5.3.2-9
- make sddm-breeze noarch (#1250204)

* Thu Aug 06 2015 Rex Dieter <rdieter@fedoraproject.org> 5.3.2-8
- sddm-breeze subpkg, userlist variant for bz #1250204

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 5.3.2-7
- Rebuilt for Boost 1.58

* Fri Jul 31 2015 Rex Dieter <rdieter@fedoraproject.org> 5.3.2-6
- Requires: kde-platform-plugin

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 5.3.2-4
- rebuild for Boost 1.58

* Thu Jul 09 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.3.2-3
- .spec cosmetics
- port selinux/drkonqi scriptlet (from kde-runtime)
- own /usr/share/drkonqi/
- %%config(noreplace) pam

* Fri Jun 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.2-2
- Make the Requires: plasmashell unversioned to break circular dependency during update

* Thu Jun 25 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.2-1
- Plasma 5.3.2

* Sat Jun 20 2015 Rex Dieter <rdieter@fedoraproject.org> 5.3.1-5
- shutdown scripts are not executed (#1234059)

* Thu Jun 18 2015 Rex Dieter <rdieter@fedoraproject.org> 5.3.1-4
- startkde.cmake: sync ScaleFactor changes, drop QT_PLUGIN_PATH munging (#1233298)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.3.1-2
- use %%{?kf5_kinit_requires}
- Requires: kf5-kactivities
- doc: make noarch, %%lang'ify

* Tue May 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.1-1
- Plasma 5.3.1

* Wed May 20 2015 Jan Grulich <jgrulich@redhat.com> - 5.3.0-8
- apply the new patch for update scripts execution

* Wed May 20 2015 Jan Grulich <jgrulich@redhat.com> - 5.3.0-7
- process update scripts after first initialization

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
