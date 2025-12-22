// Java Program to Illustrate Controller Class

package com.amiya.kafka.apachekafkaproducer;

// Importing required classes
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.web.bind.annotation.*;

// Annotation
@RestController

// Class
public class DemoController {

    // Autowiring Kafka Template
    @Autowired KafkaTemplate<String, String> kafkaTemplate;

    private static final String TOPIC = "NewTopic";

    // Publish messages using the GetMapping
    @GetMapping("/publish/{message}")
    public String publishMessage(@PathVariable("message")
                                 final String message)
    {

        // Sending the message
        kafkaTemplate.send(TOPIC, message);

        return "Published Successfully";
    }
}
