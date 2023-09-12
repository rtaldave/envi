import hashlib
import json
import random


from kivy.uix.screenmanager import NoTransition, ScreenManager
from kivymd.app import MDApp
from kivymd.material_resources import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog

from kivymd.uix.pickers import MDDatePicker


def generate_user_database():
    try:
        with open('user_data.txt', 'r') as user_data_raw:
            user_database = json.loads(user_data_raw.read())
    except:
        return []
    else:
        return user_database


def generate_user_name_list():
    user_lst = []
    lst = generate_user_database()
    for a in lst:
        user_lst.append(a['user_name'])
    user_lst.sort()
    return user_lst


def generate_barangay_list():
    try:
        with open('barangays.txt', 'r') as brgys:
            brgys_lst = brgys.readlines()
    except:
        return []
    else:
        lst = []
        for a in brgys_lst:
            lst.append(a.strip())
        lst.sort()
        return lst


def generate_household_database():
    try:
        with open('household_data.txt', 'r') as household_data_raw:
            hh_database = json.loads(household_data_raw.read())
    except:
        return []
    else:
        return hh_database


def generate_household_name_list_all():
    household_lst = []
    try:
        with open('household_data.txt', 'r') as all_hh:
            hh = json.loads(all_hh.read())
    except:
        return []
    else:
        for a in hh:
            household_lst.append(a['household_name'])
        return household_lst


def generate_household_name_list(user):
    household_lst = []
    lst = generate_household_database(user)
    for a in lst:
        household_lst.append(a['household_name'])
    household_lst.sort()
    return household_lst


class MissingUserInfo(MDDialog):
    pass


class MismatchPW(MDDialog):
    pass


class UserAlreadyExist(MDDialog):
    pass


class NewUserSaved(MDDialog):
    pass


class NoUser(MDDialog):
    pass


class WrongPW(MDDialog):
    pass


class HouseholdAlreadyExist(MDDialog):
    pass


class Interface(ScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transition = NoTransition()

    def show_details(self, obj):
        for a in self.household_database:
            if a['household_name'] == obj.text:
                self.current = 'screen_household_details'
                self.ids.detail_interviewer.text = f"Interviewer : {a['household_interviewer_name']}"
                self.ids.detail_barangay.text = f"Barangay : {a['household_barangay']}"
                self.ids.detail_purok.text = f"Purok : {a['household_purok']}"
                self.ids.detail_name.text = f"Household name : {a['household_name']}"
                self.ids.detail_level_1.text = f"Level 1 water source : {a['level_1']}"
                self.ids.detail_level_2.text = f"Level 2 water source : {a['level_2']}"
                self.ids.detail_level_3.text = f"Level 3 water source : {a['level_3']}"
                self.ids.detail_other_water.text = f"Other water source : {a['other_water']}"
                self.ids.detail_other_water_dx.text = f"Other water source description : {a['other_water_description']}"
                self.ids.detail_water_location.text = f"Water location : {a['water_location']}"
                self.ids.detail_water_availability.text = f"Water availability : {a['water_availability']}"
                self.ids.detail_micro_test.text = f"Microbiological test : {a['micro_test']}"
                self.ids.detail_micro_test_date.text = f"Microbiological test date : {a['micro_test_date']}"
                self.ids.detail_micro_test_result.text = f"Microbiological test result : {a['micro_test_result']}"
                self.ids.detail_physical_chemical_test.text = f"Physical/Chemical test : {a['physical_chemical_test']}"
                self.ids.detail_physical_chemical_test_date.text = f"Physical/Chemical test date : {a['physical_chemical_test_date']}"
                self.ids.detail_physical_chemical_test_result.text = f"Physical/Chemical test result : {a['physical_chemical_test_result']}"
                self.ids.detail_open_defecation.text = f"Open defecation : {a['open_defecation']}"
                self.ids.detail_septic.text = f"Pour/flush with septic tank : {a['septic_tank']}"
                self.ids.detail_sewerage.text = f"Pour/flush to sewerage : {a['sewerage']}"
                self.ids.detail_ventilated.text = f"Ventilated pit latrine : {a['ventilated']}"
                self.ids.detail_improvised.text = f"Improvised septic tank : {a['improvised']}"
                self.ids.detail_drainage.text = f"Pour/flush to drainage : {a['drainage']}"
                self.ids.detail_overhung.text = f"Overhung latrine : {a['overhung']}"
                self.ids.detail_open_pit.text = f"Open pit latrine : {a['open_pit']}"
                self.ids.detail_without.text = f"Without toilet : {a['without']}"
                self.ids.detail_toilet_not_shared.text = f"Toilet not shared : {a['toilet_not_shared']}"
                self.ids.detail_in_situ.text = f"Excreta disposed in situ : {a['in_situ']}"
                self.ids.detail_collected.text = f"Excreta collected : {a['collected']}"
                self.ids.detail_segregation.text = f"Waste segregation : {a['segregation']}"
                self.ids.detail_composting.text = f"Waste composting : {a['composting']}"
                self.ids.detail_recycling.text = f"Waste recycling : {a['recycling']}"
                self.ids.detail_collected_by_truck.text = f"Waste collected by truck : {a['collected_by_truck']}"
                self.ids.detail_other_waste_mgt.text = f"Other waste management : {a['others']}"
                self.ids.detail_other_waste_mgt_dx.text = f"Other waste mgt. description  : {a['other_practice']}"
                self.ids.detail_basic_water_access.text = f"Basic water access : {a['basic_water_access']}"
                self.ids.detail_safely_managed_water.text = f"Safely managed water : {a['safely_managed_water']}"
                self.ids.detail_sanitary_toilet_access.text = f"Sanitary toilet access : {a['sanitary_toilet_access']}"
                self.ids.detail_basic_sanitation_facility.text = f"Basic sanitation facility : {a['basic_sanitation_facility']}"
                self.ids.detail_safely_managed_sanitation_facility.text = f"Safely managed sanitation facility : {a['safely_managed_sanitation_facility']}"
                self.ids.detail_satisfactory_solid_waste_mgt.text = f"Satisfactory waste management : {a['satisfactory_solid_waste_mgt']}"
                self.ids.detail_complete.text = f"Complete : {a['complete']}"

    barangay_list = generate_barangay_list()
    user_database = generate_user_database()
    user_name_list = generate_user_name_list()
    household_database = generate_household_database()
    household_name_list = []
    for a in household_database:
        household_name_list.append(a['household_name'])
    household_database_user = []
    household_name_list_user = []
    current_user_info = {}
    temp_household_info = {}
    characters = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    def populate(self):
        self.ids.box.clear_widgets()
        self.household_name_list_user.sort()
        hh_sorted = []

        for a in self.household_name_list_user:
            for b in self.household_database_user:
                if a == b['household_name']:
                    hh_sorted.append(b)

        for i in hh_sorted:
            name_outer_box = MDBoxLayout(
                orientation='vertical',
                size_hint=(1, None),
                height=dp(60),
                spacing=dp(2)
            )
            name_button = MDRectangleFlatButton(
                size_hint=(1, None),
                height=dp(40),
                text=i['household_name'],
                md_bg_color=(.9, .9, .9, 1),
                halign='left',
                theme_text_color='Custom',
                text_color='blue',
                on_press=self.show_details
            )
            lbl1 = MDBoxLayout(
                size_hint=(1, None),
                height=dp(20),
                md_bg_color=(.7, .7, .7, 1)
            )
            if i['basic_water_access']:
                lbl1.md_bg_color = (.25, .25, 1, 1)

            lbl2 = MDBoxLayout(
                size_hint=(1, None),
                height=dp(20),
                md_bg_color=(.7, .7, .7, 1)
            )
            if i['safely_managed_water']:
                lbl2.md_bg_color = (.25, .25, 1, 1)

            lbl3 = MDBoxLayout(
                size_hint=(1, None),
                height=dp(20),
                md_bg_color=(.7, .7, .7, 1)
            )
            if i['sanitary_toilet_access']:
                lbl3.md_bg_color = (170/255, 80/255, 80/255, 1)

            lbl4 = MDBoxLayout(
                size_hint=(1, None),
                height=dp(20),
                md_bg_color=(.7, .7, .7, 1)
            )
            if i['basic_sanitation_facility']:
                lbl4.md_bg_color = (170/255, 80/255, 80/255, 1)

            lbl5 = MDBoxLayout(
                size_hint=(1, None),
                height=dp(20),
                md_bg_color=(.7, .7, .7, 1)
            )
            if i['safely_managed_sanitation_facility']:
                lbl5.md_bg_color = (170/255, 80/255, 80/255, 1)

            lbl6 = MDBoxLayout(
                size_hint=(1, None),
                height=dp(20),
                md_bg_color=(.7, .7, .7, 1)
            )
            if i['satisfactory_solid_waste_mgt']:
                lbl6.md_bg_color = (60 / 255, 150 / 255, 60 / 255, 1)

            lbl7 = MDBoxLayout(
                size_hint=(1, None),
                height=dp(20),
                md_bg_color=(.7, .7, .7, 1)
            )
            if i['complete']:
                lbl7.md_bg_color = (.15, .15, .15, 1)

            indicators = MDBoxLayout(
                size_hint=(1, None),
                height=dp(20),
                spacing=dp(2)
            )
            indicators.add_widget(lbl1)
            indicators.add_widget(lbl2)
            indicators.add_widget(lbl3)
            indicators.add_widget(lbl4)
            indicators.add_widget(lbl5)
            indicators.add_widget(lbl6)
            indicators.add_widget(lbl7)

            name_outer_box.add_widget(name_button)
            name_outer_box.add_widget(indicators)

            self.ids.box.add_widget(name_outer_box)

    def create_user(self):
        self.current = 'screen_new_user'

    def screen_new_user_cancel(self):
        self.ids.user_barangay.text = 'Select barangay (required)'
        self.ids.user_prefix.text = ''
        self.ids.user_first.text = ''
        self.ids.user_middle.text = ''
        self.ids.user_last.text = ''
        self.ids.user_suffix.text = ''
        self.ids.user_pw_entry.text = ''
        self.ids.user_pw_confirm.text = ''
        self.current = 'screen_welcome'

    def create_user_save(self):
        temp_name = f'{self.ids.user_last.text}, '
        if self.ids.user_prefix.text != '':
            temp_name += f'{self.ids.user_prefix.text} {self.ids.user_first.text}'
        else:
            temp_name += f'{self.ids.user_first.text}'
        if self.ids.user_suffix.text != '':
            temp_name += f' {self.ids.user_suffix.text}'
        if self.ids.user_middle.text != '':
            temp_name += f' {self.ids.user_middle.text}'

        if self.ids.user_barangay.text not in self.barangay_list:
            MissingUserInfo().open()
        elif (self.ids.user_first.text == '' or self.ids.user_last.text == '' or self.ids.user_pw_entry.text == '' or
              self.ids.user_pw_confirm.text == ''):
            MissingUserInfo().open()
        elif self.ids.user_pw_entry.text != self.ids.user_pw_confirm.text:
            MismatchPW().open()
        elif temp_name in self.user_name_list:
            UserAlreadyExist().open()
        else:

            user_id_list = []
            for a in self.user_database:
                user_id_list.append(a['user_id'])

            userid = 'none'
            while userid in user_id_list or userid == 'none':
                userid = f'{self.ids.user_barangay.text.replace(" ", "_").upper().replace("(", "").replace(")", "").replace("-", "")}_'
                for a in range(16):
                    userid += random.choice(self.characters)

            new_pw = hashlib.new('sha512')
            new_pw.update(self.ids.user_pw_entry.text.encode())

            self.user_database.append(
                {
                    'user_id': userid,
                    'user_barangay': self.ids.user_barangay.text,
                    'user_prefix': self.ids.user_prefix.text,
                    'user_first': self.ids.user_first.text,
                    'user_middle': self.ids.user_middle.text,
                    'user_last': self.ids.user_last.text,
                    'user_suffix': self.ids.user_suffix.text,
                    'user_name': temp_name,
                    'user_password': new_pw.hexdigest()
                }
            )
            with open('user_data.txt', 'w') as new_user_enter:
                new_user_enter.write(json.dumps(self.user_database))

            self.user_database = generate_user_database()
            self.user_name_list = generate_user_name_list()
            self.ids.spinner_user.values = self.user_name_list

            self.ids.user_barangay.text = 'Select barangay (required)'
            self.ids.user_prefix.text = ''
            self.ids.user_first.text = ''
            self.ids.user_middle.text = ''
            self.ids.user_last.text = ''
            self.ids.user_suffix.text = ''
            self.ids.user_pw_entry.text = ''
            self.ids.user_pw_confirm.text = ''

            NewUserSaved().open()
            self.current = 'screen_welcome'

    def change_user(self):
        for a in self.user_database:
            if a['user_name'] == self.ids.spinner_user.text:
                self.current_user_info = a

    def login(self):
        if self.ids.spinner_user.text not in self.user_name_list:
            NoUser().open()
        else:
            pw_entered = hashlib.new('sha512')
            pw_entered.update(self.ids.pw.text.encode())
            if pw_entered.hexdigest() == self.current_user_info['user_password']:
                self.household_database_user = []
                for a in self.household_database:
                    if a['household_interviewer_name'] == self.ids.spinner_user.text:
                        self.household_database_user.append(a)
                self.household_name_list_user = []
                for a in self.household_database_user:
                    self.household_name_list_user.append(a['household_name'])

                self.populate()
                self.current = 'screen_main'
            else:
                WrongPW().open()

    def add_household(self):
        self.current = 'frame_01'
        self.temp_household_info = {}

    def screen_main_back(self):
        self.current = 'screen_welcome'
        self.ids.pw.text = ''

    def household_cancel(self):
        self.ids.household_purok.text = ''
        self.ids.household_prefix.text = ''
        self.ids.household_first.text = ''
        self.ids.household_middle.text = ''
        self.ids.household_last.text = ''
        self.ids.household_suffix.text = ''
        self.ids.level_1.active = False
        self.ids.level_2.active = False
        self.ids.level_3.active = False
        self.ids.other_water.active = False
        self.ids.other_water_description.text = ''
        self.ids.other_water_description.hint_text = ''
        self.ids.other_water_description.disabled = True
        self.ids.water_location.text = 'Yes/No'
        self.ids.water_availability.text = 'Yes/No'
        self.ids.spinner_validation.text = 'Yes/No'
        self.ids.validation_text.text = ''
        self.ids.coli_spinner.text = ''
        self.ids.spinner_pc_validation.text = 'Yes/No'
        self.ids.validation_pc_text.text = ''
        self.ids.pc_spinner.text = ''
        self.ids.open_defecation.text = 'Yes/No'
        self.temp_household_info = {}
        self.ids.septic_tank.active = False
        self.ids.sewerage.active = False
        self.ids.ventilated.active = False
        self.ids.improvised.active = False
        self.ids.drainage.active = False
        self.ids.overhung.active = False
        self.ids.open_pit.active = False
        self.ids.without.active = False
        self.ids.in_situ.active = False
        self.ids.collected.active = False
        self.ids.toilet_not_shared.text = 'Yes/No'
        self.ids.segregation.active = False
        self.ids.composting.active = False
        self.ids.recycling.active = False
        self.ids.collected_by_truck.active = False
        self.ids.others.active = False
        self.ids.others_practice.text = ''
        self.ids.others_practice.hint_text = ''
        self.ids.others_practice.disabled = True
        self.current = 'screen_main'

    def frame_01_next(self):
        hh_id_list = []
        for a in self.household_database:
            hh_id_list.append(a['household_id'])

        hh_id = ''
        while hh_id == '' or hh_id in hh_id_list:
            hh_id = f'HH_{self.current_user_info["user_barangay"].upper().replace(" ", "_").replace("(", "").replace(")", "").replace("-", "")}_'
            for a in range(16):
                hh_id += random.choice(self.characters)

        household_temp_name = f'{self.ids.household_last.text}, '
        if self.ids.household_prefix.text != '':
            household_temp_name += f'{self.ids.household_prefix.text} {self.ids.household_first.text}'
        else:
            household_temp_name += f'{self.ids.household_first.text}'
        if self.ids.household_middle.text != '':
            household_temp_name += f' {self.ids.household_middle.text}'
        if self.ids.household_suffix.text != '':
            household_temp_name += f' {self.ids.household_suffix.text}'

        if self.ids.household_purok.text == '' or self.ids.household_first.text == '' or self.ids.household_last.text == '':
            MissingUserInfo().open()
        elif household_temp_name in self.household_name_list:
            HouseholdAlreadyExist().open()

        else:
            self.temp_household_info['household_interviewer_id'] = self.current_user_info['user_id']
            self.temp_household_info['household_interviewer_name'] = self.current_user_info['user_name']
            self.temp_household_info['household_barangay'] = self.current_user_info['user_barangay']
            self.temp_household_info['household_purok'] = self.ids.household_purok.text
            self.temp_household_info['household_id'] = hh_id
            self.temp_household_info['household_prefix'] = self.ids.household_prefix.text
            self.temp_household_info['household_first'] = self.ids.household_first.text
            self.temp_household_info['household_middle'] = self.ids.household_middle.text
            self.temp_household_info['household_last'] = self.ids.household_last.text
            self.temp_household_info['household_suffix'] = self.ids.household_suffix.text
            self.temp_household_info['household_name'] = household_temp_name
            self.current = 'frame_02'

    def other_water(self):
        if self.ids.other_water.active:
            self.ids.other_water_description.disabled = False
            self.ids.other_water_description.hint_text = 'Indicate source (i.e. rain water, river)'
        else:
            self.ids.other_water_description.hint_text = ''
            self.ids.other_water_description.text = ''
            self.ids.other_water_description.disabled = True

    def frame_02_previous(self):
        self.current = 'frame_01'

    def frame_02_next(self):
        if self.ids.level_1.active is False and self.ids.level_2.active is False and self.ids.level_3.active is False and self.ids.other_water.active is False:
            MissingUserInfo().open()
        else:
            if self.ids.other_water.active is True and self.ids.other_water_description.text == '':
                MissingUserInfo().open()
            else:
                self.temp_household_info['level_1'] = self.ids.level_1.active
                self.temp_household_info['level_2'] = self.ids.level_2.active
                self.temp_household_info['level_3'] = self.ids.level_3.active
                self.temp_household_info['other_water'] = self.ids.other_water.active
                self.temp_household_info['other_water_description'] = self.ids.other_water_description.text
                self.current = 'frame_03'

    def frame_03_previous(self):
        self.current = 'frame_02'

    def frame_03_next(self):
        if self.ids.water_location.text == 'Yes/No' or self.ids.water_availability.text == 'Yes/No':
            MissingUserInfo().open()
        else:
            self.temp_household_info['water_location'] = self.ids.water_location.text
            self.temp_household_info['water_availability'] = self.ids.water_availability.text
            self.current = 'frame_04'

    def frame_04_previous(self):
        self.current = 'frame_03'

    def frame_04_next(self):
        if self.ids.spinner_validation.text == 'Yes/No':
            MissingUserInfo().open()
        else:
            if self.ids.spinner_validation.text == 'No':
                self.temp_household_info['micro_test'] = self.ids.spinner_validation.text
                self.temp_household_info['micro_test_date'] = self.ids.validation_text.text
                self.temp_household_info['micro_test_result'] = self.ids.coli_spinner.text
                self.current = 'frame_05'
            else:
                if self.ids.validation_text.text == '' or self.ids.coli_spinner.text == 'Yes/No':
                    MissingUserInfo().open()
                else:
                    self.temp_household_info['micro_test'] = self.ids.spinner_validation.text
                    self.temp_household_info['micro_test_date'] = self.ids.validation_text.text
                    self.temp_household_info['micro_test_result'] = self.ids.coli_spinner.text
                    self.current = 'frame_05'

    def micro_validation_change(self):
        if self.ids.spinner_validation.text == 'Yes':
            self.ids.validation_text.disabled = False
            self.ids.validation_text.hint_text = 'Date of validation:'
            self.ids.validation_button.disabled = False
            self.ids.coli_label.disabled = False
            self.ids.coli_spinner.disabled = False
            self.ids.coli_spinner.text = 'Yes/No'
        else:
            self.ids.validation_text.text = ''
            self.ids.validation_text.hint_text = ''
            self.ids.validation_text.disabled = True
            self.ids.validation_button.disabled = True
            self.ids.coli_label.disabled = True
            self.ids.coli_spinner.text = ''
            self.ids.coli_spinner.disabled = True

    def mb_on_save(self, instance, value, date_range):
        self.ids.validation_text.text = str(value)

    def mb_on_cancel(self, instance, value):
        pass

    def mb_calendar(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.mb_on_save, on_cancel=self.mb_on_cancel)
        date_dialog.open()

    def frame_05_previous(self):
        self.current = 'frame_04'

    def frame_05_next(self):
        if self.ids.spinner_pc_validation.text == 'Yes/No':
            MissingUserInfo().open()
        else:
            if self.ids.spinner_pc_validation.text == 'No':
                self.temp_household_info['physical_chemical_test'] = self.ids.spinner_pc_validation.text
                self.temp_household_info['physical_chemical_test_date'] = self.ids.validation_pc_text.text
                self.temp_household_info['physical_chemical_test_result'] = self.ids.pc_spinner.text
                self.current = 'frame_06'

            else:
                if self.ids.validation_pc_text.text == '' or self.ids.pc_spinner.text == 'Yes/No':
                    MissingUserInfo().open()
                else:
                    self.temp_household_info['physical_chemical_test'] = self.ids.spinner_pc_validation.text
                    self.temp_household_info['physical_chemical_test_date'] = self.ids.validation_pc_text.text
                    self.temp_household_info['physical_chemical_test_result'] = self.ids.pc_spinner.text
                    self.current = 'frame_06'

    def pc_validation_change(self):
        if self.ids.spinner_pc_validation.text == 'Yes':
            self.ids.validation_pc_text.disabled = False
            self.ids.validation_pc_text.hint_text = 'Date of validation:'
            self.ids.validation_pc_button.disabled = False
            self.ids.pc_label.disabled = False
            self.ids.pc_spinner.disabled = False
            self.ids.pc_spinner.text = 'Yes/No'
        else:
            self.ids.validation_pc_text.text = ''
            self.ids.validation_pc_text.hint_text = ''
            self.ids.validation_pc_text.disabled = True
            self.ids.validation_pc_button.disabled = True
            self.ids.pc_label.disabled = True
            self.ids.pc_spinner.text = ''
            self.ids.pc_spinner.disabled = True

    def pc_on_save(self, instance, value, date_range):
        self.ids.validation_pc_text.text = str(value)

    def pc_on_cancel(self, instance, value):
        pass

    def pc_calendar(self):
        pc_date_dialog = MDDatePicker()
        pc_date_dialog.bind(on_save=self.pc_on_save, on_cancel=self.pc_on_cancel)
        pc_date_dialog.open()

    def frame_06_previous(self):
        self.current = 'frame_05'

    def frame_06_next(self):
        if self.ids.open_defecation.text == 'Yes/No':
            MissingUserInfo().open()
        else:
            self.temp_household_info['open_defecation'] = self.ids.open_defecation.text
            self.current = 'frame_07'

    def frame_07_previous(self):
        self.current = 'frame_06'

    def frame_07_next(self):
        if self.ids.septic_tank.active is False and self.ids.sewerage.active is False and self.ids.ventilated.active is False and self.ids.improvised.active is False and self.ids.drainage.active is False and self.ids.overhung.active is False and self.ids.open_pit.active is False and self.ids.without.active is False:
            MissingUserInfo().open()
        else:
            self.temp_household_info['septic_tank'] = self.ids.septic_tank.active
            self.temp_household_info['sewerage'] = self.ids.sewerage.active
            self.temp_household_info['ventilated'] = self.ids.ventilated.active
            self.temp_household_info['improvised'] = self.ids.improvised.active
            self.temp_household_info['drainage'] = self.ids.drainage.active
            self.temp_household_info['overhung'] = self.ids.overhung.active
            self.temp_household_info['open_pit'] = self.ids.open_pit.active
            self.temp_household_info['without'] = self.ids.without.active
            self.current = 'frame_08'

    def frame_08_previous(self):
        self.current = 'frame_07'

    def frame_08_next(self):
        if self.ids.toilet_not_shared.text == 'Yes/No':
            MissingUserInfo().open()
        else:
            self.temp_household_info['toilet_not_shared'] = self.ids.toilet_not_shared.text
            self.current = 'frame_09'

    def frame_09_previous(self):
        self.current = 'frame_08'

    def frame_09_next(self):
        if self.ids.in_situ.active is False and self.ids.collected.active is False:
            MissingUserInfo().open()
        else:
            self.temp_household_info['in_situ'] = self.ids.in_situ.active
            self.temp_household_info['collected'] = self.ids.collected.active
            self.current = 'frame_10'

    def frame_10_previous(self):
        self.current = 'frame_09'

    def frame_10_next(self):
        if self.ids.others.active is True and self.ids.others_practice.text == '':
            MissingUserInfo().open()
        else:
            self.temp_household_info['segregation'] = self.ids.segregation.active
            self.temp_household_info['composting'] = self.ids.composting.active
            self.temp_household_info['recycling'] = self.ids.recycling.active
            self.temp_household_info['collected_by_truck'] = self.ids.collected_by_truck.active
            self.temp_household_info['others'] = self.ids.others.active
            self.temp_household_info['other_practice'] = self.ids.others_practice.text

            if self.temp_household_info['other_water'] is False:
                self.temp_household_info['basic_water_access'] = True
            else:
                self.temp_household_info['basic_water_access'] = False

            if self.temp_household_info['water_location'] == 'Yes' and self.temp_household_info['water_availability'] == 'Yes' and self.temp_household_info['micro_test_result'] == 'Yes' and self.temp_household_info['physical_chemical_test_result'] == 'Yes':
                self.temp_household_info['safely_managed_water'] = True
            else:
                self.temp_household_info['safely_managed_water'] = False

            if self.temp_household_info['septic_tank'] or self.temp_household_info['sewerage'] or self.temp_household_info['ventilated'] or self.temp_household_info['improvised']:
                self.temp_household_info['sanitary_toilet_access'] = True
            else:
                self.temp_household_info['sanitary_toilet_access'] = False

            if self.temp_household_info['sanitary_toilet_access'] and self.temp_household_info['toilet_not_shared'] == 'Yes':
                self.temp_household_info['basic_sanitation_facility'] = True
            else:
                self.temp_household_info['basic_sanitation_facility'] = False

            if self.temp_household_info['basic_sanitation_facility'] and (self.temp_household_info['in_situ'] or self.temp_household_info['collected']):
                self.temp_household_info['safely_managed_sanitation_facility'] = True
            else:
                self.temp_household_info['safely_managed_sanitation_facility'] = False

            if (self.temp_household_info['segregation'] and self.temp_household_info['composting'] and self.temp_household_info['recycling']) or (self.temp_household_info['segregation'] and self.temp_household_info['collected_by_truck']):
                self.temp_household_info['satisfactory_solid_waste_mgt'] = True
            else:
                self.temp_household_info['satisfactory_solid_waste_mgt'] = False

            if self.temp_household_info['basic_water_access'] and self.temp_household_info['sanitary_toilet_access'] and self.temp_household_info['satisfactory_solid_waste_mgt']:
                self.temp_household_info['complete'] = True
            else:
                self.temp_household_info['complete'] = False

            db = []
            try:
                with open('household_data.txt', 'r') as old_hh_db:
                    db = json.loads(old_hh_db.read())
            except:
                pass
            else:
                pass
            finally:
                db.append(self.temp_household_info)
                with open('household_data.txt', 'w') as new_hh_db:
                    new_hh_db.write(json.dumps(db))

            self.household_database = db
            for a in self.household_database:
                self.household_name_list.append(a['household_name'])

            self.household_cancel()

            self.household_database_user = []
            for a in self.household_database:
                if a['household_interviewer_name'] == self.ids.spinner_user.text:
                    self.household_database_user.append(a)
            self.household_name_list_user = []
            for a in self.household_database_user:
                self.household_name_list_user.append(a['household_name'])

            self.populate()
            self.current = 'screen_main'

    def others_active(self):
        if self.ids.others.active:
            self.ids.others_practice.disabled = False
            self.ids.others_practice.hint_text = 'Other garbage disposal (i.e. burning)'
        else:
            self.ids.others_practice.text = ''
            self.ids.others_practice.hint_text = ''
            self.ids.others_practice.disabled = True


class EnviMDApp(MDApp):
    pass


EnviMDApp().run()
