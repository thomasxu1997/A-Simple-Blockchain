# Initializing our blockchain list
blockchain = [[1]]


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last block chain to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1])
    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a integer. """
    return int(input('Your transaction amount please: '))


def print_blockchain_elements():
    """ Output the blockchain list to the console """
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 50)


def get_user_choice():
    return input('Your choice: ')


def hack_blockchain():
    if len(blockchain) >= 1:
        blockchain[0] = 2


def verify_data():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        if block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


# Get thr first transaction input and add the value to the blockchain
tx_amount = get_transaction_value()
add_value(tx_amount)

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
        print(blockchain)
    elif user_choice == 'h':
        hack_blockchain()
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input invalid!')
    if not verify_data():
        print('Invalid blockchain!')
        break
else:
    print('User left!')

print('Done')
