# vpn-bandwidth-usage-reporter

Report VPN bandwidth use per user from a CSV: total = download + upload, OVER when it exceeds the limit (default 5000 MB), otherwise OK — heaviest user first.

## How to run

```sh
python3 main.py usage.csv
```

## Example output

```
ali: OVER (3000 MB down, 2500 MB up, 5500 MB total)
sara: OK (1000 MB down, 500 MB up, 1500 MB total)
1 user(s) over the 5000 MB limit.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
