import sqlite3
import os


def DbVerify():
    
    if os.path.isfile("articlesDB.db") == False:
        dbcreated = sqlite3.connect("articlesDB.db")
        query = ''' CREATE TABLE ArticleDownloaded([ID] INTEGER PRIMARY KEY, 
        [FName] text, [FilePath] text)'''
        
        try:
            dbcreated.execute(query)
            dbcreated.commit()
        except Exception:
            return
    
    NewDB = sqlite3.connect('articlesDB.db')
    return NewDB
    

def WriteDownload(FileName, FilePath):
    Db = DbVerify()
    Cursore = Db.cursor()
    query = f"INSERT INTO ArticleDownloaded(FName, FilePath) VALUES('{FileName}', '{FilePath}')"
    try:
        
        Cursore.execute(query)
        Db.commit()
        Db.close()
    except Exception as e:
        print("Couldnt do it", e)
        return False
    
    return True

def ReadDownload():
    results = ''
    formattedResults = []
    Db = DbVerify()
    Cursore = Db.cursor()
    query = ''' SELECT * FROM ArticleDownloaded'''
    try:
        results = Cursore.execute(query)
        formattedResults = results
        Db.commit()
        
    
    except Exception:
        return
    
    return formattedResults

def DeleteDownload(FilePath):
    Db = DbVerify()
    Cursore = Db.cursor()
    query = f"DELETE FROM ArticleDownloaded WHERE FilePath = '{FilePath}'"
    try:
        
        Cursore.execute(query)
        Db.commit()
    except Exception as e:
        print("Couldnt do it", e)
        return False
    
    return True

def Closer():
    Db = DbVerify()
    Db.close()