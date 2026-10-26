# Thabo's Corner Store — Sales Insights System (Starter Code)

This is your starting scaffold. It already contains the **shape** of the
project — file structure, function signatures, imports and docstrings —
so you can focus on the actual data, database and programming logic
described in the Project Brief.

## Folder structure

```
starter\_code/
├── README.md              <- this file
├── requirements.txt        <- Python packages you need
├── main.py                 <- entry point; runs your whole pipeline
├── data\_cleaning.py         <- Task 2: load \& clean the raw CSVs
├── database.py              <- Task 3: build the SQLite database + SQL queries
├── analysis.py               <- Task 4: functions/loops/conditionals for insights
├── visualize.py               <- Task 5: charts with matplotlib
└── security.py                 <- Task 6: simple login / password hashing
```

## Before you start

1. Make sure Python 3.10+ is installed: `python3 --version`
2. Create a virtual environment (recommended):

```bash
   python3 -m venv venv
   source venv/bin/activate        # Windows: venv\\Scripts\\activate
   ```

3. Install the required packages:

```bash
   pip install -r requirements.txt
   ```

4. Copy the `data/` folder (provided separately) so it sits **next to**
`starter\_code/`, like this:

```
   project/
   ├── data/
   │   ├── products.csv
   │   └── sales.csv
   └── starter\_code/
       └── ... (these files)
   ```

## Running your program

Once you've completed the TODOs in each file:

```bash
python main.py
```

## A note on the TODOs

Every function you need to complete has:

* A docstring explaining **what** it must do
* A `# TODO:` comment explaining **the specific steps**
* `raise NotImplementedError` as a placeholder — delete this once you've
written your own code

Do not change the function names or the arguments they accept —
`main.py` calls them by name, and your facilitator's marking checklist
also references these exact names.

Good luck — and remember to commit your progress to GitHub regularly
as you complete each task, not just once at the end!



Project Completion and Results

Task 2: Data Cleaning



The raw CSV files were loaded and cleaned using pandas.



Products: 16 raw rows reduced to 12 cleaned rows.

Sales: 71 raw rows reduced to 43 cleaned rows.

Duplicate records and invalid or incomplete data were handled.

Missing payment and customer information was handled according to the cleaning rules.

Task 3: Database



A SQLite database was created to store product and sales information.



SQL queries were used to analyse revenue per product, best-selling products, sales by payment method, revenue by category, and monthly revenue.



Primary keys and foreign keys help maintain the relationships between products and sales.



Task 4: Programming and Analysis



Python functions, loops, conditionals, lists and dictionaries were used to analyse the cleaned data.



The program reported:



Total sales records: 43

Average basket size: 2.23 units per sale

Low-stock alert: Data Bundle 1GB



Monthly sales quantities were also calculated.



Task 5: Data Visualisation



Matplotlib was used to create and save two charts:



revenue\_per\_product.png — revenue per product.

monthly\_trend.png — monthly sales quantity trend.



These images can be included as evidence in the project submission.



Task 6: Security Reflection

1\. Confidentiality



The login gate restricts access to reports by requiring a password. Password hashing avoids storing the password directly as plain text. Limiting login attempts helps reduce repeated password guessing.



2\. Integrity



Primary keys help uniquely identify records, and foreign keys help ensure that sales reference valid products. Data validation and cleaning also help improve the reliability of the stored information.



3\. Availability



Keeping the project only on one laptop creates a risk of losing access because of hardware failure, theft or accidental deletion. Regular backups in a separate, secure location can reduce this risk.



How to Run the Project



From the project root directory, run:



powershell

python starter\_code\\main.py





Install the dependencies first if necessary:



powershell

python -m pip install -r starter\_code\\requirements.txt



Project Repository



GitHub: https://github.com/yamkelamvimbi7-collab/thabo-corner-store-project

