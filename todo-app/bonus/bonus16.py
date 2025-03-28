import FreeSimpleGUI as sG
import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    with zipfile.ZipFile(pathlib.Path(dest_dir, 'compressed.zip'), 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

files_label = sG.Text("Select files to compress:")
files_button = sG.FilesBrowse("Choose")
files_input = sG.Input(key="files")

dir_label = sG.Text("Select destination folder:")
dir_button = sG.FolderBrowse("Choose")
dir_input = sG.Input(key="dir")

compress_button = sG.Button("Compress")
output_label = sG.Text(key="output")

window = sG.Window("Compress",
                   layout=[[files_label, files_input, files_button],
                           [dir_label, dir_input, dir_button],
                           [compress_button, output_label]])

while True:
    event, values = window.read()

    if event == 'Compress':
        files = values['files'].split(';')
        folder = values['dir']
        make_archive(files, folder)
        window['output'].update(value="Zip completed successfully!")
    elif event == sG.WIN_CLOSED:
        break

window.close()