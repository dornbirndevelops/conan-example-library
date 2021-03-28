#include <dena_internal.h>

#include <Poco/MD5Engine.h>
#include <Poco/DigestStream.h>

namespace dena {
    std::string get_md5_internal(std::string content) {
        Poco::MD5Engine md5engine;
        Poco::DigestOutputStream ds(md5engine);
        ds << content;
        ds.close();
        return Poco::DigestEngine::digestToHex(md5engine.digest());
    }
}
