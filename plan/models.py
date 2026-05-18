from django.db import connection


# plan module
class Plan:

    # constructor
    def __init__(self):
        self.connection = connection

    # method

    def get_home(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM plan WHERE 1 = 1")

            columns = [col[0] for col in cursor.description]

            plans = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        print(f"count {len(plans)}")
        return plans

    def create_goal(self, content):
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




        
    def create_plan(self, data):
        content = data['content']
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
        print(f"The new_plan_id: {new_plan_id} is created!")
        return new_plan_id
    
    
    def update_plan(self, data):
        content = data.get("new_plan")
        plan_id = data.get("id")
        
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE plan
                SET content=%s , updated_at = CURRENT_TIMESTAMP
                WHERE id=%s
                """,
                [content, plan_id]
            )

            row_effected = cursor.rowcount

        if row_effected == 0:
            raise ValueError('your plan is not found')
        
        print(f"The new_plan: {plan_id} is updated!")
        return plan_id