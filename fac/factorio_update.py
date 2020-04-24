import os
import shutil
import sys
import urllib3

factorio_stable = "https://factorio.com/get-download/stable/headless/linux64"

factorio_path = input('Specify Factorio path ex. \n "/home/user/factorio/" --> ')  # get factorio path
try:
    os.chdir(factorio_path)
except Exception as e:
    print("Path not found: " + factorio_path)
    print(e)

factorio_version = input('Factorio version \n ex. "0.18.xx" --> ')  # get factorio version
print("Factorio path : " + factorio_path)
print("Factorio version : " + factorio_version)
factorio_latestexperimental = "https://factorio.com/get-download/" + factorio_version + "/headless/linux64"


http = urllib3.PoolManager()
r = http.request('GET', factorio_latestexperimental, preload_content=False)
path_file = factorio_path+factorio_version
#temp dir to move all extracted data /home/user/factorio/0.xx.xx/
try:
    os.mkdir(path_file)
    shutil.unpack_archive(factorio_path+"linux64.tar", path_file, "tar")
except OSError:
    print("Creation of the directory %s failed" % path_file)
else:
    print("Successfully created the directory %s " % path_file)
r.release_conn()
path = path_file+"/factorio/"
dest = shutil.move(path, factorio_path)
print("Destination path:", dest)


"""

cd $factorio_path

echo Inserire per intero la versione che si desidera installare:
read version_number
#echo $version_number



#estrazione e rimozione file archivio
mkdir $factorio_path/factorio-$version_number/ 
tar -xf linux64 --directory $factorio_path/factorio-$version_number/
rm linux64
#copio i file appena scaricati
cp -R factorio-$version_number/factorio/* .

#cancello la dir temporanea del download
rm -rf $factorio_path/factorio-$version_number

"""
