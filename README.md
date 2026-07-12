# Expense Tracker

A small terminal application for recording expenses and income by date.

## Run it

```sh
uv run python main.py
```

## Project structure

```text
nvim-expense_tracker/
├── ui/
│   └── menu.py              # Terminal display functions
├── category_mapping.py       # Transaction category commands
├── file_manager.py           # JSON file reading and writing
├── get_function.py           # Date input, totals, and summaries
├── main.py                   # Application entry point and main menu
├── transaction_manager.py    # Transaction state and operations
├── work_functions.py         # Transaction workflow
├── transaction.json          # Local data (ignored by Git)
└── pyproject.toml            # Project metadata and dependencies
```
