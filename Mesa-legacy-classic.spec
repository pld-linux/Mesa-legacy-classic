# TODO: is separate libGLX_mesa needed for classic DRI versions, or >=22.x is still compatible?
#
# Conditional build:
%bcond_with	sse2		# SSE2 instructions
%bcond_with	tests		# tests
#
# glapi version (glapi tables in dri drivers and libglx must be in sync);
# set to current Mesa version on ABI break, when xserver tables get regenerated
# (until they start to be somehow versioned themselves)
%define		glapi_ver		7.1.0
# other packages
%define		libdrm_ver		2.4.107
%define		dri2proto_ver		2.8
%define		glproto_ver		1.4.14
%define		zlib_ver		1.2.8
%define		libglvnd_ver		1.3.4-2
%define		llvm_ver		11.0.0
%define		gcc_ver 		6:4.8.0

%ifarch %{x86_with_sse2}
%define		with_sse2	1
%endif

Summary:	Free OpenGL implementation
Summary(pl.UTF-8):	Wolnodostępna implementacja standardu OpenGL
Name:		Mesa-legacy-classic
Version:	21.3.9
Release:	1
License:	MIT (core) and others - see license.html file
Group:		X11/Libraries
#Source0:	ftp://ftp.freedesktop.org/pub/mesa/mesa-%{version}.tar.xz
## Source0-md5:	7c61a801311fb8d2f7b3cceb7b5cf308
Source0:	https://gitlab.freedesktop.org/mesa/mesa/-/archive/mesa-%{version}/mesa-mesa-%{version}.tar.bz2
# Source0-md5:	627bdfbc3a58fa4b004f2bb49228ebee
URL:		https://www.mesa3d.org/
%{?with_gallium_zink:BuildRequires:	Vulkan-Loader-devel}
BuildRequires:	bison > 2.3
BuildRequires:	elfutils-devel
BuildRequires:	expat-devel >= 1.95
BuildRequires:	flex
BuildRequires:	gcc >= %{gcc_ver}
BuildRequires:	libdrm-devel >= %{libdrm_ver}
BuildRequires:	libglvnd-devel >= %{libglvnd_ver}
BuildRequires:	libselinux-devel
BuildRequires:	libstdc++-devel >= %{gcc_ver}
BuildRequires:	libunwind-devel
BuildRequires:	libxcb-devel >= 1.13
BuildRequires:	meson >= 0.52
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(talloc) >= 2.0.1
BuildRequires:	pkgconfig(xcb-dri2) >= 1.8
BuildRequires:	pkgconfig(xcb-dri3) >= 1.13
BuildRequires:	pkgconfig(xcb-glx) >= 1.8.1
BuildRequires:	pkgconfig(xcb-present) >= 1.13
BuildRequires:	pkgconfig(xcb-randr) >= 1.12
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-Mako >= 0.8.0
BuildRequires:	rpmbuild(macros) >= 2.007
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel >= 1.0.5
BuildRequires:	xorg-lib-libXfixes-devel >= 2.0
BuildRequires:	xorg-lib-libXrandr-devel >= 1.3
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-lib-libxshmfence-devel >= 1.1
BuildRequires:	xorg-proto-dri2proto-devel >= %{dri2proto_ver}
BuildRequires:	xorg-proto-glproto-devel >= %{glproto_ver}
BuildRequires:	zlib-devel >= %{zlib_ver}
BuildRequires:	zstd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#  _glapi_tls_Dispatch is defined in libglapi, but it's some kind of symbol ldd -r doesn't notice(?)
%define		skip_post_check_so	libGL.so.1.* libGLX_mesa.so.0.*

%description
Mesa is a 3-D graphics library with an API which is very similar to
that of OpenGL(R). To the extent that Mesa utilizes the OpenGL command
syntax or state machine, it is being used with authorization from
Silicon Graphics, Inc. However, the author does not possess an OpenGL
license from SGI, and makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with SGI.

%description -l pl.UTF-8
Mesa jest biblioteką grafiki 3D z API bardzo podobnym do OpenGL(R). Do
tego stopnia, że Mesa używa składni i automatu OpenGL jest używana z
autoryzacją Silicon Graphics, Inc. Jednak autor nie posiada licencji
OpenGL od SGI i nie twierdzi, że Mesa jest kompatybilnym zamiennikiem
OpenGL ani powiązana z SGI.

%package libGL
Summary:	Free Mesa3D implementation of libGL OpenGL library
Summary(pl.UTF-8):	Wolnodostępna implementacja Mesa3D biblioteki libGL ze standardu OpenGL
License:	MIT
Group:		X11/Libraries
Requires:	%{name}-libglapi = %{version}-%{release}
Requires:	libdrm >= %{libdrm_ver}
Requires:	libxcb >= 1.13
Requires:	libglvnd-libGL >= %{libglvnd_ver}
Provides:	OpenGL = 4.6
Provides:	OpenGL-GLX = 1.4
Obsoletes:	Mesa < 6.4-2
Obsoletes:	Mesa-dri < 6.4.1-3
Obsoletes:	Mesa-dri-core < 10.0.0
Obsoletes:	X11-OpenGL-libGL < 1:7.0.0
Obsoletes:	XFree86-OpenGL-libGL < 1:7.0.0

%description libGL
Mesa is a 3-D graphics library with an API which is very similar to
that of OpenGL(R). To the extent that Mesa utilizes the OpenGL command
syntax or state machine, it is being used with authorization from
Silicon Graphics, Inc. However, the author does not possess an OpenGL
license from SGI, and makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with SGI.

This package contains libGL which implements OpenGL 4.6 and GLX 1.4
specifications. It uses DRI for rendering.

%description libGL -l pl.UTF-8
Mesa jest biblioteką grafiki 3D z API bardzo podobnym do OpenGL(R). Do
tego stopnia, że Mesa używa składni i automatu OpenGL jest używana z
autoryzacją Silicon Graphics, Inc. Jednak autor nie posiada licencji
OpenGL od SGI i nie twierdzi, że Mesa jest kompatybilnym zamiennikiem
OpenGL ani powiązana z SGI.

Ten pakiet zawiera libGL implementującą specyfikacje OpenGL 4.6 oraz
GLX 1.4. Używa DRI do renderowania.

%package libGL-devel
Summary:	Header files for Mesa3D libGL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libGL z projektu Mesa3D
License:	MIT
Group:		X11/Development/Libraries
Requires:	libglvnd-libGL-devel >= %{libglvnd_ver}
Suggests:	OpenGL-doc-man
Obsoletes:	Mesa-devel < 6.4-2
Obsoletes:	Mesa-libGL-static < 18.3
Obsoletes:	Mesa-static < 6.4-2
Obsoletes:	X11-OpenGL-devel < 1:7.0.0
Obsoletes:	X11-OpenGL-devel-base < 1:7.0.0
Obsoletes:	X11-OpenGL-static < 1:7.0.0
Obsoletes:	XFree86-OpenGL-devel < 1:7.0.0
Obsoletes:	XFree86-OpenGL-devel-base < 1:7.0.0
Obsoletes:	XFree86-OpenGL-static < 1:7.0.0

%description libGL-devel
Header files for Mesa3D libGL library.

%description libGL-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libGL z projektu Mesa3D.

%package libglapi
Summary:	Mesa GL API shared library
Summary(pl.UTF-8):	Biblioteka współdzielona Mesa GL API
Group:		Libraries
Conflicts:	Mesa-libEGL < 8.0.1-2

%description libglapi
Mesa GL API shared library, common for various APIs (EGL, GL, GLES).

%description libglapi -l pl.UTF-8
Biblioteka współdzielona Mesa GL API, wspólna dla różnych API (EGL,
GL, GLES).

%package khrplatform-devel
Summary:	Khronos platform header file
Summary(pl.UTF-8):	Plik nagłówkowy platformy Khronos
Group:		Development/Libraries
Provides:	khrplatform-devel
Conflicts:	Mesa-libEGL-devel < 8.0.1-2

%description khrplatform-devel
Khronos platform header file.

%description khrplatform-devel -l pl.UTF-8
Plik nagłówkowy platformy Khronos.

%package dri-devel
Summary:	Direct Rendering Infrastructure interface header file
Summary(pl.UTF-8):	Plik nagłówkowy interfejsu DRI (Direct Rendering Infrastructure)
Group:		Development/Libraries
Requires:	libdrm-devel >= %{libdrm_ver}
# <GL/gl.h>
Requires:	libglvnd-libGL-devel >= %{libglvnd_ver}
Conflicts:	Mesa-libGL-devel < 21.1.0-2

%description dri-devel
Direct Rendering Infrastructure interface header file.

%description dri-devel -l pl.UTF-8
Plik nagłówkowy interfejsu DRI (Direct Rendering Infrastructure).

%package -n Mesa-dri-driver-ati-radeon-R100
Summary:	X.org DRI driver for ATI R100 card family
Summary(pl.UTF-8):	Sterownik X.org DRI dla rodziny kart ATI R100
License:	MIT
Group:		X11/Libraries
Requires:	zlib >= %{zlib_ver}
Suggests:	xorg-driver-video-amdgpu
Suggests:	xorg-driver-video-ati
Obsoletes:	X11-driver-radeon-dri < 1:7.0.0
Conflicts:	xorg-xserver-libglx(glapi) > %{glapi_ver}
Conflicts:	xorg-xserver-libglx(glapi) < %{glapi_ver}

%description -n Mesa-dri-driver-ati-radeon-R100
X.org DRI driver for ATI R100 card family (Radeon 7000-7500). It
supports R100, RV100, RS100, RV200, RS200, RS250.

%description -n Mesa-dri-driver-ati-radeon-R100 -l pl.UTF-8
Sterownik X.org DRI dla rodziny kart ATI R100 (Radeon 7000-7500).
Obsługuje układy R100, RV100, RS100, RV200, RS200, RS250.

%package -n Mesa-dri-driver-ati-radeon-R200
Summary:	X.org DRI driver for ATI R200 card family
Summary(pl.UTF-8):	Sterownik X.org DRI dla rodziny kart ATI R200
License:	MIT
Group:		X11/Libraries
Requires:	zlib >= %{zlib_ver}
Suggests:	xorg-driver-video-amdgpu
Suggests:	xorg-driver-video-ati
Obsoletes:	X11-driver-radeon-dri < 1:7.0.0
Conflicts:	xorg-xserver-libglx(glapi) > %{glapi_ver}
Conflicts:	xorg-xserver-libglx(glapi) < %{glapi_ver}

%description -n Mesa-dri-driver-ati-radeon-R200
X.org DRI driver for ATI R200 card family (Radeon 8500-92xx). It
supports R200, RV250, RV280, RS300, RS350 chips.

%description -n Mesa-dri-driver-ati-radeon-R200 -l pl.UTF-8
Sterownik X.org DRI dla rodziny kart ATI R200 (Radeon 8500-92xx).
Obsługuje układy R200, RV250, RV280, RS300, RS350.

%package -n Mesa-dri-driver-intel-i915
Summary:	X.org DRI driver for Intel i915 card family
Summary(pl.UTF-8):	Sterownik X.org DRI dla rodziny kart Intel i915
License:	MIT
Group:		X11/Libraries
Requires:	zlib >= %{zlib_ver}
Obsoletes:	Mesa-dri-driver-intel-i830 < 6.5
Obsoletes:	X11-driver-i810-dri < 1:7.0.0
Conflicts:	xorg-xserver-libglx(glapi) > %{glapi_ver}
Conflicts:	xorg-xserver-libglx(glapi) < %{glapi_ver}

%description -n Mesa-dri-driver-intel-i915
X.org DRI driver for Intel i915 card family (830, 845, 852/855, 865,
915, 945, G33, Q33, Q35, Pineview).

%description -n Mesa-dri-driver-intel-i915 -l pl.UTF-8
Sterownik X.org DRI dla rodziny kart Intel i915 (830, 845, 852/855,
865, 915, 945, G33, Q33, Q35, Pineview).

%package -n Mesa-dri-driver-intel-i965
Summary:	X.org DRI driver for Intel i965 card family
Summary(pl.UTF-8):	Sterownik X.org DRI dla rodziny kart Intel i965
License:	MIT
Group:		X11/Libraries
Requires:	zlib >= %{zlib_ver}
Obsoletes:	Mesa-dri-driver-intel-i830 < 6.5
Obsoletes:	X11-driver-i810-dri < 1:7.0.0
Conflicts:	xorg-xserver-libglx(glapi) > %{glapi_ver}
Conflicts:	xorg-xserver-libglx(glapi) < %{glapi_ver}

%description -n Mesa-dri-driver-intel-i965
X.org (non-Gallium) DRI driver for Intel i965 card family (946GZ,
965G, 965Q, 965GM, 965GME, GM45, G41, B43, Q45/Q43, G45/G43, Ironlake,
Sandybridge, Ivybridge, Haswell, Ray Trail, Broadwell, Cherrytrail,
Braswell, Cherryview, Skylake, Broxton, Kabylake, Coffeelake,
Geminilake, Whiskey Lake, Comet Lake, Cannonlake, Ice Lake, Elkhart
Lake).

%description -n Mesa-dri-driver-intel-i965 -l pl.UTF-8
Sterownik X.org DRI (nie Gallium) dla rodziny kart Intel i965 (946GZ,
965G, 965Q, 965GM, 965GME, GM45, G41, B43, Q45/Q43, G45/G43, Ironlake,
Sandybridge, Ivybridge, Haswell, Ray Trail, Broadwell, Cherrytrail,
Braswell, Cherryview, Skylake, Broxton, Kabylake, Coffeelake,
Geminilake, Whiskey Lake, Comet Lake, Cannonlake, Ice Lake, Elkhart
Lake).

%package -n Mesa-dri-driver-nouveau
Summary:	X.org DRI driver for NVIDIA card family
Summary(pl.UTF-8):	Sterownik X.org DRI dla rodziny kart NVIDIA
License:	MIT
Group:		X11/Libraries
Requires:	zlib >= %{zlib_ver}
Suggests:	xorg-driver-video-nouveau
Conflicts:	xorg-xserver-libglx(glapi) > %{glapi_ver}
Conflicts:	xorg-xserver-libglx(glapi) < %{glapi_ver}

%description -n Mesa-dri-driver-nouveau
X.org DRI drivers for NVIDIA card family.

%description -n Mesa-dri-driver-nouveau -l pl.UTF-8
Sterowniki X.org DRI dla rodziny kart NVIDIA.

%prep
%setup -q -n mesa-mesa-%{version}

%build
dri_drivers="nouveau r100 r200 \
%ifarch %{ix86} %{x8664} x32
i965 i915 \
%endif
"

dri_drivers=$(echo $dri_drivers | xargs | tr ' ' ',')

%meson build \
	-Dplatforms=x11 \
	-Ddri3=enabled \
	-Ddri-drivers=${dri_drivers} \
	-Ddri-drivers-path=%{_libdir}/xorg/modules/dri \
	-Degl=disabled \
	-Dgallium-drivers= \
	-Dgbm=disabled \
	-Dgles1=disabled \
	-Dgles2=disabled \
	-Dglvnd=true \
	-Dlibunwind=enabled \
	-Dosmesa=false \
	-Dselinux=true \
	-Dsse2=%{__true_false sse2} \
	-Dvulkan-drivers=

%ninja_build -C build

%{?with_tests:%ninja_test -C build}

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# not used externally
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libglapi.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	libGL -p /sbin/ldconfig
%postun	libGL -p /sbin/ldconfig

%post	libglapi -p /sbin/ldconfig
%postun	libglapi -p /sbin/ldconfig

### libraries

%if 0
# see TODO question
%files libGL
%defattr(644,root,root,755)
%doc docs/{*.rst,README.UVD,features.txt,relnotes/*.rst}
%attr(755,root,root) %{_libdir}/libGLX_mesa.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libGLX_mesa.so.0
%attr(755,root,root) %{_libdir}/libGLX_mesa.so
%{_datadir}/drirc.d

%files libGL-devel
%defattr(644,root,root,755)
%doc docs/_extra/specs/*

%files libglapi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglapi.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libglapi.so.0
# libglapi-devel? nothing seems to need it atm.
#%attr(755,root,root) %{_libdir}/libglapi.so

%files dri-devel
%defattr(644,root,root,755)
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h
%{_pkgconfigdir}/dri.pc
%endif

### drivers: dri

%files -n Mesa-dri-driver-ati-radeon-R100
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/radeon_dri.so

%files -n Mesa-dri-driver-ati-radeon-R200
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/r200_dri.so

%ifarch %{ix86} %{x8664} x32
%files -n Mesa-dri-driver-intel-i915
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/i830_dri.so
%attr(755,root,root) %{_libdir}/xorg/modules/dri/i915_dri.so

%files -n Mesa-dri-driver-intel-i965
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/i965_dri.so
%endif

%files -n Mesa-dri-driver-nouveau
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/dri/nouveau_vieux_dri.so
