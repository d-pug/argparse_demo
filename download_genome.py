#!/usr/bin/env python3

import argparse
import os

'''
python3 download_genome.py --genome hg38 --out_dir .
'''

#####################
## Set Up Argparse ##
#####################

# Initialize argparse
parser = argparse.ArgumentParser(
    description='Download and process a genome to create a GENOME.fa file')

parser.add_argument('--genome', required=True, type=str,
    metavar='<str>', help='Abbreviated UCSC Genome Browser genome name (e.g. dm6, hg19, hg38, mm9, mm10, rn6, ce11, sacCer3, danRer11)')
    
parser.add_argument('--out_dir', required=True, type=str,
    metavar='<str>', help='Where to output GENOME/GENOME.fa file to')  
    
# Finalization of argparse
arg = parser.parse_args()

#####################
## Define Function ##
#####################

def download_genome(genome, out_dir):
    genome_links = {
        'dm6': 'https://hgdownload.soe.ucsc.edu/goldenPath/dm6/bigZips/dm6.fa.gz',
        'hg19': 'https://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/chromFa.tar.gz',
        'hg38': 'https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.chromFa.tar.gz',
        'mm9': 'https://hgdownload.soe.ucsc.edu/goldenPath/mm9/bigZips/chromFa.tar.gz',
        'mm10': 'https://hgdownload.cse.ucsc.edu/goldenPath/mm10/bigZips/chromFa.tar.gz',
        'rn6': 'https://hgdownload.cse.ucsc.edu/goldenPath/rn6/bigZips/rn6.fa.gz',
        'ce11': 'https://hgdownload.soe.ucsc.edu/goldenPath/ce11/bigZips/chromFa.tar.gz',
        'sacCer3': 'https://hgdownload.cse.ucsc.edu/goldenPath/sacCer3/bigZips/chromFa.tar.gz',
        'danRer11': 'https://hgdownload.cse.ucsc.edu/goldenPath/danRer11/bigZips/danRer11.fa.gz'
    }
    
    link = genome_links[genome]
    output_directory = os.path.join(out_dir, genome)
    os.makedirs(output_directory, exist_ok=True)
    
    os.system(f'wget {link} -P {output_directory}')
    
    if link.endswith(f'{genome}/bigZips/{genome}.fa.gz'):
        output_file = os.path.join(output_directory, f'{genome}.fa.gz')
        os.system(f'gunzip -f {output_file}')
        
    if link.endswith(f'{genome}/bigZips/chromFa.tar.gz'):
        output_file = os.path.join(output_directory, 'chromFa.tar.gz')
        os.system(f'tar -xzf {output_file} -C {output_directory}')
        os.system(f'cat {output_directory}/*.fa > {output_directory}/{genome}.fa')
        os.system(f'rm -f {output_directory}/chr*.fa')
        
    if link.endswith('hg38.chromFa.tar.gz'):
        output_file = os.path.join(output_directory, 'chromFa.tar.gz')
        os.system(f'tar -xzf {output_file} -C {output_directory}')
        os.system(f'cat {output_directory}/chroms/*.fa > {output_directory}/{genome}.fa')
        os.system(f'rm -rf {output_directory}/chroms/')
        
#####################
## Download Genome ##
#####################

download_genome(arg.genome, arg.out_dir)