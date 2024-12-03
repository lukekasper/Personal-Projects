#pragma once
#include <functional>
#include <unordered_map>
#include "Message.hpp"

class MessageHandler {
public:
    using HandlerFunc = std::function<void(const Message&)>;

    void registerHandler(int messageId, HandlerFunc handler);
    void handleMessage(const Message& msg);

private:
    std::unordered_map<int, HandlerFunc> handlers_;
};
