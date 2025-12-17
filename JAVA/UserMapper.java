@Mapper(componentModel = "spring)
public interface UserMapper {
  @Mapping(target = "timestamp", expression = "java(java.time.LocalDateTime.now())")
  UserDto toDto(User user);
}
