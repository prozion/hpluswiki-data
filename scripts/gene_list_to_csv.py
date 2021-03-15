#!/usr/bin/env python3

"""
Read and convert humchr01.txt items.
"""

import re
import csv

def main():
    """Main function"""
    gene_filename = "humchr01_for_splitting.txt"
    with open(gene_filename, 'r') as gene_file:
        original_genes = gene_file.read().splitlines()
    new_genes = []
    for gene in original_genes:
        new_gene = {}
        new_gene['gene_name'], remainder = re.split("\s+", gene, maxsplit=1)
        new_gene['chromosomal_position'], remainder = re.split("\s+", remainder, maxsplit=1)
        new_gene['swiss_prot_ac'], remainder = re.split("\s+", remainder, maxsplit=1)
        new_gene['swiss_prot_ename'], remainder = re.split("\s+", remainder, maxsplit=1)
        new_gene['mim_code'] = ""
        new_gene['description'] = ""
        if re.match(r'^\d+', remainder):
            new_gene['mim_code'], description = re.split("\s+", remainder, maxsplit=1)
        else:
            new_gene['description'] = remainder
        new_genes.append(new_gene)
        with open("humchr01.csv", 'wb') as csv_file:
            writer = csv.writer(csv_file, delimiter='\t', quotechar='\\', quoting=csv.QUOTE_MINIMAL)
            for gene in new_genes:
                writer.writerow([
                    gene['gene_name'],
                    gene['chromosomal_position'],
                    gene['swiss_prot_ac'],
                    gene['swiss_prot_ename'],
                    gene['mim_code'],
                    gene['description']
                ])

if __name__ == '__main__':
    main()
