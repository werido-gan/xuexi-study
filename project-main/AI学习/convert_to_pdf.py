
import os
import glob
import subprocess

def convert_md_to_pdf():
    search_path = 'd:\\zhq笔记\\project-main\\AI学习'
    for filename in glob.iglob(os.path.join(search_path, '**', '*.md'), recursive=True):
        print(f"Converting {filename}...")
        try:
            output_filename = os.path.splitext(filename)[0] + '.pdf'
            subprocess.run(['pandoc', filename, '-o', output_filename, '--pdf-engine=ms'], check=True)
            print(f"Successfully converted to {output_filename}")
        except Exception as e:
            print(f"Error converting {filename}: {e}")

if __name__ == '__main__':
    convert_md_to_pdf()
