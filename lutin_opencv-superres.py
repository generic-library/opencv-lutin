#!/usr/bin/python
import realog.debug as debug
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
	    'opencv/modules/superres/src/btv_l1_cuda.cpp',
	    'opencv/modules/superres/src/btv_l1.cpp',
	    'opencv/modules/superres/src/optical_flow.cpp',
	    'opencv/modules/superres/src/super_resolution.cpp',
	    #'opencv/modules/superres/src/cuda/btv_l1_gpu.cu',
	    'opencv/modules/superres/src/input_array_utility.cpp',
	    #'opencv/modules/superres/src/opencl/superres_btvl1.cl',
	    'opencv/modules/superres/src/frame_source.cpp',
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
	    "opencv/modules/superres/include/*",
	    recursive=True)
	my_module.add_depend([
	    'opencv-core',
	    'opencv-imgproc',
	    'opencv-video',
	    ])
	if "Android" in target.get_type():
		my_module.add_flag('c++', "-DANDROID")
	my_module.compile_version("C++", 2003)
	return True


