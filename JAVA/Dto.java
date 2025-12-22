@AllArgsConstructor
@Data
public class UserDto {
  /// remove field from json objects
  @JsonIgnore
  private Long id;

  /// rename field
  @JsonProperty("username")
  private String name;
  private String email;

  /// Exclude NULL values
  @JsonInclude(JsonInclude.Include.NON_NULL)
  private String phoneNumber;

  @JsonFormat(pattern = "yyy-MM-dd HH:mm:ss")
  private LocalDateTime timestamp;
}


@AllArgsConstructor
@Data
public class ProductDto {
  private Long id;
  private String name;
  private BigDecimal price;
  private String description;
  private Byte categoryId;
}

@Data
public class RegisterUserRequest {
  private String name;
  private String email;
  private String password;
}

@Data
public class UpdateUserRequest {
  private String name;
  private String email;
}
