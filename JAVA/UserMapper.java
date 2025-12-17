@Mapper(componentModel = "spring)
public interface UserMapper {
  UserDto toDto(User user);
}
