DESTDIR ?= /usr

PREFIXBIN=$(DESTDIR)/bin
PREFIXLIB=$(DESTDIR)/lib/pyglparchis
PREFIXSHARE=$(DESTDIR)/share/pyglparchis 

install:
	echo "Instalando en ${DESTDIR}"
	pylupdate4 pyglparchis.pro
	lrelease pyglparchis.pro
	pyuic4 ui/frmAbout.ui > ui/Ui_frmAbout.py 
	pyuic4 ui/frmMain.ui > ui/Ui_frmMain.py
	pyuic4 ui/wdgUserPanel.ui > ui/Ui_wdgUserPanel.py
	pyrcc4 images/glparchis.qrc > images/glparchis_rc.py
	install -o root -d $(PREFIXBIN)
	install -o root -d $(PREFIXLIB)
	install -o root -d $(PREFIXSHARE)                                                      
	install -m 755 -o root glparchis.py $(PREFIXBIN)/pyglparchis
	install -m 644 -o root datos.py $(PREFIXLIB)                
	install -m 644 -o root ui/*.py $(PREFIXLIB)                
	install -m 644 -o root images/*.py $(PREFIXLIB)
	install -m 644 -o root images/ficharoja.png $(PREFIXSHARE)
	install -m 644 -o root i18n/*.qm $(PREFIXSHARE)

uninstall:
	rm $(PREFIXBIN)/pyglparchis
	rm -Rf $(PREFIXLIB)
	rm -Rf $(PREFIXSHARE)



