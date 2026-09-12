import tiktoken


query = "What are the applications of quantum computing?"

context = """
Quantum computing uses quantum mechanics to process information.
It may have applications in cryptography, optimization,
drug discovery, and scientific simulation.
"""


encoding = tiktoken.get_encoding("cl100k_base")


query_tokens = encoding.encode(query)
context_tokens = encoding.encode(context)


print("Query tokens:", len(query_tokens))
print("Context tokens:", len(context_tokens))
print("Total tokens:", len(query_tokens) + len(context_tokens))

estimated_requests = 1000

total_tokens_for_1000 = (len(query_tokens) + len(context_tokens)) * estimated_requests

print("Total tokens for 1000 requests:", total_tokens_for_1000)