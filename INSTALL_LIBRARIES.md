# Installing Required Libraries

Since pandas and numpy are not yet installed in your environment, you'll need to install them to run the tutorials.

## Option 1: Using pip (Recommended)
```bash
python3 -m pip install pandas numpy --break-system-packages
```

## Option 2: Using pip with user flag
```bash
python3 -m pip install --user pandas numpy
```

## Option 3: System package manager (if available)
```bash
# For Ubuntu/Debian systems (if you have admin access)
sudo apt update
sudo apt install python3-pandas python3-numpy
```

## Verification
After installation, run:
```bash
python3 getting_started.py
```

You should see "✅ pandas" and "✅ numpy" messages instead of error messages.

## Troubleshooting

If you still get permission errors:
1. Try creating a virtual environment (if venv is available)
2. Use the `--break-system-packages` flag as shown in Option 1
3. Contact your system administrator if you're on a managed system

## What's Included
Once installed, you'll have access to:
- pandas for data manipulation and analysis
- numpy for numerical operations
- All the tutorial files will work correctly

Happy learning! 🐍📊