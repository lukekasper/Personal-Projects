#include "Receiver.hpp"
#include <iostream>

Receiver::Receiver(MessageFramework& framework) {
    registerHandlers(framework);
}

void Receiver::registerHandlers(MessageFramework& framework) {
    for (int i = 1; i <= 5; ++i) {
        framework.registerHandler(i, [this](const Message& msg) { handleMessage(msg); });
    }
}

void Receiver::handleMessage(const Message& msg) {
    std::cout << "Received Message: " << msg.payload << " from " << msg.sender << std::endl;
}
