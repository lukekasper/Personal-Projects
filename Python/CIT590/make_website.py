def init(filename):
    '''Converts the .txt file into a list of strings.
       Each line is a seperate string in the file list.'''

    #opens the file and reads the lines as a list of strings
    stream = open(filename)
    lines_lst = stream.readlines()
    
    return lines_lst

def name(file_lst):
    '''Extracts the name from the file as the first element in the file list.'''

    #takes the first element of the file list and strip whitespace
    list0 = file_lst[0]
    list0 = list0.strip()

    #splits both strings by the space
    list_split = list0.split(' ')

    #if the first and last names are not capitlized, raise a Runtime Error
    for i in range(0,len(list_split)):
        if (list_split[i].capitalize() != list_split[i]):
            raise RuntimeError('A valid name must begin with a capital letter')
            break
            
    return list0

def email(file_lst):
    '''Finds the email and determines relative criteria for a valid email address.'''

    flag = 0

    #iterating over the full list
    for i in range(0,len(file_lst)):
        line = file_lst[i]

        #for each letter in that line, if it has an '@', designate that line as the email address
        for j in line:
            if (j == '@'):
                email = line

    #strip whitespace and split the address by the '@' symbol
    email = email.strip()           
    email_lst = email.split('@')
    email_lst2 = email_lst[1]

    #if the first letter after the '@' is capitilized, raise a flag
    if (email_lst2 == email_lst2.capitalize()):
        flag = 1

    #if it does not end in '.com' or '.edu', raise a flag
    elif ('.com' != email_lst2[-4:] and '.edu' != email_lst2[-4:]):
        flag = 1

    #if there are any other character types besides strings (letters/symbols), raise a flag
    for i in email:
        if (type(i) != str):
            flag = 1
            
    #if any flags are raised, the email is considered to be missing
    if (flag == 1):
        email = ''
    
    return email

def courses(file_lst):
    '''Finds the courses in the .txt file and converts it into a list of courses.'''

    #iterating through the list of lines, if 'Courses' appears, designate that line as course list
    for i in range(0,len(file_lst)):
        if ('Courses' in file_lst[i]):
            line = file_lst[i]

    #strip the whitespace       
    line = line.strip()

    #iterating through the characters in that line (starting at 7 to skip over the word 'courses')
    for i in range (7,len(line)):

        #finds the first character that is a letter
        if (line[i] in 'abcdefghijklmnopqrstuvwxyz'):

            #makes that the new course list (to get rid of the punctuation) and split the courses into a list
            courses = line[i-1:len(line)]
            courses = courses.split(',')

            #removes whitespaces
            for j in range(1,len(courses)):
                courses[j] = courses[j].strip()
            break
        
    return courses
      
def projects(file_lst):
    '''Finds the projects and converts it into a list of projects.'''

    #iterates over the file list and looks for the word 'projects'
    for i in range(0,len(file_lst)):

        #if it finds it, designates that line as the projects list and finds the index
        if ('Projects' in file_lst[i]):
            line1 = file_lst[i]
            index1 = file_lst.index(line1)

    #iterates over the rest of the file and finds where projects ends (where there are at least 10 '-' signs)
    for j in range(index1,len(file_lst)):

        #finds the index for that line 
        if ('----------' in file_lst[j]):
            line2 = file_lst[j]
            index2 = file_lst.index(line2)

    #makes the new project list between that range
    projects = file_lst[index1:index2]
    projects = ''.join(projects)
    projects = projects.split('\n')

    #strips whitespace
    for l in range(0,len(projects)):
        projects[l] = projects[l].strip()

    #if the line is blank, delete it
    index = []
    count = 0
    for q in range(0,len(projects)):
        if (projects[q] == ''):
           count += 1
           index.append(q)

    
    for k in range(0,len(projects)-(count-1)):
        if (projects[k] == ''):
            projects.pop(k)

    #sets projects and eliminates 'projects' header        
    projects = projects[1:len(projects)]
                        
    return projects

def remove_tags(file):
    '''Removes last two lines of html template'''
    
    del file[-2:]
    return file

def surround_block(tag, text):
    '''Surrounds text with html block formatting.
       Inputs are user designated tag and text to be blocked.'''

    new_text = '<' + tag + '>' + text + '</' + tag + '>'
    
    return new_text

def create_email_link(email_address):
    '''Creates an email link in html format in string format.'''

    #turns email address string into a list
    lst = list(email_address)

    #iterating over the characters in email address
    for i in range(0,len(lst)):

        #when the '@' is detected, replace with '[AT]'
        if (lst[i] == '@'):
            lst[i] = '[AT]'

    #join back into a string and format via html template
    new_email = ''.join(lst)
    email_tag = '<a href="mailto:' + email_address + '">' + 'Email: ' + new_email + '</a>'
    
    return email_tag

def add_header(file):
    '''Add header to html file.'''

    file.insert(0, '<div id="page-wrap">')

    return file

def basic_html(file_lst):
    '''Organizes the name and email into the html template format.
       Concatonates both strings into a single string block.'''

    #calling functions to search file for name and email
    name1 = name(file_lst)
    email1 = email(file_lst)

    #format both to html template
    name_block = surround_block('h1', name1)
    email_tag = create_email_link(email1)
    email_block = surround_block('p', email_tag)

    #concatonate both blocks and format for html
    basic_info = '\n' + name_block + '\n' + email_block + '\n'
    basic_block = surround_block('div', basic_info)

    return basic_block

def projects_html(file_lst):
    '''Formats project list for html output'''

    #calls function to find projects from file and blocks the projects header
    project = projects(file_lst)
    block = surround_block('h2', 'Projects')

    #blocks each line of projects and seperates them with a new line
    for i in range(0,len(project)):
        project[i] = surround_block('li', project[i])
        project[i] = '\n' + project[i]

    #joins the list into a string and puts a new line
    project_lines = ''.join(project) + '\n'

    #formats the string to fit html template and concatonate the header with the projects string
    project_block = surround_block('u1', project_lines)
    project_conc = '\n' + block + '\n' + project_block + '\n'
    project_html = surround_block('div', project_conc)

    return project_html

def courses_html(file_lst):
    '''Formats courses list for html output.'''

    #calls function to find courses from file and blocks courses header
    course = courses(file_lst)
    block = surround_block('h3', 'Courses')

    #joins the courses list into a single string, blocks the courses string, and combines it with the header
    courses_str = ', '.join(course)
    courses_block = surround_block('span', courses_str)
    courses_block = '\n' + block + '\n' + courses_block + '\n'
    courses_html = surround_block('div', courses_block)

    return courses_html

def close_html():
    '''Adds the final three lines to complete the html file'''
    
    close_tag = '\n' + '</div>' + '\n' + '</body>' + '\n' + '</html>'

    return close_tag
    
def main():
    '''Main function that runs all subsequent functions and outputs the .html resume file.'''

    #loads the resume text file as a line-by-line list of strings
    file_list = init('resume.txt')

    #adds the html format to the info, projects, and courses sections
    body = basic_html(file_list) + '\n' + projects_html(file_list) + '\n' + courses_html(file_list)

    #loads the resume template and formats it according to our desired .html output
    html_list = init('resume_template.html')
    html_list = remove_tags(html_list)
    html_list = add_header(html_list)
    html_str = ''.join(html_list)

    #writes the .html template, body (our resume.txt information),
    #and finaal closing html tags, before closing the file
    f = open('resume.html', 'w')
    f.write(html_str)
    f.write(body)
    f.write(close_html())
    f.close()
    
    return

if __name__ == "__main__":
    main()
