import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk # type: ignore

# Create a basic GTK window
win = Gtk.Window(title="Hello, GTK!")
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
