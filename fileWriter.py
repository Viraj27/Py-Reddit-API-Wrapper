import os

class FileWriter( object ):

    def __init__( self ):
        self.dir = 'E:/Docx/Reddit Saves/'

    def writeListToFile( self, subName, itemList ):
        ''' Write contents of a list to a file '''
        self.filePath = os.path.join(self.dir, subName+'.txt')
        with open (self.filePath, 'w') as f:
            for item in itemList:
                f.write('{0} \n'.format(item))

    def writeCommentsToFile( self, commentsList ):
        ''' Write all accumulated contents to a file '''
        self.filePath = os.path.join(self.dir, 'webGames.txt')
        with open(self.filePath, 'w') as f:
            for comment in commentsList:
                f.write('{0} \n'.format(comment))
    