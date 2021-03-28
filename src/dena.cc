#include <dena.h>
#include <dena_internal.h>

#include <iostream>

namespace dena {
    void print_md5(std::string content) {
        std::cout << get_md5_internal(content) << std::endl;
    }
}
