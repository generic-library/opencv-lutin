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
	    'opencv/modules/stitching/src/timelapsers.cpp',
	    'opencv/modules/stitching/src/autocalib.cpp',
	    'opencv/modules/stitching/src/util.cpp',
	    'opencv/modules/stitching/src/stitcher.cpp',
	    'opencv/modules/stitching/src/camera.cpp',
	    'opencv/modules/stitching/src/blenders.cpp',
	    #'opencv/modules/stitching/src/cuda/build_warp_maps.cu',
	    #'opencv/modules/stitching/src/opencl/multibandblend.cl',
	    #'opencv/modules/stitching/src/opencl/warpers.cl',
	    'opencv/modules/stitching/src/matchers.cpp',
	    'opencv/modules/stitching/src/exposure_compensate.cpp',
	    'opencv/modules/stitching/src/motion_estimators.cpp',
	    'opencv/modules/stitching/src/seam_finders.cpp',
	    'opencv/modules/stitching/src/warpers.cpp',
	    'opencv/modules/stitching/src/warpers_cuda.cpp',
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
	    "opencv/modules/stitching/include/*",
	    recursive=True)
	my_module.add_depend([
	    'opencv-core',
	    'opencv-features2d',
	    'opencv-calib3d',
	    ])
	if "Android" in target.get_type():
		my_module.add_flag('c++', "-DANDROID")
	my_module.compile_version("C++", 2003)
	return True


