"""
Estados y Municipios de México
"""

ESTADOS_MEXICO = [
    "Aguascalientes",
    "Baja California",
    "Baja California Sur",
    "Campeche",
    "Chiapas",
    "Chihuahua",
    "Ciudad de México",
    "Coahuila",
    "Colima",
    "Durango",
    "Guanajuato",
    "Guerrero",
    "Hidalgo",
    "Jalisco",
    "México",
    "Michoacán",
    "Morelos",
    "Nayarit",
    "Nuevo León",
    "Oaxaca",
    "Puebla",
    "Querétaro",
    "Quintana Roo",
    "San Luis Potosí",
    "Sinaloa",
    "Sonora",
    "Tabasco",
    "Tamaulipas",
    "Tlaxcala",
    "Veracruz",
    "Yucatán",
    "Zacatecas"
]

MUNICIPIOS_POR_ESTADO = {
    "Aguascalientes": [
        "Aguascalientes", "Asientos", "Calvillo", "Cosío", "Jesús María",
        "Pabellón de Arteaga", "Rincón de Romos", "San José de Gracia",
        "Tepezalá", "El Llano", "San Francisco de los Romo"
    ],
    "Baja California": [
        "Ensenada", "Mexicali", "Tecate", "Tijuana", "Playas de Rosarito",
        "San Quintín", "San Felipe"
    ],
    "Baja California Sur": [
        "Comondú", "Mulegé", "La Paz", "Los Cabos", "Loreto"
    ],
    "Campeche": [
        "Calkiní", "Campeche", "Carmen", "Champotón", "Hecelchakán",
        "Hopelchén", "Palizada", "Tenabo", "Escárcega", "Calakmul",
        "Candelaria", "Seybaplaya"
    ],
    "Chiapas": [
        "Tuxtla Gutiérrez", "San Cristóbal de las Casas", "Tapachula",
        "Comitán de Domínguez", "Chiapa de Corzo", "Palenque", "Tonalá",
        "San Juan Chamula", "Villaflores", "Ocosingo", "Arriaga"
    ],
    "Chihuahua": [
        "Chihuahua", "Juárez", "Cuauhtémoc", "Delicias", "Hidalgo del Parral",
        "Nuevo Casas Grandes", "Camargo", "Jiménez", "Bocoyna", "Guachochi",
        "Ojinaga", "Meoqui", "Saucillo"
    ],
    "Ciudad de México": [
        "Álvaro Obregón", "Azcapotzalco", "Benito Juárez", "Coyoacán",
        "Cuajimalpa de Morelos", "Cuauhtémoc", "Gustavo A. Madero",
        "Iztacalco", "Iztapalapa", "Magdalena Contreras", "Miguel Hidalgo",
        "Milpa Alta", "Tláhuac", "Tlalpan", "Venustiano Carranza", "Xochimilco"
    ],
    "Coahuila": [
        "Saltillo", "Torreón", "Monclova", "Piedras Negras", "Acuña",
        "Sabinas", "Parras", "San Pedro", "Frontera", "Matamoros",
        "Ramos Arizpe", "Múzquiz"
    ],
    "Colima": [
        "Colima", "Manzanillo", "Tecomán", "Villa de Álvarez", "Armería",
        "Comala", "Coquimatlán", "Cuauhtémoc", "Ixtlahuacán", "Minatitlán"
    ],
    "Durango": [
        "Durango", "Gómez Palacio", "Lerdo", "Santiago Papasquiaro",
        "El Oro", "Guadalupe Victoria", "Pueblo Nuevo", "Mezquital",
        "Nombre de Dios", "Cuencamé", "Mapimí"
    ],
    "Guanajuato": [
        "León", "Irapuato", "Celaya", "Salamanca", "Guanajuato",
        "San Miguel de Allende", "Silao", "Pénjamo", "San Francisco del Rincón",
        "Dolores Hidalgo", "Acámbaro", "San Luis de la Paz", "Valle de Santiago",
        "Cortazar", "Moroleón", "Salvatierra"
    ],
    "Guerrero": [
        "Acapulco", "Chilpancingo", "Iguala", "Zihuatanejo", "Taxco",
        "Chilapa", "Tlapa de Comonfort", "Ciudad Altamirano", "Arcelia",
        "Coyuca de Benítez", "Petatlán"
    ],
    "Hidalgo": [
        "Pachuca", "Tulancingo", "Tula de Allende", "Tepeji del Río",
        "Tizayuca", "Ixmiquilpan", "Actopan", "Huejutla", "Apan",
        "Mineral de la Reforma", "Zempoala", "Tepeapulco"
    ],
    "Jalisco": [
        "Guadalajara", "Zapopan", "Tlaquepaque", "Tonalá", "Tlajomulco",
        "Puerto Vallarta", "Lagos de Moreno", "Tepatitlán", "El Salto",
        "Zapotlanejo", "Ocotlán", "Arandas", "Tala", "Autlán", "La Barca"
    ],
    "México": [
        "Toluca", "Ecatepec", "Nezahualcóyotl", "Naucalpan", "Tlalnepantla",
        "Chimalhuacán", "Cuautitlán Izcalli", "Ixtapaluca", "Atizapán de Zaragoza",
        "Valle de Chalco", "Nicolás Romero", "Tultitlán", "Texcoco",
        "Chalco", "Metepec", "Coacalco", "Los Reyes La Paz"
    ],
    "Michoacán": [
        "Morelia", "Uruapan", "Zamora", "Lázaro Cárdenas", "Apatzingán",
        "Zitácuaro", "Pátzcuaro", "La Piedad", "Sahuayo", "Hidalgo",
        "Tacámbaro", "Los Reyes", "Puruándiro"
    ],
    "Morelos": [
        "Cuernavaca", "Cuautla", "Jiutepec", "Temixco", "Emiliano Zapata",
        "Yautepec", "Jojutla", "Xochitepec", "Zacatepec", "Puente de Ixtla"
    ],
    "Nayarit": [
        "Tepic", "Bahía de Banderas", "Santiago Ixcuintla", "Compostela",
        "Ixtlán del Río", "Tuxpan", "San Blas", "Acaponeta", "Tecuala"
    ],
    "Nuevo León": [
        "Monterrey", "Guadalupe", "San Nicolás de los Garza", "Apodaca",
        "San Pedro Garza García", "Escobedo", "Santa Catarina", "García",
        "Cadereyta Jiménez", "Linares", "Montemorelos", "Sabinas Hidalgo"
    ],
    "Oaxaca": [
        "Oaxaca de Juárez", "Salina Cruz", "Juchitán", "Tuxtepec",
        "Huajuapan de León", "Puerto Escondido", "Tehuantepec",
        "Santa Cruz Xoxocotlán", "Pinotepa Nacional", "Santa Lucía del Camino"
    ],
    "Puebla": [
        "Puebla", "Tehuacán", "San Martín Texmelucan", "Atlixco",
        "San Pedro Cholula", "Teziutlán", "Cuautlancingo", "Amozoc",
        "Izúcar de Matamoros", "Huauchinango", "Zacatlán", "San Andrés Cholula"
    ],
    "Querétaro": [
        "Querétaro", "San Juan del Río", "Corregidora", "El Marqués",
        "Tequisquiapan", "Cadereyta de Montes", "Pedro Escobedo",
        "Jalpan de Serra", "Ezequiel Montes"
    ],
    "Quintana Roo": [
        "Cancún", "Playa del Carmen", "Chetumal", "Cozumel", "Tulum",
        "Felipe Carrillo Puerto", "Bacalar", "Isla Mujeres", "José María Morelos"
    ],
    "San Luis Potosí": [
        "San Luis Potosí", "Soledad de Graciano Sánchez", "Ciudad Valles",
        "Matehuala", "Rioverde", "Tamazunchale", "Cárdenas", "Ebano",
        "Ciudad Fernández", "Tamuín"
    ],
    "Sinaloa": [
        "Culiacán", "Mazatlán", "Los Mochis", "Guasave", "Guamúchil",
        "Navolato", "El Fuerte", "Escuinapa", "Ahome", "La Cruz"
    ],
    "Sonora": [
        "Hermosillo", "Ciudad Obregón", "Nogales", "San Luis Río Colorado",
        "Navojoa", "Guaymas", "Caborca", "Agua Prieta", "Cananea",
        "Puerto Peñasco", "Empalme"
    ],
    "Tabasco": [
        "Villahermosa", "Cárdenas", "Comalcalco", "Huimanguillo",
        "Macuspana", "Paraíso", "Cunduacán", "Teapa", "Emiliano Zapata",
        "Balancán", "Tenosique"
    ],
    "Tamaulipas": [
        "Reynosa", "Matamoros", "Nuevo Laredo", "Tampico", "Victoria",
        "Altamira", "Ciudad Madero", "Río Bravo", "Mante", "Valle Hermoso"
    ],
    "Tlaxcala": [
        "Tlaxcala", "Apizaco", "Huamantla", "Chiautempan", "Zacatelco",
        "San Pablo del Monte", "Santa Cruz Tlaxcala", "Calpulalpan",
        "Tlaxco", "Panotla"
    ],
    "Veracruz": [
        "Veracruz", "Xalapa", "Coatzacoalcos", "Poza Rica", "Córdoba",
        "Minatitlán", "Orizaba", "Boca del Río", "Tuxpan", "Papantla",
        "Martínez de la Torre", "San Andrés Tuxtla", "Río Blanco"
    ],
    "Yucatán": [
        "Mérida", "Kanasín", "Valladolid", "Tizimín", "Progreso",
        "Umán", "Ticul", "Motul", "Tekax", "Hunucmá", "Maxcanú"
    ],
    "Zacatecas": [
        "Zacatecas", "Fresnillo", "Guadalupe", "Jerez", "Río Grande",
        "Sombrerete", "Loreto", "Pinos", "Calera", "Víctor Rosales"
    ]
}

# Listas de opciones adicionales
TIPOS_MONEDA = ["MXN", "USD", "EUR"]

USOS_VEHICULO = [
    "Particular",
    "Comercial",
    "Público",
    "Carga",
    "Servicio",
    "Taxi",
    "Uber/Didi",
    "Alquiler"
]

SERVICIOS_VEHICULO = [
    "Privado",
    "Público Federal",
    "Público Estatal",
    "Público Municipal",
    "Mercantil",
    "Transporte de Pasajeros",
    "Transporte de Carga"
]

FORMAS_PAGO = [
    "Mensual",
    "Bimestral", 
    "Trimestral",
    "Cuatrimestral",
    "Semestral",
    "Anual",
    "Contado"
]

# Mapeo de forma de pago a meses
MESES_POR_FORMA_PAGO = {
    "Mensual": 1,
    "Bimestral": 2,
    "Trimestral": 3,
    "Cuatrimestral": 4,
    "Semestral": 6,
    "Anual": 12,
    "Contado": 0
}
