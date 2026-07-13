from hallucination_detector import HallucinationDetector


class DetectionEngine:

    def __init__(self):

        self.detector = HallucinationDetector()

    def display_menu(self):

        while True:

            print("\n")

            print("=" * 60)

            print("         HALLUCINATION DETECTION ENGINE")

            print("=" * 60)

            print("1. Analyze AI Response")

            print("2. View Analysis History")

            print("3. Fact Consistency Analysis")

            print("4. Response Quality Score")

            print("5. Statistics Dashboard")

            print("6. Export Analysis Report")

            print("7. Delete Analysis History")

            print("8. Exit")

            choice = input("\nEnter Choice: ").strip()

            if choice == "1":

                self.detector.detect_response()

            elif choice == "2":

                self.detector.view_history()

            elif choice == "3":

                self.detector.fact_consistency_analysis()

            elif choice == "4":

                self.detector.quality_score()

            elif choice == "5":

                self.detector.statistics()

            elif choice == "6":

                self.detector.export_report()

            elif choice == "7":

                self.detector.delete_history()

            elif choice == "8":

                print("\nThank You For Using Hallucination Detection Engine!")

                break

            else:

                print("\nInvalid Choice. Please Try Again.")


if __name__ == "__main__":

    engine = DetectionEngine()

    engine.display_menu()