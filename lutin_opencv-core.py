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
	    'opencv/modules/core/include/*',
	    recursive=True)
	my_module.add_depend([
	    'pthread',
	    'm',
	    'z',
	    'cxx',
	    ])
	
	if "Android" in target.get_type():
		my_module.add_depend("SDK")
		my_module.add_flag('c++', "-DANDROID")
	my_module.compile_version("C++", 2003)
	my_module.add_header_file([
		'generated/*'
		],
		destination_path="")
	# generate dynamic file
	generate_config_file(my_module)
	return my_module


def generate_config_file(my_module):
	#--------------------------------------------------------------------------------------
	file_data = "/* Auto generate file with lutin */\n"
	file_data+= "#pragma once\n"
	file_data+= "\n"
	file_data+= "#define HAVE_OPENCV_CALIB3D\n"
	file_data+= "#define HAVE_OPENCV_CORE\n"
	file_data+= "#define HAVE_OPENCV_FEATURES2D\n"
	file_data+= "#define HAVE_OPENCV_FLANN\n"
	#file_data+= "#define HAVE_OPENCV_HIGHGUI\n"
	#file_data+= "#define HAVE_OPENCV_IMGCODECS\n"
	file_data+= "#define HAVE_OPENCV_IMGPROC\n"
	file_data+= "#define HAVE_OPENCV_ML\n"
	file_data+= "#define HAVE_OPENCV_OBJDETECT\n"
	file_data+= "#define HAVE_OPENCV_PHOTO\n"
	file_data+= "#define HAVE_OPENCV_SHAPE\n"
	file_data+= "#define HAVE_OPENCV_STITCHING\n"
	file_data+= "#define HAVE_OPENCV_SUPERRES\n"
	file_data+= "#define HAVE_OPENCV_VIDEO\n"
	#file_data+= "#define HAVE_OPENCV_VIDEOIO\n"
	#file_data+= "#define HAVE_OPENCV_VIDEOSTAB\n"
	file_data+= "\n"
	my_module.add_generated_header_file(file_data, "opencv2/opencv_modules.hpp")
	#--------------------------------------------------------------------------------------
	file_data = "/* Auto generate file with lutin */\n"
	file_data+= "#pragma once\n"
	file_data+= "// OpenCV compiled as static or dynamic libs\n"
	file_data+= "#define BUILD_SHARED_LIBS\n"
	#file_data+= "// Compile for 'real' NVIDIA GPU architectures\n"
	#file_data+= "#define CUDA_ARCH_BIN ""\n"
	#file_data+= "// Create PTX or BIN for 1.0 compute capability\n"
	#file_data+= "#define CUDA_ARCH_BIN_OR_PTX_10\n"
	#file_data+= "// NVIDIA GPU features are used\n"
	#file_data+= "#define CUDA_ARCH_FEATURES ""\n"
	#file_data+= "// Compile for 'virtual' NVIDIA PTX architectures\n"
	#file_data+= "#define CUDA_ARCH_PTX ""\n"
	#file_data+= "// AVFoundation video libraries\n"
	#file_data+= "#define HAVE_AVFOUNDATION\n"
	#file_data+= "// V4L capturing support\n"
	#file_data+= "#define HAVE_CAMV4L\n"
	#file_data+= "// V4L2 capturing support\n"
	#file_data+= "#define HAVE_CAMV4L2\n"
	#file_data+= "// Carbon windowing environment\n"
	#file_data+= "#define HAVE_CARBON\n"
	#file_data+= "// AMD's Basic Linear Algebra Subprograms Library*/\n"
	#file_data+= "#define HAVE_CLAMDBLAS\n"
	#file_data+= "// AMD's OpenCL Fast Fourier Transform Library*/\n"
	#file_data+= "#define HAVE_CLAMDFFT\n"
	#file_data+= "// Clp support\n"
	#file_data+= "#define HAVE_CLP\n"
	#file_data+= "// Cocoa API\n"
	#file_data+= "#define HAVE_COCOA\n"
	#file_data+= "// C=\n"
	#file_data+= "#define HAVE_CSTRIPES\n"
	#file_data+= "// NVidia Cuda Basic Linear Algebra Subprograms (BLAS) API*/\n"
	#file_data+= "#define HAVE_CUBLAS\n"
	#file_data+= "// NVidia Cuda Runtime API*/\n"
	#file_data+= "#define HAVE_CUDA\n"
	#file_data+= "// NVidia Cuda Fast Fourier Transform (FFT) API*/\n"
	#file_data+= "#define HAVE_CUFFT\n"
	#file_data+= "// IEEE1394 capturing support\n"
	#file_data+= "#define HAVE_DC1394\n"
	#file_data+= "// IEEE1394 capturing support - libdc1394 v2.x\n"
	#file_data+= "#define HAVE_DC1394_2\n"
	#file_data+= "// DirectX\n"
	#file_data+= "#define HAVE_DIRECTX\n"
	#file_data+= "#define HAVE_DIRECTX_NV12\n"
	#file_data+= "#define HAVE_D3D11\n"
	#file_data+= "#define HAVE_D3D10\n"
	#file_data+= "#define HAVE_D3D9\n"
	#file_data+= "// DirectShow Video Capture library\n"
	#file_data+= "#define HAVE_DSHOW\n"
	#file_data+= "// Eigen Matrix & Linear Algebra Library\n"
	#file_data+= "#define HAVE_EIGEN\n"
	#file_data+= "// FFMpeg video library\n"
	#file_data+= "#define HAVE_FFMPEG\n"
	#file_data+= "// ffmpeg's libswscale\n"
	#file_data+= "#define HAVE_FFMPEG_SWSCALE\n"
	#file_data+= "// ffmpeg in Gentoo\n"
	#file_data+= "#define HAVE_GENTOO_FFMPEG\n"
	#file_data+= "// Geospatial Data Abstraction Library\n"
	#file_data+= "#define HAVE_GDAL\n"
	#file_data+= "// GStreamer multimedia framework\n"
	#file_data+= "#define HAVE_GSTREAMER\n"
	#file_data+= "// GTK+ 2.0 Thread support\n"
	#file_data+= "#define HAVE_GTHREAD\n"
	#file_data+= "// GTK+ 2.x toolkit\n"
	#file_data+= "#define HAVE_GTK\n"
	#file_data+= "// Define to 1 if you have the <inttypes.h> header file.\n"
	#file_data+= "#define HAVE_INTTYPES_H\n"
	#file_data+= "// Intel Perceptual Computing SDK library\n"
	#file_data+= "#define HAVE_INTELPERC\n"
	#file_data+= "// Intel Integrated Performance Primitives\n"
	#file_data+= "#define HAVE_IPP\n"
	#file_data+= "#define HAVE_IPP_ICV_ONLY\n"
	#file_data+= "// Intel IPP Async\n"
	#file_data+= "// #define HAVE_IPP_A\n"
	#file_data+= "// JPEG-2000 codec\n"
	#file_data+= "#define HAVE_JASPER\n"
	#file_data+= "// IJG JPEG codec\n"
	#file_data+= "#define HAVE_JPEG\n"
	#file_data+= "// libpng/png.h needs to be included\n"
	#file_data+= "#define HAVE_LIBPNG_PNG_H\n"
	#file_data+= "// GDCM DICOM codec\n"
	#file_data+= "#define HAVE_GDCM\n"
	#file_data+= "// V4L/V4L2 capturing support via libv4l\n"
	#file_data+= "#define HAVE_LIBV4L\n"
	#file_data+= "// Microsoft Media Foundation Capture library\n"
	#file_data+= "#define HAVE_MSMF\n"
	#file_data+= "// NVidia Video Decoding API*/\n"
	#file_data+= "#define HAVE_NVCUVID\n"
	#file_data+= "// NVidia Video Encoding API*/\n"
	#file_data+= "#define HAVE_NVCUVENC\n"
	#file_data+= "// OpenCL Support\n"
	#file_data+= "#define HAVE_OPENCL\n"
	#file_data+= "#define HAVE_OPENCL_STATIC\n"
	#file_data+= "#define HAVE_OPENCL_SVM\n"
	#file_data+= "// OpenEXR codec\n"
	#file_data+= "#define HAVE_OPENEXR\n"
	#file_data+= "// OpenGL support*/\n"
	#file_data+= "#define HAVE_OPENGL\n"
	#file_data+= "// OpenNI library\n"
	#file_data+= "#define HAVE_OPENNI\n"
	#file_data+= "// OpenNI library\n"
	#file_data+= "#define HAVE_OPENNI2\n"
	#file_data+= "// PNG codec\n"
	#file_data+= "#define HAVE_PNG\n"
	file_data+= "// Posix threads (pthreads)\n"
	file_data+= "#define HAVE_PTHREADS\n"
	file_data+= "// parallel_for with pthreads\n"
	file_data+= "#define HAVE_PTHREADS_PF\n"
	#file_data+= "// Qt support\n"
	#file_data+= "#define HAVE_QT\n"
	#file_data+= "// Qt OpenGL support\n"
	#file_data+= "#define HAVE_QT_OPENGL\n"
	#file_data+= "// QuickTime video libraries\n"
	#file_data+= "#define HAVE_QUICKTIME\n"
	#file_data+= "// QTKit video libraries\n"
	#file_data+= "#define HAVE_QTKIT\n"
	#file_data+= "// Intel Threading Building Blocks\n"
	#file_data+= "#define HAVE_TBB\n"
	#file_data+= "// TIFF codec\n"
	#file_data+= "#define HAVE_TIFF\n"
	#file_data+= "// Unicap video capture library\n"
	#file_data+= "#define HAVE_UNICAP\n"
	#file_data+= "// Video for Windows support\n"
	#file_data+= "#define HAVE_VFW\n"
	#file_data+= "// V4L2 capturing support in videoio.h\n"
	#file_data+= "#define HAVE_VIDEOIO\n"
	#file_data+= "// Win32 UI\n"
	#file_data+= "#define HAVE_WIN32UI\n"
	#file_data+= "// XIMEA camera support\n"
	#file_data+= "#define HAVE_XIMEA\n"
	#file_data+= "// Xine video library\n"
	#file_data+= "#define HAVE_XINE\n"
	#file_data+= "// Define if your processor stores words with the most significant byte\n"
	#file_data+= "// first (like Motorola and SPARC, unlike Intel and VAX).\n"
	#file_data+= "#define WORDS_BIGENDIAN\n"
	#file_data+= "// gPhoto2 library\n"
	#file_data+= "#define HAVE_GPHOTO2\n"
	#file_data+= "// VA library (libva)\n"
	#file_data+= "#define HAVE_VA\n"
	#file_data+= "// Intel VA-API/OpenCL\n"
	#file_data+= "#define HAVE_VA_INTEL\n"
	#file_data+= "// Lapack\n"
	#file_data+= "#define HAVE_LAPACK\n"
	#file_data+= "// FP16\n"
	#file_data+= "#define HAVE_FP16\n"
	#my_module.add_generated_header_file(file_data, "opencv2/cvconfig.h", True)
	my_module.add_generated_header_file(file_data, "cvconfig.h", True)
	
	file_data = "/* Auto generate file with lutin */\n"
	file_data+= "#pragma once\n"
	my_module.add_generated_header_file(file_data, "custom_hal.hpp")
	file_data = "\"generate with lutin build system ...\\n\""
	my_module.add_generated_header_file(file_data, "version_string.inc")
	
	

