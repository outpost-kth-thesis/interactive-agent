def response(flow):
    if flow.request.scheme == "http":
        print(f"\n=== REQUEST ===\n{flow.request.method} {flow.request.url}")
        print("".join([f"{k}: {v}\n" for k, v in flow.request.headers.items()]))
        print(flow.request.get_text())

        print(f"\n=== RESPONSE ===\n{flow.response.status_code} {flow.response.reason}")
        print("".join([f"{k}: {v}\n" for k, v in flow.response.headers.items()]))
        print(flow.response.get_text())