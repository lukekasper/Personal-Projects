#include "Sender.hpp"
#include <chrono>
#include <thread>

Sender::Sender(MessageFramework& framework) : framework_(framework) {}

void Sender::sendMessages() {
    for (int i = 1; i <= 5; ++i) {
        Message msg = {i, "Sender", "Receiver", "Message " + std::to_string(i)};
        framework_.sendMessage(msg);
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
}
