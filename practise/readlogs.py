from app.modules.analyzer import analyze_log

with open("logs/sample.log", "r") as file:

    for line in file:

        result = analyze_log(line)

        print("Log:", line.strip())

        print("Analysis:", result)

        print("----------------")