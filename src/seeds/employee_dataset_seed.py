import os
import csv
import re
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

RAW_URL = os.environ["DATABASE_URL"]

CSV_PATH  = os.getenv("CSV_PATH", "artifacts/df_merged.csv")
CSV_DELIM = os.getenv("CSV_DELIM", ";")

engine = create_engine(RAW_URL, future=True)

YES = {"oui", "y", "true", "1"}
NO  = {"non", "n", "false", "0"}

def map_bool_to_int(v: str | None):
    if v is None: 
        return None
    s = str(v).strip().lower()
    if s in YES: 
        return 1
    if s in NO: 
        return 0
    return None

def map_percent_to_int(v: str | None):
    if not v: 
        return None
    m = re.search(r"-?\d+", str(v))
    return int(m.group(0)) if m else None

def seed_employee_dataset(session: Session):
    with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=CSV_DELIM)
        cols = reader.fieldnames or []
        if not cols:
            raise RuntimeError("CSV sans en-tête.")

        rows = []
        for r in reader:
            r["a_quitte_l_entreprise"] = map_bool_to_int(r.get("a_quitte_l_entreprise"))
            r["augementation_salaire_precedente"] = map_percent_to_int(
                r.get("augementation_salaire_precedente")
            )
            rows.append(r)

        if not rows:
            return

        sql = text(
            f"INSERT INTO employee_dataset ({', '.join(cols)}) "
            f"VALUES ({', '.join(':'+c for c in cols)})"
        )
        session.execute(sql, rows)

def main():
    with Session(engine) as s:
        seed_employee_dataset(s)
        s.commit()

if __name__ == "__main__":
    main()
