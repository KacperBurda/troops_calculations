from soldier import Soldier
from ranks import Private, Officer
from payment_bonuses import BonusForManeuvers, BonusForNegotiations


def main() -> None:

    # henrys_bonus = BonusForManeuvers(maneuvers_number=4)
    # henry = Soldier(id=12243, name='Henry', rank=Private(), bonus_pay2=henrys_bonus)
    # print(henry)
    # print(' ' * 20)
    #
    # toms_rank = Private(hourly_pay_rate=15, hours_worked=34)
    # tom = Soldier(id=12243, name='Tom', rank=toms_rank)
    # print(tom)
    # print(' ' * 20)
    #
    # paul_bonus_pay = BonusForNegotiations()
    # paul_bonus_pay2 = BonusForManeuvers(maneuvers_number=2)
    # paul = Soldier(id=34646, name='Paul', rank=Private(hourly_pay_rate=15, hours_worked=30),
    #                bonus_pay=paul_bonus_pay, bonus_pay2=paul_bonus_pay2)
    # print(paul)
    # print(' ' * 20)
    #
    # stevens_rank = Private(hourly_pay_rate=15, hours_worked=34)
    # steven = Soldier(id=12243, name='Steven', rank=stevens_rank,
    #                  bonus_pay=BonusForManeuvers(maneuvers_number=2))
    # print(steven)
    # print(' ' * 20)
    #
    # tims_rank = Officer(hourly_pay_rate=20, hours_worked=21)
    # tim = Soldier(id=453, name='Tim', rank=tims_rank, bonus_pay=BonusForManeuvers())
    # print(tim)
    # print(' ' * 20)
    #
    # johns_rank = Officer(hourly_pay_rate=50, hours_worked=24)
    # johns_bonus = BonusForManeuvers(maneuvers_number=4)
    # john = Soldier(id=12243, name='John', rank=johns_rank,
    #                bonus_pay=johns_bonus, bonus_pay2=BonusForNegotiations())
    # print(john)
    # print(' ' * 20)
    #
    # # del henry  # <-------- deletion of henry!
    # # del paul  # <--------- deletion of paul!
    #
    # mikes_bonus = BonusForManeuvers(maneuvers_number=6)
    # mike = Soldier(id=12243, name='Mike',
    #                rank=Private(hourly_pay_rate=15, hours_worked=12), bonus_pay2=mikes_bonus)
    # print(mike)
    # print(' ' * 20)
    #
    # print(Soldier.total_info_about_troops())

if __name__ == "__main__":
    main()
