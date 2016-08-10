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
	    'opencv/modules/ml/src/rtrees.cpp',
	    'opencv/modules/ml/src/nbayes.cpp',
	    'opencv/modules/ml/src/lr.cpp',
	    'opencv/modules/ml/src/svm.cpp',
	    'opencv/modules/ml/src/em.cpp',
	    'opencv/modules/ml/src/gbt.cpp',
	    'opencv/modules/ml/src/data.cpp',
	    'opencv/modules/ml/src/knearest.cpp',
	    'opencv/modules/ml/src/kdtree.cpp',
	    'opencv/modules/ml/src/testset.cpp',
	    'opencv/modules/ml/src/tree.cpp',
	    'opencv/modules/ml/src/ann_mlp.cpp',
	    'opencv/modules/ml/src/boost.cpp',
	    'opencv/modules/ml/src/inner_functions.cpp',
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
	    "opencv/modules/ml/include/*",
	    recursive=True)
	my_module.add_module_depend([
	    'opencv-core'
	    ])
	if target.name=="Android":
		my_module.compile_flags('c++', "-DANDROID")
	my_module.compile_version("C++", 2003)
	return my_module


