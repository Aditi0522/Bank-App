# Fun Bank Account System

Welcome to our fun and interactive bank account management system! Manage your virtual accounts with ease. Ready? Let's go!

## Features

1. **Create Account** 📝
2. **Use Account** 🔑
3. **Update Account** ✏️
4. **Delete Account** 🗑️
5. **Exit** 🚪

## How It Works

### Bank Account Class

#### Methods

- **create_account(name, phone, pw, amt)**: This method allows you to create a new bank account by providing your name, phone number, a password, and an initial deposit amount. Each new account gets a unique account ID, and you'll get a friendly reminder to note it down.

- **use_account()**: Access your account by entering your account ID and password. Once authenticated, you can:
  - Transfer money to another account.
  - Deposit money into your account.
  - Withdraw money from your account.
  - Check your current account balance.
  - Exit the menu.

- **update_account()**: Update your account details by entering your account ID and password. You can update your name, phone number, or password.

- **delete_account()**: Delete your account by entering your account ID and password. If confirmed, the account will be marked as deleted and removed from the active accounts list.

### Main Menu Function

Displays a fun and user-friendly menu to create, use, update, or delete an account. You can navigate through the options by entering the corresponding index number.

- **Create Account**: Enter your details and create a new account.
- **Use Account**: Access and manage your account operations.
- **Update Account**: Modify your existing account details.
- **Delete Account**: Permanently remove your account.
- **Exit Application**: Close the application.

Enjoy managing your accounts with our simple and fun system!
