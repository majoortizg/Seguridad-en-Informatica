import 'package:flutter/material.dart';
import 'recuerdo.dart';
import 'recuerdo_dba.dart';
import 'recuerdoDetails.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Recuerdos GPS',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.pink),
      ),
      home: const MyHomePage(title: 'Mis Recuerdos'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  final String title;
  const MyHomePage({super.key, required this.title});
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final RecuerdoDA _recuerdoDA = RecuerdoDA();
  List<Recuerdo> _recuerdos = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadRecuerdos();
  }

  Future<void> _loadRecuerdos() async {
    _recuerdos = await _recuerdoDA.getAll();
    setState(() => _isLoading = false);
  }

  void _addRecuerdo() async {
    final nuevo = Recuerdo();
    final result = await Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => AlbumDetallesView(recuerdo: nuevo)),
    );
    if (result != null) {
      await _recuerdoDA.insert(result);
      _loadRecuerdos();
    }
  }

  void _editRecuerdo(Recuerdo r) async {
    final result = await Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => AlbumDetallesView(recuerdo: r)),
    );
    if (result != null) {
      await _recuerdoDA.update(result);
      _loadRecuerdos();
    }
  }

  void _deleteRecuerdo(int id) async {
    await _recuerdoDA.delete(id);
    _loadRecuerdos();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.title), centerTitle: true),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : _recuerdos.isEmpty
          ? const Center(child: Text('No hay recuerdos guardados'))
          : ListView.builder(
        itemCount: _recuerdos.length,
        itemBuilder: (context, index) {
          final r = _recuerdos[index];
          return Card(
            margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
            child: ListTile(
              leading: r.imagenUrl.isNotEmpty
                  ? Image.network(r.imagenUrl, width: 60, fit: BoxFit.cover)
                  : const Icon(Icons.image_not_supported),
              title: Text(r.titulo),
              subtitle: Text('${r.descripcion}\nLat: ${r.latitud}, Long: ${r.longitud}'),
              isThreeLine: true,
              trailing: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  IconButton(icon: const Icon(Icons.edit), onPressed: () => _editRecuerdo(r)),
                  IconButton(icon: const Icon(Icons.delete), onPressed: () => _deleteRecuerdo(r.id)),

                ],
              ),
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _addRecuerdo,
        child: const Icon(Icons.add),
      ),
    );
  }
}
