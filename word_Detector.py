import os

def word_detect(filename):
    with open(filename,"r") as f:
        content=f.read()

    if "ashish" in content.lower():
        return True
    else:
        return False


if __name__=="__main__":
    dir_content = os.listdir()
    nfile=0

    for file in dir_content:
        if file.endswith("txt"):
            print(f'\nDetecting Word in {file}')
            Word= word_detect(file)
            if (Word):
                print(f"\nWord found in {file}")
                nfile=nfile+1
            else:
                print(f"\nWord not found in {file}")
                
print(f'\n{nfile} Number of files found Word!!!!\n')