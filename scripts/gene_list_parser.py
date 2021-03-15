#!/usr/bin/env python3

"""
Read and convert humchr01.txt items.
"""

import re
import json

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
        mim_code = ""
        description = ""
        if re.match(r'^\d+', remainder):
            new_gene['mim_code'], description = re.split("\s+", remainder, maxsplit=1)
        else:
            new_gene['description'] = remainder
        new_genes.append(new_gene)
    with open("humchr01.json", "w") as humchr_json_file:
        json.dump(new_genes, humchr_json_file, ensure_ascii=False, sort_keys=True, indent=4)

if __name__ == '__main__':
    main()
