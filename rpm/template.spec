Name:           ros-indigo-rocon-gateway-graph
Version:        0.7.5
Release:        0%{?dist}
Summary:        ROS rocon_gateway_graph package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rocon_gateway_graph
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-indigo-python-qt-binding
Requires:       ros-indigo-qt-dotgraph
Requires:       ros-indigo-qt-gui-py-common
Requires:       ros-indigo-rocon-gateway
Requires:       ros-indigo-rocon-gateway-utils
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rosservice
Requires:       ros-indigo-rostopic
Requires:       ros-indigo-rqt-gui
Requires:       ros-indigo-rqt-gui-py
BuildRequires:  ros-indigo-catkin

%description
An rqt plugin that displays the gateway graph across multiple ros masters from
the perspective of the master executing the plugin.

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

