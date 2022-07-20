from app.graph import CircuitGraph

import unittest
import logging

logger = logging.getLogger(__name__)


class TestGraph(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up circuit graph instances for testing"""

        logger.info("\n=== TESTING GRAPH.PY ===")
        cls.A = CircuitGraph("app/circuits/test/test.xml")

    def test_find_cycles(self) -> None:
        """Test ability to find cycles"""

        cycles = self.A.find_cycles()
        self.assertEqual(cycles, [])

    def test_find_paths(self) -> None:
        """Test ability to find paths"""

        paths = self.A.find_paths("board_0_wire_0", "board_0_wire_1")
        self.assertEqual(
            paths, [["board_0_wire_0", "board_0_wire_2", "board_0_wire_1"]]
        )


if __name__ == "__main__":
    unittest.main()
