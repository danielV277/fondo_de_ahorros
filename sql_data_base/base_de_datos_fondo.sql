create table integrantes(
	numero_id varchar(10) primary key,
	tipo_id char (2),
	nombres varchar(50),
	apellidos varchar(50),
	telefono char(10),
	correo varchar(50),
	direccion varchar(80),
    barrio varchar(60),
	fecha_nacimiento date,
	fecha_registro date default CURRENT_TIMESTAMP
)

alter table integrantes add constraint chk_tipo_id check (tipo_id in ('CC','TI'))

create table administradores(
	numero_id varchar(10),
	correo varchar(50) unique,
	contraseña text,
    foreign key(numero_id) references integrantes(numero_id)
)

create EXTENSION if not exists pgcrypto

INSERT INTO administradores(numero_id,correo,contraseña)
VALUES ('1000000001','juan.perez@example.com' ,crypt('1234', gen_salt('bf')));

SELECT * FROM administradores WHERE correo = 'juan.perez@example.com'
AND contraseña = crypt('1234', contraseña);

create table ahorros(
	numero_id varchar(10),
	numero_de_aportes int,
	ahorros_totales numeric(15,2),
	foreign key(numero_id) references integrantes(numero_id)
)

create table registro_aportes(
	id_registro varchar(12) primary key,
	id_integrante varchar(10) references integrantes(numero_id),
	tipo char(2),
	valor int
)

ALTER TABLE registro_aportes
ADD COLUMN fecha_registo TIMESTAMP DEFAULT current_timestamp;

CREATE OR REPLACE FUNCTION insertar_ahorros_nuevo_integrante()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO ahorros
    VALUES (NEW.numero_id,0,0) 
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER insertar_ahorros_nuevo_integrante_trigger
AFTER INSERT ON integrantes
FOR EACH ROW
EXECUTE FUNCTION insertar_ahorros_nuevo_integrante();


CREATE OR REPLACE FUNCTION actualizar_ahorros()
RETURNS TRIGGER AS $$
BEGIN
    -- Incrementar el número de aportes en 1
    UPDATE ahorros
    SET numero_de_aportes = numero_de_aportes + 1,
        ahorros_totales = ahorros_totales + NEW.valor  -- Acumular el valor del aporte
    WHERE numero_id = NEW.id_integrante;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER actualizar_ahorros_trigger
AFTER INSERT ON registro_aportes
FOR EACH ROW
EXECUTE FUNCTION actualizar_ahorros();

--poblamiento de prueba

INSERT INTO integrantes (numero_id, tipo_id, nombres, apellidos, telefono, correo, direccion, barrio, fecha_nacimiento)
VALUES 
('1000000001', 'CC', 'Juan Carlos', 'Pérez López', '3200000001', 'juan.perez@example.com', 'Calle 1 # 2-3', 'Barrio A', '1990-01-01'),
('1000000002', 'TI', 'María Fernanda', 'Gómez Martínez', '3200000002', 'maria.gomez@example.com', 'Calle 2 # 3-4', 'Barrio B', '1991-02-02'),
('1000000003', 'CC', 'Carlos Eduardo', 'Rodríguez González', '3200000003', 'carlos.rodriguez@example.com', 'Calle 3 # 4-5', 'Barrio C', '1992-03-03'),
('1000000004', 'TI', 'Ana María', 'Martínez Hernández', '3210000004', 'ana.martinez@example.com', 'Calle 4 # 5-6', 'Barrio D', '1993-04-04'),
('1000000005', 'CC', 'Pedro Pablo', 'López Ramírez', '3110000005', 'pedro.lopez@example.com', 'Calle 5 # 6-7', 'Barrio E', '1994-05-05'),
('1000000006', 'TI', 'Luisa Fernanda', 'Hernández Sánchez', '3120000006', 'luisa.hernandez@example.com', 'Calle 6 # 7-8', 'Barrio F', '1995-06-06'),
('1000000007', 'CC', 'Jorge Andrés', 'Sánchez Torres', '3130000007', 'jorge.sanchez@example.com', 'Calle 7 # 8-9', 'Barrio G', '1996-07-07'),
('1000000008', 'TI', 'Laura Isabel', 'Ramírez Jiménez', '3140000008', 'laura.ramirez@example.com', 'Calle 8 # 9-10', 'Barrio H', '1997-08-08'),
('1000000009', 'CC', 'Andrés Felipe', 'Torres Díaz', '3150000009', 'andres.torres@example.com', 'Calle 9 # 10-11', 'Barrio I', '1998-09-09'),
('1000000010', 'TI', 'Marta Lucía', 'Jiménez Moreno', '3160000010', 'marta.jimenez@example.com', 'Calle 10 # 11-12', 'Barrio J', '1999-10-10');


insert into registro_aportes(id_registro,id_integrante,tipo,valor) 
values ('100000000001','1000000001','AH',25000);