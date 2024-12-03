#include "MessageHandler.hpp"

void MessageHandler::registerHandler(int messageId, HandlerFunc handler) {
    handlers_[messageId] = handler;
}

void MessageHandler::handleMessage(const Message& msg) {
    if (handlers_.find(msg.id) != handlers_.end()) {
        handlers_[msg.id](msg);
    }
}
