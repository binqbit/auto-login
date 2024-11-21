# Auto Login

### Description
This is a simple tool that allows you to automatically log in to various services in the terminal.

### Install
```bash
pip install -r requirements.txt
```

### Parameters
- `--admin`: This parameter is needed to provide access to the correct work if it is launched through the left software. `Optional`
- `--cmd`: The command that will be executed. `Optional`
- `--login`: Your login. `Optional`
- `--password`: Your password or password name in the keyring. `Optional`

### Keyring
- Create `.env` file in the root directory.
- Add the following lines to the file:
    ```env
    PASSWORDS = password_name1:password1, password_name2:password2
    ```

### Example Of Use
- Auto git pull:
    ```bash
    auto-login --cmd "git pull" --login your_login --password github_password_name
    ```

- Auto login to the server:
    ```bash
    auto-login --cmd "ssh user@server" --login your_login --password your_password
    ```

### How To Use
- Install the requirements.
- Add this path to the system PATH variable.
- Create a new shortcut on your desktop.
- Open the shortcut properties.
- Add the command to the target field: auto-login --admin --cmd <command> --login <your_login> --password <your_password>
- Add keys shortcuts to run this file.
- If you need to authenticate somewhere, you can press the key combination you need and the program will automatically enter the required credentials.