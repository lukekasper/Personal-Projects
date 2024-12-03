#include "MessageFramework.hpp"
#include "Sender.hpp"
#include "Receiver.hpp"

int main() {
    MessageFramework framework;
    framework.start();

    Sender sender(framework);
    Receiver receiver(framework);

    std::thread senderThread([&sender]() { sender.sendMessages(); });

    // Wait for the sender to finish
    senderThread.join();

    // Give some time for the receiver to process all messages
    std::this_thread::sleep_for(std::chrono::seconds(1));

    framework.stop();
    return 0;
}
