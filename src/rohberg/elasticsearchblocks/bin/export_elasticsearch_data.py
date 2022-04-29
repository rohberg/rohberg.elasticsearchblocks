# https://kb.objectrocket.com/elasticsearch/export-elasticsearch-documents-as-csv-html-and-json-files-in-python-using-pandas-348
"""
Run with
python /Users/katjasuss/Plone/igib/deployigib/work/zope/src/rohberg.elasticsearchblocks/src/rohberg/elasticsearchblocks/bin/export_elesticsearch_data.py
"""
from datetime import datetime
import time

esindex = 'plone2020'
es_export_file = 'export_elasticsearch_data.csv'


def main():
    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')
    # print(timestamp)
    start_time = time.time()

    try:
        # import the Elasticsearch low-level client library
        from elasticsearch import Elasticsearch

        # import Pandas, JSON, and the NumPy library
        import pandas
        import json
        import numpy as np

    except ImportError as error:
        print("\nImportError:", error)
        print("Please use 'pip3' to install the necessary packages.")
        quit()

    # create a client instance of the library
    print("\nCreate client instance of Elasticsearch.")
    elastic_client = Elasticsearch()

    """
    MAKE API CALL TO CLUSTER AND CONVERT
    THE RESPONSE OBJECT TO A LIST OF
    ELASTICSEARCH DOCUMENTS
    """
    # total num of Elasticsearch documents to get with API call
    total_docs = 20
    print("\nmaking API call to Elasticsearch for", total_docs, "documents.")
    response = elastic_client.search(
        index=esindex,
        body={},
        size=total_docs
    )

    # grab list of docs from nested dictionary response
    print("putting documents in a list")
    elastic_docs = response["hits"]["hits"]

    """
    GET ALL OF THE ELASTICSEARCH
    INDEX'S FIELDS FROM _SOURCE
    """
    #  create an empty Pandas DataFrame object for docs
    docs = pandas.DataFrame()

    # iterate each Elasticsearch doc in list
    print("\ncreating objects from Elasticsearch data.")
    for num, doc in enumerate(elastic_docs):

        # get _source data dict from document
        source_data = doc["_source"]

        # get _id from document
        _id = doc["_id"]

        # create a Series object from doc dict object
        doc_data = pandas.Series(source_data, name=_id)

        # append the Series object to the DataFrame object
        docs = docs.append(doc_data)

    """
    EXPORT THE ELASTICSEARCH DOCUMENTS PUT INTO
    PANDAS OBJECTS
    """
    print("\nexporting Pandas objects to different file types.")

    # export the Elasticsearch documents as a JSON file
    # docs.to_json("objectrocket.json")

    # export Elasticsearch documents to a CSV file
    docs.to_csv(
        es_export_file,
        ",",
        columns=["portal_type", "title", "blocks_plaintext", "manualfile__extracted"]
    )  # CSV delimited by commas

    print("\n\ntime elapsed:", time.time() - start_time)


if __name__ == "__main__":
    main()
