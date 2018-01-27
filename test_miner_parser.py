import miner_parser
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)


class TestMinerParser(unittest.TestCase):
    def test_parse_miner(self):
        # Set up the test input and expected output
        testdata = [
            {"test_input": "Jan 14 13:55:15 server1 cpuminer[2355]: accepted: 94/94 (100.00%), 1.15 khash/s (yay!!!)",
             "expected": (
                "miner.hashrate",
                1515938115,
                1150.0,
                {"metric_type": "gauge",
                 "unit": "hash/s",
                 "tags": "pid:2355"})},
            {"test_input": "Jan 14 13:55:15 server1 cpuminer[2355]: accepted: 2118/2126 (99.62%), 1.15 khash/s (booooo)",
             "expected": None},
            {"test_input": "Jan 14 13:55:15 server1 ccminer[4345]: accepted: 27/27 (diff 0.443), 13.91 MH/s (yes!)",
             "expected": (
                "miner.hashrate",
                1515938115,
                13910000.0,
                {"metric_type": "gauge",
                 "unit": "hash/s",
                 "tags": "pid:4345"})},
            {"test_input": "Jan 14 13:55:15 server1 ccminer[589]: accepted: 1591/1592 (diff 0.030), 13.86 MH/s (booooo)",
             "expected": None},
            {"test_input": "Jan 14 13:36:58 botia systemd[1]: Started Start CPUMiner.",
             "expected": None},
        ]
        for data in testdata:
            actual = miner_parser.parse_miner(logging, data['test_input'])
            expected = data['expected']
            self.assertEqual(expected, actual, "%s != %s" % (expected, actual))
