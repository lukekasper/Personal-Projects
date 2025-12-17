@AllArgsConstructor
@Getter
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
