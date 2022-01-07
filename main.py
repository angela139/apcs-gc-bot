import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from time import sleep
import getpass

student_array = []


def main():
    driver = uc.Chrome()
    driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    username = input("Email: ")
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(username)
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()
    sleep(2)
    password = getpass.getpass('Password: ')
    driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button').click()
    two_step_check = input("Have you been logged in? ")
    if two_step_check == "Yes":
        print("Can continue")
    else:
        print("Error")
        driver.quit()
        quit()
    assignment_link = input("Please paste in your assignment link: ")
    # Sample assignment link
    # "https://classroom.google.com/u/0/c/NDI1NzE0MzUyNjM3/a/NDI1NzE3OTE1OTAy/submissions/by-status/and-sort-last-name/all"
    # "https://classroom.google.com/c/MzgwMTA3MTc2MDE2/a/NDE3ODU4NzAzODE0/submissions/by-status/and-sort-last-name/student/MTI2NDY4NTE1"
    driver.get(assignment_link)
    sleep(2)
    num_students = len(driver.find_elements(By.CLASS_NAME, 'WkZsyc'))
    print(num_students)
    for student in range(num_students):
        name = driver.find_elements(By.CLASS_NAME, 'J33wTc')[student].text
        print(name)
        link = driver.find_elements(By.CLASS_NAME, 'vwNuXe')[student].get_attribute("href")
        print(link)
        student_dict = {"name": name.split()[0], "link": link}
        student_array.append(student_dict)

    print(student_array)
    sleep(3)
    driver.quit()

    f = open("work.md", "a")
    for work in student_array:
        f.write("\n" + "[" + work["name"] + "](" + work["link"] + ")" + " " + " " + " ")
    f.close()


if __name__ == "__main__":
    main()
