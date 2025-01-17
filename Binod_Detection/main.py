import os

def isBinod(filename):
    with open(filename,"r")as f:
        fileContent = f.read()
    
    # Detect all forms of Binod like bInoD
    if "binod" in fileContent.lower():
        return True
    else:
        return False

if __name__=="__main__":
    # listing the contents of this folder
    dir_contents = os.listdir()

    nBinod = 0
    # for each text file, run isBinod for them
    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting Binod in {item}\n")
            flag = isBinod(item)
            if (flag):
                print(f"Binod found in {item}\n")
                nBinod += 1
            else:
                print(f"Binod not found in {item}\n")
    print("****************Binod Detector summary ***********\n")
    print(f"{nBinod} files found with Binod hidden into them\n")