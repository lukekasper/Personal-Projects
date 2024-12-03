#include "MessageFramework.hpp"

void MessageFramework::start() {
    workerThread_ = std::thread([this]() { processMessages(); });
}

void MessageFramework::stop() {
    running_ = false;
    if (workerThread_.joinable()) {
        workerThread_.join();
    }
}

void MessageFramework::sendMessage(const Message& msg) {
    messageQueue_.push(msg);
}

void MessageFramework::registerHandler(int messageId, MessageHandler::HandlerFunc handler) {
    messageHandler_.registerHandler(messageId, handler);
}

void MessageFramework::processMessages() {
    while (running_) {
        Message msg = messageQueue_.pop();
        messageHandler_.handleMessage(msg);
    }
}
