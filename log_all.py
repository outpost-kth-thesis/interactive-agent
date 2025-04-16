def request(flow):
    print(f">>> Request: {flow.request.method} {flow.request.url}")

def response(flow):
    print(f"<<< Response: {flow.response.status_code} {flow.request.url}")
