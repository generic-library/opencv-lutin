#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "opencv Image processing library"

def get_licence():
	return "APAPCHE-2"

def get_maintainer():
	return ["Maksim Shabunin <maksim.shabunin@itseez.com>"]

def get_version():
	return [3,1,0]

def configure(target, my_module):
	my_module.add_src_file([
	    'opencv/modules/calib3d/src/polynom_solver.cpp',
	    'opencv/modules/calib3d/src/circlesgrid.cpp',
	    'opencv/modules/calib3d/src/compat_ptsetreg.cpp',
	    'opencv/modules/calib3d/src/calibinit.cpp',
	    'opencv/modules/calib3d/src/upnp.cpp',
	    'opencv/modules/calib3d/src/epnp.cpp',
	    'opencv/modules/calib3d/src/checkchessboard.cpp',
	    'opencv/modules/calib3d/src/ptsetreg.cpp',
	    'opencv/modules/calib3d/src/five-point.cpp',
	    'opencv/modules/calib3d/src/fisheye.cpp',
	    'opencv/modules/calib3d/src/levmarq.cpp',
	    'opencv/modules/calib3d/src/stereobm.cpp',
	    'opencv/modules/calib3d/src/triangulate.cpp',
	    'opencv/modules/calib3d/src/compat_stereo.cpp',
	    'opencv/modules/calib3d/src/quadsubpix.cpp',
	    'opencv/modules/calib3d/src/homography_decomp.cpp',
	    'opencv/modules/calib3d/src/stereosgbm.cpp',
	    #'opencv/modules/calib3d/src/opencl/stereobm.cl',
	    'opencv/modules/calib3d/src/calibration.cpp',
	    'opencv/modules/calib3d/src/fundam.cpp',
	    'opencv/modules/calib3d/src/rho.cpp',
	    'opencv/modules/calib3d/src/dls.cpp',
	    'opencv/modules/calib3d/src/posit.cpp',
	    'opencv/modules/calib3d/src/solvepnp.cpp',
	    'opencv/modules/calib3d/src/p3p.cpp',
	    'opencv/modules/calib3d/src/main.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    "-DCVAPI_EXPORTS",
	    "-D__OPENCV_BUILD=1",
	    "-fsigned-char",
	    "-W",
	    "-Wall",
	    "-Werror=return-type",
	    "-Werror=non-virtual-dtor",
	    "-Werror=address",
	    "-Werror=sequence-point",
	    "-Wformat",
	    "-Werror=format-security",
	    "-Wmissing-declarations",
	    "-Winit-self",
	    "-Wpointer-arith",
	    "-Wshadow",
	    "-Wsign-promo",
	    "-Wno-narrowing",
	    "-Wno-delete-non-virtual-dtor",
	    "-fdiagnostics-show-option",
	    "-Wno-long-long",
	    "-fomit-frame-pointer",
	    "-ffunction-sections",
	    "-fvisibility=hidden",
	    "-fvisibility-inlines-hidden",
	    ])
	my_module.add_header_file(
	    "opencv/modules/calib3d/include/*",
	    recursive=True)
	my_module.add_depend([
	    'opencv-core',
	    'opencv-features2d',
	    ])
	if "Android" in target.get_type():
		my_module.add_flag('c++', "-DANDROID")
	my_module.compile_version("C++", 2003)
	return True


