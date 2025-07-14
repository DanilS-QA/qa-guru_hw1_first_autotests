from selene import browser, be, have

def test_success_login():
    browser.open('https://niffler.qa.guru')
    browser.element('[id="username"]').type('qaguru_test')
    browser.element('[id="password"]').type('12345')
    browser.element('[id="login-button"]').click()

    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.quit()

def test_success_login_with_press_enter():
    browser.open('https://niffler.qa.guru')
    browser.element('[id="username"]').type('qaguru_test')
    browser.element('[id="password"]').type('12345').press_enter()

    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.quit()

def test_wrong_credentials():
    browser.open('https://niffler.qa.guru')
    browser.element('[id="username"]').type('qaguru_test')
    browser.element('[id="password"]').type('12345sgscqwr').press_enter()

    browser.element('[class="form__error-container"]').should(have.text('Неверные учетные данные пользователя'))
    browser.quit()

def test_username():
    browser.open('https://niffler.qa.guru')
    browser.element('[id="username"]').type('qaguru_test')
    browser.element('[id="password"]').type('12345')
    browser.element('[id="login-button"]').click()
    browser.element('[data-testid="PersonIcon"]').click()
    browser.element('[href="/profile"]').click()
    browser.element('[id="username"]').should(have.value('qaguru_test'))
    browser.quit()

def test_logout():
    browser.open('https://niffler.qa.guru')
    browser.element('[id="username"]').type('qaguru_test')
    browser.element('[id="password"]').type('12345')
    browser.element('[id="login-button"]').click()
    browser.element('[data-testid="PersonIcon"]').click()
    browser.all('li.MuiMenuItem-root').element_by(have.text('Sign out')).click()

    # browser.all('li.MuiMenuItem-root')
    # browser.all('li.MuiMenuItem-root') browser – объект Selene для работы с браузером.
    # .all() – ищет все элементы, соответствующие локатору (аналог find_elements в Selenium). 'li.MuiMenuItem-root' – CSS-селектор, который ищет все теги <li> с классом MuiMenuItem-root.
    # 'li.MuiMenuItem-root' – CSS-селектор, который ищет все теги <li> с классом MuiMenuItem-root
    # .element_by(have.text('Sign out'))
    # .element_by() – фильтрует найденные элементы по условию.
    # have.text('Sign out') – проверяет, что у элемента есть текст "Sign out" (регистрозависимо).

    browser.all('button.MuiButtonBase-root').element_by(have.text('Log out')).click()
    browser.element('[class="header"]').should(have.text('Log in'))
    browser.quit()