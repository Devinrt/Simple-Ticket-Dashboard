"""Simple KPI calculator for help‑desk tickets."""
import csv, sys
from datetime import datetime, timedelta

DATE_FMT = "%Y-%m-%d %H:%M"

def parse_csv(path):
    with open(path, newline='') as fh:
        return list(csv.DictReader(fh))

def kpis(rows):
    closed = [r for r in rows if r['status'].lower() == 'closed']
    open_tickets = [r for r in rows if r['status'].lower() != 'closed']
    total = len(rows)
    avg_res_ms = 0
    breaches = 0
    for r in closed:
        created = datetime.strptime(r['created_at'], DATE_FMT)
        resolved = datetime.strptime(r['resolved_at'], DATE_FMT)
        delta = resolved - created
        avg_res_ms += delta.total_seconds()
        if delta > timedelta(hours=24):
            breaches += 1
    avg_res = avg_res_ms / len(closed) if closed else 0
    return {
        'total': total,
        'closed': len(closed),
        'open': len(open_tickets),
        'avg_res_hours': avg_res/3600,
        'sla_breaches': breaches
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python ticket_stats.py <csv_file>")
        return
    rows = parse_csv(sys.argv[1])
    stats = kpis(rows)
    print(f"Total tickets: {stats['total']}")
    print(f"Closed tickets: {stats['closed']}")
    print(f"Open tickets: {stats['open']}")
    print(f"Avg. resolution time: {stats['avg_res_hours']:.1f} hours")
    print(f"SLA breaches (>24h): {stats['sla_breaches']}")

if __name__ == "__main__":
    main()
