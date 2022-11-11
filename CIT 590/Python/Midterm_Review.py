def init(filename):
    '''
    Read a file and insert information into two dictionaries.
    The key-value pair is given in the comments.
    You can assume that each line in the file has the format "emp_name,manager_name"
    Return both dictionaries from this function.
    '''
    # managers : dictionary to store every employee's manager.
    # One employee has no manager if he's a leader of his team.
    emp_manager = {}

    # members: dictionary to store all members of a manager at the first level of connection
    members = {}
    
    f = open(filename,'r')
    for line in f:
        line1 = line.strip()
        emp, manager = line1.split(',')
        if (manager != ''):
            emp_manager[emp] = manager
            lst = members.get(manager, [])
            lst.append(emp)
            members[manager] = lst
        else:
            emp_manager[emp] = manager
            members[manager] = emp
        line = f.readline()
    f.close()
    return (emp_manager,members)

def get_emp_name(members,man_name):
    '''
    Return all the names of the employees of a certain manager.
    Note that the manager may not exist.
    '''
    employees = members.get(man_name)
    print(employees, 'is managed by', man_name)

    return

def top_manager_name(members,emp_manager,emp):
    '''
    One employee can also be another's manager.
    Given an employee, can you find his top manager, which is the manager in the highest level?
    '''

    flag = 0
    manager = emp_manager.get(emp)

    while (flag == 0):
        if (manager == 'none'):
            flag = 1
            manager = emp
        
        else:
            emp = manager
            manager = emp_manager.get(manager)
            
    return manager

def get_co_emp(members,emp):
    '''
    Given an employee, return his coworkers who have the same manager.
    If the employee does not exist or if he has no coworkers, return an empty list.
    '''

    pass

def dismiss(members,emp_manager,emp):
    '''
    We now want to dismiss a given employee A.
    If A has members, then all the members will have a new manager, who is the manager of A.
    if A doesn't has his own manager, when he is dismissed, each of his memebers will be the manager of their own. For example, A has two members B and C while A has no manager.When A is dismissed, B will be the manager of himself.
    '''

    pass

def hire(members,emp_manager,emp,manager):
    '''
    We hire a new employee and assign a new manager. The employee should not be in either members or emp_manager.
    The manager must be hired in advance.
    Return False if we cannot do the operation, return True if we can.
    '''

    pass
    
def main():

    emp_manager, members = init("emp.txt")
    #get_emp_name(members,'Mary')
    #top_manager_name(members,emp_manager,')
    print(emp_manager, members, sep = '\n')

    # insert code to make some queries

if __name__ == "__main__":
    main()
