@EnableKafka
@Configuration
public class Config {

    // Function to establish a connection
    // between Spring application
    // and Kafka server
    @Bean
    public ConsumerFactory<String, Student>
    studentConsumer()
    {

        // HashMap to store the configurations
        Map<String, Object> map
            = new HashMap<>();

        // put the host IP in the map
        map.put(ConsumerConfig
                    .BOOTSTRAP_SERVERS_CONFIG,
                "127.0.0.1:9092");

        // put the group ID of consumer in the map
        map.put(ConsumerConfig
                    .GROUP_ID_CONFIG,
                "id");
        map.put(ConsumerConfig
                    .KEY_DESERIALIZER_CLASS_CONFIG,
                StringDeserializer.class);
        map.put(ConsumerConfig
                    .VALUE_DESERIALIZER_CLASS_CONFIG,
                JsonDeserializer.class);

        // return message in JSON formate
        return new DefaultKafkaConsumerFactory<>(
            map, new StringDeserializer(),
            new JsonDeserializer<>(Student.class));
    }

    @Bean
    public ConcurrentKafkaListenerContainerFactory<String,
                                                   Student>
    studentListner()
    {
        ConcurrentKafkaListenerContainerFactory<String,
                                                Student>
            factory
            = new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(studentConsumer());
        return factory;
    }
}
