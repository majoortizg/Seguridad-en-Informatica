class Recuerdo {
  int id;
  String titulo;
  String descripcion;
  String imagenUrl;
  double latitud;
  double longitud;
  bool favorito;
  String categoria;
  DateTime? fechaRecuerdo;

  Recuerdo({
    this.id = 0,
    this.titulo = '',
    this.descripcion = '',
    this.imagenUrl = '',
    this.latitud = 0.0,
    this.longitud = 0.0,
    this.favorito = false,
    this.categoria = 'Sin especificar',
    this.fechaRecuerdo,
  });

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'titulo': titulo,
      'descripcion': descripcion,
      'imagenUrl': imagenUrl,
      'latitud': latitud,
      'longitud': longitud,
      'favorito': favorito ? 1 : 0,
      'categoria': categoria,
      'fechaRecuerdo': fechaRecuerdo?.toIso8601String(),
    };
  }

  factory Recuerdo.fromJson(Map<String, dynamic> json) {
    return Recuerdo(
      id: json['id'] ?? 0,
      titulo: json['titulo'] ?? '',
      descripcion: json['descripcion'] ?? '',
      imagenUrl: json['imagenUrl'] ?? '',
      latitud: json['latitud'] ?? 0.0,
      longitud: json['longitud'] ?? 0.0,
      favorito: (json['favorito'] ?? 0) == 1,
      categoria: json['categoria'] ?? 'Sin especificar',
      fechaRecuerdo: json['fechaRecuerdo'] != null
          ? DateTime.tryParse(json['fechaRecuerdo'])
          : null,
    );
  }
}
