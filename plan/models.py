from django.db import connection


# plan module
class Plan:

    # constructor
    def __init__(self):
        self.connection = connection

    # method

    def get_home(self):
        print('step 3 backendan database keldi')
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM plan WHERE 1 = 1")

            columns = [col[0] for col in cursor.description]

            plans = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        print(f"count {len(plans)}")
        print('databasedan backendga qaytdi step-4')
        return plans

    def create_goal(self, content):
        print('step 3 backenddan database keldi')
        with self.connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO plan
                SET content=%s,
                created_at=CURRENT_TIMESTAMP,
                updated_at=CURRENT_TIMESTAMP
                """,
                [content]
            )

            cursor.execute("SELECT LAST_INSERT_ID()")

            new_plan_id = cursor.fetchone()[0]

        print(f"The new_plan_id: {new_plan_id} is created!")
        print('databasedan backendga qaytdi step-4')




        
    def create_plan(self, data):
        content = data['content']
        print('step3: backenddan database crud req yuborildi')
        with self.connection.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO plan (content, created_at, updated_at )
                VALUES(%s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                """,
                [content]
            )

            cursor.execute("SELECT LAST_INSERT_ID()")

            new_plan_id = cursor.fetchone()[0]
        print('step4 : Databasedan backendga malumot yuborildi')
        print(f"The new_plan_id: {new_plan_id} is created!")
        return new_plan_id
       