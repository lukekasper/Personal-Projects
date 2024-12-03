#pragma once
#include <string>

struct Message {
    int id;
    std::string sender;
    std::string receiver;
    std::string payload;
};
