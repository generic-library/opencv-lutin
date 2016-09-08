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
	    'opencv/modules/photo/src/tonemap.cpp',
	    'opencv/modules/photo/src/contrast_preserve.cpp',
	    'opencv/modules/photo/src/align.cpp',
	    'opencv/modules/photo/src/seamless_cloning_impl.cpp',
	    'opencv/modules/photo/src/inpaint.cpp',
	    'opencv/modules/photo/src/denoising.cuda.cpp',
	    'opencv/modules/photo/src/denoising.cpp',
	    #'opencv/modules/photo/src/cuda/nlm.cu',
	    'opencv/modules/photo/src/merge.cpp',
	    'opencv/modules/photo/src/npr.cpp',
	    'opencv/modules/photo/src/calibrate.cpp',
	    #'opencv/modules/photo/src/opencl/nlmeans.cl',
	    'opencv/modules/photo/src/hdr_common.cpp',
	    'opencv/modules/photo/src/denoise_tvl1.cpp',
	    'opencv/modules/photo/src/seamless_cloning.cpp',
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
	    "opencv/modules/photo/include/*",
	    recursive=True)
	my_module.add_depend([
	    'opencv-core',
	    'opencv-imgproc'
	    ])
	if "Android" in target.get_type():
		my_module.add_flag('c++', "-DANDROID")
	my_module.compile_version("C++", 2003)
	return my_module


