import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import 'recuerdo.dart';

class RecuerdoDA {
  static Database? _db;

  Future<Database> get db async {
    _db ??= await initDb();
    return _db!;
  }

  Future<Database> initDb() async {
    final path = join(await getDatabasesPath(), 'recuerdos.db');
    return openDatabase(
      path,
      version: 1,
      onCreate: (Database db, int version) async {
        await db.execute('''
          CREATE TABLE recuerdos (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            descripcion TEXT,
            imagenUrl TEXT,
            latitud REAL,
            longitud REAL,
            favorito INTEGER,
            categoria TEXT,
            fechaRecuerdo TEXT
          )
        ''');
      },
    );
  }

  Future<void> insert(Recuerdo r) async {
    final database = await db;
    r.id = await getMaxId();
    await database.insert('recuerdos', r.toJson());
  }

  Future<void> update(Recuerdo r) async {
    final database = await db;
    await database.update('recuerdos', r.toJson(), where: 'id = ?', whereArgs: [r.id]);
  }

  Future<void> delete(int id) async {
    final database = await db;
    await database.delete('recuerdos', where: 'id = ?', whereArgs: [id]);
  }

  Future<List<Recuerdo>> getAll() async {
    final database = await db;
    final List<Map<String, dynamic>> maps = await database.query('recuerdos');
    return maps.map((e) => Recuerdo.fromJson(e)).toList();
  }

  Future<int> getMaxId() async {
    final database = await db;
    final res = await database.rawQuery('SELECT MAX(id) as id FROM recuerdos');
    return ((res.first['id'] as int?) ?? 0) + 1;
  }
}
