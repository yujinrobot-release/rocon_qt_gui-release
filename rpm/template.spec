Name:           ros-indigo-concert-qt-make-a-map
Version:        0.7.11
Release:        0%{?dist}
Summary:        ROS concert_qt_make_a_map package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/concert_qt_teleop
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-indigo-qt-gui-py-common
Requires:       ros-indigo-rocon-console
Requires:       ros-indigo-rocon-qt-library
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin

%description
An rqt plugin for SLAM using concert robots

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
* Thu Jul 09 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.7.11-0
- Autogenerated by Bloom

* Mon Apr 27 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.7.10-0
- Autogenerated by Bloom

* Mon Mar 30 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.7.9-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.7.8-0
- Autogenerated by Bloom

* Mon Mar 02 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.7.7-0
- Autogenerated by Bloom

* Sat Feb 28 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.7.6-0
- Autogenerated by Bloom

* Mon Feb 09 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.7.5-0
- Autogenerated by Bloom

* Tue Dec 30 2014 Jihoon Lee <jihoonlee.in@gmail.com> - 0.7.4-0
- Autogenerated by Bloom

* Mon Dec 29 2014 Jihoon Lee <jihoonlee.in@gmail.com> - 0.7.3-0
- Autogenerated by Bloom

* Sat Nov 29 2014 Jihoon Lee <jihoonlee.in@gmail.com> - 0.7.2-0
- Autogenerated by Bloom

