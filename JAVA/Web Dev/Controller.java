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

    var userDto = userMapper.toDto(user);
    var uri = uriBuilder.path("/users/{id}").buildAndExpand(userDto.getId()).toUri();
    return ResponseEntity.created(uri).body(userDto);
  }

  // Action-based request
  @PostMapping("/{id}/change-password")
  public ResponseEntity<Void> changePassword(
    @PathVariable(name = "id") Long id,
    @Requestbody ChangePasswordRequest request,
  ) {
    var user = userRepository.findById(id).orElse(null);
    if (user == null) {
      return ResponseEntity.notFound().build();
    }

    if (!user.getPassword().equals(request.getOldPassword())) {
      return new ResponseEntity<>(HttpStatus.UNAUTHORIZED);
    }

    // Only need to use mapper when updating large or complex objects, not simple string fields
    user.setPassword(request.getNewPassword());
    userRepository.save(user);
    return ResponseEntity.noContent().build();
  }

  @PutMapping("/{id}")
  public ResponseEntity<UserDto> updateUser(
    @PathVariable(name = "id") Long id,
    @Requestbody UpdateUserRequest request,
  ) {
    var user = userRepository.findById(id).orElse(null);
    if (user == null) {
      return ResponseEntity.notFound().build();
    }
    
    userMapper.update(request, user);
    userRepository.save(user);
    return ResponseEntity.ok(userMapper.toDto(user));
  }

  @DeleteMapping("/{id}")
  public ResponseEntity<Void> deleteUser(
    @PathVariable(name = "id") Long id,
  ) {
    var user = userRepository.findById(id).orElse(null);
    if (user == null) {
      return ResponseEntity.notFound().build();
    }
    
    userRepository.delete(user);
    return ResponseEntity.noContent().build();
  }
}


@RestController
@AllArgsConstructor
@RequestMapping("/products")
public class ProductController {
  private final ProductRepository productRepository;
  private final ProductMapper productMapper;
  private final CategoryRepository categoryRepository;
  private final IdempotencyService idempotencyService;
  
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

  /// IDEMPOTENCY EXAMPLE
  @PostMapping
  public ResponseEntity<ProductDto> createProduct(
    @RequestHeader("Idempotency-Key") String idempotencyKey,
    @Requestbody ProudctDto productDto,
    UriComponentsBuilder uriBuilder
  ) {
    
    // 1. Check if we already have a stored response
    var stored = idempotencyService.getStoredResponse(idempotencyKey);
    if (stored.isPresent()) {
        try {
            ProductDto dto = new ObjectMapper().readValue(stored.get(), ProductDto.class);
            URI uri = uriBuilder.path("/products/{id}")
                                .buildAndExpand(dto.getId())
                                .toUri();
            return ResponseEntity.created(uri).body(dto);
        } catch (Exception e) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }

    // 2. Try to acquire lock
    boolean lockAcquired = idempotencyService.acquireLock(idempotencyKey);
    if (!lockAcquired) {
        // Lock exists but no stored response → still processing
        return ResponseEntity.status(HttpStatus.CONFLICT)
                             .body(null);
    }

    // 3. Perform business logic
    var category = categoryRepository.findById(productDto.getCategoryId()).orElse(null);
    if (category == null) {
        return ResponseEntity.badRequest().build();
    }

    var product = productMapper.toEntity(productDto);
    product.setCategory(category);
    productRepository.save(product);

    productDto.setId(product.getId());
    URI uri = uriBuilder.path("/products/{id}")
                        .buildAndExpand(productDto.getId())
                        .toUri();

    // 4. Store final response
    idempotencyService.storeResponse(idempotencyKey, productDto);

    return ResponseEntity.created(uri).body(productDto);
  }

  @PutMapping("/{id}")
  public ResponseEntity<ProductDto> updateProduct(
    @PathVariable(name = "id") Long id,
    @Requestbody ProudctDto productDto,
  ) {
    var category = categoryRepository.findById(productDto.getCategoryId()).orElse(null);
    if (category == null) {
      return ResponseEntity.badRequest().build();
    }
    
    var product = productRepository.findById(id).orElse(null);
    if (product == null) {
      return ResponseEntity.notFound().build();
    }
    
    productMapper.update(productDto, product);
    product.setCategory(category);
    productRepository.save(product);
    productDto.setId(product.getId());
    return ResponseEntity.ok(productDto);
  }

  @DeleteMapping("/{id}")
  public ResponseEntity<Void> deleteProduct(
    @PathVariable(name = "id") Long id,
  ) {
    var product = productRepository.findById(id).orElse(null);
    if (product == null) {
      return ResponseEntity.notFound().build();
    }
    
    productRepository.delete(product);
    return ResponseEntity.noContent().build();
  }
}
