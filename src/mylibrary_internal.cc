#include <mylibrary_internal.h>

#include <boost/version.hpp>
#include <sstream>

namespace mylibrary {
    std::string get_boost_info() {
        std::stringstream ss;
        ss << "Using Boost "     
          << BOOST_VERSION / 100000     << "."  // major version
          << BOOST_VERSION / 100 % 1000 << "."  // minor version
          << BOOST_VERSION % 100;               // patch level
        return ss.str();
    }
}
