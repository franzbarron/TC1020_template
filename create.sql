CREATE TABLE Departamento(
    numero      int             AUTO_INCREMENT,
    nombre      varchar(255)    NOT NULL,
    oficina     varchar(10)     NOT NULL,
    telefono    varchar(50)     NOT NULL,
    PRIMARY KEY(numero)
);

CREATE TABLE Profesor(
    pID     char(9),
    nombre  varchar(255)    NOT NULL,
    PRIMARY KEY(pID)
);

CREATE TABLE Alumno(
    matricula       char(9),
    curp            char(18)        NOT NULL,
    nombre          varchar(255)    NOT NULL,
    sexo            char(1)         NOT NULL,
    bDate           date            NOT NULL,
    telefono        varchar(50),
    celular         varchar(50),
    direccion       varchar(255)    NOT NULL,
    departamento    int             NOT NULL,
    carrera         varchar(4)      NOT NULL,
    CHECK(sexo IN ('H', 'M')),
    FOREIGN KEY(carrera)        REFERENCES Carreras(inicialismo),
    FOREIGN KEY(departamento)   REFERENCES Departamento(numero),
    PRIMARY KEY(matricula),
    UNIQUE(curp)
);

CREATE TABLE Curso(
    numero          varchar(10),
    nombre          varchar(255)    NOT NULL,
    descripcion     text            NOT NULL,
    horasPorSemana  int(2)          NOT NULL,
    semestre        int(1)          NOT NULL,
    departamento    int             NOT NULL,
    FOREIGN KEY(departamento) REFERENCES Departamento(numero),
    PRIMARY KEY(numero)
);

CREATE TABLE Grupo(
    numero      int(3),
    semestre    char(2),
    anio        year,
    curso       varchar(10),
    profesor    char(9)         NOT NULL,
    CHECK(semestre IN ('EM', 'AD')),
    FOREIGN KEY(curso)      REFERENCES Curso(numero),
    FOREIGN KEY(profesor)   REFERENCES Profesor(pID),
    PRIMARY KEY(numero, semestre, anio, curso)
);

CREATE TABLE Ecoas(
    profesor        char(9),
    grupo           int(3),
    calificacion    int(3),
    CHECK(calificacion <= 100),
    CONSTRAINT PK_Ecoas PRIMARY KEY(profesor, grupo),
    FOREIGN KEY(profesor)   REFERENCES Profesor(pID),
    FOREIGN KEY(grupo)      REFERENCES Grupo(numero)
);

CREATE TABLE CursosImpartidos(
    profesor    char(9),
    curso       varchar(10),
    semestre    char(2),
    anio        year,
    CHECK(semestre IN ('EM', 'AD')),
    FOREIGN KEY(curso)      REFERENCES Curso(numero),
    FOREIGN KEY(profesor)   REFERENCES Profesor(pID),
    CONSTRAINT pk_ci PRIMARY KEY(profesor, curso, semestre, anio)
);

CREATE TABLE CursosCursados(
    alumno          char(9),
    curso           varchar(10),
    semestre        char(2),
    anio            year,
    calificacion    int(3),
    CHECK(calificacion <= 100),
    CHECK(semestre IN('EM', 'AD')),
    FOREIGN KEY(alumno) REFERENCES Alumno(matricula),
    FOREIGN KEY(curso)  REFERENCES Curso(numero),
    CONSTRAINT pk_cc    PRIMARY KEY(alumno, curso, semestre, anio)
);

CREATE TABLE PerteneceGrupo(
    alumno      char(9),
    curso       varchar(10),
    grupo       int(3),
    semestre    char(2) NOT NULL,
    anio        year    NOT NULL,
    FOREIGN KEY(alumno) REFERENCES Alumno(matricula),
    FOREIGN KEY(curso)  REFERENCES Curso(numero),
    FOREIGN KEY(grupo)  REFERENCES Grupo(numero),
    CONSTRAINT  pk_pg   PRIMARY KEY(alumno, grupo, curso)
);