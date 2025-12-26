################################################################################
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.
################################################################################

################################################################################
# This program is used for quality testing the menus in Andy's Ham Radio Linux (AHRL).
# It is run by the AHRL developer prior to releasing a new version of AHRL.
#
# Currently, it works well on Xubuntu Linux, and would probably work well
# on any system using XFCE due to the menu layout.  This program has also been
# tested on the Raspberry Pi OS.
#
# Copyright 2025, Andy Stewart (KB1OIQ)
#
# Some programs exist in multiple menus, therefore, there are
# multiple functions defined to open the application.
#
# Example:  open_ais_catcher()         - opens the program using the default menu
#           open_ais_catcher_ti_menu() - opens the program using the Teachers Institute menu
#
#           open_fldigi()              - opens the program using the default menu
#           open_fldigi_nbems_menu()   - opens the program using the NBEMS menu
#
################################################################################

import os.path
import pyautogui
import platform
import subprocess
import time

################################################################################
# Global variables
################################################################################

sleep_time = 5
menu_sleep_time = 1

arduino_sleep_time = 10
chirp_sleep_time = 10
firefox_sleep_time = 10
flwkey_sleep_time = 10
freedv_sleep_time = 10
fritzing_sleep_time = 10
gnuradio_sleep_time = 15
gridtracker2_sleep_time = 10
hamclock_sleep_time = 15
morse_runner_sleep_time = 10
not1mm_sleep_time = 10
satdump_sleep_time = 10
sdrpp_sleep_time = 10
yaac_sleep_time = 5

################################################################################
# Function: kill_freedv
#           for some reason, process_status() can't kill freedv.
#           Try moving the mouse and using the File->Exit menu.
################################################################################

def kill_freedv():
	pyautogui.moveTo(20,60)
	pyautogui.click()
	pyautogui.press(['down'])
	pyautogui.press('enter')

################################################################################
# Function: process_status
#           determine if a named process exists,
#           kill it, and report status.
################################################################################

def process_status(process_name):
	print(f"{process_name}:")
	try:
		subprocess.check_output(["pgrep", process_name])
		print(f"\tprocess exists")

		try:
			subprocess.check_output(["pkill", "-9", process_name])
			print(f"\tsuccessfully killed")
		except:
			print(f"\tError - could not kill process {process_name}")

	except subprocess.CalledProcessError:
		print(f"\tError - process does NOT exist.")

	print(f"")

################################################################################
# Functions for opening the top level AHRL menu
################################################################################

def open_menu():
	# This works on XFCE and Raspberry Pi since the menu is in the top corner.
	#print(f"open_menu()")
	pyautogui.moveTo(1,1)
	pyautogui.click()
	time.sleep(menu_sleep_time)

def menu_entry(entry):
	#print(f"menu_entry()")
	if (platform.machine() == "aarch64"):
		pyautogui.press('down', presses=entry-1)
	else:
		pyautogui.press('down', presses=entry)

	time.sleep(menu_sleep_time)
	pyautogui.press('enter')

def open_ahrl_menu():
	open_menu()
	#print(f"open_ahrl_menu()")
	if (platform.machine() == "aarch64"):
		pyautogui.press('down', presses=9)
	else:
		pyautogui.press(['down', 'down', 'right'])
		pyautogui.press('down', presses=4)
		pyautogui.press('enter')
	time.sleep(menu_sleep_time)

################################################################################
# Functions for opening the AHRL submenus
################################################################################

def open_ahrl_antenna_menu():
	open_ahrl_menu()
	#print(f"open_ahrl_antenna_menu()")
	if (platform.machine() == "aarch64"):
		pyautogui.press('right', presses=2)
		time.sleep(menu_sleep_time)
	else:
		pyautogui.press('left')
		pyautogui.press('down')
		pyautogui.press('enter')

def open_ahrl_arrl_teachers_institute_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=1)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=2)
		pyautogui.press('enter')

def open_ahrl_cw_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=2)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=3)
		pyautogui.press('enter')

def open_ahrl_digital_modes_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=3)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=4)
		pyautogui.press('enter')

def open_ahrl_documentation_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=4)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=5)
		pyautogui.press('enter')

def open_ahrl_electronic_design_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=5)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=6)
		pyautogui.press('enter')

def open_ahrl_hf_propagation_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=6)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=7)
		pyautogui.press('enter')

def open_ahrl_logging_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=7)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=8)
		pyautogui.press('enter')

def open_ahrl_m17_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=8)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=9)
		pyautogui.press('enter')

def open_ahrl_nbems_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=9)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=10)
		pyautogui.press('enter')

def open_ahrl_rig_control_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=10)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=11)
		pyautogui.press('enter')

def open_ahrl_satellites_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=11)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=12)
		pyautogui.press('enter')

def open_ahrl_sdr_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=12)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=13)
		pyautogui.press('enter')

def open_ahrl_tracking_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=13)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=14)
		pyautogui.press('enter')

def open_ahrl_workarounds_menu():
	open_ahrl_menu()
	if (platform.machine() == "aarch64"):
		pyautogui.press('right')
		pyautogui.press('down', presses=14)
		pyautogui.press('right')
	else:
		pyautogui.press('left')
		pyautogui.press('down', presses=15)
		pyautogui.press('enter')

################################################################################
# Functions for opening the applications
################################################################################

def open_ais_catcher():
	open_ahrl_tracking_menu()
	menu_entry(1)
	time.sleep(firefox_sleep_time)
	process_status("firefox")

def open_ais_catcher_ti_menu():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(1)
	time.sleep(firefox_sleep_time)
	process_status("firefox")

def open_antscope2():
	if (platform.machine() != "aarch64"):
		open_ahrl_antenna_menu()
		print(f"open_antscope2()")
		menu_entry(1)
		time.sleep(sleep_time)
		process_status("AntScope2")

def open_arduino():
	open_ahrl_electronic_design_menu()
	menu_entry(1)
	time.sleep(arduino_sleep_time)
	process_status("java")

def open_arduino_ti_menu():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(2)
	time.sleep(arduino_sleep_time)
	process_status("java")

def open_chirp():
	open_ahrl_rig_control_menu()
	menu_entry(1)
	time.sleep(chirp_sleep_time)
	process_status("chirp")

def open_chirp_ti_menu():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(3)
	time.sleep(chirp_sleep_time)
	process_status("chirp")

def open_coil64():
	open_ahrl_electronic_design_menu()
	menu_entry(2)
	time.sleep(sleep_time)
	process_status("Coil64")

def open_cqrlog():
	open_ahrl_logging_menu()
	menu_entry(1)
	time.sleep(sleep_time)
	process_status("cqrlog")

def open_direwolf():
	open_ahrl_digital_modes_menu()
	menu_entry(1)
	time.sleep(sleep_time)
	process_status("direwolf")

def open_direwolf_ti_menu():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(4)
	time.sleep(sleep_time)
	process_status("direwolf")

def open_dream():
	open_ahrl_sdr_menu()
	menu_entry(1)
	time.sleep(sleep_time)
	process_status("dream")

def open_ebook2cw():
	open_ahrl_cw_menu()
	menu_entry(1)
	time.sleep(sleep_time)
	process_status("ebook2cw")

def open_fix_sound():
	open_ahrl_workarounds_menu()
	menu_entry(1)
	time.sleep(sleep_time)
	process_status("fix_sound")

def open_fl_moxgen():
	open_ahrl_antenna_menu()
	if (platform.machine() == "aarch64"):
		menu_entry(2)
	else:
		menu_entry(3)

	time.sleep(sleep_time)
	process_status("fl_moxgen")

def open_flaa():
	open_ahrl_antenna_menu()
	if (platform.machine() == "aarch64"):
		menu_entry(1)
	else:
		menu_entry(2)

	time.sleep(sleep_time)
	process_status("flaa")

def open_flamp():
	open_ahrl_digital_modes_menu()
	menu_entry(2)
	time.sleep(sleep_time)
	process_status("flamp")

def open_flamp_nbems_menu():
	open_ahrl_nbems_menu()
	menu_entry(1)
	time.sleep(sleep_time)
	process_status("flamp")

def open_flarq():
	open_ahrl_digital_modes_menu()
	menu_entry(3)
	time.sleep(sleep_time)
	process_status("flarq")

def open_flcluster():
	open_ahrl_hf_propagation_menu()
	menu_entry(1)
	time.sleep(sleep_time)
	process_status("flcluster")

def open_fldigi():
	open_ahrl_digital_modes_menu()
	menu_entry(4)
	time.sleep(sleep_time)
	process_status("fldigi")

def open_fldigi_nbems_menu():
	open_ahrl_nbems_menu()
	menu_entry(2)
	time.sleep(sleep_time)
	process_status("fldigi")

def open_fllog():
	open_ahrl_logging_menu()
	menu_entry(2)
	time.sleep(sleep_time)
	process_status("fllog")

def open_flmsg():
	open_ahrl_digital_modes_menu()
	menu_entry(5)
	time.sleep(sleep_time)
	process_status("flmsg")

def open_flmsg_nbems_menu():
	open_ahrl_nbems_menu()
	menu_entry(3)
	time.sleep(sleep_time)
	process_status("flmsg")

def open_flnet():
	open_ahrl_logging_menu()
	menu_entry(3)
	time.sleep(sleep_time)
	process_status("flnet")

def open_flrig():
	open_ahrl_rig_control_menu()
	menu_entry(2)
	time.sleep(sleep_time)
	process_status("flrig")

def open_flwrap():
	open_ahrl_digital_modes_menu()
	menu_entry(6)
	time.sleep(sleep_time)
	process_status("flwrap")

def open_flwkey():
	open_ahrl_cw_menu()
	menu_entry(2)
	time.sleep(flwkey_sleep_time)
	process_status("flwkey")

def open_fox_telemetry():
	open_ahrl_satellites_menu()
	menu_entry(1)
	time.sleep(sleep_time)
	process_status("java")

def open_freedv():
	open_ahrl_digital_modes_menu()
	menu_entry(7)
	time.sleep(freedv_sleep_time)
	process_status("freedv")
	# For some reason, process_status() can't kill freedv
	# so a function was created to move the mouse cursor
	# to execute File->Exit.
	kill_freedv()

def open_fritzing():
	open_ahrl_electronic_design_menu()
	menu_entry(3)
	time.sleep(fritzing_sleep_time)
	process_status("Fritzing")

def open_gerbview():
	open_ahrl_electronic_design_menu()
	menu_entry(6)
	time.sleep(sleep_time)
	process_status("gerbview")

def open_glfer():
	open_ahrl_digital_modes_menu()
	menu_entry(8)
	time.sleep(sleep_time)
	process_status("glfer")

def open_gnuradio_grc():
	open_ahrl_sdr_menu()
	menu_entry(2)
	time.sleep(gnuradio_sleep_time)
	process_status("gnuradio")

def open_gnuradio_grc_ti_menu():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(5)
	time.sleep(gnuradio_sleep_time)
	process_status("gnuradio")

def open_gpredict():
	open_ahrl_satellites_menu()
	menu_entry(2)
	time.sleep(sleep_time)
	process_status("gpredict")

def open_gpredict_ti_menu():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(6)
	time.sleep(sleep_time)
	process_status("gpredict")

def open_gqrx():
	open_ahrl_sdr_menu()
	menu_entry(3)
	time.sleep(sleep_time)
	process_status("gqrx")

def open_gridtracker2():
	open_ahrl_digital_modes_menu()
	menu_entry(9)
	time.sleep(gridtracker2_sleep_time)
	process_status("gridtracker2")

def open_grig():
	open_ahrl_rig_control_menu()
	menu_entry(3)
	time.sleep(sleep_time)
	process_status("grig")

def open_gspiceui():
	open_ahrl_electronic_design_menu()
	menu_entry(4)
	time.sleep(sleep_time)
	process_status("gspiceui")

def open_hamclock():
	open_ahrl_hf_propagation_menu()
	menu_entry(2)
	time.sleep(hamclock_sleep_time)
	process_status("hamclock")

def open_ibp():
	open_ahrl_hf_propagation_menu()
	menu_entry(3)
	time.sleep(sleep_time)
	process_status("ibp")

def open_js8call():
	open_ahrl_digital_modes_menu()
	menu_entry(10)
	time.sleep(sleep_time)
	process_status("js8call")

def open_js8spotter():
	open_ahrl_digital_modes_menu()
	menu_entry(11)
	time.sleep(sleep_time)
	process_status("python")

def open_jtdx():
	open_ahrl_digital_modes_menu()
	menu_entry(12)
	time.sleep(sleep_time)
	process_status("jtdx")

def open_kicad():
	open_ahrl_electronic_design_menu()
	menu_entry(5)
	time.sleep(sleep_time)
	process_status("kicad")

def open_klog():
	open_ahrl_logging_menu()
	menu_entry(4)
	time.sleep(sleep_time)
	process_status("klog")

def open_linrad():
	open_ahrl_sdr_menu()
	menu_entry(4)
	time.sleep(sleep_time)
	process_status("linrad")

def open_mvoice():
	open_ahrl_m17_menu()
	menu_entry(1)
	time.sleep(sleep_time)
	process_status("mvoice")

def open_morse_runner():
	if (platform.machine() != "aarch64"):
		open_ahrl_cw_menu()
		menu_entry(3)
		time.sleep(morse_runner_sleep_time)
		process_status("MorseRunner")

def open_mshv():
	open_ahrl_digital_modes_menu()
	menu_entry(13)
	time.sleep(sleep_time)
	process_status("MSHV")

def open_not1mm():
	if (platform.machine() != "aarch64"):
		open_ahrl_logging_menu()
		menu_entry(5)
		time.sleep(not1mm_sleep_time)
		process_status("not1mm")

def open_notepad():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(7)
	time.sleep(sleep_time)
	process_status("notepad")

def open_pcbnew():
	open_ahrl_electronic_design_menu()
	menu_entry(7)
	time.sleep(sleep_time)
	process_status("pcbnew")

def open_pskreporter():
	open_ahrl_hf_propagation_menu()
	menu_entry(4)
	time.sleep(firefox_sleep_time)
	process_status("firefox")

def open_putty():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(8)
	time.sleep(sleep_time)
	process_status("putty")

def open_qgrid():
	open_ahrl_hf_propagation_menu()
	menu_entry(5)
	time.sleep(sleep_time)
	process_status("qgrid")

def open_qlog():
	open_ahrl_logging_menu()
	if (platform.machine() == "aarch64"):
		menu_entry(5)
	else:
		menu_entry(6)

	time.sleep(sleep_time)
	process_status("qlog")

def open_qrq():
	open_ahrl_cw_menu()
	if (platform.machine() == "aarch64"):
		menu_entry(3)
	else:
		menu_entry(4)

	time.sleep(sleep_time)
	process_status("qrq")

def open_qsstv():
	open_ahrl_digital_modes_menu()
	menu_entry(14)
	time.sleep(sleep_time)
	process_status("qsstv")

def open_qtel():
	open_ahrl_digital_modes_menu()
	menu_entry(15)
	time.sleep(sleep_time)
	process_status("qtel")

def open_qttinysa():
	open_ahrl_electronic_design_menu()
	menu_entry(8)
	time.sleep(sleep_time)
	process_status("python")

def open_quisk():
	open_ahrl_sdr_menu()
	menu_entry(5)
	time.sleep(sleep_time)
	process_status("python")

def open_rf_exp_calc():
	open_ahrl_antenna_menu()
	if (platform.machine() == "aarch64"):
		menu_entry(3)
	else:
		menu_entry(4)

	time.sleep(firefox_sleep_time)
	process_status("firefox")

def open_satdump():
	open_ahrl_satellites_menu()
	menu_entry(3)
	time.sleep(satdump_sleep_time)
	process_status("satdump")

def open_satdump_ti_menu():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(9)
	time.sleep(satdump_sleep_time)
	process_status("satdump")

def open_sdr_cleanup():
	open_ahrl_sdr_menu()
	menu_entry(7)
	time.sleep(sleep_time)

def open_sdrpp():
	open_ahrl_sdr_menu()
	menu_entry(6)
	time.sleep(sdrpp_sleep_time)
	process_status("sdrpp")

def open_sdrpp_ti_menu():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(10)
	time.sleep(sdrpp_sleep_time)
	process_status("sdrpp")

def open_smith_chart():
	open_ahrl_electronic_design_menu()
	menu_entry(9)
	time.sleep(sleep_time)
	process_status("gsmc")

def open_solar_data():
	open_ahrl_hf_propagation_menu()
	menu_entry(6)
	time.sleep(sleep_time)
	process_status("display")

def open_sunclock():
	open_ahrl_hf_propagation_menu()
	menu_entry(7)
	time.sleep(sleep_time)
	process_status("sunclock")

def open_sylpheed():
	pyautogui.alert(text='Not yet implemented', title='open_sylpheed()', button='OK')
	time.sleep(sleep_time)
	process_status("sylpheed")

def open_sylpheed_nbems_menu():
	open_ahrl_nbems_menu()
	menu_entry(4)
	time.sleep(sleep_time)
	process_status("sylpheed")

def open_tqsl():
	open_ahrl_logging_menu()
	if (platform.machine() == "aarch64"):
		menu_entry(6)
	else:
		menu_entry(7)

	time.sleep(sleep_time)
	process_status("tqsl")

def open_virtual_radar_server():
	open_ahrl_tracking_menu()
	menu_entry(2)
	time.sleep(firefox_sleep_time)
	process_status("mono")
	process_status("firefox")

def open_virtual_radar_server_ti_menu():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(11)
	time.sleep(firefox_sleep_time)
	process_status("mono")
	process_status("firefox")

def open_voacap():
	open_ahrl_hf_propagation_menu()
	menu_entry(8)
	time.sleep(firefox_sleep_time)
	process_status("firefox")

def open_wfview():
	open_ahrl_rig_control_menu()
	menu_entry(4)
	time.sleep(sleep_time)
	process_status("wfview")

def open_wsjtx():
	open_ahrl_digital_modes_menu()
	menu_entry(16)
	time.sleep(sleep_time)
	process_status("wsjtx")

def open_wsjtx_improved():
	open_ahrl_digital_modes_menu()
	menu_entry(17)
	time.sleep(sleep_time)
	process_status("wsjtx_improved")

def open_xastir():
	open_ahrl_tracking_menu()
	menu_entry(3)
	time.sleep(sleep_time)
	process_status("xastir")

def open_xcwcp():
	open_ahrl_cw_menu()
	if (platform.machine() == "aarch64"):
		menu_entry(4)
	else:
		menu_entry(5)

	time.sleep(sleep_time)
	process_status("xcwcp")

def open_xdx():
	open_ahrl_hf_propagation_menu()
	menu_entry(9)
	time.sleep(sleep_time)
	process_status("xdx")

def open_xlog():
	open_ahrl_logging_menu()
	if (platform.machine() == "aarch64"):
		menu_entry(7)
	else:
		menu_entry(8)

	time.sleep(sleep_time)
	process_status("xlog")

def open_xnec2c():
	open_ahrl_antenna_menu()
	if (platform.machine() == "aarch64"):
		menu_entry(4)
	else:
		menu_entry(5)

	time.sleep(sleep_time)
	process_status("xnec2c")

def open_xwefax():
	open_ahrl_digital_modes_menu()
	menu_entry(18)
	time.sleep(sleep_time)
	process_status("xwefax")

def open_yaac():
	open_ahrl_tracking_menu()
	menu_entry(4)
	time.sleep(yaac_sleep_time)
	process_status("java")

def open_yaac_ti_menu():
	open_ahrl_arrl_teachers_institute_menu()
	menu_entry(12)
	time.sleep(yaac_sleep_time)
	process_status("java")

################################################################################
# Functions for testing menu entries
################################################################################

def test_antenna_menus():
	if (platform.machine() != "aarch64"):
		open_antscope2()

	open_flaa()
	open_fl_moxgen()
	open_rf_exp_calc()
	open_xnec2c()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - antenna', button='OK')
	time.sleep(sleep_time)

# Some programs live in both the ARRL Teachers Institute menu and
# on other place.  Thus, two functions are needed.
# Naming convention:  open_APP() and open_APP_ti_menu()

def test_teachers_institute_menus():
	open_ais_catcher_ti_menu()
	open_arduino_ti_menu()
	open_chirp_ti_menu()
	open_direwolf_ti_menu()
	open_gnuradio_grc_ti_menu()
	open_gpredict_ti_menu()
	open_notepad()
	open_putty()
	open_satdump_ti_menu()
	open_sdrpp_ti_menu()
	open_virtual_radar_server_ti_menu()
	open_yaac_ti_menu()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - teachers institute', button='OK')
	time.sleep(sleep_time)

def test_cw_menus():
	open_ebook2cw()
	open_flwkey()
	if (platform.machine() != "aarch64"):
		open_morse_runner()

	open_qrq()
	open_xcwcp()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - cw', button='OK')
	time.sleep(sleep_time)

def test_digital_modes_menus():
	open_direwolf()
	open_flamp()
	open_flarq()
	open_fldigi()
	open_flmsg()
	open_flwrap()
	open_freedv()
	open_glfer()
	open_gridtracker2()
	open_js8call()
	open_js8spotter()
	open_jtdx()
	open_mshv()
	open_qsstv()
	open_qtel()
	open_wsjtx()
	open_wsjtx_improved()
	open_xwefax()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - digital_modes', button='OK')
	time.sleep(sleep_time)

def test_documentation_menus():
	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - documentation', button='OK')
	time.sleep(sleep_time)

def test_electronic_design_menus():
	open_arduino()
	open_coil64()
	open_fritzing()
	open_gspiceui()
	open_kicad()
	open_gerbview()
	open_pcbnew()
	open_qttinysa()
	open_smith_chart()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - electronic_design', button='OK')
	time.sleep(sleep_time)

def test_hf_propagation_menus():
	open_flcluster()
	open_hamclock()
	open_ibp()
	open_pskreporter()
	open_qgrid()
	open_solar_data()
	open_sunclock()
	open_voacap()
	open_xdx()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - hf_propagation', button='OK')
	time.sleep(sleep_time)

def test_logging_menus():
	open_cqrlog()
	open_fllog()
	open_flnet()
	open_klog()
	open_not1mm()
	open_qlog()
	open_tqsl()
	open_xlog()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - logging', button='OK')
	time.sleep(sleep_time)

def test_m17_menus():
	open_mvoice()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - m17', button='OK')
	time.sleep(sleep_time)

def test_nbems_menus():
	open_flamp_nbems_menu()
	open_fldigi_nbems_menu()
	open_flmsg_nbems_menu()
	open_sylpheed_nbems_menu()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - nbems', button='OK')
	time.sleep(sleep_time)

def test_rig_control_menus():
	open_chirp()
	open_flrig()
	open_grig()
	open_wfview()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - rig_control', button='OK')
	time.sleep(sleep_time)

def test_satellites_menus():
	open_fox_telemetry()
	open_gpredict()
	open_satdump()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - satellites', button='OK')
	time.sleep(sleep_time)

def test_sdr_menus():
	open_dream()
	open_gnuradio_grc()
	open_gqrx()
	open_linrad()
	open_quisk()
	open_sdrpp()
	open_sdr_cleanup()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - sdr', button='OK')
	time.sleep(sleep_time)

def test_tracking_menus():
	open_ais_catcher()
	open_virtual_radar_server()
	open_xastir()
	open_yaac()

	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - tracking', button='OK')
	time.sleep(sleep_time)

def test_workarounds_menus():
	open_fix_sound()
	pyautogui.alert(text='Press to continue', title='AHRL Menu Test - workarounds', button='OK')
	time.sleep(sleep_time)

################################################################################
# Do the real work here
################################################################################

test_antenna_menus()
test_teachers_institute_menus()
test_cw_menus()
test_digital_modes_menus()
test_documentation_menus()
test_electronic_design_menus()
test_hf_propagation_menus()
test_logging_menus()
test_m17_menus()
test_nbems_menus()
test_rig_control_menus()
test_satellites_menus()
test_sdr_menus()
test_tracking_menus()
test_workarounds_menus()
