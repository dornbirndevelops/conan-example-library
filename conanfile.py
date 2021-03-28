from conans import ConanFile, CMake


class DenaLibraryConan(ConanFile):
    name = "dena_library"
    version = "1.0"

    description = "Example showcase on how to develop a C++ library depending on other libraries with Conan Package Manager and CMake"
    url = "https://github.com/dornbirndevelops/conan-example-library"
    license = "feel free to use it"

    # combination of settings and options create a unique identifier
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    
    # build the package automatically if requested configuration is not available
    build_policy = "missing"
    # use cmakes "find_package" functionality to access the required software packages
    generators = "cmake_find_package"
    # prevent copying sources to build folder
    no_copy_source = True

    # provide sources within this package
    def export_sources(self):
        self.copy("src/*")
        self.copy("include/*")
        self.copy("CMakeLists.txt")

    # manipulate available options based on settings used
    def config_options(self):
        if self.settings.compiler == 'Visual Studio':
            del self.options.fPIC

    #def configure(self):

    # required software packages during execution
    def requirements(self):
        self.requires("poco/1.10.1@")

    #def package_id(self):

    # required software packages during build
    def build_requirements(self):
        self.build_requires("cmake/3.19.6@")

    #def system_requirements(self):

    #def build_id(self):

    # provide external source code from outside the package
    def source(self):
        pass

    # bring in required software package files needed at runtime
    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def _get_configured_cmake(self):
        cmake = CMake(self)
        #cmake.definitions["SOME_DEFINITION"] = "VALUE"
        cmake.configure()
        return cmake

    # compile the binaries of the package
    def build(self):
        self._get_configured_cmake().build()

    # bundle the necessary resources into the package
    def package(self):
        self._get_configured_cmake().install()
    
    # provide content information to the future consumer
    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        self.cpp_info.libs = ['dena_library']  # The libs to link against
        self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
        self.cpp_info.bindirs = ['bin']  # Directories where executables and shared libs can be found
