import os
import datetime

class FileModificationChecker():

    def __init__(self, outputDir):
        self.outputDir = outputDir
        self.filesBefore = os.listdir(self.outputDir)
        self.statMapBefore = self._getStatMap()

    def getModifiedFiles(self):
        modifiedFiles = []
        statMapAfter = self._getStatMap()
        for k,v in statMapAfter.iteritems():
            if k not in self.statMapBefore:
                modifiedFiles.append(k)
            else:
                vBefore = self.statMapBefore[k]
                if v.st_mtime != vBefore.st_mtime:
                    modifiedFiles.append(k)
        return modifiedFiles

    def printModifiedFiles(self):
        print "Created or Modified:"
        print self.getModifiedFiles()

    def _getStatMap(self):
        statMap = {}
        files = os.listdir(self.outputDir)
        for filename in files:
            statMap[filename] = os.stat(self.outputDir + filename)
        return statMap