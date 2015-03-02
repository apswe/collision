#!/usr/bin/env python2.7

# Copyright 2013-2014 Matthias Wilhelm

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from matplotlib.font_manager import FontProperties


######################################################
###############    PLOT OPTIONS    ###################
######################################################
Au = np.sqrt(1e4)

mode = ("sync", "usync")[1]
content = ("same", "unif")[1]
decision = ("soft", "hard")[0]
######################################################
######################################################


mpl.rc_file("../rc/3fig-contour-rc.txt")

def plot():
	data = np.load("data/ser_Au%.2f_%s_%s_v2.npz"%(Au, content, decision))

	Zs = data["SER_S"]
	Zu = data["SER_U"]
	Z = (Zu if mode in ("usync",) else Zs)

	tau_range = data["tau_range"]
	phi_range = data["phi_range"]

	PHI, TAU = np.meshgrid(phi_range, tau_range)

	print("DEBUG: If 'Inputs x and y must be 1D or 2D.' -> Shape mismatch PHI, TAU, Z: ", PHI.shape, TAU.shape, Z.shape)

	CSf  = plt.contourf(TAU, PHI/np.pi, Z, levels=(0.0, 1e-3, 0.25, 0.9, 1.0), colors=("0.0", "0.5", "0.75", "1."), origin="lower")
	CS2 = plt.contour(CSf, levels=(0.9, 0.25, 1e-3), colors=("1.0", "r", "w"), linewidths=(0., 0.75, 1.0), origin="lower", hold="on")

	plt.axis([-1.5, 1.5, -1, 1])
	plt.xlabel(r"Time offset $\tau$ ($/T$)", labelpad=2)
	plt.ylabel(r"Carrier phase offset $\varphi_c$ ($/\pi$)", labelpad=0)

	plt.annotate(r"capture zone", xy=(-0.35, 0.125), xytext=(-1.425, 0.475), color="0.0",
        fontproperties=FontProperties(size=10, style="italic"),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", color="0.55", lw=1.25))
	plt.annotate("", xy=(-0.35, 0.85), xytext=(-0.8, 0.525),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2", lw=1.25, color="0.55"))
	plt.annotate("", xy=(-0.35, -0.85), xytext=(-0.9, 0.45),
        arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2", lw=1.25, color="0.55"))

	plt.savefig("pdf/serc_Au%.2f_%s_%s_%s_v2.pdf"%(Au, mode, content, decision))
	#plt.savefig("png/serc2_Au%.2f_%s_%s_%s.png"%(Au, mode, content, decision), dpi=600)

def colorbar_only():
	fig = plt.figure(figsize=(0.375, 1.92))
	ax1 = fig.add_axes([0, 0.05, 0.25, 1])

	cmap = mpl.colors.ListedColormap(["0.0", "0.5", "0.75", "1.0"])

	bounds = [0.0, 1e-3, 0.25, 0.9, 1.0]
	norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
	cb2 = mpl.colorbar.ColorbarBase(ax1, cmap=cmap,
                                         norm=norm,
                                         boundaries=bounds,
                                         ticks=bounds, # optional
                                         orientation="vertical")

	cb2.set_ticklabels(["0", "$10^{-3}$", "0.25", "0.9", "1"])
	cb2.set_label(r"Symbol error rate ($\mathrm{SER}$)", fontsize=12, labelpad=6)

	plt.savefig("pdf/cb.pdf")

######################################################
if __name__ == "__main__":
	plot()
	#colorbar_only()
