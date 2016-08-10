#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "opencv photo processing library"

def get_licence():
	return "APAPCHE-2"

def get_maintainer():
	return ["Maksim Shabunin <maksim.shabunin@itseez.com>"]

def get_version():
	return [3,1,0]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'opencv/modules/video/src/bgfg_gaussmix2.cpp',
	    'opencv/modules/video/src/bgfg_KNN.cpp',
	    'opencv/modules/video/src/lkpyramid.cpp',
	    'opencv/modules/video/src/ecc.cpp',
	    'opencv/modules/video/src/tvl1flow.cpp',
	    'opencv/modules/video/src/compat_video.cpp',
	    'opencv/modules/video/src/kalman.cpp',
	    #'opencv/modules/video/src/opencl/pyrlk.cl',
	    #'opencv/modules/video/src/opencl/optical_flow_farneback.cl',
	    #'opencv/modules/video/src/opencl/optical_flow_tvl1.cl',
	    #'opencv/modules/video/src/opencl/bgfg_mog2.cl',
	    'opencv/modules/video/src/optflowgf.cpp',
	    'opencv/modules/video/src/camshift.cpp',
	    ])
	
	my_module.compile_flags('c++', [
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
	    "opencv/modules/video/include/*",
	    recursive=True)
	my_module.add_module_depend([
	    'opencv-core',
	    'opencv-imgproc',
	    ])
	if target.name=="Android":
		my_module.compile_flags('c++', "-DANDROID")
	my_module.compile_version("C++", 2003)
	return my_module


