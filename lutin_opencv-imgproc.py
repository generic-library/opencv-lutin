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
	    'opencv/modules/imgproc/src/geometry.cpp',
	    'opencv/modules/imgproc/src/connectedcomponents.cpp',
	    'opencv/modules/imgproc/src/emd.cpp',
	    'opencv/modules/imgproc/src/morph.cpp',
	    'opencv/modules/imgproc/src/gabor.cpp',
	    'opencv/modules/imgproc/src/accum.cpp',
	    'opencv/modules/imgproc/src/smooth.cpp',
	    'opencv/modules/imgproc/src/distransform.cpp',
	    'opencv/modules/imgproc/src/tables.cpp',
	    'opencv/modules/imgproc/src/generalized_hough.cpp',
	    'opencv/modules/imgproc/src/utils.cpp',
	    'opencv/modules/imgproc/src/featureselect.cpp',
	    'opencv/modules/imgproc/src/templmatch.cpp',
	    'opencv/modules/imgproc/src/subdivision2d.cpp',
	    'opencv/modules/imgproc/src/approx.cpp',
	    'opencv/modules/imgproc/src/samplers.cpp',
	    'opencv/modules/imgproc/src/rotcalipers.cpp',
	    'opencv/modules/imgproc/src/grabcut.cpp',
	    'opencv/modules/imgproc/src/histogram.cpp',
	    'opencv/modules/imgproc/src/filter.cpp',
	    'opencv/modules/imgproc/src/shapedescr.cpp',
	    'opencv/modules/imgproc/src/imgwarp.cpp',
	    'opencv/modules/imgproc/src/drawing.cpp',
	    'opencv/modules/imgproc/src/main.cpp',
	    'opencv/modules/imgproc/src/matchcontours.cpp',
	    'opencv/modules/imgproc/src/demosaicing.cpp',
	    'opencv/modules/imgproc/src/phasecorr.cpp',
	    'opencv/modules/imgproc/src/pyramids.cpp',
	    'opencv/modules/imgproc/src/clahe.cpp',
	    'opencv/modules/imgproc/src/hershey_fonts.cpp',
	    'opencv/modules/imgproc/src/thresh.cpp',
	    'opencv/modules/imgproc/src/hough.cpp',
	    'opencv/modules/imgproc/src/cornersubpix.cpp',
	    'opencv/modules/imgproc/src/canny.cpp',
	    'opencv/modules/imgproc/src/color.cpp',
	    'opencv/modules/imgproc/src/floodfill.cpp',
	    'opencv/modules/imgproc/src/linefit.cpp',
	    'opencv/modules/imgproc/src/deriv.cpp',
	    'opencv/modules/imgproc/src/spatialgradient.cpp',
	    'opencv/modules/imgproc/src/colormap.cpp',
	    'opencv/modules/imgproc/src/undistort.cpp',
	    'opencv/modules/imgproc/src/lsd.cpp',
	    'opencv/modules/imgproc/src/min_enclosing_triangle.cpp',
	    'opencv/modules/imgproc/src/contours.cpp',
	    'opencv/modules/imgproc/src/sumpixels.cpp',
	    'opencv/modules/imgproc/src/segmentation.cpp',
	    'opencv/modules/imgproc/src/blend.cpp',
	    'opencv/modules/imgproc/src/corner.cpp',
	    'opencv/modules/imgproc/src/intersection.cpp',
	    'opencv/modules/imgproc/src/convhull.cpp',
	    'opencv/modules/imgproc/src/moments.cpp',
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
	    "opencv/modules/imgproc/include/*",
	    recursive=True)
	my_module.add_module_depend([
	    'opencv-core'
	    ])
	if target.name=="Android":
		my_module.compile_flags('c++', "-DANDROID")
	my_module.compile_version("C++", 2003)
	return my_module


