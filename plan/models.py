from django.db import models, connection

# plan modeul

class Plan():

#static 


#constructor
 def __init__(self):
  self.connection=connection


#method 
 def get_home(self):
   with self.connection.cursor() as cursor:
    cursor.execute("SELECT * FROM plan WHERE  1 = 1")
    columns = [col[0] for col in cursor.description]
    plans = [dict(zip(columns, row)) for row in cursor.fetchall()]
   print(f"count {len(plans)}")
   return plans
