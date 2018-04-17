#!/usr/bin/python3
# ACM v0.1
# Первый релиз перезапущенного ACM. Данная версия — Linux-only.

import gi, re, sys, time, tkinter
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk, Wnck

colors = {
#	"Regex_title":		'_color_',
	".*Chromium$":		'#263238',
	"VK Messenger.*":	'#1f2333',
	".*GIMP$":		'#f2f1f0',
} # example. TODO: move to JSON DB

def title():
	while Gtk.events_pending(): Gtk.main_iteration()
	s.force_update()
	if (sys.platform in ['linux']):
		c = s.get_active_window()
		if (all([p in c.get_state().value_names for p in [
			'WNCK_WINDOW_STATE_MAXIMIZED_HORIZONTALLY',
			'WNCK_WINDOW_STATE_MAXIMIZED_VERTICALLY'
		]])): r = c.get_name()
	# print(s.get_active_window().get_state().value_names) # DEBUG
	return r

def loop():
	w.lower()
	try: c = title()
	except: c = None
	if (c):
		for i in colors:
			if (re.match(i, c)):
				w.config(background=colors[i])
				w.attributes('-alpha', 1)
				break
	else: w.attributes('-alpha', 0) # TODO: only when no maximized window
	w.update()
	time.sleep(0.05) # TODO: manual/dynamic

def main():
	global s, w
	s = Wnck.Screen.get_default()
	w = tkinter.Tk()
	w.overrideredirect(True)
	w.geometry("%dx24" % w.winfo_screenwidth())
	w.title('ACM v1.0')
	w.config(background='black')
	while (True):
		try: loop()
		except Exception as ex: sys.stderr.write("Caught Exception on line %d: %s\n" % (ex.__traceback__.tb_lineno, ex))
		except KeyboardInterrupt as ex: exit(ex if (ex.args) else '')

if (__name__ == '__main__'): main()

# by Sdore, 2018
