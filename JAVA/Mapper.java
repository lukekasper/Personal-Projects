@Mapper(componentModel = "spring")
public interface UserMapper {
  @Mapping(target = "timestamp", expression = "java(java.time.LocalDateTime.now())")
  UserDto toDto(User user);
}

@Mapper(componentModel = "spring")
public interface ProductMapper {
  @Mapping(target = "categoryId", source = "category.id")
  ProductDto toDto(Product product);
}
