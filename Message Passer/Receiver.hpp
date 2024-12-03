#pragma once
#include "MessageFramework.hpp"

class Receiver {
public:
    Receiver(MessageFramework& framework);
    void handleMessage(const Message& msg);

private:
    void registerHandlers(MessageFramework& framework);
};
