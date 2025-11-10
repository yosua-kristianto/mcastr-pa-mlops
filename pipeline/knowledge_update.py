from config import databaseConnection
from model import Knowledge, ModelLog
import pandas
from datetime import date

from sqlalchemy import func

from config import Log

def updateKnowledge():
    session = databaseConnection()

    try:
        # --- Step 1: Check existing knowledge count ---
        knowledge_count = session.query(func.count(Knowledge.id)).filter(Knowledge.deleted_at == None).scalar()

        if knowledge_count == 0:
            Log.i("Knowledge table is empty. Loading initial data from emotions.csv")
            data_frame = pandas.read_csv("emotions.csv")

            records = [
                Knowledge(
                    id=str(row["id"]),
                    prompt=row["text"],
                    label=int(row["label"])
                )
                for _, row in data_frame.iterrows()
            ]

            session.add_all(records)
            session.commit()
            Log.i("Successfully initialized knowledge table with data from emotions.csv")
        else:
            Log.i("Checking today's model logs")
            today = date.today()

            logs = (
                session.query(ModelLog)
                .filter(
                    func.date(ModelLog.created_at) == today,
                    ModelLog.deleted_at == None
                )
                .all()
            )

            if not logs:
                Log.i("No new model logs found for today. Skipping knowledge update.")
            else:
                new_records = []
                for log in logs:
                    label_value = log.feedback_actual_output if log.feedback_actual_output is not None else log.model_output
                    new_records.append(
                        Knowledge(
                            id=log.uuid,
                            prompt=log.prompt,
                            label=int(label_value)
                        )
                    )

                session.add_all(new_records)
                session.commit()
                Log.i(f"Inserted {len(new_records)} new knowledge entries from today's logs.")
    except Exception as e:
        session.rollback()
        Log.e(e)
    finally:
        session.close()
        print("[INFO] Database session closed.")