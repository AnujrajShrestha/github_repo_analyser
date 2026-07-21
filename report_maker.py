def create_report(state: dict):

    separator = "\n" + "-" * 60 + "\n"

    with open("report.txt", "w", encoding="utf-8") as fs:

        fs.write(separator)
        fs.write("Step 1 - Analysis agent is working\n")
        fs.write(separator)

        for key, value in state["analysis_result"].items():
            fs.write(f"{key}: {value}\n")

        fs.write(separator)
        fs.write("Step 2 - Summarize Agent is working\n")
        fs.write(separator)

        for key, value in state["summarize_result"].items():
            fs.write(f"{key}: {value}\n")

        fs.write(separator)
        fs.write("Step 3 - Review Agent is working\n")
        fs.write(separator)

        for key, value in state["review_result"].items():
            fs.write(f"{key}: {value}\n")
    return "report.txt"