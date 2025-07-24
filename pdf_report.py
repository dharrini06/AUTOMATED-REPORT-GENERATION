import pandas as pd
from fpdf import FPDF

# Step 1: Load Data
df = pd.read_csv("data.csv")  # Replace with your actual file
summary = df.describe()

# Step 2: Generate PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Automated Data Analysis Report", ln=1, align='C')

pdf.set_font("Arial", size=12)
pdf.ln(10)

# Basic Info
pdf.cell(200, 10, txt=f"Total rows: {len(df)}", ln=1)
pdf.cell(200, 10, txt=f"Total columns: {len(df.columns)}", ln=1)

pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Statistical Summary", ln=1)

# Add summary stats
pdf.set_font("Arial", size=10)
for col in summary.columns:
    pdf.cell(200, 10, txt=f"\nColumn: {col}", ln=1)
    for stat in summary.index:
        value = round(summary[col][stat], 2)
        pdf.cell(200, 10, txt=f"{stat.capitalize()}: {value}", ln=1)

# Step 3: Save
pdf.output("automated_report.pdf")
