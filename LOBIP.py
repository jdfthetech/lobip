#! /usr/bin/python

#Life of Brian Image Processor - RIP Terry Jones

from tkinter import Tk, Label, Button, filedialog, simpledialog, Entry
import os
from PIL import Image


# gui class

class lobipGUI:
    def __init__(self, master):
    
       
        self.master = master
        master.title("Life of  Brian Image Processor")
        
        
        screenWidth = root.winfo_screenwidth()
        screenHeight = root.winfo_screenheight()
        
        # adjust dimensions to middle of screen and make room for box
        
        xLocation = screenWidth / 2 - 245
        yLocation = screenHeight / 2 - 95    
        
        # have to convert to int because geometry doesn't like floats
        
        xLocation = int(xLocation)
        yLocation = int(yLocation)
        
        # specify geometry, must make coords a string normally looks like "490x190+220+200"
        
        root.geometry("490x190+"+str(xLocation)+"+"+str(yLocation))        

        # using grid rather than pack to set buttons in correct spot
                
        self.label = Label(master, text="Enter Pixel Amount:  ")        
        self.label.grid(column=0,row=0)
        
        self.pixelsEntry = Entry(master)
        self.pixelsEntry.grid(column=1,row=0)

        self.pixelAmount = Label(master, text="Your Pixel Amount:  ")
        self.pixelAmount.grid(column=0,row=1)    
        
        self.path1 = Label(master, text="Your Chosen Directory:  ")
        self.path1.grid(column=0,row=2)    
        
        self.pathLookup_button = Button(master, text="Select Directory", command=self.pathLookup)
        self.pathLookup_button.grid(column=1,row=3)

        self.buffer1 = Label(master, text="       ") 
        self.buffer1.grid(column=0,row=4)


        self.buffer2 = Label(master, text="       ")
        self.buffer2.grid(column=0,row=5)   
       
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(column=4,row=6)
        
        self.processDir = Button(master, text="Process Folder", command= self.doWork)
        self.processDir.grid(column=0, row=6)
        

       
    def pathLookup(self):
        global folderpath
        folderpath = filedialog.askdirectory()
        #print(str(folderpath)) 
        
        # give us some dots if it's too long and truncate
        folderpathString = folderpath

        if (len(folderpathString) > 37):
            folderpathString = folderpathString[:36] + "..."
            
        else:
            folderpathString = folderpath

        self.pathLabel = Label(self.master, text=folderpathString,width=40,anchor='w')
        self.pathLabel.grid(column=1,row=2)

        pixels = self.pixelsEntry.get()
        
        self.pixelAmountLabel = Label(self.master, text=pixels,anchor='w')
        self.pixelAmountLabel.grid(column=1,row=1)                
        

        return folderpath

        
        
    def completed(self,pixels):
        self.buffer3 = Label(self.master, text= str(pixels) + "_thumbs Dir Created",anchor='w')
        self.buffer3.grid(column=1,row=5)             
        
    def doWork(self):
        
        # get pixel data
        pixels = self.pixelsEntry.get()
        # change dir
        os.chdir(folderpath)
        # process functions
        pixelSize(pixels)
        makeDir(pixels)
        resizePics(pixels)
        self.completed(pixels)
        self.completeLabel = Label(self.master, text="Images are located in the  " + str(pixels) + "_thumbs directory.",anchor='w')
        self.completeLabel.grid(column=1,row=7)    
     
           
        



def pixelSize(pixels):

    print("Your images are processed and are located in the  " + str(pixels) + "_thumbs directory.")

def makeDir(pixels):
    if os.path.exists( str(pixels) + "_thumbs"):
        pass
    else:
       os.mkdir(( str(pixels) + "_thumbs"))

def resizePics(pixels):
    for file in os.listdir('.'):

        #this function creates the images and tosses them in the folder    
        def imageProcess():
            image = Image.open(file)
            filename, file_extension = os.path.splitext(file)
            # have to make a tuple out of pixels because of PIL requirements
            listSize = [int(pixels),int(pixels)]
            imageSize = tuple(listSize)
            image.thumbnail(imageSize)
            image.save( str(pixels) +'_thumbs/{}_{}{}'.format(filename, pixels, file_extension))            

        #do it only for image file types
        if file.endswith('.jpg'):
            imageProcess()
 
        elif file.endswith('.jpeg'):
            imageProcess()

        elif file.endswith('.png'):
            imageProcess()

    

# display gui and loop it    
if __name__ == "__main__":        
    root = Tk()
    my_gui = lobipGUI(root)
    root.mainloop()