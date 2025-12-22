@Service
public class KafkaService {

    // Annotation required to listen
    // the message from Kafka server
    @KafkaListener(topics = "JsonTopic",
                   groupId = "id", containerFactory
                                   = "studentListner")
    public void
    publish(Student student)
    {
        System.out.println("New Entry: "
                           + student);
    }
}
