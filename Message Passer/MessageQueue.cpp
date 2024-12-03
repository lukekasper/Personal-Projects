#include "MessageQueue.hpp"

void MessageQueue::push(const Message& msg) {
    std::unique_lock<std::mutex> lock(mtx_);
    queue_.push(msg);
    cv_.notify_one();
}

Message MessageQueue::pop() {
    std::unique_lock<std::mutex> lock(mtx_);
    cv_.wait(lock, [this]() { return !queue_.empty(); });
    Message msg = queue_.front();
    queue_.pop();
    return msg;
}
