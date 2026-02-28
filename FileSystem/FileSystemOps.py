
# todo: from logging import Logger

import os, io, shutil

# pylint: disable=no-name-in-module
from PySide6.QtCore import QLockFile    

from AppUtils import GuardedList



#
# FileSystemOps - file system operations..directory and file manipulation
#
class FileSystemOps:

    PathSep = "/"

    @staticmethod
    def doesFileExist( path: str ):
        return os.path.isfile(path)
    
    
    @staticmethod
    def doesDirExist( path: str ):
        return os.path.isdir(path)
  

    @staticmethod
    def deleteFile( filePath: str ):
        os.remove( filePath )


    @staticmethod
    def createDir( path: str ):
   
        if FileSystemOps.doesDirExist( path ) == False:
            os.mkdir( path ) 
            return True
        return False
            

    # create a directories
    @staticmethod
    def createDirs( path: str ):
        
        if FileSystemOps.doesDirExist( path ) == False:
            os.makedirs( path ) 
            return True
        return False


    # delete an empty directory
    @staticmethod
    def deleteDir( emptyDir: str ):
        os.rmdir( emptyDir )



    # delete a populated directory tree
    @staticmethod
    def deleteDirs( path: str ):
        if os.path.isdir(path):
            shutil.rmtree( path )
        

                    
    @staticmethod
    def getFileSize( fileName: str, binaryFile: bool = True ) -> int:
        
        if not FileSystemOps.doesFileExist( fileName ):
            return int(0)

        readType = "r"
        if binaryFile:
            readType = "rb"

        file = open( fileName, readType, int(-1), encoding="utf-8" )
        if file.readable():
        
            file.seek( 0, io.SEEK_END )
            fsize = file.tell()
            file.close()
            return fsize

        return int(-1)  # -1 as an error value
        
            
    # find files
    @staticmethod
    def findFiles( dirPath: str, searchPattern: str ): 
        
        retFiles = [str]

        if FileSystemOps.doesDirExist( dirPath ) == False:
            # todo: Logger.error( f"Invalid Directory: {dirPath} requested in FileSystemOps.findFiles" )
            return retFiles

        dirList = os.listdir( dirPath ) 
        for filename in dirList:

            filepath = (dirPath + FileSystemOps.PathSep + filename)
            if os.path.isfile( filepath ):

                if filename.find( searchPattern ) != -1:
                    retFiles.append( filepath )         # type: ignore

        return retFiles

    

    # see if a file matching a partial file name exists
    @staticmethod
    def isFileInDirectory( dirPath: str, fileNamePattern: str ) -> bool:
        
        if FileSystemOps.doesFileExist( dirPath ) == False:
            return False

        itemList = os.listdir( dirPath ) 
        for item in itemList:

            if item.find( fileNamePattern ) != -1:
                return True

        return False



    # find a files full name/path
    @staticmethod
    def getFilePath( dirPath: str, fileNamePattern: str ) -> str:
        
        if FileSystemOps.doesFileExist( dirPath ) == False:
            return ""

        itemList = os.listdir( dirPath ) 
        for item in itemList:

            if item.find( fileNamePattern ) != -1:
                return (dirPath + FileSystemOps.PathSep + item)

        return ""



    # find a file...search all directories
    @staticmethod
    def searchRecursively( dirPath: str, findFileName: str ) -> str:

        if FileSystemOps.doesFileExist( dirPath ) == False:
            return ""

        dirList = os.listdir( dirPath ) 
        for entry in dirList:

            if os.path.isdir( (dirPath + FileSystemOps.PathSep + entry) ):
                
                filePath = FileSystemOps.searchRecursively( (dirPath + FileSystemOps.PathSep + entry), findFileName )
                if len(filePath) > 0:
                    return filePath

            elif os.path.isfile( (dirPath + FileSystemOps.PathSep + entry) ):
                
                if entry.find( findFileName ) != -1:
                    return (dirPath + FileSystemOps.PathSep + entry)
       
        return ""



    # see if a directory has files in it
    @staticmethod
    def isDirPopulated( path: str ):

        if not os.path.isdir(path):
            return False  # Path does not exist or is not a directory

        for entry in os.listdir(path):
            
            dirEntry = os.path.join(path, entry)
            if os.path.isfile(dirEntry):
                return True  # Found at least one file

        return False  # No files found in the directory



    # get the files in a directory
    @staticmethod
    def getDirFiles( path: str ) -> GuardedList:

        dirFiles = GuardedList()

        if not os.path.isdir(path):
            return dirFiles

        for entry in os.listdir(path):

            dirEntry = os.path.join(path, entry)

            if os.path.isfile(dirEntry):
                dirFiles.addItem( entry )

        return dirFiles
 


    # get the directories in a directory
    @staticmethod
    def getDirDirectories( path: str ) -> GuardedList:

        dirDirectories = GuardedList()

        if not os.path.isdir(path):
            return dirDirectories
            
        for entry in os.listdir(path):
            dirEntry = os.path.join(path, entry)
            if os.path.isdir(dirEntry):
                dirDirectories.addItem( entry )

        return dirDirectories
 


    # copy a directory
    @staticmethod
    def copyDir( srcDir: str, dstDir: str ):
        
        if not os.path.isdir(srcDir):
            return False

        srcLock = QLockFile( srcDir )
        dstLock = QLockFile( dstDir )

        srcLock.lock()
        dstLock.lock()

        shutil.copytree( srcDir, dstDir )

        srcLock.unlock()
        dstLock.unlock()

        return True





