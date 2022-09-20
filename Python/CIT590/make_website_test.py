import unittest

from make_website import*

class Make_Website_Test(unittest.TestCase):

    global f
    global g
    global h
    global letter
    global cap_letter
    
    f = init('resume.txt')
    g = init('resume_test.txt')
    h = init('resume_template.html')
    letter = 'abcdefghijklmnopqrstuvwxyz'
    cap_letter = letter.upper()
    
    def test_init(self):
        self.assertTrue(type(f) == list)
        self.assertFalse(type(f[2]) != str)
        self.assertFalse(f == '')

    def test_name(self):
        list0 = name(f)
        
        self.assertTrue(type(name(f)) == str)
        self.assertNotEqual(list0[0], '')
        self.assertNotEqual(list0[len(list0)-1], '')
        self.assertRaises(RuntimeError,name,g)

    def test_email(self):
        email_add = email(f)
        
        self.assertTrue(type(email_add) == str)
        self.assertIn('@',email_add)

        email_lst = email_add.split('@')
        email_lst2 = email_lst[1]
        self.assertNotEqual(email_lst2,email_lst2.capitalize())

        self.assertTrue('.com' == email_lst2[-4:] or '.edu' == email_lst2[-4:])
        self.assertFalse('.org' == email_lst2[-4:])

        for i in email_add:
            self.assertIs(type(i),str)

    def test_projects(self):
        global letter
        global cap_letter
        
        project = projects(f)
        project1 = project[0]

        self.assertTrue(type(project) == list)
        self.assertTrue(project1[0] in cap_letter or project1[0] in letter)

        for i in project1:
            self.assertTrue(type(i) == str)

        for i in range(1,len(project)):
            self.assertNotEqual(project[i],'')

    def test_courses(self):
        course = courses(f)
        course1 = course[0]

        self.assertTrue(type(course) == list)
        self.assertTrue(course1[0] in cap_letter or course1[0] in letter)
        self.assertNotIn('Courses',course1)

        for i in range(0,len(course)):
            self.assertNotIn(':',course[i])
            self.assertNotIn('-',course[i])
            
    def test_remove_tags(self):
        global h
        
        h = remove_tags(h)
        self.assertFalse(h[-2] == '</body>' and h[-1] == '</html>')

    def test_create_email_link(self):
        email_add = 'lukekasper25@gmail.com'

        email_link = create_email_link(email_add)

        self.assertTrue(type(email_link) == str)
        self.assertIn('[AT]', email_link)
        self.assertNotEqual(email_add,email_link)
        self.assertIn(email_add, email_link)

    def testadd_header(self):
        global h

        h = add_header(h)

        self.assertTrue(h[0] == '<div id="page-wrap">')

    def test_basic_html(self):
        basic_h = basic_html(f)

        self.assertTrue(type(basic_h) == str)
        self.assertEqual(basic_h[0:5],'<div>')
        self.assertTrue(basic_h[-6:] == '</div>')

    def test_projects_html(self):
        project_h = projects_html(f)
    
        self.assertTrue(type(project_h) == str)
        self.assertEqual(project_h[0:5],'<div>')
        self.assertTrue(project_h[-6:] == '</div>')
        
        project_list = project_h.split('\n')
        self.assertTrue(project_list[1] == '<h2>Projects</h2>')
        self.assertEqual(project_list[2],'<u1>')
        self.assertEqual(project_list[-2],'</u1>')

        for i in range(3,4):
            project_line = project_list[i]
            self.assertTrue(project_line[0:4] == '<li>')
            self.assertTrue(project_line[-5:] == '</li>')

    def test_courses_html(self):
        courses_h = courses_html(f)

        self.assertTrue(type(courses_h) == str)
        self.assertEqual(courses_h[0:5],'<div>')
        self.assertTrue(courses_h[-6:] == '</div>')

        courses_list = courses_h.split('\n')
        self.assertTrue(courses_list[1] == '<h3>Courses</h3>')

        courses_line = courses_list[2]
        self.assertTrue(courses_line[0:6] == '<span>')
        self.assertTrue(courses_line[-7:] == '</span>')

    def test_close_html(self):
        tag = close_html()

        global h

        self.assertTrue(type(tag) == str)

        h.append(tag)

        self.assertEqual(h[-1],'\n</div>\n</body>\n</html>')
             
if __name__  == '__main__':
    unittest.main()
