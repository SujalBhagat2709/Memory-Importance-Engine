import json
import os
import re


class HallucinationDetector:

    def __init__(self):

        self.file_name = "analysis_history.json"

        self.history = []

        self.load_history()

        self.known_keywords = {

            "python", "java", "sql", "docker",

            "fastapi", "flask", "api", "machine",

            "learning", "database", "cloud",

            "authentication", "jwt", "linux",

            "git", "tensorflow", "pytorch",

            "react", "javascript", "backend",

            "frontend", "microservices"

        }

    def load_history(self):

        if os.path.exists(self.file_name):

            try:

                with open(

                    self.file_name,

                    "r",

                    encoding="utf-8"

                ) as file:

                    self.history = json.load(file)

            except:

                self.history = []

    def save_history(self):

        with open(

            self.file_name,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.history,

                file,

                indent=4

            )

    def tokenize(self, text):

        return re.findall(

            r"[a-zA-Z0-9]+",

            text.lower()

        )

    def confidence_score(

        self,

        supported,

        total

    ):

        if total == 0:

            return 0

        return round(

            (supported / total) * 100,

            2

        )

    def detect_response(self):

        print("\n========== RESPONSE ANALYSIS ==========\n")

        question = input(

            "User Question: "

        )

        print(

            "\nEnter AI Response"

        )

        print(

            "Press ENTER twice to finish.\n"

        )

        lines = []

        while True:

            line = input()

            if line == "":

                break

            lines.append(line)

        response = "\n".join(lines)

        words = self.tokenize(

            response

        )

        total = len(words)

        supported = 0

        unsupported = []

        for word in words:

            if (

                word in self.known_keywords

                or

                word.isdigit()

            ):

                supported += 1

            elif len(word) <= 3:

                supported += 1

            else:

                unsupported.append(

                    word

                )

        confidence = self.confidence_score(

            supported,

            total

        )

        if confidence >= 80:

            risk = "Low"

        elif confidence >= 60:

            risk = "Medium"

        else:

            risk = "High"

        report = {

            "question": question,

            "confidence": confidence,

            "risk": risk,

            "supported": supported,

            "total_words": total,

            "unsupported": unsupported

        }

        self.history.append(

            report

        )

        self.save_history()

        print("\n========== RESULT ==========\n")

        print(

            "Confidence Score :",

            confidence,

            "%"

        )

        print(

            "Risk Level :",

            risk

        )

        print(

            "Supported Terms :",

            supported

        )

        print(

            "Total Words :",

            total

        )

        print(

            "Possible Unsupported Terms :"

        )

        if unsupported:

            for word in sorted(

                set(unsupported)

            ):

                print(

                    "-",

                    word

                )

        else:

            print(

                "None"

            )

    def view_history(self):

        if not self.history:

            print("\nNo Analysis History.")

            return

        print("\n========== ANALYSIS HISTORY ==========\n")

        for number, report in enumerate(

            self.history,

            start=1

        ):

            print(

                "Analysis :",

                number

            )

            print(

                "Question :",

                report["question"]

            )

            print(

                "Confidence :",

                report["confidence"],

                "%"

            )

            print(

                "Risk :",

                report["risk"]

            )

            print("-" * 60)

    def fact_consistency_analysis(self):

        if not self.history:

            print("\nNo Analysis History Available.")

            return

        latest = self.history[-1]

        confidence = latest["confidence"]

        print("\n========== FACT CONSISTENCY ==========\n")

        print("Question :")

        print(latest["question"])

        print()

        print("Confidence Score :", confidence, "%")

        if confidence >= 90:

            print("Consistency : Excellent")

        elif confidence >= 75:

            print("Consistency : Good")

        elif confidence >= 60:

            print("Consistency : Moderate")

        else:

            print("Consistency : Poor")

        print()

        print("Hallucination Risk :", latest["risk"])

    def quality_score(self):

        if not self.history:

            print("\nNo Analysis History Available.")

            return

        latest = self.history[-1]

        confidence = latest["confidence"]

        unsupported = len(

            latest["unsupported"]

        )

        score = confidence - (unsupported * 2)

        if score < 0:

            score = 0

        print("\n========== RESPONSE QUALITY ==========\n")

        print("Quality Score :", round(score, 2), "/100")

        if score >= 90:

            print("Excellent Response")

        elif score >= 75:

            print("Good Response")

        elif score >= 60:

            print("Needs Improvement")

        else:

            print("Poor Response")

    def statistics(self):

        if not self.history:

            print("\nNo Statistics Available.")

            return

        total = len(self.history)

        average = sum(

            report["confidence"]

            for report in self.history

        ) / total

        high = 0

        medium = 0

        low = 0

        for report in self.history:

            if report["risk"] == "High":

                high += 1

            elif report["risk"] == "Medium":

                medium += 1

            else:

                low += 1

        print("\n========== ANALYSIS STATISTICS ==========\n")

        print("Total Analyses :", total)

        print("Average Confidence :", round(average, 2), "%")

        print("Low Risk :", low)

        print("Medium Risk :", medium)

        print("High Risk :", high)

    def export_report(self):

        if not self.history:

            print("\nNo Report Available.")

            return

        report_name = "hallucination_report.txt"

        with open(

            report_name,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                "========== HALLUCINATION REPORT ==========\n\n"

            )

            for report in self.history:

                file.write(

                    f"Question : {report['question']}\n"

                )

                file.write(

                    f"Confidence : {report['confidence']}%\n"

                )

                file.write(

                    f"Risk : {report['risk']}\n"

                )

                file.write(

                    f"Supported Terms : {report['supported']}\n"

                )

                file.write(

                    f"Total Words : {report['total_words']}\n"

                )

                file.write(

                    "Possible Unsupported Terms:\n"

                )

                for word in report["unsupported"]:

                    file.write(

                        f"- {word}\n"

                    )

                file.write(

                    "-" * 60 + "\n"

                )

        print("\nReport Exported Successfully.")

        print("File :", report_name)

    def delete_history(self):

        if not self.history:

            print("\nHistory Empty.")

            return

        choice = input(

            "\nDelete Entire History? (yes/no): "

        ).lower()

        if choice == "yes":

            self.history.clear()

            self.save_history()

            print("\nHistory Deleted Successfully.")

        else:

            print("\nCancelled.")