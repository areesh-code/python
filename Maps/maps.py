import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import folium
from PIL import Image, ImageTk
import os

class MapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Map App")
        self.root.geometry("800x600")
        
        
        self.locations = {
            "North": (60.0, -100.0),
            "South": (-60.0, -100.0),
            "East": (0.0, 100.0),
            "West": (0.0, -100.0),
            "Center": (0.0, 0.0)
        }

        
        self.create_widgets()
        self.map_frame = None
        
    def create_widgets(self):
        
        title_label = tk.Label(self.root, text="Map Navigator", font=("Arial", 24, "bold"))
        title_label.pack(pady=10)
        
        
        button_frame = ttk.LabelFrame(self.root, text="Navigate to Coordinates", padding=(10, 10))
        button_frame.pack(pady=10)
        
        for name, coords in self.locations.items():
            btn = ttk.Button(button_frame, text=name, command=lambda n=name: self.show_location(n))
            btn.pack(side=tk.LEFT, padx=5)
        
        
        self.map_label = tk.Label(self.root, text="Map will appear here", font=("Arial", 16), bg="lightgray")
        self.map_label.pack(pady=10, fill=tk.BOTH, expand=True)

    def show_location(self, location_name):
        coords = self.locations[location_name]
        self.generate_map(location_name, coords)

    def generate_map(self, location_name, coords):
        
        fmap = folium.Map(location=coords, zoom_start=4)
        folium.Marker(location=coords, popup=f"{location_name}: {coords}").add_to(fmap)

        
        map_file = "temp_map.html"
        fmap.save(map_file)

        
        self.save_map_as_image(map_file)

    def save_map_as_image(self, map_file):
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.service import Service
            from selenium.webdriver.chrome.options import Options
            
            
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--window-size=800x600')

            service = Service("chromedriver")  
            driver = webdriver.Chrome(service=service, options=options)

            
            driver.get(f"file://{os.path.abspath(map_file)}")
            screenshot_path = "temp_map.png"
            driver.save_screenshot(screenshot_path)
            driver.quit()

           
            img = Image.open(screenshot_path)
            img = img.resize((800, 400), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)

            self.map_label.config(image=photo, text="")
            self.map_label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Unable to display map: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MapApp(root)
    root.mainloop()

 
 
    
