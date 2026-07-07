import os
from PIL import Image
import pypandoc
import shutil
def mass_convertor_text(folder_for_conver,old_format,new_format):
    for file in os.listdir(folder_for_conver):
        if file.endswith(old_format):
            if old_format == 'txt':
                try:
                    file=shutil.copyfile(file, file.replace('.txt', '.md'))
                    pypandoc.convert_file(file, new_format, outputfile=file.replace('.' + 'md', '.' + new_format))
                    os.remove(file)
                except RuntimeError:
                   print(f'Нет формата {new_format}/Нельзя преобразовать {old_format} в {new_format}')

            else:
                try:
                    pypandoc.convert_file(file, new_format, outputfile=file.replace('.' + old_format, '.' + new_format))
                except RuntimeError:
                   print(f'Нет формата {new_format}/Нельзя преобразовать {old_format} в {new_format}')

def mass_convertor_png(folder_for_conver,old_format,new_format):
    for file in os.listdir(folder_for_conver):
        if file.endswith(old_format):
            try:
                img = Image.open(file)
                if new_format == 'jpeg' or new_format == 'jpg':
                    new_format = 'jpeg'
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                img.save(file.replace(old_format,new_format), format=new_format.upper())
            except RuntimeError:
                print(f'Нет формата {new_format}/Нельзя преобразовать {old_format} в {new_format}')
if __name__ == '__main__':
    old_format = input('Напишите тип файла из который вы хотите изменить(по типу doc, png, и т.п)\n')
    new_format = input('Напишите тип файла в который вы хотите преобразовать(по типу doc, png, и т.п)\n')

    folder_for_conver = os.path.join(os.path.realpath(__file__).replace('convert_file.py', ''), 'ПапкаКонвертации')
    os.chdir(folder_for_conver)
    init_format = ['png', 'jpeg', 'jpg', 'gif', 'bmp', 'tiff', 'svg', 'webp', 'avif']
    if old_format in init_format:
        mass_convertor_png(folder_for_conver,old_format,new_format)
    else:
        mass_convertor_text(folder_for_conver,old_format,new_format)