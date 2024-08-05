from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

class DragAndDropAutomation:
    def __init__(self, driver_path, url):
        self.driver_path = driver_path
        self.url = url
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def perform_drag_and_drop(self):
        # Switch to the frame containing the drag and drop elements
        frame = self.driver.find_element(By.CLASS_NAME, "demo-frame")
        self.driver.switch_to.frame(frame)

        # Locate the draggable element
        draggable = self.driver.find_element(By.ID, "draggable")

        # Locate the droppable element
        droppable = self.driver.find_element(By.ID, "droppable")

        # Perform the drag and drop action
        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable, droppable).perform()

    def teardown(self):
        # Wait for a few seconds to observe the result
        time.sleep(5)
        self.driver.quit()

    def run(self):
        self.setup()
        self.perform_drag_and_drop()
        self.teardown()

if __name__ == "__main__":
    driver_path = 'path/to/chromedriver'  # Update this with the actual path to your ChromeDriver
    url = "https://jqueryui.com/droppable/"

    automation = DragAndDropAutomation(driver_path, url)
    automation.run()
