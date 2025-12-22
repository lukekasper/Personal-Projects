@Mapper(componentModel = "spring")
public interface UserMapper {
  @Mapping(target = "timestamp", expression = "java(java.time.LocalDateTime.now())")
  UserDto toDto(User user);
  User toEntity(RegisterUserRequest request);
  void update(UpdateUserRequest request, @MappingTarget User, user);
}


@Mapper(componentModel = "spring")
public interface ProductMapper {
  @Mapping(target = "categoryId", source = "category.id")
  ProductDto toDto(Product product);
  Product toEntity(ProductDto productDto);
  @Mapping(target = "id", ignore = true)
  void update(ProductDto productDto, @MappingTarget Product, product);
}
