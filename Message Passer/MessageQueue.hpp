#pragma once
#include <queue>
#include <mutex>
#include <condition_variable>
#include "Message.hpp"

class MessageQueue {
public:
    void push(const Message& msg);
    Message pop();

private:
    std::queue<Message> queue_;
    std::mutex mtx_;
    std::condition_variable cv_;
};
