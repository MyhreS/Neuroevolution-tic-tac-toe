import unittest
import unittest
import random
from genotype import Genotype, NodeGene, ConnectionGene

class TestNodeGene(unittest.TestCase):
    def test_init(self):
        node = NodeGene(0, 'input')
        self.assertEqual(node.node_id, 0)
        self.assertEqual(node.node_type, 'input')

class TestConnectionGene(unittest.TestCase):
    def test_init(self):
        connection = ConnectionGene(0, 1, 0.5, 0, True)
        self.assertEqual(connection.in_node, 0)
        self.assertEqual(connection.out_node, 1)
        self.assertEqual(connection.weight, 0.5)
        self.assertEqual(connection.enabled, True)
        self.assertEqual(connection.innovation_number, 0)
class TestGenotype(unittest.TestCase):
    def test_init(self):
        genotype = Genotype()
        self.assertEqual(genotype.nodes, [])
        self.assertEqual(genotype.connections, [])
    def test_add_node(self):
        genotype = Genotype()
        genotype.add_node(0, 'input')
        self.assertEqual(len(genotype.nodes), 1)
        self.assertEqual(genotype.nodes[0].node_id, 0)
        self.assertEqual(genotype.nodes[0].node_type, 'input')

    def test_add_connection(self):
        genotype = Genotype()
        genotype.add_connection(0, 1, 0, True)
        self.assertEqual(len(genotype.connections), 1)
        self.assertEqual(genotype.connections[0].in_node, 0)
        self.assertEqual(genotype.connections[0].out_node, 1)
        self.assertEqual(genotype.connections[0].enabled, True)
        self.assertEqual(genotype.connections[0].innovation_number, 0)


if __name__ == '__main__':
    unittest.main()
