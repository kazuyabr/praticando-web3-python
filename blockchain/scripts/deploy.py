from ape import accounts, project

def deploy():
    account = accounts.load("FileHashRegistry")
    # Assume you have a contract named `MyContract` in your project's contracts folder.
    return account.deploy(project.FileHashRegistry)