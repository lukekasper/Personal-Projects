https://www.geeksforgeeks.org/java/spring-boot-kafka-producer-example/

#### Steps to publish messages in Kafka:
1.  Run Apache Zookeeper server: `C:\kafka>.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties`
2.  Run Apache Kafka server: `C:\kafka>.\bin\windows\kafka-server-start.bat .\config\server.properties`
3.  Listen to messages coming from new topics: `C:\kafka>.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic NewTopic --from-beginning`
