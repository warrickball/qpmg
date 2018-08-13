====
qpmg
====

::

  usage: qpmg [-h] [-x X [X ...]] [-y Y [Y ...]] [--xlabel XLABEL [XLABEL ...]]
              [--ylabel YLABEL [YLABEL ...]] [--legend LEGEND [LEGEND ...]]
              [--style STYLE] [--title TITLE [TITLE ...]]
              [--style-file STYLE_FILE]
              filenames [filenames ...]

``qpmg`` is a simple Python script to quickly inspect output that adheres to the
format used by MESA's profiles and histories and GYRE's summaries and mode
files. While ``qpmg`` provides some options, it's intended for quick inspection
rather than publication-quality plots. To see the list of available columns in
a file, run ``qpmg`` on a given file. The defaults will cause an error that
displays the available columns.

positional arguments: ``filenames``

optional arguments:

-h, --help              show this help message and exit
-x X, -y Y              Column(s) to use for the x and y variables. The code
                        loops through however many x and y keys you give
                        (inner loop over x, outer loop over y) but most of the
                        time you probably only want one x variable.
--xlabel XLABEL, --ylabel YLABEL    Overrides the axis label with the given string.
                        Accepts spaces. i.e. 'effective temperature' is OK.
                        Default is to use the first argument of -x/-y.
--legend LABELS         If 'auto', add a legend using the filenames as keys.
                        Otherwise, use the arguments as a list of keys.
                        Default is no legend.
--style STYLE           .
--title TITLE           Adds the given title to the plot. Accepts spaces. i.e.
                        'my plot' is OK. Default is no title.
--style-file STYLE_FILE         Specifies a matplotlib style file to load.

Installation
------------

``qpmg`` is available through ``pip``:

::
   
  pip install qpmg

You can also clone this GitHub repo:

::
   
  git clone https://github.com/warrickball/qpmg.git
  cd qpmg
  pip install -e .

or similar.

Finally, the program is entirely constrained in the script ``qpmg``,
so you can download this one file and use it as you please.  For
example, I keep ``$HOME/.local/bin`` in my ``$PATH`` variable, so I
might get the latest version of the script with

::

  wget https://raw.githubusercontent.com/warrickball/qpmg/master/qpmg -O $HOME/.local/bin
