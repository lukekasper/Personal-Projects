// Creating a custom exception that can be thrown when a user tries to add a customer that already exists
package com.customer.exception;

public class CustomerAlreadyExistsException extends RuntimeException {
    private String message;

    public CustomerAlreadyExistsException() {}

    public CustomerAlreadyExistsException(String msg) {
        super(msg);
        this.message = msg;
    }
}

// Creating a custom exception that can be thrown when a user tries to update/delete a customer that doesn't exist
public class NoSuchCustomerExistsException extends RuntimeException {
    private String message;

    public NoSuchCustomerExistsException() {}

    public NoSuchCustomerExistsException(String msg) {
        super(msg);
        this.message = msg;
    }
}
