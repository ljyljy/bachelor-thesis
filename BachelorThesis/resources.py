#
# General
#
FONT = 'monospace 10'

#
# FILEFORMATTINGS
#

ff_FILETITLE_a = 'Arousal Plot'
ff_FILETAG_a = '.aplot'

ff_FILETITLE_e = 'European Data Format'
ff_FILETAG_e = '.edf'

ff_FILETITLE_s = 'NSRR-formatted Sleep Stage Annotation'
ff_FILETAG_s = '.xml'

#
# HELP MENU TEXTS
#

hm_ABOUT_TEXT = [	"About",
					"-"*50,
					"Copyright (C) Michael Kirkegaard, Nicklas Hansen."
					]

hm_FORMAT_TEXT = [	"File Formats",
					"-"*50,
					"- PSG files must be in European Data Format (*.edf file extension) and must contain PPG and ECG signals.",
					"- Arousal Plots are saved with *.aplot file extension and must be created through this software."
					]
		
hm_COMMANDS_TEXT =	[	"Application Commands",
						"-"*50,
						"-"*20,
						"File Menu",
						"-"*20,
						["- New",	"<Shift-N>:",		"Make new arousal plot from a PSG file. Will start analysis automatically"],
						["- Open",	"<Shift-O>:",		"Open an arousal plot file (i.e. an already analysed PSG file)."],
						["- Save",	"<Shift-S>:",		"Save an arousal plot file."],
						["- Close",	"<Shift-C>:",		"Close currently opened arousal plot file."],
						["- Exit",	"<Shift-Escape>:",	"Close application."],
						"",
						"-"*20,
						"Help Menu",
						"-"*20,
						"<Escape> or <Enter> or <Shift-C>:     Close popup windows shortcuts.",
						]