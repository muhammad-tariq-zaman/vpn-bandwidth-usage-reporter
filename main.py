"""Report VPN bandwidth use per user against a monthly limit.

Usage: python3 main.py usage.csv [--limit 5000]
CSV columns: user,download_mb,upload_mb.
Total = download + upload. OVER when the total exceeds the
limit (default 5000 MB), otherwise OK. Heaviest user first.
"""
import argparse, csv, sys
from collections import defaultdict

def report(rows, limit=5000):
    per_user = defaultdict(lambda: {"download": 0, "upload": 0})
    for row in rows:
        user = row["user"].strip()
        per_user[user]["download"] += int(row["download_mb"])
        per_user[user]["upload"] += int(row["upload_mb"])
    out = []
    for user in sorted(per_user):
        download = per_user[user]["download"]
        upload = per_user[user]["upload"]
        total = download + upload
        verdict = "OVER" if total > limit else "OK"
        out.append((user, download, upload, total, verdict))
    return sorted(out, key=lambda r: -r[3])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--limit", type=int, default=5000)
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        results = report(list(csv.DictReader(f)), args.limit)
    for user, download, upload, total, verdict in results:
        print(f"{user}: {verdict} ({download} MB down, {upload} MB up, {total} MB total)")
    print(f"{sum(1 for *_, v in results if v == 'OVER')} user(s) over the {args.limit} MB limit.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
