import customtkinter as ctk
from PIL import Image
import random
import os
import pyperclip
from data.CTkScrollableDropdown import *
from data.modules import GenerateNick
from data.lists import *
import time

selected_hero = None
selected_items = []
selected_talant = None
selected_pose = None
created_spells = []
used_spells = []

sequence = ""


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # установка иконки
        image_path = os.path.join(os.path.dirname(__file__), "data", "icons", "icon1.ico")
        self.iconbitmap(image_path)

        # инициализация окна и названия
        self.geometry("940x600")
        self.title('Dota Fun')
        self.resizable(False, False)

        # объявление переменных
        self.self_select_hero_var = ctk.Variable(value=False)
        self.settings_visible = ctk.Variable(value=False)
        self.build_visible = ctk.Variable(value=True)
        self.nickname_visible = ctk.Variable(value=False)
        self.req_item_var = ctk.Variable()
        self.req_sapog_var = ctk.Variable()
        self.pizdec_var = ctk.Variable()
        self.nicky = None
        self.invoker_active = False
        self.start_time = None
        self.spells_created = 0
        # self.spell_list = list(skills_combinations.keys())
        self.start_time = None
        self.game_started = ctk.Variable(value=False)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0, fg_color='#1e1f22')
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        logo_path = os.path.join(os.path.dirname(__file__), "data", "icons", "000.png")
        self.logo = ctk.CTkImage(dark_image=Image.open(logo_path), size=(148, 78))
        self.logo_label = ctk.CTkLabel(master=self.sidebar_frame, text='', image=self.logo, fg_color='transparent')
        self.logo_label.grid(row=0, column=0, sticky='nsew', pady=15)
        self.build_button = ctk.CTkButton(self.sidebar_frame, text='Build', command=self.show_build)
        self.build_button.grid(row=1, column=0, padx=20, pady=10)
        self.nickname_button = ctk.CTkButton(self.sidebar_frame, text='Nickname', command=self.show_nickname)
        self.nickname_button.grid(row=2, column=0, padx=20, pady=10)
        self.invoker_button = ctk.CTkButton(self.sidebar_frame, text='Invoker Game', command=self.show_invoker)
        self.invoker_button.grid(row=3, column=0, padx=20, pady=10)
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")

        self.build_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.nickname_frame = ctk.CTkFrame(self.main_frame, fg_color='transparent')

        self.invoker_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.bind("<Key>", self.key_press)

        # Никнейм
        self.textbox = ctk.CTkTextbox(master=self.nickname_frame, width=600, height=50, border_color='white',
                                      font=('Comic Sans MS', 16), corner_radius=20)
        self.textbox.grid(row=0, column=0, sticky="nsew", padx=80, pady=(100, 30))
        self.textbox.insert("0.0", 'Nickname')
        self.nickgenerate_btn = ctk.CTkButton(master=self.nickname_frame, width=100, text='Generate',
                                              command=self.set_name)
        self.nickgenerate_btn.grid(row=1, column=0, sticky='n')
        self.copy_btn = ctk.CTkButton(master=self.nickname_frame, width=100, text='Copy', command=self.copy_nick)
        self.copy_btn.grid(row=2, column=0, pady=(10, 300), sticky='n')

        # Генерация билдов
        self.generate_frame = ctk.CTkFrame(master=self.build_frame, fg_color='transparent')
        self.generate_frame.grid(row=1, column=0, sticky='nsew', padx=80)
        self.btn_generate = ctk.CTkButton(master=self.generate_frame, text='Generate', width=100,
                                          command=self.set_build)
        self.btn_generate.grid(row=1, column=0, pady=(25, 25), padx=250)
        self.hero_image_label = ctk.CTkLabel(master=self.generate_frame, text='')
        self.hero_image_label.grid(row=2, column=0, pady=10, sticky='n')
        self.talent_image_label = ctk.CTkLabel(master=self.generate_frame, text='')
        self.talent_image_label.grid(row=2, column=0, padx=(250, 0), pady=10)
        self.pose_image_label = ctk.CTkLabel(master=self.generate_frame, text='', fg_color='transparent')
        self.pose_image_label.grid(row=1, column=0, padx=0, pady=(90, 0))
        self.item_image_frame = ctk.CTkFrame(master=self.generate_frame, fg_color='transparent')
        self.item_image_frame.grid(row=3, column=0, pady=10, sticky='n')
        # фрейм с настройками
        self.settings_frame = ctk.CTkFrame(master=self.build_frame, fg_color='transparent')
        self.settings_frame.grid(row=0, column=0, sticky='w')
        self.settings_button_path = os.path.join(os.path.dirname(__file__), "data", "icons", "settings.png")
        self.settings_button_image = ctk.CTkImage(dark_image=Image.open(self.settings_button_path), size=(25, 25))
        self.btn_settings = ctk.CTkButton(master=self.settings_frame, text='', image=self.settings_button_image,
                                          width=25, fg_color='transparent', command=self.show_settings_frame)
        self.btn_settings.grid(row=0, column=0, padx=(20, 0), pady=(20, 0))
        self.configure_frame = ctk.CTkFrame(master=self.settings_frame, fg_color='transparent')
        self.combobox = ctk.CTkButton(master=self.configure_frame, text='Выбрать героя', width=250,
                                      fg_color='transparent', border_width=1)
        self.combobox.grid(row=2, column=1, padx=(0, 80), pady=10)
        CTkScrollableDropdown(self.combobox, values=[hero['name'] for hero in heroes], height=270, resize=False,
                              button_height=30, scrollbar=False, command=lambda e: self.combobox.configure(text=e))
        self.hero_selection_label = ctk.CTkLabel(master=self.configure_frame, text='Выберите героя')
        self.hero_selection_label.grid(row=2, column=0, padx=(0, 80), pady=10)
        self.self_select_hero_switch = ctk.CTkSwitch(master=self.configure_frame, text='Свой герой',
                                                     variable=self.self_select_hero_var)
        self.self_select_hero_switch.grid(row=3, column=0, columnspan=2, pady=10, padx=(0, 320))
        self.switch_req_item = ctk.CTkSwitch(master=self.configure_frame, text='Обязательная Khanda',
                                             variable=self.req_item_var)
        self.switch_req_item.grid(row=0, column=0)
        self.switch_sapog_item = ctk.CTkSwitch(master=self.configure_frame, text='Обязательный сапог',
                                               variable=self.req_sapog_var)
        self.switch_sapog_item.grid(row=1, column=0, pady=10)
        self.switch_pizdec = ctk.CTkSwitch(master=self.configure_frame, text='FullPizdec',
                                           variable=self.pizdec_var, border_color='red', text_color='red',
                                           progress_color='red')
        self.switch_pizdec.grid(row=0, column=1, pady=10, padx=50)

        # INVOKER GAME
        self.settings_game_frame = ctk.CTkFrame(self.invoker_frame, fg_color='transparent')
        self.settings_game_frame.grid(row=0, column=0, sticky='w')
        self.settings_button_image = ctk.CTkImage(dark_image=Image.open(self.settings_button_path), size=(25, 25))
        self.btn_settings = ctk.CTkButton(self.settings_game_frame, text='', image=self.settings_button_image,
                                          width=25, fg_color='transparent')
        self.btn_settings.grid(row=0, column=0, padx=(20, 0), pady=(20, 0))
        self.configure_game_frame = ctk.CTkFrame(self.settings_game_frame, fg_color='transparent')
        self.timer_switcher = ctk.CTkSwitch(self.configure_game_frame, font=('Helvetica', 12),
                                            text='Сбрасывать игру автоматически по достижению времени:')
        self.timer_switcher.grid(row=0, column=0, padx=(0, 15),sticky='w')
        self.time_textbox = ctk.CTkTextbox(master=self.configure_game_frame, width=100, height=10,
                                           border_color='white', font=('Helvetica', 12), corner_radius=10)
        self.time_textbox.grid(row=0, column=1, sticky='n')

        zaglushka_path = os.path.join(os.path.dirname(__file__), "data", "invoker", "skills", "zaglushka.png")
        image1 = ctk.CTkImage(dark_image=Image.open(zaglushka_path), size=(96, 96))
        self.game_frame = ctk.CTkFrame(self.invoker_frame, fg_color='transparent')
        self.game_frame.grid(row=1, column=0, sticky='nsew')
        self.game_btn = ctk.CTkButton(self.game_frame, text='Start Game', width=60,
                                      command=self.start_game)
        self.game_btn.grid(row=0, column=0, padx=350, pady=(20, 20))
        self.skill_frame = ctk.CTkFrame(self.game_frame, fg_color='transparent')
        self.skill_frame.grid(row=1, column=0, pady=(0, 80), sticky='n')
        self.timer_label = ctk.CTkLabel(self.skill_frame, text="00:00", font=("Helvetica", 48))
        self.timer_label.grid(row=0, column=0, pady=15, sticky='n')
        self.stc_label = ctk.CTkLabel(self.skill_frame, text='')
        self.stc_label.grid(row=1, column=0, sticky='n')
        self.stc_label.configure(image=image1)
        self.qwe_frame = ctk.CTkFrame(self.game_frame, fg_color='transparent')
        self.qwe_frame.grid(row=2, column=0, sticky='n', padx=80)
        self.qwe_labels = [ctk.CTkLabel(self.qwe_frame, text='') for _ in range(3)]
        for i, label in enumerate(self.qwe_labels):
            label.grid(row=0, column=i + 1, padx=5)
            label.configure(image=image1)
        self.created_spells_labels = [ctk.CTkLabel(self.qwe_frame, text='') for _ in range(2)]
        for i, label in enumerate(self.created_spells_labels):
            label.grid(row=0, column=i+3 + 1, padx=(10, 0))
            label.configure(image=image1)
        saves_path = os.path.join(os.path.dirname(__file__), "data", "saves.txt")
        with open(saves_path, 'r') as f:
            record = f.read().strip()
        self.record_time = ctk.CTkLabel(self.game_frame, text=f'Record: {record}', font=("Helvetica", 24))
        self.record_time.grid(row=3, column=0, sticky='n')

    def show_build(self):
        try:
            self.nickname_frame.grid_forget()
            self.invoker_frame.grid_forget()
            self.build_frame.grid(row=0, column=0, sticky='nsew')
            self.invoker_active = False
        except:
            pass

    def show_nickname(self):
        try:
            self.build_frame.grid_forget()
            self.invoker_frame.grid_forget()
            self.nickname_frame.grid(row=0, column=0, sticky='nsew')
            self.invoker_active = False
        except:
            pass

    def show_invoker(self):
        try:
            self.build_frame.grid_forget()
            self.nickname_frame.grid_forget()
            self.invoker_frame.grid(row=1, column=0, sticky='nsew')
            self.invoker_active = True  # Устанавливаем invoker_active как True
        except:
            pass

    def show_settings_frame(self):  # функция отображения настроек
        if self.settings_visible:
            self.configure_frame.grid(row=1, column=1, padx=(66, 130), pady=10, sticky='nsew')
            self.settings_visible = False
        else:
            self.configure_frame.grid_forget()
            self.settings_visible = True

    def show_game_settings_frame(self):  # функция отображения настроек
        if self.settings_visible:
            self.configure_game_frame.grid(row=1, column=1, padx=(66, 130), pady=10, sticky='nsew')
            self.settings_visible = False
        else:
            self.configure_game_frame.grid_forget()
            self.settings_visible = True

    def set_build(self):  # функция отображения героя и предметов
        global selected_hero
        global selected_items
        global selected_talant
        global selected_pose

        self.hero_image_label.configure(image=None)
        self.hero_image_label.image = None

        if self.self_select_hero_var.get():
            try:
                selected_hero_name = self.combobox.cget("text")
                selected_hero = [hero for hero in heroes if hero['name'] == selected_hero_name][0]
            except IndexError:
                selected_hero = random.choice(heroes)
        else:
            selected_hero = random.choice(heroes)

        hero_image_path = os.path.join(os.path.dirname(__file__), "data", "hero", selected_hero['image'])
        hero_image = ctk.CTkImage(dark_image=Image.open(hero_image_path), size=(128, 72))
        self.hero_image_label.configure(image=hero_image)
        self.hero_image_label.image = hero_image

        selected_talant = random.choice(talants)
        talant_image_path = os.path.join(os.path.dirname(__file__), "data", "talants", selected_talant['image'])
        talant_image = ctk.CTkImage(dark_image=Image.open(talant_image_path), size=(80, 80))
        self.talent_image_label.configure(image=talant_image)
        self.talent_image_label.image = talant_image

        weights = [1] * (len(pose) - 1) + [0.05]
        selected_pose = random.choices(pose, weights)[0]
        pose_image_path = os.path.join(os.path.dirname(__file__), "data", "poses", selected_pose['image'])
        pose_image = ctk.CTkImage(dark_image=Image.open(pose_image_path), size=(161, 32))
        self.pose_image_label.configure(image=pose_image)
        self.pose_image_label.image = talant_image

        item_limit = 6
        selected_items = []
        if not self.pizdec_var.get():
            if self.req_item_var.get() and self.req_sapog_var.get():
                required_item = items[45]
                sapog = random.choice([item for item in sapogi if item['name'] not in selected_items])
                selected_items.append(sapog)
                selected_items.append(required_item)
            elif self.req_item_var.get():
                required_item = items[45]
                selected_items.append(required_item)
            elif self.req_sapog_var.get():
                sapog = random.choice(sapogi)
                selected_items.append(sapog)
            while len(selected_items) < item_limit:
                random_item = random.choice(items)
                if random_item not in selected_items:
                    selected_items.append(random_item)
        else:
            while len(selected_items) < item_limit:
                random_item = random.choice(items)
                selected_items.append(random_item)

        self.item_image_frame.destroy()
        self.item_image_frame = ctk.CTkFrame(master=self.generate_frame, fg_color='transparent')
        self.item_image_frame.grid(row=3, column=0, pady=10, sticky='n')

        item_images = [
            ctk.CTkImage(dark_image=Image.open(os.path.join(os.path.dirname(__file__), "data", "items", item['image'])),
                         size=(88, 64))
            for item in selected_items
        ]

        image_labels = [
            ctk.CTkLabel(master=self.item_image_frame, image=image, text='')
            for image in item_images
        ]

        for label, i in zip(image_labels, range(len(selected_items))):
            label.grid(row=0, column=i, padx=5)

    def set_name(self):
        a = GenerateNick()
        self.nicky = a.generate()
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", self.nicky)

    def copy_nick(self):
        pyperclip.copy(self.nicky)

    def check_combination(self, sequence, item_dict):
        if not self.invoker_active:
            return

        combinations = list(item_dict.values())[0]
        return sequence in combinations

    def key_press(self, event):
        if not self.invoker_active:
            return

        global sequence
        key_codes = {81: "q", 87: "w", 69: "e", 82: "r", 13: "enter"}
        if event.keycode in key_codes:
            if key_codes[event.keycode] == "r":
                self.check_created_spells()
            elif key_codes[event.keycode] == "enter":
                self.start_game()
            else:
                key_pressed = key_codes[event.keycode]
                sequence = sequence[-2:] + key_pressed
                self.update_labels(sequence[-3:])
        else:
            return

    def update_labels(self, key_sequence):
        if not self.invoker_active:
            return

        quas_path = os.path.join(os.path.dirname(__file__), "data", "invoker", "qwe", "Quas_icon.png")
        quas_image = ctk.CTkImage(dark_image=Image.open(quas_path), size=(96, 96))
        wex_path = os.path.join(os.path.dirname(__file__), "data", "invoker", "qwe", "Wex_icon.png")
        wex_image = ctk.CTkImage(dark_image=Image.open(wex_path), size=(96, 96))
        exort_path = os.path.join(os.path.dirname(__file__), "data", "invoker", "qwe", "Exort_icon.png")
        exort_image = ctk.CTkImage(dark_image=Image.open(exort_path), size=(96, 96))
        for i, key in enumerate(key_sequence):
            if key == "q":
                self.qwe_labels[i].configure(image=quas_image)
            elif key == "w":
                self.qwe_labels[i].configure(image=wex_image)
            else:
                self.qwe_labels[i].configure(image=exort_image)

    def check_created_spells(self):
        if not self.invoker_active:
            return

        global created_spells, stc_item, item_dict
        for item_dict in skills_combinations:
            item_name = list(item_dict.keys())[0]
            if self.check_combination(sequence, item_dict):
                if item_name in created_spells:
                    continue
                created_spells.insert(0, item_name)  # Добавляем новый элемент в начало списка
                if len(created_spells) > 2:
                    created_spells.pop()  # Удаляем последний элемент, если длина списка превышает 2
                self.update_created_spells(created_spells)

                try:
                    if item_name == stc_item and self.game_started is True:
                        self.update_stc()
                        selected_stc = list(random.choice(skills_combinations).keys())[0]
                except:
                    pass

                return  # Выходим из функции после обновления

    def update_created_spells(self, created_spells):
        if not self.invoker_active:
            return

        # Получаем путь к директории, где находится скрипт
        script_dir = os.path.dirname(os.path.abspath(__file__))

        for i, label in enumerate(self.created_spells_labels):
            if i < len(created_spells):
                item_name = created_spells[i]
                item_dict = next((d for d in skills_combinations if item_name in d), None)
                if item_dict:
                    skill_name = item_name.upper()
                    image_path = os.path.join(script_dir, "data", "invoker", "skills", f"{skill_name}.jpg")
                    if os.path.exists(image_path):
                        image = ctk.CTkImage(dark_image=Image.open(image_path), size=(96, 96))
                        label.configure(image=image)
                    else:
                        label.configure(image=None)
                else:
                    label.configure(image=None)
            else:
                label.configure(image=None)

    def start_game(self):
        self.game_started = True
        global used_spells, created_spells, item_dict
        used_spells = []
        created_spells = []  # Обнуляем список созданных заклинаний
        image_path = os.path.join(os.path.dirname(__file__), "data", "invoker", "skills", "zaglushka.png")
        image1 = ctk.CTkImage(dark_image=Image.open(image_path), size=(96, 96))
        for i, label in enumerate(self.created_spells_labels):
            label.configure(image=image1)
        self.start_time = None  # Сбрасываем start_time
        self.update_clock()  # Запускаем таймер
        self.update_stc()

    def update_clock(self):
        now = time.time()
        if not self.start_time:
            self.start_time = now
        elapsed = now - self.start_time
        minutes, seconds = divmod(elapsed, 60)
        seconds, milliseconds = divmod(seconds, 1)
        time_str = f"{int(seconds):02d}:{int(milliseconds * 100):02d}"
        self.timer_label.configure(text=time_str)

        # Проверяем, достигли ли мы предела в 10 заклинаний
        if len(used_spells) >= 10:
            self.game_started = False
            self.save_record(time_str)
            return

        self.after(10, self.update_clock)

    def save_record(self, record):
        saves_path = os.path.join(os.path.dirname(__file__), "data", "saves.txt")
        try:
            # Читаем предыдущий рекорд из файла, если он существует
            try:
                with open(saves_path, 'r') as f:
                    previous_record = f.read().strip()
            except FileNotFoundError:
                previous_record = None

            # Если нет предыдущего рекорда или новый рекорд лучше, сохраняем его
            if not previous_record or self.is_better_record(record, previous_record):
                with open(saves_path, 'w') as f:
                    f.write(str(record))
                self.record_time.configure(text=f'Record {record}')
        except Exception as e:
            print(f"Ошибка при сохранении рекорда: {e}")

    def is_better_record(self, new_record, previous_record):
        # Предполагается, что меньшее время лучше
        new_time = self.convert_time_to_seconds(new_record)
        previous_time = self.convert_time_to_seconds(previous_record)
        return new_time < previous_time

    def convert_time_to_seconds(self, time_str):
        if not time_str:
            return float('inf')  # Если время не указано, считаем его бесконечным
        seconds, milliseconds = time_str.split(':')
        return float(seconds) + float(milliseconds) / 100

    def update_stc(self): # stc - spell to craft
        global stc_item

        # Получаем список неиспользованных заклинаний
        unused_spells = [d for d in skills_combinations if list(d.keys())[0] not in used_spells]

        # Если все заклинания были использованы, очищаем used_spells
        if not unused_spells:
            used_spells.clear()
            unused_spells = skills_combinations

        # Выбираем случайное неиспользованное заклинание
        selected_stc = random.choice(unused_spells)
        stc_item = list(selected_stc.keys())[0]
        used_spells.append(stc_item)  # Добавляем использованное заклинание в список

        image_path = os.path.join(os.path.dirname(__file__), selected_stc['image'])
        image = ctk.CTkImage(dark_image=Image.open(image_path), size=(96, 96))
        self.stc_label.configure(image=image)



if __name__ == '__main__':
    app = App()
    app.mainloop()
