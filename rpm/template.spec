Name:           ros-indigo-rocon-qt-gui
Version:        0.7.6
Release:        0%{?dist}
Summary:        ROS rocon_qt_gui package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/rocon_qt_gui
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-concert-admin-app
Requires:       ros-indigo-concert-conductor-graph
Requires:       ros-indigo-concert-qt-make-a-map
Requires:       ros-indigo-concert-qt-map-annotation
Requires:       ros-indigo-concert-qt-service-info
Requires:       ros-indigo-concert-qt-teleop
Requires:       ros-indigo-rocon-gateway-graph
Requires:       ros-indigo-rocon-qt-app-manager
Requires:       ros-indigo-rocon-qt-library
Requires:       ros-indigo-rocon-qt-listener
Requires:       ros-indigo-rocon-qt-master-info
Requires:       ros-indigo-rocon-qt-teleop
Requires:       ros-indigo-rocon-remocon
BuildRequires:  ros-indigo-catkin

%description
Qt gui applications for interacting with the rocon framework.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Feb 28 2015 Daniel Stonier <d.stonier@gmail.com> - 0.7.6-0
- Autogenerated by Bloom

* Mon Feb 09 2015 Daniel Stonier <d.stonier@gmail.com> - 0.7.5-0
- Autogenerated by Bloom

* Tue Dec 30 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.4-0
- Autogenerated by Bloom

* Mon Dec 29 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.3-0
- Autogenerated by Bloom

* Sat Nov 29 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.2-0
- Autogenerated by Bloom

* Tue Aug 26 2014 Daniel Stonier <d.stonier@gmail.com> - 0.7.0-0
- Autogenerated by Bloom

