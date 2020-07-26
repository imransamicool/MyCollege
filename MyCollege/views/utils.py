from ..views.StudentsV import opr_menu


def banner(sy_mb):
    msg = 'Welcome to My College'
    print(len(msg)*sy_mb)
    print(msg)
    print(len(msg) * sy_mb)
    opr_menu()
