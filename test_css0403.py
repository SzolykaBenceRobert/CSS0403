import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_container_style():
    driver = webdriver.Chrome()  # vagy más webdriver (pl. Firefox)
    driver.get("file://" + os.path.abspath("CSS0403.html"))
    
    # Container margin ellenőrzése
    container = driver.find_element(By.CLASS_NAME, "container")
    margin = container.value_of_css_property("margin")
    assert margin == "10%"  # margin beállítása 10%-ra

    # Container háttérszínének ellenőrzése
    background_color = container.value_of_css_property("background-color")
    assert background_color == "rgb(240, 230, 140)"  # Khaki szín, RGB formátumban

    # Container belső margó ellenőrzése
    padding = container.value_of_css_property("padding")
    assert padding == "20px"  # 20px belső margó

    # Container szegélye ellenőrzése
    border = container.value_of_css_property("border")
    assert border == "3px solid rgb(0, 255, 255)"  # Aqua színű szegély

    # Aside elem stílusa
    aside = driver.find_element(By.TAG_NAME, "aside")
    width = aside.value_of_css_property("width")
    assert width == "90px"  # 90px szélesség
    height = aside.value_of_css_property("height")
    assert height == "90px"  # 90px magasság
    background_color = aside.value_of_css_property("background-color")
    assert background_color == "rgb(255, 255, 255)"  # Fehér háttérszín
    float_value = aside.value_of_css_property("float")
    assert float_value == "right"  # Jobbra úszás
    border_left = aside.value_of_css_property("border-left")
    assert border_left == "5px solid rgb(165, 42, 42)"  # Brown színű bal oldali szegély

    # H1 betűtípus ellenőrzése
    h1 = driver.find_element(By.TAG_NAME, "h1")
    font_family = h1.value_of_css_property("font-family")
    assert font_family == "sans-serif"  # Talpatlan betűtípus

    # P elem sorkizárása
    p = driver.find_element(By.TAG_NAME, "p")
    text_align = p.value_of_css_property("text-align")
    assert text_align == "justify"  # Sorkizárt szöveg

    # P elemben 2. szó (ipsum) félkövérre állítása
    spans = p.find_elements(By.TAG_NAME, "span")
    assert spans[1].value_of_css_property("font-weight") == "bold"  # Az "ipsum" szó félkövér

    # P elemben 3. és 4. szó dőlt betűsítése
    assert spans[2].value_of_css_property("font-style") == "italic"  # 3. szó dőlt
    assert spans[3].value_of_css_property("font-style") == "italic"  # 4. szó dőlt

    driver.quit()

