-- DEPARTAMENTOS
INSERT INTO
  Departamento (nombre, oficina, telefono)
VALUES
  ('Bioingeniería', 'A1-103', '+529789888349');
INSERT INTO
  Departamento (nombre, oficina, telefono)
VALUES
  (
    'Tecnologías Sostenibles y Civil',
    'A1-127',
    '+528180466131'
  );
INSERT INTO
  Departamento (nombre, oficina, telefono)
VALUES
  ('Ciencias', 'A7-211', '+528180285440');
INSERT INTO
  Departamento (nombre, oficina, telefono)
VALUES
  ('Computación', 'A2-217', '+528180911200');
-- PROFESORES
INSERT INTO
  Profesor
VALUES('L00000001', 'Elsy Genny Molina Solis');
INSERT INTO
  Profesor
VALUES('L00000002', 'Mónica Delgado');
INSERT INTO
  Profesor
VALUES('L00000003', 'Hilda Lizette Menchaca Torre');
INSERT INTO
  Profesor
VALUES('L00000004', 'Ana Yael Vanoye Garcia');
INSERT INTO
  Profesor
VALUES('L00000005', 'Emma Ines Cortes Soriano');
INSERT INTO
  Profesor
VALUES('L00000006', 'Maria Magdalena Morales');
INSERT INTO
  Profesor
VALUES('L00000007', 'Raúl Yusta G');
INSERT INTO
  Profesor
VALUES('L00000009', 'Claudio Alberto Patin Torres');
INSERT INTO
  Profesor
VALUES('L00000010', 'Carlos Astengo Noguez');
INSERT INTO
  Profesor
VALUES('L00000011', 'Salvador Mancilla Hernandez');
INSERT INTO
  Profesor
VALUES('L00000012', 'Isabel Cristina Elizondo Ordonez');
INSERT INTO
  Profesor
VALUES('L00000013', 'Jorge Eugenio de la Garza Becerra');
INSERT INTO
  Profesor
VALUES('L00000014', 'Carlos Manuel Hinojosa Espinosa');
INSERT INTO
  Profesor
VALUES('L00000015', 'Rodolfo Rodriguez y Masegosa');
INSERT INTO
  Profesor
VALUES('L00000016', 'Flavio Fernando Contreras Torres');
INSERT INTO
  Profesor
VALUES('L00000017', 'Oscar Arturo Garza Castañón');
INSERT INTO
  Profesor
VALUES('L00000018', 'Ramon Felipe Brena Pinero');
INSERT INTO
  Profesor
VALUES('L00000019', 'Etna Aurora Rojas');
INSERT INTO
  Profesor
VALUES('L00000020', 'Elda Guadalupe Quiroga González');
INSERT INTO
  Profesor
VALUES('L00000021', 'María Dhelma Rendón Saldívar');
INSERT INTO
  Profesor
VALUES('L00000022', 'Francisco Javier Sierra Valdez');
INSERT INTO
  Profesor
VALUES('L00000023', 'Santa Esmeralda Tejeda Torres');
INSERT INTO
  Profesor
VALUES(
    'L00000024',
    'Maria Guadalupe Roque Dias de Leon'
  );
--ALUMNOS
INSERT INTO
  Alumno
VALUES(
    'A00821358',
    'SAFJ000820HASLRRX9',
    'Jairo Salas Frías',
    'H',
    '2000-08-20',
    '+529203149866',
    '+5215169780571',
    'Hartland Avenue 829 Jarvisville 64183 Monterrey, Nuevo León',(
      SELECT
        numero
      FROM
        Departamento
      WHERE
        nombre = 'Bioingeniería'
    ),
    (
      SELECT
        inicialismo
      FROM
        Carreras
      WHERE
        inicialismo = 'IDS'
    )
  );
INSERT INTO
  Alumno
VALUES(
    'A01195681',
    'CABX960731MQTVLN23',
    'Xenia Blanco Cavazos',
    'M',
    '1996-07-31',
    '+528183324958',
    '+5218180527517',
    'Avenida Generalísimo 56 Rúa do Paseo 64294 Monterrey, Nuevo León',(
      SELECT
        numero
      FROM
        Departamento
      WHERE
        nombre = 'Computación'
    ),
    (
      SELECT
        inicialismo
      FROM
        Carreras
      WHERE
        inicialismo = 'ITC'
    )
  );
-- CURSOS
INSERT INTO
  Curso
VALUES(
    'BT1009',
    'Biología y desarrollo sustentable',
    'Al finalizar el curso el alumno serácapaz de comprender los procesos básicos en los que se fundamenta la vida, desde el nivel celular hasta el ecosistémico, proporcionandole las bases indispensables en el diseño de programas de desarrollo sostenible.',
    '3',
    '1',
    (
      SELECT
        numero
      FROM
        Departamento
      WHERE
        nombre = 'Bioingeniería'
    )
  );
INSERT INTO
  Curso
VALUES(
    'DS1005',
    'Cambio climático y uso de energía',
    'Al finalizar el curso, el alumno serácapaz de entender el papel que tienen en la atmósfera terrestre los compuestos gaseosos de baja concentración en su relación con el potencial de calentamiento global, asícomo el potencial para acidificación de los océanos y la destrucción de la capa de ozono, explicar con base en principios básicos la función del bióxido de carbono y otros gases de invernadero y su potencial para reforzar la re-radiación atmosférica, asícomo el potencial de acidificación oceánica del bióxido de carbono y su vínculo en la alteración de los ecosistemas marinos, entender y explicar los principios físicos básicos de las fuentes renovables de energía como son los colectores solares, los sistemas fotovoltaicos, las mareas y el oleaje, el uso del viento; asícomo la disponibilidad energética en la biomasa de residuos agrícolas y forestales, asícomo de los elementos pasivos en construcciones y vincular los principios básicos de energía renovable con las tecnologías pertinentes para la futura disciplina profesional del estudiante y conocer los impactos del cambio climático y las estrategias para su mitigación y adaptación.',
    '3',
    '1',
    (
      SELECT
        numero
      FROM
        Departamento
      WHERE
        nombre = 'Tecnologías Sostenibles y Civil'
    )
  );
INSERT INTO
  Curso
VALUES(
    'F1002',
    'Física I',
    'Al finalizar el alumno serácapaz de aplicar conceptos físicos y matemáticos en la cinemática y dinámica lineal y angular empleando un lenguaje vectorial y aplicar los conceptos de las leyes de la Física para proponer soluciones a escenarios que involucran partículas en movimiento y/u objetos en rotación.',
    '4',
    '1',
    (
      SELECT
        numero
      FROM
        Departamento
      WHERE
        nombre = 'Ciencias'
    )
  );
INSERT INTO
  Curso
VALUES(
    'MA1015',
    'Matemáticas I',
    'Al final del curso, el alumno serácapaz de reconocer en situaciones reales la variación de una magnitud con respecto a otra, y representar matemáticamente la relación entre ellas y analizar el comportamiento de la magnitud de estudio utilizando las herramientas del cálculo diferencial.',
    '3',
    '1',
    (
      SELECT
        numero
      FROM
        Departamento
      WHERE
        nombre = 'Ciencias'
    )
  );
INSERT INTO
  Curso
VALUES(
    'TC1003',
    'Matemáticas discretas',
    'Al finalizar el curso, el alumno serácapaz de: razonar de manera rigurosa y formal usando las herramientas que le da la lógica formal, usar la inducción como método de razonamiento y demostración y usar los grafos como medio de modelar estructuras de datos.',
    '3',
    '1',
    (
      SELECT
        numero
      FROM
        Departamento
      WHERE
        nombre = 'Computación'
    )
  );
INSERT INTO
  Curso
VALUES(
    'TC1014',
    'Fundamentos de programación',
    'Al finalizar este curso el alumno sea capaz de aplicar la lógica para generar algoritmos que den solución a problemas de ingeniería.',
    '3',
    '1',
    (
      SELECT
        numero
      FROM
        Departamento
      WHERE
        nombre = 'Computación'
    )
  );
INSERT INTO
  Curso
VALUES(
    'TC1022',
    'Introducción a la ingeniería en tecnologías computacionales',
    'Al finalizar el curso el alumno conocerálas características de un egresado de la carrera en la que estáinscrito, sus competencias, su campo laboral y de desarrollo profesional. Asimismo, conocerála estructura organizacional del Tecnológico de Monterrey y sus principales reglamentos.',
    '3',
    '1',
    (
      SELECT
        numero
      FROM
        Departamento
      WHERE
        nombre = 'Computación'
    )
  );
-- GRUPOS
INSERT INTO
  Grupo
VALUES(
    1,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'BT1009'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000001'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '1'
    )
  );
INSERT INTO
  Grupo
VALUES(
    1,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'DS1005'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000002'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '2'
    )
  );
INSERT INTO
  Grupo
VALUES(
    2,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'DS1005'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000003'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '3'
    )
  );
INSERT INTO
  Grupo
VALUES(
    3,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'DS1005'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000004'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '4'
    )
  );
INSERT INTO
  Grupo
VALUES(
    4,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'DS1005'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000004'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '5'
    )
  );
INSERT INTO
  Grupo
VALUES(
    5,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'DS1005'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000005'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '6'
    )
  );
INSERT INTO
  Grupo
VALUES(
    6,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'DS1005'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000006'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '7'
    )
  );
INSERT INTO
  Grupo
VALUES(
    7,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'DS1005'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000007'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '8'
    )
  );
INSERT INTO
  Grupo
VALUES(
    8,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'DS1005'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000007'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '9'
    )
  );
INSERT INTO
  Grupo
VALUES(
    1,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'F1002'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000013'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '10'
    )
  );
INSERT INTO
  Grupo
VALUES(
    2,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'F1002'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000014'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '11'
    )
  );
INSERT INTO
  Grupo
VALUES(
    3,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'F1002'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000022'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '12'
    )
  );
INSERT INTO
  Grupo
VALUES(
    4,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'F1002'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000015'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '13'
    )
  );
INSERT INTO
  Grupo
VALUES(
    5,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'F1002'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000023'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '14'
    )
  );
INSERT INTO
  Grupo
VALUES(
    6,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'F1002'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000016'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '15'
    )
  );
INSERT INTO
  Grupo
VALUES(
    7,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'F1002'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000015'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '16'
    )
  );
INSERT INTO
  Grupo
VALUES(
    8,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'F1002'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000014'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '17'
    )
  );
INSERT INTO
  Grupo
VALUES(
    9,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'F1002'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000017'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '18'
    )
  );
INSERT INTO
  Grupo
VALUES(
    1,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'MA1015'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000009'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '19'
    )
  );
INSERT INTO
  Grupo
VALUES(
    2,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'MA1015'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000010'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '20'
    )
  );
INSERT INTO
  Grupo
VALUES(
    3,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'MA1015'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000011'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '21'
    )
  );
INSERT INTO
  Grupo
VALUES(
    4,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'MA1015'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000021'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '22'
    )
  );
INSERT INTO
  Grupo
VALUES(
    5,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'MA1015'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000021'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '23'
    )
  );
INSERT INTO
  Grupo
VALUES(
    6,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'MA1015'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000012'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '24'
    )
  );
INSERT INTO
  Grupo
VALUES(
    1,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'TC1003'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000018'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '25'
    )
  );
INSERT INTO
  Grupo
VALUES(
    1,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'TC1014'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000024'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '26'
    )
  );
INSERT INTO
  Grupo
VALUES(
    2,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'TC1014'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000019'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '27'
    )
  );
INSERT INTO
  Grupo
VALUES(
    1,
    'EM',
    2019,
    (
      SELECT
        numero
      FROM
        Curso
      WHERE
        numero = 'TC1022'
    ),
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000020'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '28'
    )
  );
-- ECOAS
INSERT INTO
  Ecoas
VALUES
  (
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000017'
    ),
    (
      SELECT
        numero
      FROM
        Grupo
      WHERE
        numero = '9'
        AND profesor = 'L00000017'
        AND semestre = 'EM'
        AND anio = '2019'
        AND curso = 'F1002'
    ),
    81
  );
INSERT INTO
  Ecoas
VALUES
  (
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000020'
    ),
    (
      SELECT
        numero
      FROM
        Grupo
      WHERE
        numero = '1'
        AND profesor = 'L00000020'
        AND semestre = 'EM'
        AND anio = '2019'
        AND curso = 'TC1022'
    ),
    100
  );
-- PERTENECE GRUPO
INSERT INTO
  PerteneceGrupo
VALUES(
    (
      SELECT
        matricula
      FROM
        alumno
      WHERE
        matricula = 'A00821358'
    ),
    (
      SELECT
        numero
      FROM
        curso
      WHERE
        numero = 'BT1009'
    ),
    (
      SELECT
        numero
      FROM
        grupo
      WHERE
        numero = '1'
        AND semestre = 'EM'
        AND anio = '2019'
        AND curso = 'BT1009'
    ),
    'EM',
    '2019'
  );
INSERT INTO
  PerteneceGrupo
VALUES(
    (
      SELECT
        matricula
      FROM
        alumno
      WHERE
        matricula = 'A01195681'
    ),
    (
      SELECT
        numero
      FROM
        curso
      WHERE
        numero = 'TC1003'
    ),
    (
      SELECT
        numero
      FROM
        grupo
      WHERE
        numero = '1'
        AND semestre = 'EM'
        AND anio = '2019'
        AND curso = 'TC1003'
    ),
    'EM',
    '2019'
  );
INSERT INTO
  PerteneceGrupo
VALUES(
    (
      SELECT
        matricula
      FROM
        alumno
      WHERE
        matricula = 'A01195681'
    ),
    (
      SELECT
        numero
      FROM
        curso
      WHERE
        numero = 'TC1022'
    ),
    (
      SELECT
        numero
      FROM
        grupo
      WHERE
        numero = '1'
        AND semestre = 'EM'
        AND anio = '2019'
        AND curso = 'TC1022'
    ),
    'EM',
    '2019'
  );
INSERT INTO
  PerteneceGrupo
VALUES(
    (
      SELECT
        matricula
      FROM
        alumno
      WHERE
        matricula = 'A01195681'
    ),
    (
      SELECT
        numero
      FROM
        curso
      WHERE
        numero = 'TC1014'
    ),
    (
      SELECT
        numero
      FROM
        grupo
      WHERE
        numero = '2'
        AND semestre = 'EM'
        AND anio = '2019'
        AND curso = 'TC1014'
    ),
    'EM',
    '2019'
  );
-- Libres
INSERT INTO
  Libre
VALUES(
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000001'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '1'
    )
  );
INSERT INTO
  Libre
VALUES(
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000001'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '3'
    )
  );
INSERT INTO
  Libre
VALUES(
    (
      SELECT
        pID
      FROM
        Profesor
      WHERE
        pID = 'L00000014'
    ),
    (
      SELECT
        id
      FROM
        Horario
      WHERE
        id = '6'
    )
  );