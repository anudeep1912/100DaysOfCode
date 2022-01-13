from selenium import webdriver

# Pre-requisites 1. Download the chrome web driver or web driver for the browser you need to control.

chrome_driver_path = "D:\\Anudeep\\100DaysOfCode\\Development\\chromedriver"   # path of the web driver
driver = webdriver.Chrome(chrome_driver_path)                                  # defining a driver object

driver.get("https://www.python.org/")                    # opening a website in browser
indexed_list = driver.find_element_by_class_name("menu")        # Some of the methods are deprecated.
list_times = driver.find_elements_by_css_selector(".event-widget time")  # Correct usage in next lesson
list_events = driver.find_elements_by_css_selector(".event-widget a")[1:]
events_dict = {}
for i in range(len(list_times)):
    events_dict[i] = {
        "time": list_times[i].text,
        "Event": list_events[i].text
    }

# Created a dictionary with the dates of events on python.

print(events_dict)

driver.quit()