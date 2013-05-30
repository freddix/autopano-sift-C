Summary:	SIFT Feature Detection implementation
Name:		autopano-sift-C
Version:	2.5.1
Release:	6
License:	GPL v2, but SIFT algorithm may require license in some countries
Group:		Applications/Graphics
Source0:	http://heanet.dl.sourceforge.net/hugin/%{name}-%{version}.tar.gz
# Source0-md5:	b9bade07e8c4f2ea383c22a082c260e0
Patch0:		%{name}-link.patch
URL:		http://wiki.panotools.org/Autopano-sift-C
BuildRequires:	cmake
BuildRequires:	libjpeg-devel
BuildRequires:	libpano13-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SIFT algorithm provides the capability to identify key feature
points within arbitrary images. It further extracts highly distinct
information for each such point and allows to characterize the point
invariant to a number of modifications to the image. It is invariant
to contrast/brightness changes, to rotation, scaling and partially
invariant to other kinds of transformations. The algorithm can be
flexibly used to create input data for image matching, object
identification and other computer vision related algorithms.

autopano-sift-C is a C port of the C# software autopano-sift. It is
somewhat faster and doesn't require a C# runtime. Additionally,
autopano-sift-C has experimental modifications to perform feature
identification in conformal image space, this helps with wide angle or
fisheye Projection photographs.

%prep
%setup -q
%patch0 -p1

# don't override optflags with cmake-predefined values
sed -i 's/NOT CMAKE_BUILD_TYPE/GFY/' CMakeLists.txt

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# resolve conflict with autopano-sift
mv $RPM_BUILD_ROOT%{_mandir}/man1/autopano{,-c}.1
mv $RPM_BUILD_ROOT%{_mandir}/man1/generatekeys{,-c}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.1ST
%attr(755,root,root) %{_bindir}/autopano
%attr(755,root,root) %{_bindir}/autopano-c-complete.sh
%attr(755,root,root) %{_bindir}/autopano-sift-c
%attr(755,root,root) %{_bindir}/generatekeys
%{_mandir}/man1/autopano-c.1*
%{_mandir}/man1/autopano-c-complete.1*
%{_mandir}/man1/generatekeys-c.1*
%{_mandir}/man7/autopano-sift-c.7*

