import glob
import shutil
import os
from argparse import ArgumentParser
import logging

logging.basicConfig(level=logging.INFO)

args = ArgumentParser()
args.add_argument('-i', dest='input_dir', required=True)
args.add_argument('-o', dest='output_dir', required=True)
args.add_argument('-f', dest= 'archive_format', default='zip')


def get_file_list(input_dir, file_format):
    try:
        if (not os.path.exists(input_dir)) or (not os.path.isdir(input_dir)):
            raise Exception("Check whether the directory exists or not!")
        return glob.glob(os.path.join(input_dir,f'*.{file_format}'))
    except Exception as e:
        raise Exception("Trouble Getting file List: {}".format(str(e)))


def unarchive(compress_list, output_dir,archive_format ):
    try:
        for compressed_file in compress_list:
            shutil.unpack_archive(
                compressed_file,
                os.path.join(
                    output_dir,
                    os.path.basename(compressed_file).split('.')[0]
                ),
                archive_format
            )
    except Exception as e:
        raise Exception("Trouble extracting Files :{}".format(str(e)))


def main():
    results = args.parse_args()
    input_dir = results.input_dir
    output_dir = results.output_dir
    archive_format = results.archive_format

    try:
        logging.info("Getting file list")
        file_list = get_file_list(input_dir, archive_format)

        logging.info("Extracting Files")
        unarchive(file_list, output_dir,archive_format)
        logging.info(f"Done Extracting at location {output_dir}")
    except Exception as e:
        raise Exception(str(e))



if __name__ == "__main__":
    main()