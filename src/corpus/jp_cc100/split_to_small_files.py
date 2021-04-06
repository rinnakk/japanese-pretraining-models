import os
from tqdm import tqdm

from corpus.jp_cc100.config import Config

config = Config()
N_LINES_PER_FILE = 1e6

if __name__ == "__main__":
    if not os.path.exists(f"{config.doc_data_dir}"):
        os.makedirs(f"{config.doc_data_dir}")

    output_file_id = 0
    output_file = open(f"{config.doc_data_dir}/{output_file_id}.txt", "w+", encoding="utf-8")
    cur_n_lines = 0

    with open(f"{config.raw_data_dir}/ja.txt", "r", encoding="utf-8") as input_file:
        with tqdm() as pbar:
            for line in input_file:
                line = line.strip()
                
                output_file.write(line + "\n")
                cur_n_lines += 1
                # pbar.update(1)

                if line == "":
                    output_file.write
                    if cur_n_lines >= N_LINES_PER_FILE:
                        output_file.flush()
                        output_file.close()
                        output_file_id += 1
                        cur_n_lines = 0
                        output_file = open(f"{config.doc_data_dir}/{output_file_id}.txt", "w+", encoding="utf-8")
                        pbar.set_description(f"created {output_file_id} files")
                    

