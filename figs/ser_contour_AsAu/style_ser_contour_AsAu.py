import matplotlib as mpl
import matplotlib.pyplot as plt

class Style(object):
	def __init__(self):
		pass

class Style1col(Style):

	def apply(self, mode, content, decision, wide):
		if mode == "sync":
			mpl.rc_file("../rc/1fig-contour-rc.txt")

		elif mode == "usync":
			if decision in ("soft",):
				mpl.rc_file("../rc/1fig-contour-rc.txt")
			else:
				mpl.rc_file("../rc/2fig-contour-rc.txt")


	def annotate(self, mode, content, decision, wide):
		if wide:
			self._annotate_wide()
		else:
			self._annotate()


	def _annotate(self):
		plt.annotate(r"$\delta_\mathrm{SIR}$", xy=(-0.25, 1), xytext=(-1.25, 3), color="w", fontsize=8,
				arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", color="w"))

	def _annotate_wide(self):
		plt.annotate(r"$\delta_\mathrm{SIR}$", xy=(-0.25, 1), xytext=(-2.75, 1.35), color="w", fontsize=8,
				arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", color="w"))

