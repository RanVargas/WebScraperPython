import sqlite3
import os


def DbVerify():
    
    if os.path.isFile("articleDB") == False:
        dbcreated = sqlite3.connect("articlesDB")
        query = ''' CREATE TABLE ArticleDownloaded([ID] INTEGER PRIMARY KEY, 
        [FName] text, [FilePath] text)'''
        
        try:
            dbcreated.execute(query)
            dbcreated.commit()
        except Exception:
            return
    
    dbcreated = sqlite3.connect('articlesDB')
    return dbcreated
    

def WriteDownload(FileName, FilePath):
    Db = DbVerify()
    query = f'''INSERT INTO ArticleDownloaded(FName, FilePath) 
                VALUES('{FileName}', '{FilePath}')'''
    try:
        Db.execute(query)
        Db.commit()
    except Exception:
        return False
    
    return True

def ReadDownload():
    results = ''
    Db = DbVerify()
    query = ''' SELECT * FROM ArticleDownloaded'''
    try:
        results = Db.execute(query)
        Db.commit()
    except Exception:
        return
    
    return 