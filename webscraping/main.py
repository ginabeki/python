from bs4 import BeautifulSoup
# install Beautifulsoup
#install lxml
# access files
with open('index.html', 'r') as html_file:
    content = html_file.read()

# read  html file from real website, web scraping is basically information pulling
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify)
    # capture all h5 tags element
    # courses_html_tags = soup.find_all('h5')
    # # print(courses_html_tags)
    # for course in courses_html_tags:
    #     print(course.text)
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
    