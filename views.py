from datasource import orcldb

pool = orcldb.pool
api_username = orcldb.api_username
api_pwd = orcldb.api_pwd

def getData(query,id):
    #cur = con.cursor()
    con = pool.acquire()
    cur = con.cursor()
    cur.execute(query,id=id)
    r = cur.fetchall()   
    
    cols = [x[0] for x in cur.description]
    colType = [x[1] for x in cur.description]
 
    result = []        
    for x in r:
        ind = 0
        obj = {} 
        for i in x:             
            if colType[ind].name == 'DB_TYPE_DATE':
                obj[cols[ind]] = str(i) 
            else:
                obj[cols[ind]] = i      
                                     
            ind = ind + 1
        result.append(obj)
    #print(result)
    cur.close()
    pool.release(con)

    return result