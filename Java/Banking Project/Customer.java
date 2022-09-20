package banking;

public class Customer {

		String name;
		String address;
		
		/**
		 * Creates instance of Customer.
		 * @param name
		 */
		public Customer(String name) {
			this.name = name;
		}
		
		public void setAddress(String address) {
			this.address = address;
		}
		
		public String getName() {
			return this.address;
		}
}
