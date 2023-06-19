def ele_edit_page():
    return {
        "refs" : '//*[@id="refs"]',
        "titleUI" : '//*[@id="content-header"]/div/div[4]',
        "custom_function" : "custom_function_str",
        "custom_feature" : 'custom_feature',
        "custom_steps_display" : 'custom_steps_display',
        "successfully_message" : '//div[text()="Successfully updated the test case."]',
        "edit_btn" : '//*[@id="content-header"]/div/div[3]/a[1]',
        "title_txt" : '//*[@id="content-header"]/div/div[4]'
}

def ele_login_page():
    return {
        "user" : 'name',
        "password" : 'password',
        "login_btn" : "button_primary",
}