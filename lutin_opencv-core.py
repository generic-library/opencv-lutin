#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "opencv CORE library matrix computation evironement"

def get_licence():
	return "APAPCHE-2"

def get_maintainer():
	return ["Maksim Shabunin <maksim.shabunin@itseez.com>"]

def get_version():
	return [3,1,0]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'opencv/modules/core/src/stl.cpp',
	    'opencv/modules/core/src/matrix_decomp.cpp',
	    'opencv/modules/core/src/array.cpp',
	    'opencv/modules/core/src/matop.cpp',
	    'opencv/modules/core/src/mathfuncs_core.cpp',
	    'opencv/modules/core/src/tables.cpp',
	    'opencv/modules/core/src/matmul.cpp',
	    'opencv/modules/core/src/copy.cpp',
	    'opencv/modules/core/src/algorithm.cpp',
	    'opencv/modules/core/src/cuda_info.cpp',
	    'opencv/modules/core/src/types.cpp',
	    'opencv/modules/core/src/umatrix.cpp',
	    'opencv/modules/core/src/arithm.cpp',
	    'opencv/modules/core/src/opencl/runtime/opencl_clamdblas.cpp',
	    'opencv/modules/core/src/opencl/runtime/opencl_clamdfft.cpp',
	    'opencv/modules/core/src/opencl/runtime/opencl_core.cpp',
	    'opencv/modules/core/src/split.cpp',
	    'opencv/modules/core/src/lapack.cpp',
	    'opencv/modules/core/src/conjugate_gradient.cpp',
	    'opencv/modules/core/src/system.cpp',
	    'opencv/modules/core/src/ocl.cpp',
	    'opencv/modules/core/src/lda.cpp',
	    'opencv/modules/core/src/out.cpp',
	    'opencv/modules/core/src/persistence.cpp',
	    'opencv/modules/core/src/alloc.cpp',
	    'opencv/modules/core/src/directx.cpp',
	    'opencv/modules/core/src/stat.cpp',
	    'opencv/modules/core/src/matrix.cpp',
	    'opencv/modules/core/src/cuda_host_mem.cpp',
	    'opencv/modules/core/src/glob.cpp',
	    'opencv/modules/core/src/mathfuncs.cpp',
	    'opencv/modules/core/src/convert.cpp',
	    'opencv/modules/core/src/cuda_gpu_mat.cpp',
	    'opencv/modules/core/src/downhill_simplex.cpp',
	    'opencv/modules/core/src/kmeans.cpp',
	    'opencv/modules/core/src/rand.cpp',
	    'opencv/modules/core/src/parallel.cpp',
	    'opencv/modules/core/src/dxt.cpp',
	    'opencv/modules/core/src/parallel_pthreads.cpp',
	    'opencv/modules/core/src/va_intel.cpp',
	    'opencv/modules/core/src/merge.cpp',
	    'opencv/modules/core/src/command_line_parser.cpp',
	    'opencv/modules/core/src/datastructs.cpp',
	    'opencv/modules/core/src/gl_core_3_1.cpp',
	    'opencv/modules/core/src/opengl.cpp',
	    'opencv/modules/core/src/pca.cpp',
	    'opencv/modules/core/src/lpsolver.cpp',
	    'opencv/modules/core/src/cuda_stream.cpp',
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
	    "-Wundef",
	    "-Winit-self",
	    "-Wpointer-arith",
	    "-Wshadow",
	    "-Wsign-promo",
	    "-Wno-narrowing",
	    "-Wno-delete-non-virtual-dtor",
	    "-fdiagnostics-show-option",
	    "-Wno-long-long",
	    #"-pthread",
	    "-fomit-frame-pointer",
	    "-msse",
	    "-msse2",
	    "-mno-avx",
	    "-msse3",
	    "-mno-ssse3",
	    "-mno-sse4.1",
	    "-mno-sse4.2",
	    "-ffunction-sections",
	    "-fvisibility=hidden",
	    "-fvisibility-inlines-hidden",
	    ])
	if target.config["mode"] == "release":
		my_module.compile_flags('c++', "-DNDEBUG")
	else:
		my_module.compile_flags('c++', "-DDEBUG")
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "opencv", "modules", "core", "src"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "opencv", "modules", "core"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "opencv"))
	my_module.add_header_file(
	    'opencv/modules/core/include/*',
	    recursive=True)
	my_module.add_module_depend([
	    'cxx',
	    'pthread'
	    ])
	my_module.compile_version("C++", 2003)
	return my_module


