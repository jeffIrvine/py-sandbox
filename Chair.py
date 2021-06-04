import psycopg2

con = psycopg2.connect('dbname=postgres user=postgres password=postgres')
cur = con.cursor()

class Chair: 
  def insert(chair): 
    cur.execute('''
    INSERT INTO chairs (url)
    VALUES('{0}')
    RETURNING *;
    '''.format(chair['url']))

    con.commit()
    chair = cur.fetchone()
    return {
      'results': chair
    }