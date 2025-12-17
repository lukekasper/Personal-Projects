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
public class PayPalPaymentService implements PaymentService {
  
  @Override
  public void processPayment(double amount) {
    System.out.print.ln("PAYPAL");
    System.out.print.ln("Amount: " + amount);
  }
}


/// Dependent Order Service
public class OrderService {
  
  private PaymentService paymentService;

  public OrderService(PaymentService paymentService) {
    this.paymentService = paymentService;
  }
  public void placeOrder() {
    paymentService.processPayment(amount: 10);
  }
}


/// Main
@SpringBootApplication
public class StoreApplication {
  
  public static void main(String[] args) {
    var orderService = new OrderService(new StripePaymentService());
    orderService.placeOrder();

    var orderService2 = new OrderService(new PayPalPaymentService());
    orderService2.placeOrder();
  }
}
  
