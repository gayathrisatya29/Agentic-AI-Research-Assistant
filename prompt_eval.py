# M1.4 - Prompt Engineering Evaluation

test_queries = [
    {
        "query": "How does solar energy generate electricity?",
        "expected": "Solar energy"
    },
    {
        "query": "What are the uses of CRISPR in medicine?",
        "expected": "CRISPR in medicine"
    },
    {
        "query": "What are the applications of quantum computing?",
        "expected": "Quantum computing"
    },
    {
        "query": "How can AI help detect cancer earlier?",
        "expected": "AI in cancer detection"
    },
    {
        "query": "What causes climate change?",
        "expected": "Climate change"
    },
    {
        "query": "How do electric vehicles reduce emissions?",
        "expected": "Electric vehicles"
    },
    {
        "query": "What are the benefits of cloud computing?",
        "expected": "Cloud computing"
    },
    {
        "query": "How does blockchain work in finance?",
        "expected": "Blockchain in finance"
    },
    {
        "query": "What are the applications of robotics in healthcare?",
        "expected": "Robotics in healthcare"
    },
    {
        "query": "How does gene therapy treat disease?",
        "expected": "Gene therapy"
    }
]


# Example predictions for demonstration
predictions = [
    "Solar energy",
    "CRISPR in medicine",
    "Quantum computing",
    "AI in cancer detection",
    "Climate change",
    "Electric vehicles",
    "Cloud computing",
    "Blockchain in finance",
    "Robotics in healthcare",
    "Gene therapy"
]


correct = 0

for i in range(len(test_queries)):
    expected = test_queries[i]["expected"]
    predicted = predictions[i]

    if expected == predicted:
        correct += 1


accuracy = (correct / len(test_queries)) * 100

print(f"Correct: {correct}/{len(test_queries)}")
print(f"Accuracy: {accuracy:.1f}%")