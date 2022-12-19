from unittest import TestCase, main
from unittest.mock import ANY
from aocfw import TestCaseMixin
from p1 import Solution
from graph import AdjacencyList


class SolutionTests(TestCase, TestCaseMixin):

    solution = Solution
    source = 'sample.txt'
    given = 1651

    def create_graph(self):
        graph = AdjacencyList()
        for v, w, e in self.get_parsed_data():
            graph.set_vertex_value(v, w)
            [graph.add_edge(v, a) for a in e]
        return graph

    def test_graph(self):
        graph = self.create_graph()
        self.assertSetEqual(set(graph.get_adjacent('AA')), {'DD', 'II', 'BB'})
        self.assertSetEqual(set(graph.get_adjacent('BB')), {'CC', 'AA'})
        self.assertSetEqual(set(graph.get_adjacent('CC')), {'DD', 'BB'})
        self.assertSetEqual(set(graph.get_adjacent('JJ')), {'II'})

    def test_graph_get_path(self):
        graph = self.create_graph()
        self.assertListEqual(graph.get_path('AA', 'EE'), ['DD', 'EE'])
        self.assertListEqual(graph.get_path('JJ', 'HH'), ['II', 'AA', 'DD', 'EE', 'FF', 'GG', 'HH'])
        dd_bb = graph.get_path('DD', 'BB')
        self.assertListEqual(dd_bb, [ANY, 'BB'])
        if dd_bb[0] != 'AA' and dd_bb[0] != 'CC':
            self.fail('get_path returned incorrect value')

    def test_compute_target_values(self):
        s = Solution.new()
        s.build_graph(self.get_parsed_data())
        ans = s.compute_target_values('AA', 'DD', 30)
        self.assertTupleEqual(ans, (28, 560))

    def test_compute_target_path(self):
        s = Solution.new()
        s.build_graph(self.get_parsed_data())
        ans = s.compute_target_path(['AA', 'DD', 'BB', 'JJ', 'HH', 'EE', 'CC'])
        self.assertEqual(ans, 1651)


if __name__ == '__main__':
    main()
