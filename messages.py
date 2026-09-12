# M1.5 - Three-turn conversation history

messages = [
    {
        "role": "system",
        "content": "You are a research assistant."
    }
]

# Turn 1
messages.append({
    "role": "user",
    "content": "What is quantum computing?"
})

messages.append({
    "role": "assistant",
    "content": "Quantum computing uses quantum mechanics to process information."
})

# Turn 2
messages.append({
    "role": "user",
    "content": "What are its applications?"
})

messages.append({
    "role": "assistant",
    "content": "Quantum computing may be useful in areas such as cryptography, optimization, and scientific simulation."
})

# Turn 3
messages.append({
    "role": "user",
    "content": "What are its advantages?"
})

messages.append({
    "role": "assistant",
    "content": "Its potential advantages include solving some problems more efficiently and simulating complex systems."
})


# Display the complete conversation
for message in messages:
    print(message["role"], ":", message["content"])