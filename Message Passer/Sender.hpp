#pragma once
#include "MessageFramework.hpp"

class Sender {
public:
    Sender(MessageFramework& framework);
    void sendMessages();

private:
    MessageFramework& framework_;
};
