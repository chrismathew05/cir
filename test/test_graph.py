from app.graph import CircuitGraph

import unittest
import logging

logger = logging.getLogger(__name__)


class TestGraph(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("\n=== TESTING GRAPH.PY ===")

    def test_graph(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
