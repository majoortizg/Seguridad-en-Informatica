import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'recuerdo.dart';

class AlbumDetallesView extends StatefulWidget {
  final Recuerdo recuerdo;
  const AlbumDetallesView({super.key, required this.recuerdo});

  @override
  State<AlbumDetallesView> createState() => _AlbumDetallesViewState();
}

class _AlbumDetallesViewState extends State<AlbumDetallesView> {
  late Recuerdo recuerdo;
  final TextEditingController ctrlLink = TextEditingController();

  @override
  void initState() {
    super.initState();
    recuerdo = widget.recuerdo;
    ctrlLink.text = recuerdo.imagenUrl;
    _getLocation();
  }

  Future<void> _getLocation() async {
    LocationPermission permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied) {
      permission = await Geolocator.requestPermission();
    }
    if (permission == LocationPermission.deniedForever) return;

    Position pos = await Geolocator.getCurrentPosition();
    setState(() {
      recuerdo.latitud = pos.latitude;
      recuerdo.longitud = pos.longitude;
    });
  }

  Future<void> _selectDate() async {
    final DateTime? picked = await showDatePicker(
      context: context,
      initialDate: recuerdo.fechaRecuerdo ?? DateTime.now(),
      firstDate: DateTime(1960),
      lastDate: DateTime(2029),
    );
    if (picked != null) {
      setState(() {
        recuerdo.fechaRecuerdo = picked;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(recuerdo.titulo.isEmpty ? 'Nuevo Recuerdo' : recuerdo.titulo)),
      body: ListView(
        padding: const EdgeInsets.all(10),
        children: [
          TextFormField(
            initialValue: recuerdo.titulo,
            decoration: const InputDecoration(labelText: 'Título'),
            onChanged: (v) => recuerdo.titulo = v,
          ),
          TextFormField(
            initialValue: recuerdo.descripcion,
            decoration: const InputDecoration(labelText: 'Descripción'),
            onChanged: (v) => recuerdo.descripcion = v,
          ),
          SizedBox(
            height: 200,
            width: 200,
            child: Image.network(
                recuerdo.imagenUrl,
                fit: BoxFit.cover
            ),
          ),
          TextFormField(
            controller: ctrlLink,
            //initialValue: album.imageUrl,
            decoration: InputDecoration(
              labelText: 'Link imagen',
              suffixIcon: IconButton(
                onPressed: () {
                  setState(() {
                    recuerdo.imagenUrl = '';
                    ctrlLink.text = '';
                  }
                  );
                },
                icon: Icon(Icons.clear),
              ),
            ),
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Por favor ingrese el link de la imagen';
              }
              return null;
            },
            onChanged: (value) {
              setState(() {
                recuerdo.imagenUrl = value;
              }
              );
            },

          ),
          /*TextFormField(
            controller: ctrlLink,
            decoration: const InputDecoration(labelText: 'URL Imagen'),
            onChanged: (v) => recuerdo.imagenUrl = v,
          ),*/
          ListTile(
            leading: const Icon(Icons.calendar_today),
            title: const Text('Fecha del Recuerdo'),
            subtitle: Text(recuerdo.fechaRecuerdo?.toString() ?? 'No seleccionada'),
            onTap: _selectDate,
          ),
          ListTile(
            leading: const Icon(Icons.location_on),
            title: const Text('Ubicación GPS'),
            subtitle: Text('Lat: ${recuerdo.latitud}, Long: ${recuerdo.longitud}'),
          ),
          CheckboxListTile(
            value: recuerdo.favorito,
            title: const Text('Favorito'),
            onChanged: (v) => setState(() => recuerdo.favorito = v ?? false),
          ),
          DropdownButton<String>(
            value: recuerdo.categoria,
            onChanged: (v) => setState(() => recuerdo.categoria = v!),
            items: ["En Pareja", "Solo", "Amigos", "Familia", "Viajes", "Sin especificar"]
                .map((e) => DropdownMenuItem(value: e, child: Text(e)))
                .toList(),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => Navigator.pop(context, recuerdo),
        child: const Icon(Icons.save),
      ),
    );
  }
}
