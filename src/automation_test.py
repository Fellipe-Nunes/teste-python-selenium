import unittest
from register_test import RegisterTest
from frame_test import FrameTest
from datepicker_test import DatepickerTest
from slider_test import SliderTest

if __name__ == "__main__":
    # Executar apenas o teste de registro
    register_suite = unittest.TestLoader().loadTestsFromTestCase(RegisterTest)
    unittest.TextTestRunner().run(register_suite)

    # Executar apenas o teste de frames
    frame_suite = unittest.TestLoader().loadTestsFromTestCase(FrameTest)
    unittest.TextTestRunner().run(frame_suite)

    # Executar apenas o teste de datepicker
    datepicker_suite = unittest.TestLoader().loadTestsFromTestCase(DatepickerTest)
    unittest.TextTestRunner().run(datepicker_suite)

    # Executar apenas o teste de slider
    slider_suite = unittest.TestLoader().loadTestsFromTestCase(SliderTest)
    unittest.TextTestRunner().run(slider_suite)
