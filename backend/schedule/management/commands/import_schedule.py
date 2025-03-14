import csv
from datetime import datetime
from dateutil import parser
from django.core.management.base import BaseCommand
from schedule.models import Schedule  # Replace 'schedule' with your actual Django app name

class Command(BaseCommand):
    help = "Import schedule data from a CSV file into the database"

    def handle(self, *args, **kwargs):
        file_path = 'C:/Users/minil/OneDrive/Desktop/Projects/baseball_dashboard/schedule.csv'  # ✅ Update with the actual CSV file path

        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # ✅ Skip the header row

                for row in reader:
                    try:
                        # Extract necessary columns
                        date_str = row[0]  # START DATE (Column 1)
                        start_time_str = row[1]  # START TIME (Column 2)
                        subject = row[3]  # SUBJECT (Column 4 - Contains "Away Team at Home Team")
                        location = row[4]  # LOCATION (Column 5)
                        broadcast = row[5]  # BROADCAST INFO (Column 6)
                        end_time_str = row[8]  # END TIME (Column 9)

                        # Split "Away Team at Home Team"
                        # Print the raw subject column for debugging
                        self.stdout.write(self.style.WARNING(f"DEBUG: Raw SUBJECT Value - '{subject}'"))

                        try:
                            away_team, home_team = subject.split(' at ')
                        except ValueError:
                            self.stdout.write(self.style.ERROR(f"ERROR: Could not split SUBJECT: '{subject}'"))
                            continue
                        

                        # Convert date and time formats
                        date = parser.parse(date_str, yearfirst=False).date()
                        start_time = datetime.strptime(start_time_str, '%I:%M %p').time()
                        end_time = datetime.strptime(end_time_str, '%I:%M %p').time()

                        # ✅ Insert into the database
                        schedule_entry = Schedule(
                          date=date,
                          start_time=start_time,
                          away_team=away_team.strip(),
                          home_team=home_team.strip(),
                          location=location.strip(),
                          broadcast=broadcast.strip(),
                          end_time=end_time
                        )
                        schedule_entry.save()  # ✅ Force save
                        self.stdout.write(self.style.SUCCESS(f"✅ SAVED: {away_team} at {home_team} on {date}"))


                    except ValueError:
                        self.stdout.write(self.style.WARNING(f"Skipping row due to incorrect SUBJECT format: {subject}"))
                        continue

            self.stdout.write(self.style.SUCCESS("✅ CSV data successfully imported into the database!"))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("🚨 Error: CSV file not found. Check the file path and try again."))
