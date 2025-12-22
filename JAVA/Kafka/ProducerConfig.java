// Java program to serialize the
// object of the model class

@Configuration
public class StudentConfig {

    @Bean
    public ProducerFactory<String, Student>
    producerFactory()
    {
        // Create a map of a string
        // and object
        Map<String, Object> config
            = new HashMap<>();

        config.put(
            ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,
            "127.0.0.1:9092");

        config.put(
            ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG,
            StringSerializer.class);

        config.put(
            ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG,
            JsonSerializer.class);

        return new DefaultKafkaProducerFactory<>(config);
    }

    @Bean
    public KafkaTemplate<String, Student>
    kafkaTemplate()
    {
        return new KafkaTemplate<>(
            producerFactory());
    }
}
