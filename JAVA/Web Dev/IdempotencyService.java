@Service
public class IdempotencyService {

    private final StringRedisTemplate redis;
    private final ObjectMapper objectMapper;

    public IdempotencyService(StringRedisTemplate redis, ObjectMapper objectMapper) {
        this.redis = redis;
        this.objectMapper = objectMapper;
    }

    public Optional<String> getStoredResponse(String key) {
        String response = redis.opsForValue().get("idempotency:" + key + ":response");
        return Optional.ofNullable(response);
    }

    public boolean acquireLock(String key) {
        Boolean success = redis.opsForValue().setIfAbsent(
            "idempotency:" + key,
            "LOCKED",
            Duration.ofSeconds(30)
        );
        return Boolean.TRUE.equals(success);
    }

    public void storeResponse(String key, Object response) {
        try {
            String json = objectMapper.writeValueAsString(response);
            redis.opsForValue().set(
                "idempotency:" + key + ":response",
                json,
                Duration.ofHours(24)
            );
        } catch (Exception e) {
            throw new RuntimeException("Failed to serialize idempotent response", e);
        }
    }
}
