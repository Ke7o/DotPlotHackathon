import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np

class PatientDataExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_file()
        self.us_scan_ids = []

    def read_file(self):
        """Read the CSV file into a pandas DataFrame."""
        try:
            return pd.read_csv(self.file_path)
        except FileNotFoundError:
            print("The file was not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def find_patient(self):
        """Search for a patient by either ID or name based on user input and display details."""
        search_term = input("Enter Patient ID or Name: ")
        if self.data is not None:
            try:
                if search_term.isdigit():
                    results = self.data[self.data['Patient ID'] == int(search_term)]
                else:
                    results = self.data[self.data['Patient Name'].str.contains(search_term, case=False, na=False)]
                self.display_results(results)
            except KeyError as e:
                print(f"Error: The data does not contain the expected column: {e}")
            except Exception as e:
                print(f"An unexpected error occurred during the search: {e}")
        else:
            print("Data is not loaded properly.")

    def display_results(self, results):
        """Display the patient details if found."""
        if not results.empty:
            print("Patient Details Found:")
            print(results[['Patient ID', 'Patient Name', 'Age', 'Height (cm)', 'Weight (kg)', 'History of breast cancer', 'US scan ID']])
            # Extract and store unique US Scan IDs, splitting by space
            us_scan_id_set = set()
            for ids in results['US scan ID']:
                us_scan_id_set.update(ids.split())
            self.us_scan_ids = list(us_scan_id_set)  # Convert set back to list
            print(f"Extracted US Scan IDs: {self.us_scan_ids}")
        else:
            print("No patient found with the given input.")
            self.us_scan_ids = []
   
    def get_US_ID(self):
         if self.us_scan_ids:
             for scan_id in self.us_scan_ids:
                print(f"Patient scan ID is: {scan_id}")
             return self.us_scan_ids
         else:
             print("No US scan IDs available.")
             return []

class GetScansHistory(PatientDataExtractor):
    def __init__(self, scan_file_path):
        self.scan_file_path = scan_file_path
        self.scan_data = self.load_scan_data()

    def load_scan_data(self):
        """Read the US scans CSV file into a pandas DataFrame."""
        try:
            scan_data = pd.read_csv(self.scan_file_path)
            return scan_data
        except FileNotFoundError:
            print("The file was not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    def get_scan_data(self):
        """Search for a patient's scan history based on the US scan IDs."""
        us_scan_ids = patient_extractor.get_US_ID()  # Ensure we get the latest scan IDs list
        if us_scan_ids:
            for scan_id in us_scan_ids:
                if self.scan_data is not None:
                    try:
                        if str(scan_id).isdigit():
                            results = self.scan_data[self.scan_data['US scan ID'] == int(scan_id)]
                        else:
                            results = self.scan_data[self.scan_data['US scan ID'] == scan_id]
                        self.display_results(results)
                    except KeyError as e:
                        print(f"Error: The data does not contain the expected column: {e}")
                    except Exception as e:
                        print(f"An unexpected error occurred during the search: {e}")
                else:
                    print("Data is not loaded properly.")
        else:
            print("No US scan IDs to search for.")

    def display_results(self, results):
        """Display the patient details if found."""
        if not results.empty:
            print("Patient scan history:")
            print(results[['US scan ID', 'Coordinates', 'Scan Date', 'Diagnosis']])
        else:
            print("No patient found with the given input.")

class GetScanImages(PatientDataExtractor):

    def __init__(self, image_folder_path):
        self.image_folder_path = image_folder_path

    def load_and_display_image(self, us_scan_ids):
        """Load and display images corresponding to the given scan IDs."""
        if us_scan_ids:
            for scan_id in us_scan_ids:
                try:
                    image_path = os.path.join(self.image_folder_path, f"{scan_id}.png")
                    print(f"Looking for image at: {image_path}")
                    if os.path.exists(image_path):
                        img = Image.open(image_path)
                        plt.imshow(img)
                        plt.axis('off')  # Hide axes
                        plt.title(f"US Scan ID: {scan_id}")
                        plt.show()
                    else:
                        print(f"No image found for US Scan ID: {scan_id}")
                except Exception as e:
                    print(f"An error occurred while loading the image for US Scan ID {scan_id}: {e}")
        else:
            print("No US scan IDs to display images for.")

    
# Example usage:
path = r"C:\Users\Zavier\OneDrive\Documents\DotPlot accelerator\Dotplot Hackathon\Hackathon_Data_Dotplot\Patients.csv"
scan_path = r"C:\Users\Zavier\OneDrive\Documents\DotPlot accelerator\Dotplot Hackathon\Hackathon_Data_Dotplot\US_scans.csv"
image_folder_path = r"C:\Users\Zavier\OneDrive\Documents\DotPlot accelerator\Dotplot Hackathon\Hackathon_Data_Dotplot\US scans"
patient_extractor = PatientDataExtractor(path)
patient_extractor.find_patient()
scan_id = patient_extractor.get_US_ID()
# Using GetScans to retrieve and print scan data based on US Scan IDs found
get_scans = GetScansHistory(scan_path)
get_scans.get_scan_data()


# Display the image based on the US Scan ID
image_display = GetScanImages(image_folder_path)
image_display.load_and_display_image(scan_id)
