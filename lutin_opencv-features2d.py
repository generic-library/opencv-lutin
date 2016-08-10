#!/usr/bin/python
import lutin.module as module
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

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'opencv/modules/features2d/src/bagofwords.cpp',
	    'opencv/modules/features2d/src/kaze/fed.cpp',
	    'opencv/modules/features2d/src/kaze/nldiffusion_functions.cpp',
	    'opencv/modules/features2d/src/kaze/KAZEFeatures.cpp',
	    'opencv/modules/features2d/src/kaze/AKAZEFeatures.cpp',
	    'opencv/modules/features2d/src/agast.cpp',
	    'opencv/modules/features2d/src/agast_score.cpp',
	    'opencv/modules/features2d/src/keypoint.cpp',
	    'opencv/modules/features2d/src/fast.cpp',
	    'opencv/modules/features2d/src/akaze.cpp',
	    'opencv/modules/features2d/src/orb.cpp',
	    'opencv/modules/features2d/src/brisk.cpp',
	    'opencv/modules/features2d/src/mser.cpp',
	    'opencv/modules/features2d/src/kaze.cpp',
	    'opencv/modules/features2d/src/feature2d.cpp',
	    #'opencv/modules/features2d/src/opencl/fast.cl',
	    #'opencv/modules/features2d/src/opencl/orb.cl',
	    #'opencv/modules/features2d/src/opencl/brute_force_match.cl',
	    'opencv/modules/features2d/src/fast_score.cpp',
	    'opencv/modules/features2d/src/evaluation.cpp',
	    'opencv/modules/features2d/src/draw.cpp',
	    'opencv/modules/features2d/src/matchers.cpp',
	    'opencv/modules/features2d/src/dynamic.cpp',
	    'opencv/modules/features2d/src/main.cpp',
	    'opencv/modules/features2d/src/blobdetector.cpp',
	    'opencv/modules/features2d/src/gftt.cpp',
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
	    "opencv/modules/features2d/include/*",
	    recursive=True)
	my_module.add_module_depend([
	    'opencv-core',
	    'opencv-flann',
	    'opencv-imgproc',
	    ])
	if target.name=="Android":
		my_module.compile_flags('c++', "-DANDROID")
	my_module.compile_version("C++", 2003)
	return my_module


