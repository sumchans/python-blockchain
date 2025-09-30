genesis_block = {
    'previous_hash':'', 
    'index':0, 
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Sumesh'
participants = {'Sumesh'}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount}
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)
   

def mine_block():
    last_block = blockchain[-1]
    """
    The line creates a string representation of the last block's contents by:
        Iterating over each key in last_block.
        Converting each value to a string: str(last_block[key]).
        Joining all these string values with hyphens (-) between them.
    """
    hashed_block = hash_block(last_block)
    print(hashed_block)
    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain), 
        'transactions': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the transaction: ') 
    tx_amount= float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)

def get_user_choice():
    user_input=input('Your choice: ')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20)

def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True    
    

waiting_for_input = True

while waiting_for_input:
    print('Please choose: ')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')

    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        # print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash':'', 
                'index':0, 
                'transactions': [{'sender':'Sumesh', 'recipient':'Shalini', 'amount':'18'}]
        }
    elif user_choice == 'q':
        waiting_for_input = False      
    else:
        print('Input was invalid, please pick a value from list!')

    verify_chain()
    
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break

else:
    print('User left!')

print('Done!')