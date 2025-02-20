import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def googleMapsDistanceCheck(startAddress, endAddress):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Pixel 4 API 35"
    options.app_package = "com.example.myapplication"
    options.app_activity = "com.example.myapplication.MainActivity"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    try:
        wait = WebDriverWait(driver, 15)  

        driver.press_keycode(3)

        wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Maps"))).click()

        wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.google.android.apps.maps:id/search_omnibox_text_box"))).click()

        search_box = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.google.android.apps.maps:id/search_omnibox_edit_text")))
        search_box.click()
        search_box.send_keys(endAddress)
        driver.press_keycode(66)  

        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(14)'))).click()


        start_location = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(8)')))
        start_location.click()
        search_box.send_keys(startAddress)
        driver.press_keycode(66) 



        # wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.rivian.android.consumer:id/rivian_pill_button_container"))).click()

        # wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.rivian.android.consumer:id/soc_indicator_chevron"))).click()

        # start_address = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.rivian.android.consumer:id/location_search_edittext")))
        # start_address.click()
        # start_address.send_keys(startAddress)

        # wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.rivian.android.consumer:id/search_suggestion_title"))).click()

        # wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.rivian.android.consumer:id/rivian_pill_button_container"))).click()

        # trip_duration_element = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.rivian.android.consumer:id/trip_itinerary_header_duration")))
        # trip_duration = trip_duration_element.text
        # return trip_duration

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()
        
if __name__ == "__main__":
    print(googleMapsDistanceCheck("560 Westmount Rd N, Waterloo, ON N2L 0A9", "Waterloo Public Library - John M. Harper Branch, 500 Fischer-Hallman Rd N, Waterloo, ON N2L 0B1"))
    
