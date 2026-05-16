from app.modules.analyzer import analyze_log

with open("logs/sample.log", "r") as file:

    with open("logs/alerts.txt", "w") as alerts_file:

        for line in file:

            result = analyze_log(line)

            alerts_file.write(result + "\n")