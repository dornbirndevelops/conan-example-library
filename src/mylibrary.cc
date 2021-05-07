#include <mylibrary.h>
#include <mylibrary_internal.h>

#include <iostream>

namespace mylibrary {
    void print_boost_info() {
        std::cout << get_boost_info() << std::endl;
    }
}
