class Students:

    def __init__(self):
        self.birthday = [("Katrina", "2002-03-16"),    ("Pola", "2002-12-31"),    ("Anna", "1995-09-03"),    ("Annemieke", "1992-11-18"),    ("Kate", "1991-07-22"),    ("Victoria", "1994-06-10"),    ("Laszlo", "1990-04-25"),    ("Akash", "1996-03-09"),    ("Jarick", "1989-08-05"),    ("Liam", "1997-03-09"),    ("Olivia", "1994-12-20"),    ("Noah", "1993-02-14"),    ("Ava", "1988-03-09"),    ("William", "1992-07-02"),    ("Sophia", "1995-04-11"),    ("James", "1990-09-08"),    ("Isabella", "1991-06-27"),    ("Ethan", "1998-01-03"),    ("Mia", "1996-11-29"),    ("Benjamin", "1987-03-31"),    ("Charlotte", "1992-08-12"),    ("Alexander", "1995-05-06"),    ("Amelia", "1993-10-15"),    ("Michael", "1991-11-23"),    ("Emily", "1990-06-18"),    ("Daniel", "1994-09-19"),    ("Abigail", "1996-12-07"),    ("Matthew", "1989-04-04"),    ("Sofia", "1997-07-01"),    ("Jacob", "1992-02-23")]

    def extract_month_day(self, date):
        # ex:  "2002-03-16" return: 03-16
        return date[5::]


    def sort_bday(self):
        return sorted(self.birthday, key=lambda x: (int(x[1][5:7]), int(x[1][8::])))

