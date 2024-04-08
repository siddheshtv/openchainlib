import hashlib

class OpenChainBlock:
    def __init__(self, previous_hash_block, full_nodes_list, light_nodes_list, transaction_list, worker_nodes_list) -> None:
        self.previous_hash_block = previous_hash_block
        self.full_nodes_list = full_nodes_list
        self.light_nodes_list = light_nodes_list
        self.transaction_list = transaction_list
        self.worker_nodes_list = worker_nodes_list
        return None

