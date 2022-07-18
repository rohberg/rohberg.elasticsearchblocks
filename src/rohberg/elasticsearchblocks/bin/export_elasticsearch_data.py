# https://kb.objectrocket.com/elasticsearch/export-elasticsearch-documents-as-csv-html-and-json-files-in-python-using-pandas-348
"""
Run with
python /Users/katjasuss/Plone/igib/deployigib/work/zope/src/rohberg.elasticsearchblocks/src/rohberg/elasticsearchblocks/bin/export_elesticsearch_data.py
"""
import time


esindex = 'plone2020productive'
columns_to_be_exported = [
    "portal_type",
    "title",
    "blocks_plaintext",
    "manualfile__extracted"
]
es_export_file = 'export_elasticsearch_data.csv'


def main():
    start_time = time.time()

    try:
        # import the Elasticsearch low-level client library
        from elasticsearch import Elasticsearch

        # import Pandas, JSON, and the NumPy library
        import pandas

    except ImportError as error:
        print(error)
        print("Please use 'pip' to install the necessary packages.")
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
    total_docs = 10000
    # Take the user's parameters and put them into a
    # Python dictionary structured as an Elasticsearch query:
    query_body = {
        "query": {
            "bool": {
                "must": {
                    "match": {      
                        "portal_type": 'Manual'
                    }
                }
            }
        }
    }
    print("\nMake API call to Elasticsearch for", total_docs, "documents.")
    response = elastic_client.search(
        index=esindex,
        body=query_body,
        size=total_docs
    )

    # grab list of docs from nested dictionary response
    print("Put documents in a list.")
    elastic_docs = response["hits"]["hits"]

    """
    GET ALL OF THE ELASTICSEARCH
    INDEX'S FIELDS FROM _SOURCE
    """
    #  create an empty Pandas DataFrame object for docs
    docs = pandas.DataFrame()

    # iterate each Elasticsearch doc in list
    print("\nCreate objects from Elasticsearch data.")
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

    # export Elasticsearch documents to a CSV file
    docs.to_csv(
        es_export_file,
        ",",
        columns=columns_to_be_exported
    )  # CSV delimited by commas

    print("\n\nTime elapsed:", time.time() - start_time)


if __name__ == "__main__":
    main()
