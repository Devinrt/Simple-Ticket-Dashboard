# Simple Ticket Dashboard

A Python script that converts a raw help‑desk ticket export into quick‑hit KPIs
(ticket volume, average resolution time, SLA breaches, etc.).

## Why this exists
Incorporates Automation into the help desk position, with this you can:
* Work with CSV data exports
* Understand common help‑desk metrics

## How to run

```bash
python ticket_stats.py sample_tickets.csv
```

You’ll see something like:

```
Total tickets: 10
Closed tickets: 9
Open tickets: 1
Avg. resolution time: 6h 12m
SLA breaches (>24h): 2
```

## Files

| File | Purpose |
|------|---------|
| `ticket_stats.py` | Main script |
| `sample_tickets.csv` | Example data you can replace with your own export |
| `.gitignore` | Keeps the repo clean |
| `LICENSE` | MIT license |
