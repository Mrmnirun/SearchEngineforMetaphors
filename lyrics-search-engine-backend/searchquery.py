from elasticsearch import Elasticsearch


def basic_search(query):
    q = {
        "query": {
            "query_string": {
                "query": query
            }
        },"size":100
    }
    return q


def advanced_search(query, fields):
    q = {
        "query": {
            "multi_match": {
                "query":    query,
                "fields": fields
            }
        },"size":100
    }
    return q


def search_metaphor(query, fields, metaphor):
    return {
        "query": {
            "bool": {
                "must": {
                    "match": {
                        "metaphors.target": {
                            "query": metaphor
                        }
                    }
                },
                "should": {
                    "multi_match": {
                        "query":    query,
                        "fields": fields
                    }
                }
            }
        },"size":100
    }
    

INDEX = 'lyrics-test'
client = Elasticsearch(HOST="http://localhost", PORT=9200,
                       http_auth=('elastic', '_mVCwJ+3syHnE4*4E1f*'))


def search(query, filter, fields, metaphor):
    # result = client. (index=INDEX,body=standard_analyzer(query))
    # keywords = result ['tokens']['token']
    # print(keywords)

    # query_body= process(query)
    if (metaphor):
        query_body = search_metaphor(query, fields, metaphor)
    else:
        query_body = advanced_search(
            query, fields) if filter else basic_search(query)
    print('Making Basic Search ')
    res = client.search(index=INDEX, body=query_body)
    return res
