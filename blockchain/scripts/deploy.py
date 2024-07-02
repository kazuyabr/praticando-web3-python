from ape import accounts, project
from ape_accounts import generate_account

def deploy():
    
    account, mnemonic = generate_account("ganache-account", "law pigeon tree lunch exile gasp setup legal nurse tray drill sting")
    
    # Assume you have a contract named `MyContract` in your project's contracts folder.
    return account.deploy(project.FileHashRegistry)

def main():
    deploy()

if __name__ == "__main__":
    main()