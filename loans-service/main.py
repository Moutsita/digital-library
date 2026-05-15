from fastapi import FastAPI
from datetime import datetime
import csv
import os

app = FastAPI(title="Loans Service")

# Stockage temporaire en mémoire
loans = []


@app.post("/loans/borrow")
def borrow(loan: dict):
    loan["id"] = len(loans) + 1
    loan["loan_date"] = str(datetime.now().date())
    loan["returned"] = False
    loans.append(loan)
    return loan


@app.post("/loans/return/{loan_id}")
def return_book(loan_id: int):
    for loan in loans:
        if loan["id"] == loan_id:
            loan["returned"] = True
            loan["return_date"] = str(datetime.now().date())
            return loan
    return {"error": "Not found"}


@app.get("/loans")
def list_loans():
    return loans


@app.get("/loans/user/{user_id}")
def user_loans(user_id: int):
    return [loan for loan in loans if loan["user_id"] == user_id]


@app.get("/loans/overdue")
def overdue():
    # Version simplifiée : tout emprunt non retourné est considéré comme en retard
    return [loan for loan in loans if not loan["returned"]]


@app.get("/loans/export")
def export_loans():
    # Crée le dossier /app/data s'il n'existe pas
    os.makedirs("/app/data", exist_ok=True)

    file_path = "/app/data/loans.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["user_id", "book_id"])
        writer.writeheader()

        for loan in loans:
            writer.writerow({
                "user_id": loan["user_id"],
                "book_id": loan["book_id"]
            })

    return {
        "message": "Export successful",
        "file": file_path,
        "rows": len(loans)
    }