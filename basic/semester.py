# This exercise uses a data structure that stores Udacity course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }


courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                        'teacher': 'Dave',
                        'assistant': 'Peter C.'},
                'cs373': {'name': 'Programming a Robotic Car',
                        'teacher': 'Sebastian',
                        'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                        'teacher': 'Dave',
                        'assistant': 'Sarah'},
                'cs212': {'name': 'The Design of Computer Programs',
                        'teacher': 'Peter N.',
                        'assistant': 'Andy',
                        'prereq': 'cs101'},
                'cs253': {'name': 'Web Application Engineering - Building a Blog',
                        'teacher': 'Steve',
                        'prereq': 'cs101'},
                'cs262': {'name': 'Programming Languages - Building a Web Browser',
                        'teacher': 'Wes',
                        'assistant': 'Peter C.',
                        'prereq': 'cs101'},
                'cs373': {'name': 'Programming a Robotic Car',
                        'teacher': 'Sebastian'},
                'cs387': {'name': 'Applied Cryptography',
                        'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                        'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                        'teacher': 'Jasper'},
                    }
    }


def when_offered(courses, course):
    semester=[]
    for s in courses:
        for c in courses[s]:
            if c == course: semester.append(s)
    return semester



print(when_offered(courses, 'cs101'))
# Correct result: 
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result: 
# []