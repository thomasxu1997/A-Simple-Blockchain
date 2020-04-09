# 初始化区块链，假设祖先区块的值为1
blockchain = [[1]]


def chain_updation():
    blockchain.append([pre_block, cur_block])


def get_pre_block():
    return blockchain[-1]


def get_cur_block():
    return int(input("current block value: "))


pre_block = get_pre_block()
cur_block = get_cur_block()
chain_updation()

pre_block = get_pre_block()
cur_block = get_cur_block()
chain_updation()

pre_block = get_pre_block()
cur_block = get_cur_block()
chain_updation()

print(blockchain)
