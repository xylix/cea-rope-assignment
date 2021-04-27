from rope import (
    Rope,
    delete_range,
    insert,
    create_rope_from_map,
    rotate_left,
    rotate_right,
    rebalance,
)
import unittest

# These tests are here as a starting point, they are not comprehensive
class Testing(unittest.TestCase):
    def test_rope_basics(self):
        self.assertEqual(Rope("test").to_string(), "test")

    def test_deletion(self):
        self.assertEqual(delete_range(Rope("test"), 1, 2).to_string(), "tst")
        self.assertEqual(delete_range(Rope("test"), 2, 4).to_string(), "te")
        self.assertEqual(delete_range(Rope("test"), 0, 2).to_string(), "st")

    def test_insertion(self):
        self.assertEqual(insert(Rope("test"), "123", 2).to_string(), "te123st")
        self.assertEqual(insert(Rope("test"), "123", 4).to_string(), "test123")
        self.assertEqual(insert(Rope("test"), "123", 0).to_string(), "123test")

    def test_extra_credit_rebalancing(self):
        self.assertEqual(
            rotate_left(
                create_rope_from_map(
                    {
                        "text": "3",
                        "left": {"text": "a"},
                        "right": {
                            "text": "5",
                            "left": {"text": "b"},
                            "right": {
                                "text": "7",
                                "left": {"text": "c"},
                                "right": {"text": "d"},
                            },
                        },
                    }
                )
            ).to_dictionary(),
            {
                "text": "5",
                "left": {"text": "3", "left": {"text": "a"}, "right": {"text": "b"}},
                "right": {"text": "7", "left": {"text": "c"}, "right": {"text": "d"}},
            },
        )
        self.assertEqual(
            rotate_right(
                create_rope_from_map(
                    {
                        "text": "5",
                        "left": {
                            "text": "3",
                            "right": {"text": "b"},
                            "left": {
                                "text": "2",
                                "left": {"text": "d"},
                                "right": {"text": "c"},
                            },
                        },
                        "right": {"text": "a"},
                    }
                )
            ).to_dictionary(),
            {
                "text": "3",
                "left": {"text": "2", "left": {"text": "d"}, "right": {"text": "c"}},
                "right": {"text": "5", "left": {"text": "b"}, "right": {"text": "a"}},
            },
        )

        balancedTree = {"text": "b", "left": {"text": "a"}, "right": {"text": "c"}}

        self.assertEqual(
            rebalance(
                create_rope_from_map(
                    {
                        "text": "c",
                        "left": {"text": "a", "right": {"text": "b"}},
                    }
                )
            ).to_dictionary(),
            balancedTree,
        )
        self.assertEqual(
            rebalance(
                create_rope_from_map(
                    {
                        "text": "c",
                        "left": {"text": "b", "left": {"text": "a"}},
                    }
                )
            ).to_dictionary(),
            balancedTree,
        )
        self.assertEqual(
            rebalance(
                create_rope_from_map(
                    {
                        "text": "a",
                        "right": {"text": "b", "right": {"text": "c"}},
                    }
                )
            ).to_dictionary(),
            balancedTree,
        )
        self.assertEqual(
            rebalance(
                create_rope_from_map(
                    {
                        "text": "a",
                        "right": {"text": "c", "left": {"text": "b"}},
                    }
                )
            ).to_dictionary(),
            balancedTree,
        )


if __name__ == "__main__":
    unittest.main()
