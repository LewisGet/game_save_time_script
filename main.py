def wait_and_click(image):
    wait(image)
    click(image)

def try_execute(try_times, execute_function, fail_execute_function):
    for i in range(try_times):
        try:
            execute_function()
            break
        except:
            fail_execute_function()


def can_execute_task():
    # 之後改成全 python 在使用 os list 圖片
    can_execute = ["lost_controler.png", "field_guard.png", "outside_monster.png", "clearup_monster.png"]

    return can_execute


def get_can_execute_task():
    def get_task_button():
        wait_and_click("ui/daily_six/get_it.png")

    def fail_function():
        sleep(1)

    has_accepted_list = [i for i in findAll("ui/daily_six/accepted.png")]

    for task_title in can_execute_task():
        for tasks in findAll(Pattern("ui/daily_six/task_type/" + task_title).similar(0.88)):
            is_accepted = False

            for has_accepted in has_accepted_list:
                acx, acy = has_accepted.x, has_accepted.y
                x, y = tasks.x, tasks.y

                if x in range(acx - 50, acx + 50) and y in range(acy - 180, acy - 80):
                    is_accepted = True

            if is_accepted is False:
                click(tasks)
                try_execute(3, get_task_button, fail_function)


def check_good_task_numbers():
    return_number = 0

    for i in can_execute_task():
        return_number = return_number + len(findAll(i))

    return return_number


def open_activity():
    wait_and_click("ui/activity.png")
    sleep(0.5)


def open_daily_six_menu():
    open_activity()
    wait_and_click(Pattern("ui/daily_six/main_menu_image.png").targetOffset(0,188))


def get_daily_six_task():
    open_daily_six_menu()

    for i in range(99):
        sleep(1)
        get_can_execute_task()

        has_accepted = [i for i in findAll("ui/daily_six/accepted.png")]
        
        if len(has_accepted) == 6:
            break

        wait_and_click("ui/daily_six/reflush_button.png")

    wait_and_click("ui/close.png")
    wait_and_click("ui/close_2.png")


def start_task():
    open_daily_six_menu()
    wait_and_click("ui/daily_six/accepted.png")
    wait_and_click("ui/daily_six/doit.png")

def finish_up_all_task():
    for i in range(50):
    start_task()
    sleep(60)

    try:
        find("ui/daily_six/done.png")
        wait_and_click("ui/close.png")
        break
    except:
        pass

get_daily_six_task()
finish_up_all_task()
