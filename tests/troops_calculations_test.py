import unittest
from soldier import Soldier
from ranks import Private, Officer
from payment_bonuses import BonusForManeuvers, BonusForNegotiations


class TestClassPrivate(unittest.TestCase):

    def test_instance_private(self):
        soldier_one_rank = Private()
        self.assertEqual(soldier_one_rank.get_payment(), 1000,
                         msg="Base payment for Soldier with Private rank is equal to 1000")

        soldier_two_rank = Private(hourly_pay_rate=30, hours_worked=20)
        self.assertEqual(soldier_two_rank.get_payment(), 1600,
                         msg="Base payment for Soldier with Private rank is equal to 1000"
                             " + hourly pay tate * hours worked is equal to 600")

    def test_instance_private_negative_value(self):
        with self.assertRaises(ValueError):
            soldier_one_rank = Private(hourly_pay_rate=-40, hours_worked=-30)
        with self.assertRaises(ValueError):
            soldier_one_rank = Private(hourly_pay_rate=40, hours_worked=-30)
        with self.assertRaises(ValueError):
            soldier_one_rank = Private(hourly_pay_rate=-40, hours_worked=30)

    def test_instance_private_not_integer(self):
        with self.assertRaises(TypeError):
            soldier_one_rank = Private(hourly_pay_rate='tree', hours_worked=30)
        with self.assertRaises(TypeError):
            soldier_one_rank = Private(hourly_pay_rate=40, hours_worked='twenty')
        with self.assertRaises(TypeError):
            soldier_one_rank = Private(hourly_pay_rate=40.57, hours_worked=30)


class TestClassOfficer(unittest.TestCase):

    def test_instance_officer(self):
        officer_one_rank = Officer()
        self.assertEqual(officer_one_rank.get_payment(), 4000,
                         msg="Base payment for Soldier with Officer rank is equal to 4000")

        officer_two_rank = Officer(hourly_pay_rate=30, hours_worked=20)
        self.assertEqual(officer_two_rank.get_payment(), 4600,
                         msg="Base payment for Soldier with Private rank is equal to 4000"
                             " + hourly pay tate * hours worked is equal to 600")

    def test_instance_officer_negative_value(self):
        with self.assertRaises(ValueError):
            officer_one_rank = Private(hourly_pay_rate=-40, hours_worked=-30)
        with self.assertRaises(ValueError):
            officer_one_rank = Private(hourly_pay_rate=40, hours_worked=-30)
        with self.assertRaises(ValueError):
            officer_one_rank = Private(hourly_pay_rate=-40, hours_worked=30)

    def test_instance_officer_not_integer(self):
        with self.assertRaises(TypeError):
            officer_one_rank = Private(hourly_pay_rate='tree', hours_worked=30)
        with self.assertRaises(TypeError):
            officer_one_rank = Private(hourly_pay_rate=40, hours_worked='twenty')
        with self.assertRaises(TypeError):
            officer_one_rank = Private(hourly_pay_rate=40.57, hours_worked=30)

class TestBonusForManeuvers(unittest.TestCase):

    def test_bonus_for_maneuvers(self):
        bonus_one = BonusForManeuvers()
        self.assertEqual(bonus_one.get_payment(), 150)  # single bonus for maneuvers is worth 150
        bonus_two = BonusForManeuvers(maneuvers_number=4)
        self.assertEqual(bonus_two.get_payment(), 600)  # participating four times in bonus for maneuvers is worth 600

    def test_bonus_for_maneuvers_negative_value_and_not_integer(self):
        with self.assertRaises(ValueError):
            bonus_one = BonusForManeuvers(maneuvers_number=-4)
        with self.assertRaises(TypeError):
            bonus_one = BonusForManeuvers(maneuvers_number=5.67)
        with self.assertRaises(TypeError):
            bonus_one = BonusForManeuvers(maneuvers_number='-two')

class TestBonusForNegotiations(unittest.TestCase):

    def test_bonus_for_negotiations(self):
        bonus_one = BonusForNegotiations()
        self.assertEqual(bonus_one.get_payment(), 1000)  # bonus for negotiations is worth 1000

        with self.assertRaises(TypeError):
            bonus_one = BonusForNegotiations(4)   # single time bonus


class TestClassSoldier(unittest.TestCase):

    def test_instance_soldier_creation_with_default_values(self):
        soldier_one = Soldier(name='Charles', id=1234, rank=Private())
        self.assertTrue(soldier_one)
        self.assertIsInstance(soldier_one, Soldier)

    def test_instance_soldier_creation_with_one_bonus(self):
        soldier_one_bonus = BonusForManeuvers()
        soldier_one = Soldier(name='Charles',
                              id=1234,
                              rank=Private(),
                              bonus_pay=soldier_one_bonus)
        self.assertTrue(soldier_one)
        self.assertIsInstance(soldier_one, Soldier)

    def test_instance_creation_with_two_bonuses(self):
        soldier_one_bonus = BonusForManeuvers()
        soldier_one_bonus2 = BonusForManeuvers()
        soldier_one = Soldier(name='Charles',
                              id=1234,
                              rank=Private(),
                              bonus_pay=soldier_one_bonus,
                              bonus_pay2=soldier_one_bonus2)
        self.assertTrue(soldier_one)
        self.assertIsInstance(soldier_one, Soldier)

    def test_compute_pay_only_base(self):
        """Compute pay method with base pay only"""
        soldier_one = Soldier(name='Charles', id=1234, rank=Private())
        self.assertEqual(soldier_one.compute_pay(), 1000,
                         msg="Base payment for Soldier with Private rank is equal to 1000")

        soldier_two = Soldier(name='Mike', id=4321, rank=Officer())
        self.assertEqual(soldier_two.compute_pay(), 4000,
                         msg="Base payment for Soldier with Officer rank is equal to 4000")

    def test_compute_pay_with_add_ons_private(self):
        """Compute pay method with additional hours worked and bonus for negotiation skills training"""
        soldier_one = Soldier(name='Charles', id=1234,
                              rank=Private(hourly_pay_rate=10, hours_worked=15),
                              bonus_pay=BonusForNegotiations())
        self.assertEqual(soldier_one.compute_pay(),
                         2150, msg="Base payment for Soldier with Private rank is equal to '1000'"
                                   " + '10 * 15' for hours worked"
                                   " + '1000' Bonus for an additional negotiation skills training,"
                                   " sum should be equal to 2150")

    def test_compute_pay_with_add_ons_officer(self):
        """Compute pay method with additional hours worked and bonus for maneuvers & negotiation skills training"""
        soldier_one = Soldier(name='Charles', id=1234,
                              rank=Officer(hourly_pay_rate=25, hours_worked=16),
                              bonus_pay=BonusForNegotiations(), bonus_pay2=BonusForManeuvers(maneuvers_number=4))
        self.assertEqual(soldier_one.compute_pay(),
                         6000, msg="Base payment for Soldier with Officer rank is equal to '4000"
                                   " + '25 * 16' for hours worked"
                                   " + '1000' Bonus for an additional negotiation skills training"
                                   " + '4 * 150' bonus for maneuvers, sum should be equal to 3000")

    def test_repr_method(self):
        soldier_one = Soldier(name='Charles', id=1234, rank=Private())
        self.assertEqual(repr(soldier_one), "Charles is Private with monthly payment of: 1000$.")

        soldier_mickey = Soldier(name='Mickey', id=2222,
                                 rank=Officer(hourly_pay_rate=25, hours_worked=16),
                                 bonus_pay=BonusForNegotiations(), bonus_pay2=BonusForManeuvers(maneuvers_number=4))
        self.assertEqual(repr(soldier_mickey), "Mickey is Officer with monthly payment of: 6000$.")

    def test_total_info_about_troops_first(self):
        soldier_one = Soldier(name='Charles', id=1234, rank=Private())  # 1000
        soldier_two = Soldier(name='Hans', id=211, rank=Private())  # 1000
        soldier_three = Soldier(name='George', id=23, rank=Private())  # 1000
        officer_four = Soldier(name='Max', id=2113, rank=Officer())  # 4000
        actual = Soldier.total_info_about_troops()
        expected = "There are troops in total number of 4 available:\n" \
                   "3 soldiers and 1 officers, with total payment of 7000$."
        self.assertEqual(actual, expected)

    def test_total_info_about_troops_second(self):
        soldier_one = Soldier(name='Charles', id=1234, rank=Private(hourly_pay_rate=20, hours_worked=34))  # 1680
        officer_one = Soldier(name='Hans', id=211, rank=Officer(hourly_pay_rate=40, hours_worked=15),  # 4600
                              bonus_pay=BonusForNegotiations())  # 1000
        soldier_two = Soldier(name='Max', id=213, rank=Private(),  # 1000
                              bonus_pay=BonusForManeuvers(maneuvers_number=5),  # 750
                              bonus_pay2=BonusForNegotiations())  # 1000
        officer_two = Soldier(name='George', id=23, rank=Officer(),  # 4000
                              bonus_pay=BonusForManeuvers(maneuvers_number=12))  # 1800
        actual = Soldier.total_info_about_troops()
        expected = "There are troops in total number of 4 available:\n" \
                   "2 soldiers and 2 officers, with total payment of 15830$."  # 15830
        self.assertEqual(actual, expected)

    def test_total_info_about_troops_after_remove_objects_first(self):
        soldier_one = Soldier(name='Charles', id=1234, rank=Private())  # 1000
        soldier_two = Soldier(name='Hans', id=211, rank=Private())  # 1000
        soldier_three = Soldier(name='George', id=211, rank=Private())  # 1000
        del soldier_three  # -1000
        officer_four = Soldier(name='Max', id=21, rank=Officer())  # 1000
        actual = Soldier.total_info_about_troops()
        expected = "There are troops in total number of 3 available:\n" \
                   "2 soldiers and 1 officers, with total payment of 6000$."  # 6000
        self.assertEqual(actual, expected)

    def test_total_info_about_troops_after_remove_objects_second(self):
        soldiers_one_rank = Private(hourly_pay_rate=20, hours_worked=34)
        soldier_one = Soldier(name='Charles', id=1234, rank=soldiers_one_rank)  # 1680
        officers_one_rank = Officer(hourly_pay_rate=40, hours_worked=15)
        officer_one = Soldier(name='Hans', id=21, rank=officers_one_rank,  # 4600
                              bonus_pay=BonusForNegotiations())  # 1000
        soldier_two = Soldier(name='Max', id=2113, rank=Private(),  # 1000
                              bonus_pay=BonusForManeuvers(maneuvers_number=5),  # 750
                              bonus_pay2=BonusForNegotiations())  # 1000
        officer_two_bonus = BonusForManeuvers(maneuvers_number=12)
        officer_two = Soldier(name='George', id=23, rank=Officer(),  # 4000
                              bonus_pay2=officer_two_bonus)  # 1800
        del soldier_one  # -1680
        del officer_one  # -5600
        del officer_two  # -5800
        actual = Soldier.total_info_about_troops()
        expected = "There are troops in total number of 1 available:\n" \
                   "1 soldiers and 0 officers, with total payment of 2750$."  # 2750
        self.assertEqual(actual, expected)

    def test_total_info_about_troops_after_remove_all_objects(self):
        soldier_one = Soldier(name='Charles', id=1234, rank=Private(hourly_pay_rate=20, hours_worked=34))  # 1680
        officer_one = Soldier(name='Hans', id=21, rank=Officer(hourly_pay_rate=40, hours_worked=15),  # 4600
                              bonus_pay=BonusForNegotiations())  # 1000
        soldier_two_bonus = BonusForManeuvers(maneuvers_number=5)
        soldier_two_bonus2 = BonusForNegotiations()
        soldier_two = Soldier(name='Max', id=2113, rank=Private(),  # 1000
                              bonus_pay=soldier_two_bonus,  # 750
                              bonus_pay2=soldier_two_bonus2)  # 1000
        officer_two = Soldier(name='George', id=23, rank=Officer(),  # 4000
                              bonus_pay2=BonusForManeuvers(maneuvers_number=12))  # 1800
        del soldier_one  # -1680
        del officer_one  # -5600
        del officer_two  # -5800
        del soldier_two  # -2750
        actual = Soldier.total_info_about_troops()
        expected = "There are troops in total number of 0 available:\n" \
                   "0 soldiers and 0 officers, with total payment of 0$."  # 0
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
