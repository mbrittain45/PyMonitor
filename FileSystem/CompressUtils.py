
import os



# todo: have a window for the user to check archives via a command line like interface



#
# Usage: 7z <command> [<switches>...] <archive_name> [<file_names>...] [@listfile]
#
# Switches that can be added to otherCmds in the construction of the object
#     
# -ai[r[-|0]]{@listfile|!wildcard} : Include archives, -ax[r[-|0]]{@listfile|!wildcard} : eXclude archives, 
# -ao{a|s|t|u} : set Overwrite mode, -an : disable archive_name field, -bs{o|e|p}{0|1|2} : set output stream for output/error/progress line,
# -i[r[-|0]]{@listfile|!wildcard} : Include filenames, -m{Parameters} : set compression Method, -mmt[N] : set number of CPU threads,
# -mx[N] : set compression level: -mx1 (fastest) ... -mx9 (ultra), -p{Password} : set Password, -r[-|0] : Recurse subdirectories, 
# -sa{a|e|s} : set Archive name mode, -scc{UTF-8|WIN|DOS} : set charset for console input/output, -scrc[CRC32|CRC64|SHA1|SHA256|*] : set hash function for x, e, h commands
# -sdel : delete files after compression, -seml[.] : send archive by email, -slp : set Large Pages mode, -slt : show technical information for l (List) command, -snl : store symbolic links as links,
# -sni : store NT security information, -sns[-] : store NTFS alternate streams, -so : write data to stdout, -spd : disable wildcard matching for file names, -spe : eliminate duplication of root folder for extract command
# -spf : use fully qualified file paths, -ssc[-] : set sensitive case mode, -sse : stop archive creating, if it can't open some input file, -ssw : compress shared files
# -stl : set archive timestamp from the most recently modified file, -stm{HexMask} : set CPU thread affinity mask (hexadecimal number), -stx{Type} : exclude archive type
# -t{Type} : Set type of archive, -u[-][p#][q#][r#][x#][y#][z#][!newArchiveName] : Update options, -v{Size}[b|k|m|g] : Create volumes, -w[{path}] : assign Work directory. Empty path means a temporary directory
# -x[r[-|0]]{@listfile|!wildcard} : eXclude filenames,  -y : assume Yes on all queries     
#
class CompressUtils:
    
    
    @staticmethod
    def compressDir( archiveName: str, dirPath: str = "*.*", outDir: str = "", otherCmds: str = "" ):
        os.system( ".\\..\\ThirdParty\\7z.exe a {} {} -o{} -bd{}".format( archiveName, dirPath, outDir, otherCmds ) )


    @staticmethod
    def compressFile( archiveName: str, filePath: str, outDir: str = "", otherCmds: str = "" ):
        os.system( ".\\..\\ThirdParty\\7z.exe a {} {} -o{} -bd{}".format( archiveName, filePath, outDir, otherCmds ) )


    @staticmethod
    def decompressDir( archiveName: str, dirPath: str, outDir: str = "", otherCmds: str = "" ):
        os.system( ".\\..\\ThirdParty\\7z.exe e {} {} -o{} -bd{}".format( archiveName, dirPath, outDir, otherCmds ) )


    @staticmethod
    def decompressFile( archiveName: str, filePath: str, outDir: str = "", otherCmds: str = "" ):
        os.system( ".\\..\\ThirdParty\\7z.exe e {} {} -o{} -bd{}".format( archiveName, filePath, outDir, otherCmds ) )


    @staticmethod
    def deleteFromArchive( archiveName: str, deleteRegEx: str = "*.*", outDir: str = "", otherCmds: str = "" ):
        os.system( ".\\..\\ThirdParty\\7z.exe d {} {} -o{} -bd{}".format( archiveName, deleteRegEx, outDir, otherCmds ) )


    @staticmethod
    def listArchiveContents( archiveName: str, pipeToFile: str = "temp.txt", otherCmds: str = "" ):
        os.system( ".\\..\\ThirdParty\\7z.exe l {} -slt -bd{} > {}".format( archiveName, pipeToFile, otherCmds ) )


    @staticmethod
    def calcHashValues( dirPathOrAchiveName: str, pipeToFile: str = "temp.txt", otherCmds: str = "" ):
        os.system( ".\\..\\ThirdParty\\7z.exe h {} -bd{} > {}".format( dirPathOrAchiveName, pipeToFile, otherCmds ) )
        

    @staticmethod
    def testArchiveValidity( archiveName: str, pipeToFile: str = "temp.txt", otherCmds: str = "" ):
        os.system( ".\\..\\ThirdParty\\7z.exe t {} -bd{} > {}".format( archiveName, pipeToFile, otherCmds ) )
  

    @staticmethod
    def updateFiles( archiveName: str, newDirPath: str, outDir: str = "", otherCmds: str = "" ):
        os.system( ".\\..\\ThirdParty\\7z.exe u {} {} -o{} -bd{}".format( archiveName, newDirPath, outDir, otherCmds ) )
        

    @staticmethod
    def renameFiles( archiveName: str, renameRegEx: str, outDir: str = "", otherCmds: str = "" ):
        os.system( ".\\..\\ThirdParty\\7z.exe rn {} {} -o{} -bd{}".format( archiveName, renameRegEx, outDir, otherCmds ) )
    

    @staticmethod
    def extractFiles( archiveName: str, dirPath: str, outDir: str = "", otherCmds: str = "" ):
        os.system( ".\\..\\ThirdParty\\7z.exe x {} {} -o{} -bd{}".format( archiveName, dirPath, outDir, otherCmds ) )
    


