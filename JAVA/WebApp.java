@Controller
public class HomeController {
  @RequestMapping("/")
  public String index(Model model) {
    model.addAttribute("name", "luke");
    return "index";
  }
}


@RestController
public class MessageController {
  @RequestMapping("/hello")
  public Message sayHello() {
    return new Message("Hello World!);
  }
}


@RestController
@AllArgsConstructor
@RequestMapping("/users")
public class UserController {
  private final UserRepository userRepository;
  private final UserMapper userMapper;
  
  @GetMapping
  public List<UserDto> getAllUsers(@RequestParam String sort) {
    return userRepository.findAll(Sort.by(sort))
        .stream()
        .map(userMapper::toDto)
        .toList();  /// userRepository extends JpaRepository
  }

  @GetMapping("/{id}")
  public ResponseEntity<UserDto> getUser(@PathVariable Long id) {
    var user = userRepository.findById(id).orElse(null);
    if (user == null) {
      return ResponseEntity.notFound().build();
    }
    return ResponseEntity.ok(userMapper.toDto(user));
  }
}
