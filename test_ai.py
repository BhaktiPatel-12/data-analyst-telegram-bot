from agent import analyze_question
question = """
Calculate the average of:
10,20,30

Return JSON:
{
"average": number
}
"""
answer = analyze_question(question)
print(answer)