%define		_enable_debug_packages	%{nil}
%define		debug_package		%{nil}

%define		itkver 3.16

Summary:	Extended language support for ITK
Name:		wrapitk
Version:	0.3.0
Release:	%mkrel 1
License:	BSDish
Group:		Sciences/Other
URL:		http://code.google.com/p/wrapitk/
Source0:	http://wrapitk.googlecode.com/files/wrapitk-0.3.0.tar.bz2
BuildRequires:	cmake >= 2.4.8
BuildRequires:	cableswig >= %{itkver}
BuildRequires:	doxygen
BuildRequires:  fftw-devel
BuildRequires:  ghostscript
BuildRequires:  imagemagick
BuildRequires:  itk-devel >= %{itkver}
BuildRequires:  libuuid-devel
BuildRequires:  python-numarray-devel
BuildRequires:	python-vtk-devel >= 5.0
BuildRequires:  swig
BuildRequires:  tcl tk
# needed for backport to 2006.0
%if %mdkversion >= 200610
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
%endif
BuildRequires:  tetex
BuildRequires:  tetex-dvips
BuildRequires:  tetex-latex
BuildRequires:  texinfo
BuildRequires:	vtk-devel >= 5.0
%py_requires	-d

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
# for upgrade from package with ITK version
Epoch:          3

Patch0:		wrapitk-0.3.0-prefix.patch

%description
ITK is an open-source software system to support the Visible Human Project. 
Currently under active development, ITK employs leading-edge segmentation 
and registration algorithms in two, three, and more dimensions.

The Insight Toolkit was developed by six principal organizations, three 
commercial (Kitware, GE Corporate R&D, and Insightful) and three academic 
(UNC Chapel Hill, University of Utah, and University of Pennsylvania). 
Additional team members include Harvard Brigham & Women's Hospital, 
University of Pittsburgh, and Columbia University. The funding for the 
project is from the National Library of Medicine at the National Institutes 
of Health. NLM in turn was supported by member institutions of NIH (see 
sponsors). 

#-----------------------------------------------------------------------
%package	devel
Summary:	ITK header files for building C++ code
Group:		Development/C++
Requires:	cmake >= 2.2
Requires:	cableswig >= %{itkver}
Requires:	itk-devel >= %{itkver}

%description	devel
ITK is an open-source software system to support the Visible Human Project. 
Currently under active development, ITK employs leading-edge segmentation 
and registration algorithms in two, three, and more dimensions.

The Insight Toolkit was developed by six principal organizations, three 
commercial (Kitware, GE Corporate R&D, and Insightful) and three academic 
(UNC Chapel Hill, University of Utah, and University of Pennsylvania). 
Additional team members include Harvard Brigham & Women's Hospital, 
University of Pittsburgh, and Columbia University. The funding for the 
project is from the National Library of Medicine at the National Institutes 
of Health. NLM in turn was supported by member institutions of NIH (see 
sponsors). 

%files		devel
%defattr(0644,root,root,0755)
%{_libdir}/InsightToolkit/WrapITK/Configuration
%{_libdir}/InsightToolkit/WrapITK/WrapITKConfig.cmake
%{_datadir}/cmake/Modules/FindWrapITK.cmake

#-----------------------------------------------------------------------
%package	-n python-itk
Summary:	Python bindings for ITK
Group:		Development/Python
Requires:	python
Requires:	itk >= %{itker}
Requires(pre):	itk >= %{itker}
Obsoletes:	itk-python
Provides:	itk-python

%description	-n python-itk
ITK is an open-source software system to support the Visible Human Project. 
Currently under active development, ITK employs leading-edge segmentation 
and registration algorithms in two, three, and more dimensions.

The Insight Toolkit was developed by six principal organizations, three 
commercial (Kitware, GE Corporate R&D, and Insightful) and three academic 
(UNC Chapel Hill, University of Utah, and University of Pennsylvania). 
Additional team members include Harvard Brigham & Women's Hospital, 
University of Pittsburgh, and Columbia University. The funding for the 
project is from the National Library of Medicine at the National Institutes 
of Health. NLM in turn was supported by member institutions of NIH (see 
sponsors). 

%files		-n python-itk
%defattr(0644,root,root,0755)
%{_libdir}/InsightToolkit/WrapITK/Python
%{_libdir}/InsightToolkit/WrapITK/lib/*.py
%{_libdir}/InsightToolkit/WrapITK/lib/*Python.so
%{_libdir}/python%{pyver}/site-packages/WrapITK.pth
%{_sysconfdir}/ld.so.conf.d/python-itk.conf
# exclude numarray files
%exclude %{_libdir}/InsightToolkit/WrapITK/Python/BufferConversion.py
%exclude %{_libdir}/InsightToolkit/WrapITK/Python/Configuration/BufferConversionConfig.py
%exclude %{_libdir}/InsightToolkit/WrapITK/lib/BufferConversionPython.py
%exclude %{_libdir}/InsightToolkit/WrapITK/lib/itkPyBufferPython.py
%exclude %{_libdir}/InsightToolkit/WrapITK/lib/_BufferConversionPython.so
# exclude itkvtk files
%exclude %{_libdir}/InsightToolkit/WrapITK/Python/ItkVtkGlue.py
%exclude %{_libdir}/InsightToolkit/WrapITK/Python/Configuration/ItkVtkGlueConfig.py
%exclude %{_libdir}/InsightToolkit/WrapITK/lib/ItkVtkGluePython.py
%exclude %{_libdir}/InsightToolkit/WrapITK/lib/itkImageToVTKImageFilterPython.py
%exclude %{_libdir}/InsightToolkit/WrapITK/lib/itkVTKImageToImageFilterPython.py
%exclude %{_libdir}/InsightToolkit/WrapITK/lib/_ItkVtkGluePython.so
%doc article/*.pdf

#-----------------------------------------------------------------------
%package	-n python-itk-numarray
Summary:	Convert itk buffers to numarray objects
Group:		Development/Python
Requires:	python
Requires:	python-numarray
Requires:	python-itk = %{epoch}:%{version}

%description	-n python-itk-numarray
Convert itk buffers to numarray objects

%files		-n python-itk-numarray
%defattr(0644,root,root,0755)
%{_libdir}/InsightToolkit/WrapITK/Python/BufferConversion.py
%{_libdir}/InsightToolkit/WrapITK/Python/Configuration/BufferConversionConfig.py
%{_libdir}/InsightToolkit/WrapITK/lib/BufferConversionPython.py
%{_libdir}/InsightToolkit/WrapITK/lib/itkPyBufferPython.py
%{_libdir}/InsightToolkit/WrapITK/lib/_BufferConversionPython.so

#-----------------------------------------------------------------------
%package	-n python-itkvtk
Summary:	Convert itk buffers to vtk ones
Group:		Development/Python
Requires:	python
Requires:	python-itk = %{epoch}:%{version}

%description	-n python-itkvtk
Convert itk buffers to vtk ones

%files		-n python-itkvtk
%defattr(0644,root,root,0755)
%{_libdir}/InsightToolkit/WrapITK/Python/ItkVtkGlue.py
%{_libdir}/InsightToolkit/WrapITK/Python/itkvtk.py
%{_libdir}/InsightToolkit/WrapITK/Python/Configuration/ItkVtkGlueConfig.py
%{_libdir}/InsightToolkit/WrapITK/lib/ItkVtkGluePython.py
%{_libdir}/InsightToolkit/WrapITK/lib/itkImageToVTKImageFilterPython.py
%{_libdir}/InsightToolkit/WrapITK/lib/itkVTKImageToImageFilterPython.py
%{_libdir}/InsightToolkit/WrapITK/lib/_ItkVtkGluePython.so

#-----------------------------------------------------------------------
%package	-n itkvtk-devel
Summary:	Convert itk buffers to vtk ones
Group:		Development/C++
Requires:	itk-devel

%description	-n itkvtk-devel
Convert itk buffers to vtk ones

%files		-n itkvtk-devel
%defattr(0644,root,root,0755)
%{_includedir}/InsightToolkit/BasicFilters/*

#-----------------------------------------------------------------------
%package	-n tcl-itk
Summary:	Tcl bindings for ITK
Group:		Development/Python
Requires:	tcl
Requires:	itk >= %{itker}
Requires(pre):	itk >= %{itker}
Obsoletes:	itk-tcl
Provides:	itk-tcl

%description	-n tcl-itk
ITK is an open-source software system to support the Visible Human Project. 
Currently under active development, ITK employs leading-edge segmentation 
and registration algorithms in two, three, and more dimensions.

The Insight Toolkit was developed by six principal organizations, three 
commercial (Kitware, GE Corporate R&D, and Insightful) and three academic 
(UNC Chapel Hill, University of Utah, and University of Pennsylvania). 
Additional team members include Harvard Brigham & Women's Hospital, 
University of Pittsburgh, and Columbia University. The funding for the 
project is from the National Library of Medicine at the National Institutes 
of Health. NLM in turn was supported by member institutions of NIH (see 
sponsors). 

%files		-n tcl-itk
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/itkwish
%{_libdir}/InsightToolkit/WrapITK/Tcl
%{_libdir}/InsightToolkit/WrapITK/lib/*Tcl.so

#-----------------------------------------------------------------------
%prep
%setup -q

%patch0 -p1

#-----------------------------------------------------------------------
%build
(
%cmake	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DWRAP_ITK_INSTALL_PREFIX:PATH=%{_libdir}/InsightToolkit/WrapITK \
	-DCMAKE_CXX_COMPILER:PATH=%{_bindir}/c++ \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DWRAP_ITK_PYTHON:BOOL=ON \
	-DWRAP_ITK_TCL:BOOL=ON \
	-DWRAP_ITK_JAVA:BOOL=OFF \
	-DWRAP_unsigned_char:BOOL=ON \
	-DDOXYGEN_MAN_PATH:PATH=%{_mandir}/ \
	-DITK_DIR:PATH=%{_libdir}/itk-%{itkver}
%make
)

export LD_LIBRARY_PATH=`pwd`/build/bin:`pwd`/bin/lib:$LD_LIBRARY_PATH
export PYTHONPATH=`pwd`/build/Languages/Python:`pwd`/build/lib:$PYTHONPATH

# build the article
pushd article
    make
popd

# build the external projects
pushd ExternalProjects/PyBuffer/
    (
    %cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DWRAP_ITK_INSTALL_PREFIX:PATH=%{_libdir}/InsightToolkit/WrapITK \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DWrapITK_DIR:PATH=`pwd`/../../../build
    %make
    )
popd

pushd ExternalProjects/ItkVtkGlue
# disable tcl - it doesn't work yet
    (
    %cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DWRAP_ITK_INSTALL_PREFIX:PATH=%{_libdir}/InsightToolkit/WrapITK \
	-DCMAKE_BUILD_TYPE:STRING=Release \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DWrapITK_DIR:PATH=`pwd`/../../../build \
	-DBUILD_WRAPPERS:BOOL=ON \
	-DVTK_DIR:PATH=%{_libdir}/vtk \
	-DWRAP_ITK_TCL:BOOL=OFF \
	-DITK_DIR:PATH=%{_libdir}/itk-%{itkver}
    %make
    )
popd

#-----------------------------------------------------------------------
%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std -C build

# workaround not found library
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/InsightToolkit/WrapITK/lib >> %{buildroot}/%{_sysconfdir}/ld.so.conf.d/python-itk.conf

export LD_LIBRARY_PATH=`pwd`/build/bin:`pwd`/bin/lib:$LD_LIBRARY_PATH
export PYTHONPATH=`pwd`/build/Languages/Python:`pwd`/build/lib:$PYTHONPATH

# install the external projects
%makeinstall_std -C ExternalProjects/PyBuffer/build

%makeinstall_std -C ExternalProjects/ItkVtkGlue/build

mkdir -p %{buildroot}%{_bindir}
mv -f %{buildroot}%{_libdir}/InsightToolkit/WrapITK/bin/itkwish %{buildroot}%{_bindir}
rmdir %{buildroot}%{_libdir}/InsightToolkit/WrapITK/bin

#-----------------------------------------------------------------------
%check

export LD_LIBRARY_PATH=`pwd`/build/bin:`pwd`/bin/lib:$LD_LIBRARY_PATH
export PYTHONPATH=`pwd`/build/Languages/Python:`pwd`/build/lib:$PYTHONPATH

%if 0
pushd build
    # tcl test are failing without DISPLAY
    ctest -E Tcl
popd
%endif

%if 0
# FIXME
pushd ExternalProjects/ItkVtkGlue/build
    ctest
popd
%endif

#-----------------------------------------------------------------------
%clean
rm -rf %{buildroot}

#-----------------------------------------------------------------------
%if %mdkversion < 200900
%post -n python-itk -p /sbin/ldconfig
%endif

#-----------------------------------------------------------------------
%if %mdkversion < 200900
%postun -n python-itk -p /sbin/ldconfig
%endif
