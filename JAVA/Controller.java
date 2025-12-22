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
  public List<UserDto> getAllUsers(
    @RequestHeader(name = "x-auth-token") String authToken,
    @RequestParam(required = false, defaultValue = "", name = "sort") String sort
  ) {

    if (!Set.of("name", "email").contains(sort))
        sort = "name";
    
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

  @PostMapping
  public ResponseEntity<UserDto> createUser(
    @Requestbody RegisterUserRequest request,
    UriComponentsBuilder uriBuilder
  ) {
    var user = userMapper.toEntity(request);
    userRepository.save(user);

    var userDto = usermapper.toDto(user);
    uriBuilder.path("/users/{id}").buildAndExpand(userDto.getId()).toUri();
    return ResponseEntity.created;
  }
}


@RestController
@AllArgsConstructor
@RequestMapping("/products")
public class ProductController {
  private final ProductRepository productRepository;
  private final ProductMapper productMapper;
  
  @GetMapping
  public List<ProductDto> getAllProducts(
    @RequesatParam(name = "categoryId", required = false) Byte categoryId
  ) {
    List<Product> products;
    if (categoryId != null) {
      products = productRepository.findByCategoryId(categoryId);
    }
    else {
      products = productRepository.findAllWithCategory();
    }
    return products.stream().map(productMapper::toDto).toList();
  }
