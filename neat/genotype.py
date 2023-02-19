import random

class Genotype:
    def __init__(self):
        self.nodes = []
        self.connections = []

    def add_node(self, node_id, node_type):
        self.nodes.append(NodeGene(node_id, node_type))

    def add_connection(self, id_in_node, id_out_node, enabled=True, innovation_number=None):
        weight = random.random() * 0.8 + 0.1
        self.connections.append(ConnectionGene(id_in_node, id_out_node, weight, enabled, innovation_number))


class NodeGene:
    def __init__(self, node_id, node_type):
        self.node_id = node_id
        self.node_type = node_type

class ConnectionGene:
    def __init__(self, in_node, out_node, weight, innovation_number=None, enabled=True):
        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.enabled = enabled
        self.innovation_number = innovation_number



"""
class Genotype:
    def __init__(self, input_size, output_size):
        self.nodes = []
        self.connections = []
        self.input_size = input_size
        self.output_size = output_size
        self.max_node_id = input_size + output_size - 1

        for i in range(input_size):
            self.nodes.append(NodeGene(i, 'input'))
        for i in range(output_size):
            node_id = i + input_size
            self.nodes.append(NodeGene(node_id, 'output'))

    def print_genotype(self):
        print("Nodes:")
        for node in self.nodes:
            print(node.id, node.type)
        print("Connections:")
        for conn in self.connections:
            print(conn.in_node, conn.out_node, conn.weight, conn.enabled, conn.innovation_number)

    def add_node(self, node_id, node_type):
        self.nodes.append(NodeGene(node_id, node_type))

    def add_connection(self, in_node, out_node, enabled=True, innovation_number=None):
        # The weight is set between 0.1 and 0.9
        weight = random.random() * 0.8 + 0.1
        self.connections.append(ConnectionGene(in_node, out_node, weight, enabled, innovation_number))

    def get_node(self, node_id):
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None

    def get_enabled_connections(self):
        return [conn for conn in self.connections if conn.enabled]

    def get_output_nodes(self):
        return [node for node in self.nodes if node.type == 'output']


class NodeGene:
    def __init__(self, node_id, node_type):
        self.id = node_id
        self.type = node_type
"""
"""

class ConnectionGene:
    def __init__(self, in_node, out_node, weight, enabled=True, innovation_number=None):
        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.enabled = enabled
        self.innovation_number = innovation_number
"""