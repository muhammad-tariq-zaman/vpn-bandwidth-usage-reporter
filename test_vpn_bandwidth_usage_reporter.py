import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import report

def row(u, down, up):
    return {"user": u, "download_mb": str(down), "upload_mb": str(up)}

class TestVPNBandwidth(unittest.TestCase):
    def test_total_computed(self):
        self.assertEqual(report([row("ali", 3000, 2500)])[0][3], 5500)
    def test_over_limit(self):
        self.assertEqual(report([row("ali", 3000, 2500)])[0][4], "OVER")
    def test_ok_under_limit(self):
        self.assertEqual(report([row("ali", 1000, 500)])[0][4], "OK")
    def test_exactly_at_limit_ok(self):
        self.assertEqual(report([row("ali", 4000, 1000)])[0][4], "OK")
    def test_rows_aggregated_per_user(self):
        self.assertEqual(report([row("ali", 1000, 0), row("ali", 2000, 0)])[0][3], 3000)
    def test_heaviest_first(self):
        r = report([row("a", 100, 0), row("b", 4000, 0)])
        self.assertEqual(r[0][0], "b")
