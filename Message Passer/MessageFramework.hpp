#pragma once
#include <thread>
#include "MessageQueue.hpp"
#include "MessageHandler.hpp"

class MessageFramework {
public:
    void start();
    void stop();
    void sendMessage(const Message& msg);
    void registerHandler(int messageId, MessageHandler::HandlerFunc handler);

private:
    void processMessages();

    MessageQueue messageQueue_;
    MessageHandler messageHandler_;
    std::thread workerThread_;
    bool running_ = true;
};
