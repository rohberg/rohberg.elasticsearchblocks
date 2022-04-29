# https://kb.objectrocket.com/elasticsearch/export-elasticsearch-documents-as-csv-html-and-json-files-in-python-using-pandas-348
"""
Run with
python /Users/katjasuss/Plone/igib/deployigib/work/zope/src/rohberg.elasticsearchblocks/src/rohberg/elasticsearchblocks/bin/extract_possible_lexicon_terms.py
"""

import re

es_export_file = 'export_elasticsearch_data.csv'
possible_lexicon_terms_file = "extract_possible_lexicon_terms.txt"

regexp = r"[A-ZÄÖÜ][a-zA-Z_äöüÄÖÜß]+"


def main():
    with open(es_export_file, 'r') as inputfile:
        data = inputfile.read()
        # print(data[:300])
        words = re.findall(regexp, data)
        print(f"{len(set(words))} gefundene Wörter")
        with open(possible_lexicon_terms_file, 'w') as exportfile:
            for word in sorted(set(words)):
                # print(word)
                exportfile.write(f"{word}\n")


if __name__ == "__main__":
    main()
