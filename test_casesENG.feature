Feature: Advantage Online Shopping Tests

  Scenario: Register a new user
    Given the user accesses the registration page
    When they fill in the required fields correctly
    And click the "Register" button
    Then the account should be created successfully

  Scenario: Login with valid credentials
    Given the user has a valid account
    When they enter their username and password correctly
    And click the "Login" button
    Then they should be redirected to the homepage logged in

  Scenario: Login with invalid credentials
    Given the user is on the login page
    When they enter an incorrect username or password
    And click the "Login" button
    Then an error message should be displayed

  Scenario: Add a product to the cart
    Given the user accesses a product page
    When they click the "Add to Cart" button
    Then the product should appear in the shopping cart

  Scenario: Remove an item from the cart
    Given the user has an item in the cart
    When they click the "Remove" button next to the product
    Then the item should be removed from the cart

  Scenario: Update item quantity in the cart
    Given the user has an item in the cart
    When they change the item quantity to "2"
    And confirm the update
    Then the item quantity in the cart should be "2"

  Scenario: Successfully complete a purchase
    Given the user has items in the cart
    When they click the "Checkout" button
    And fill in the payment and shipping details correctly
    And confirm the purchase
    Then the purchase should be completed successfully

  Scenario: Attempt to checkout without logging in
    Given the user has added items to the cart
    When they attempt to checkout without logging in
    Then the system should prompt them to log in before completing the purchase

  Scenario: Apply a valid discount coupon
    Given the user is on the cart page
    When they enter a valid discount coupon
    And confirm the coupon application
    Then the discount should be applied to the total purchase amount

  Scenario: Apply an invalid discount coupon
    Given the user is on the cart page
    When they enter an invalid discount coupon
    And confirm the coupon application
    Then an error message should be displayed

  Scenario: View order details on the profile page
    Given the user has completed a purchase
    When they access the orders page in their profile
    Then the purchase details should be displayed correctly

  Scenario: User logout
    Given the user is logged in
    When they click the "Logout" button
    Then they should be logged out and redirected to the homepage

  Scenario: Password recovery
    Given the user forgot their password
    When they access the "Forgot Password" option
    And enter their registered email
    Then the system should send a recovery link to their email

  Scenario: Filter products by category
    Given the user is on the products page
    When they select a specific category
    Then only products from that category should be displayed

  Scenario: Change delivery address in profile
    Given the user is on the profile page
    When they edit the delivery address
    And save the changes
    Then the new address should be updated correctly
