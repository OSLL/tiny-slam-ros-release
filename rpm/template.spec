Name:           ros-jade-tiny-slam
Version:        0.1.2
Release:        3%{?dist}
Summary:        ROS tiny_slam package

Group:          Development/Libraries
License:        MIT
URL:            http://wiki.ros.org/tiny_slam
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-message-filters
Requires:       ros-jade-rosbag-storage
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-tf
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-rosbag-storage
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-tf

%description
TinySLAM ROS implementation

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Aug 08 2016 OSLL <ros@osll.ru> - 0.1.2-3
- Autogenerated by Bloom

* Fri Aug 05 2016 OSLL <ros@osll.ru> - 0.1.2-2
- Autogenerated by Bloom

* Fri Jul 15 2016 OSLL <ros@osll.ru> - 0.1.2-1
- Autogenerated by Bloom

* Fri Jul 15 2016 OSLL <ros@osll.ru> - 0.1.2-0
- Autogenerated by Bloom

