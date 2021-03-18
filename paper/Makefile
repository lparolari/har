# The latex source filename
MAINFILE?=main

# The build strategy
BUILD_STRATEGY?=pdf3

# The source folder
SRC?=`pwd`

# Main recipe
# ===========

${MAINFILE}.pdf: compile


# Build pdf recipes
# =================

compile: pdf

pdf: ${BUILD_STRATEGY}

pdf1: pdflatex bib pdflatex
pdf2: dxjoke-tectonic-docker
pdf3: blang-latex-docker

clean: clear
clear:
	rm -f *.pdf *.aux *.fdb_latexmk *.fls *.log *.out *.pdf *.toc

# Specific recipes
# ================

# pdf 1
# -----

pdflatex:
	pdflatex ${MAINFILE}.tex
bib:
	biber ${MAINFILE}

# pdf 2
# -----

dxjoke-tectonic-docker:
	docker pull dxjoke/tectonic-docker
	docker run --mount src=${SRC},target=/usr/src/tex,type=bind dxjoke/tectonic-docker /bin/sh -c "tectonic --keep-intermediates --reruns 0 ${MAINFILE}.tex;"

# pdf 3
# -----

blang-latex-docker: latexdockercmd.sh
	./latexdockercmd.sh latexmk -cd -f -interaction=batchmode -pdf ${MAINFILE}.tex

blang-latex-docker-debug:
	./latexdockercmd.sh pdflatex ${MAINFILE}.tex

latexdockercmd.sh:
	wget https://raw.githubusercontent.com/blang/latex-docker/master/latexdockercmd.sh
	chmod +x latexdockercmd.sh
