# библиотека для задания normal

class Person:
    def __init__(self, surname, io):
        self.surname = surname
        self.io = io

    def get_full_name(self):
        self.full_name = self.surname + ' ' + self.io
        return self.full_name


class Schoolkid(Person):
    def __init__(self, surname, io, parents, class_name, class_subj):
        Person.__init__(self, surname, io)
        self.parents = parents
        self.class_name = class_name
        self.class_subj = class_subj

    def get_class_id(self):
        return self.class_name

    def get_class_kids_list(self):
        self.class_kids_list = [self.get_full_name(), self.class_name]
        return self.class_kids_list

    def get_kid_subj_list(self):
        self.kid_subj_list = [self.get_full_name(), self.class_subj]
        return self.kid_subj_list

    def get_parent_list(self):
        self.kid_parent_list = [self.get_full_name(), self.parents]
        return self.kid_parent_list

    def get_class_subj_list(self):
        self.class_subj_list = [self.class_name, self.class_subj]
        return self.class_subj_list


class Teacher(Person):
    def __init__(self, surname, io, subj):
        Person.__init__(self, surname, io)
        self.subj = subj

    def get_teachers_list(self):
        self.teachers_list = [self.get_full_name(), self.subj]
        return self.teachers_list
