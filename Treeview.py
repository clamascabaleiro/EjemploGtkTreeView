import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Fiestra(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo con Gtk.Treeview")
        self.set_default_size(400, 300)

        boxV = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)

        modelo = Gtk.ListStore(str,str,float,bool,int)
        modelo.append(["Hotel Melia" , "García Barbón 48", 75.38,True, 1])
        modelo.append(["Hotel Galeones", "Avda Madrid", 80.88 , False, 2])
        modelo.append(["Hotel Bahía", "Paseo as Avenidas 55", 60.38, True, 5])

        vista = Gtk.TreeView(model = modelo)
        boxV.pack_start (vista,True,True,0)

        celdaText = Gtk.CellRendererText()
        celdaText.set_property ("editable", False)
        columnaHotel = Gtk.TreeViewColumn ('Aloxamento', celdaText, text = 0)
        vista.append_column (columnaHotel)

        celdaDireccion = Gtk.CellRendererText()
        celdaDireccion.set_property("editable", True)
        celdaDireccion.connect("edited", self.on_celdaDireccion_edited,modelo)
        columnaDireccion = Gtk.TreeViewColumn('Direccion', celdaDireccion, text=1)
        vista.append_column(columnaDireccion)

        celdaOcupacion = Gtk.CellRendererProgress()
        columnaOcupacion = Gtk.TreeViewColumn('Ocupacion', celdaOcupacion, value=2)
        vista.append_column(columnaOcupacion)

        celdaCheck = Gtk.CellRendererToggle()
        celdaCheck.connect("toggled",self.on_celdaCheck_toggled ,modelo)
        columnaMascotas = Gtk.TreeViewColumn('Mascotas', celdaCheck, active=3)
        vista.append_column(columnaMascotas)
        #columnaMascotas.add_attribute(celdaCheck, "active",3)

        columnaCategoria = Gtk.TreeViewColumn('Categoria', celdaText, text=4)
        vista.append_column(columnaCategoria)

        boxH = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL)
        self.txtHotel = Gtk.Entry()
        self.txtDireccion = Gtk.Entry()
        self.txtOcupacion = Gtk.Entry()
        self.chkMascota = Gtk.CheckButton()
        self.cmbCategoria = Gtk.ComboBox()
        btnNovo = Gtk.Button("Novo")
        btnNovo.connect ("clicked" , self.on_btnNovo_clicked, modelo)

        boxH.pack_start(self.txtHotel,True,True,0)
        boxH.pack_start(self.txtDireccion, True, True, 0)
        boxH.pack_start(self.txtOcupacion, True, True, 0)
        boxH.pack_start(self.chkMascota, True, True, 0)
        boxH.pack_start(self.cmbCategoria, True, True, 0)
        boxH.pack_start(btnNovo, True, True, 0)
        boxV.pack_start(boxH,True,True,0)

        self.add(boxV)

        modeloCat = Gtk.ListStore(str,int)
        modeloCat.append(["*", 1])
        modeloCat.append(["**", 2])
        modeloCat.append(["***", 3])
        modeloCat.append(["****", 4])
        modeloCat.append(["*****", 5])
        self.cmbCategoria.set_model(modeloCat)
        self.cmbCategoria.pack_start(celdaText,True)
        self.cmbCategoria.add_attribute(celdaText,"text", 0)

        self.show_all()
        self.connect("destroy", Gtk.main_quit)

    def on_celdaCheck_toggled(self,control,fila,modelo):
        modelo [fila] [3] = not modelo [fila] [3]

    def on_celdaDireccion_edited(self,control,fila,texto,modelo):
        modelo [fila] [1] = texto

    def on_btnNovo_clicked(self,boton,modelo):
        modCat = self.cmbCategoria.get_model()
        indice = self.cmbCategoria.get_active_iter()
        modelo.append([self.txtHotel.get_text(),
                       self.txtDireccion.get_text(),
                       float(self.txtOcupacion.get_text()),
                       self.chkMascota.get_active(),
                       modCat [indice][1]])



if __name__ == "__main__":
    Fiestra()
    Gtk.main()
