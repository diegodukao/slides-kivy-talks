import pyscreenshot


def save_screenshot(slide_num):
    pyscreenshot.grab_to_file("screenshots/{}.png".format(slide_num))
