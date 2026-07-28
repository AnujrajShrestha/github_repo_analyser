def create_report(state: dict):

    separator = "\n" + "-" * 60 + "\n"

    with open("report.txt", "w", encoding="utf-8") as fs:

        fs.write(separator)
        fs.write("Summary:\n")
        fs.write(separator)
        fs.write(state["summary"])

        fs.write(separator)
        fs.write("Architecture: \n")
        fs.write(separator)
        fs.write(state["architecture"]) 

        fs.write(separator)
        fs.write("Review: \n")
        fs.write(separator)
        fs.write(state['review'])
    return "langGraph/report.txt"