from conans import ConanFile, CMake


class DenaLibraryConan(ConanFile):
    name = "dena_library"
    version = "1.0"
    # The combination of these fields make a package unique
    settings = "os", "compiler", "build_type", "arch"
    # Conan creates for the required Conan packages
    # a find_package script (module style)
    generators = "cmake_find_package"
    # If a required Conan package does not have binary package
    # then it can build it.
    build_policy = "missing"
    url = "https://github.com/dornbirndevelops/conan-example-library"
    license = "feel free to use it"
    description = "Example showcase on how to develop a C++ library depending on other libraries with Conan Package Manager and CMake"

    # Tools required for building
    def build_requirements(self):
        self.build_requires("cmake/3.19.6@")

    # Conan packages needed for building
    def requirements(self):
        self.requires("poco/1.10.1@")

    # Copy the source files (relative to conanfile.py)
    # into the Conan package (self.export_sources_folder)
    def export_sources(self):
        self.copy("src/*")
        self.copy("include/*")
        self.copy("CMakeLists.txt")
        self.copy("conanfile.py")

    def _configure_cmake(self):
        cmake = CMake(self)
        #cmake.definitions["SOME_DEFINITION"] = "VALUE"
        cmake.configure()
        return cmake

    # How to build the package
    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    # How to create the package
    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        self.cpp_info.libs = ['dena_library']  # The libs to link against
        #self.cpp_info.system_libs = []  # System libs to link against
        self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
        #self.cpp_info.resdirs = ['res']  # Directories where resources, data, etc. can be found
        #self.cpp_info.bindirs = ['bin']  # Directories where executables and shared libs can be found
        #self.cpp_info.srcdirs = []  # Directories where sources can be found (debugging, reusing sources)
        #self.cpp_info.build_modules = {}  # Build system utility module files
        #self.cpp_info.defines = []  # preprocessor definitions
        #self.cpp_info.cflags = []  # pure C flags
        #self.cpp_info.cxxflags = []  # C++ compilation flags
        #self.cpp_info.sharedlinkflags = []  # linker flags
        #self.cpp_info.exelinkflags = []  # linker flags
        #self.cpp_info.components  # Dictionary with the different components a package may have
        #self.cpp_info.requires = None  # List of components from requirements
