import pandas
from pandas.core.frame import DataFrame

res = {'columns': [{'name': 'service.name', 'type': 'keyword'}, {'name': 'url.domain', 'type': 'keyword'},
                   {'name': 'url.port', 'type': 'long'}, {'name': 'trace.id', 'type': 'keyword'},
                   {'name': 'span.id', 'type': 'keyword'}, {'name': 'span.name', 'type': 'keyword'},
                   {'name': 'event.outcome', 'type': 'keyword'}, {'name': 'span.duration.us', 'type': 'long'}],
       'rows': [['unknown_service_java', '10.10.0.90', 7109, '1490d360dbe5a86257a53b79db921112', None, None, 'success',
                 None],
                ['unknown_service_java', '10.10.0.90', 7109, '4dc0a0885df2d3dcfca3bdda7d2f2d4f', None, None, 'success',
                 None],
                ['unknown_service_java', '10.10.0.90', 7109, '40b34b5278a4a18e3a779e54dfed3501', None, None, 'success',
                 None],
                ['unknown_service_java', '10.10.0.90', 7109, '7d075f815bf3e7a25cd0c8786da39232', None, None, 'failure',
                 None],
                ['unknown_service_java', '10.10.0.90', 7109, '668031f97a7d106b19fd929ccaf104c9', None, None, 'failure',
                 None],
                ['Java-otel-demo', '127.0.0.1', 8989, '8331bbc3c7d34e7e2f18f66815a3a96d', None, None, 'success', None],
                ['Java-otel-demo', '127.0.0.1', 8910, 'd8b8287dadf7455b431ffc3cc8b6e5ee', None, None, 'failure', None],
                ['Java-otel-demo', None, None, '8331bbc3c7d34e7e2f18f66815a3a96d', 'd8a97c6c35cf4361', 'HTTP GET',
                 'failure', 1048960],
                ['Java-otel-demo', None, None, '8331bbc3c7d34e7e2f18f66815a3a96d', '844c73c6a17ae895', 'HTTP GET',
                 'success', 95668],
                ['Java-otel-demo', None, None, 'd8b8287dadf7455b431ffc3cc8b6e5ee', '2767ced6572ea62d',
                 'ResponseFacade.sendError', 'unknown', 682],
                ['Java-otel-demo', None, None, '8331bbc3c7d34e7e2f18f66815a3a96d', 'd7ecbb3d71bead2b',
                 'SELECT test.user', 'unknown', 134372],
                ['Java-otel-demo', None, None, '8331bbc3c7d34e7e2f18f66815a3a96d', 'aac51701a2ee94bf',
                 'HelloController.hello', 'unknown', 11006648],
                ['Java-otel-demo', None, None, 'd8b8287dadf7455b431ffc3cc8b6e5ee', '312d499399624d7f',
                 'ResourceHttpRequestHandler.handleRequest', 'unknown', 9729],
                ['Java-otel-demo', None, None, 'd8b8287dadf7455b431ffc3cc8b6e5ee', '56bf27480e44cbab',
                 'BasicErrorController.error', 'unknown', 440060]]}


columns_name = [tmpdict['name'] for tmpdict in res['columns']]
df = DataFrame(res['rows'])
df.columns =columns_name



def server_info(df):
    agg_dict = {'trace.id': ['count'], 'span.id': ['count'], 'event.outcome': lambda x: (x == 'failure').sum(), }
    df_node_grouped = df.groupby(['service.name'], as_index=True).agg(agg_dict)
    df_node_grouped.columns = pandas.Series(['trace_count', 'span_count', 'error_span_count'])
    result_dict = df_node_grouped.to_dict(orient="index")
    server_info_list = []
    for k, v in result_dict.items():
        v["service_name"] = k
        server_info_list.append(v)
    server_info = {"server_info":server_info_list}

    print(server_info)
def node_info(df):
    df['url.domain'].fillna(df['trace.id'].map(df.dropna(subset = ["url.domain", "url.port"]).set_index('trace.id')['url.domain']),inplace=True)
    df['url.port'].fillna(df['trace.id'].map(df.dropna(subset = ["url.domain", "url.port"]).set_index('trace.id')['url.port']),inplace=True)

    agg_dict = {'trace.id':['count'],'span.id':['count'],'event.outcome':lambda x: (x == 'failure').sum(),}
    df_node_grouped = df.groupby(['service.name','url.domain','url.port'],as_index=True).agg(agg_dict)
    df_node_grouped.columns = pandas.Series(['trace_count', 'span_count','error_span_count'])
    result_dict = df_node_grouped.to_dict(orient="index")


    a = 'Java-otel-demo'

    node_info_list = []
    for k,v in result_dict.items():
        if a == k[0]:
            v["domain"] = k[1]
            v["port"] = str(int(k[2]))
            node_info_list.append(v)
    node_info = {"node_info":node_info_list}
    print(node_info)
