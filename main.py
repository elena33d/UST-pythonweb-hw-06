from src.database import SessionLocal
from src.my_select import (
    select_1, select_2, select_3, select_4, select_5,
    select_6, select_7, select_8, select_9, select_10
)

def main():
    session = SessionLocal()

    print("Select 1:", select_1(session))
    print("Select 2:", select_2(session, 1))
    print("Select 3:", select_3(session, 1))
    print("Select 4:", select_4(session))
    print("Select 5:", select_5(session, 1))
    print("Select 6:", select_6(session, 1))
    print("Select 7:", select_7(session, 1, 1))
    print("Select 8:", select_8(session, 1))
    print("Select 9:", select_9(session, 1))
    print("Select 10:", select_10(session, 1, 1))

    session.close()


if __name__ == "__main__":
    main()