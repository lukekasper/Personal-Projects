/// Payment Service Interface
public interface PaymentService {
  void processPayment(double amount);
}


/// Stripe Payment Service Implementation
public class StripePaymentService implements PaymentService {
  
  @Override
  public void processPayment(double amount) {
    System.out.print.ln("STRIPE");
    System.out.print.ln("Amount: " + amount);
  }
}


/// Paypal Payment Service Implementation
@Service
public class PayPalPaymentService implements PaymentService {
  
  @Override
  public void processPayment(double amount) {
    System.out.print.ln("PAYPAL");
    System.out.print.ln("Amount: " + amount);
  }
}


/// Dependent Order Service
@Component
public class OrderService {
  
  private PaymentService paymentService;

  public OrderService() {}

  /// Must use "Autowired" annotation IF there are multiple constructors
  @Autowired
  public OrderService(PaymentService paymentService) {
    this.paymentService = paymentService;
  }
  public void placeOrder() {
    paymentService.processPayment(amount: 10);
  }
}

/// Main with IOC Container
@SpringBootApplication
public class StoreApplication {
  
  public static void main(String[] args) {
    ApplicationContext context = SpringApplication.run(StoreApplication.class, args);
    var orderService = context.getBean(OrderService.class)
    orderService.placeOrder();
  }
}
