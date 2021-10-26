import os

def TransferData():
    for root,dirs,files in os.walk(file_from):
    for name in files:
        print(os.path.join(root,name))
    for name in dirs:
        print(os.path.join(root,name))

    relative_path = os.path.relpath(local_path, file form)
    dropbox_path = os.path.join(file_to,relative_path)
    
    with open(local_path, 'rb') as f:
    dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))
    
TransferData()