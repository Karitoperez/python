-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-05-2024 a las 22:56:59
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `registrarse`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `archivos`
--

CREATE TABLE `archivos` (
  `FileID` int(11) NOT NULL,
  `FileName` varchar(255) NOT NULL,
  `FilePath` varchar(255) NOT NULL,
  `UploadDate` timestamp NULL DEFAULT current_timestamp(),
  `UserID` int(11) DEFAULT NULL,
  `FolderID` int(11) DEFAULT NULL,
  `promedio_calificaciones` decimal(5,2) DEFAULT 0.00,
  `descripcion` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `archivos`
--

INSERT INTO `archivos` (`FileID`, `FileName`, `FilePath`, `UploadDate`, `UserID`, `FolderID`, `promedio_calificaciones`, `descripcion`) VALUES
(50, 'Elaboracion de Mockups.pdf', 'uploads\\Elaboracion de Mockups.pdf', '2024-05-13 18:51:34', 19, 66, 4.00, 'Este documento ayuda y facilita la creación de los Mockups para los proyectos que lo necesiten.'),
(51, 'Fundamentos de Ingenieria en SIstemas.pdf', 'uploads\\Fundamentos de Ingenieria en SIstemas.pdf', '2024-05-13 19:02:12', 19, 66, 2.00, 'Este documento de ayudas e ideas para los fundamentos que implica la Ingeniería en sistemas.'),
(52, 'Fundamentos de Ingenieria Industrial.pdf', 'uploads\\Fundamentos de Ingenieria Industrial.pdf', '2024-05-13 19:03:24', 19, 66, 1.50, 'Los Fundamentos de la ingenieria Industrial se encuentran plasmados en el anterior pdf.'),
(53, 'Guia de Normas APA V7.pdf', 'uploads\\Guia de Normas APA V7.pdf', '2024-05-13 19:04:33', 19, 66, 3.00, 'Guia clara y especifica para la elaboracion de documentos usando normas APA 7ma edicion.'),
(54, 'Guia Uso Mendeley.pdf', 'uploads\\Guia Uso Mendeley.pdf', '2024-05-13 19:06:02', 19, 66, 3.00, 'Una guia para el uso de Mendeley, una herramienta para la elaboracion de trabajos escritos.'),
(55, 'Dispositivos Electronicos 8va.edicion.pdf', 'uploads\\Dispositivos Electronicos 8va.edicion.pdf', '2024-05-13 19:16:56', 19, 67, 2.00, 'Nos presenta diferentes dispositivos electronicos, con los cuales podemos familiarizarnos'),
(56, 'Dispositivos y Aplicaciones.pdf', 'uploads\\Dispositivos y Aplicaciones.pdf', '2024-05-13 19:19:44', 19, 67, 5.00, 'Aplicaciones Para el manejo de la electronica.'),
(57, 'Electronica Basica.pdf', 'uploads\\Electronica Basica.pdf', '2024-05-13 19:20:07', 19, 67, 4.00, 'Conceptos basicos de la electronica'),
(58, 'Electronica Elemental.pdf', 'uploads\\Electronica Elemental.pdf', '2024-05-13 19:21:16', 19, 67, 4.00, 'Este pdf nos demuestra un poco mas a fondo la Electronica Fundamental.'),
(59, 'Presentacion Conceptos Basicos.pdf', 'uploads\\Presentacion Conceptos Basicos.pdf', '2024-05-13 19:21:51', 19, 67, 3.00, 'Presetacion de los conceptos basicos de la electronica, junto con sus distintas aplicaciones'),
(60, 'Presentacion Conceptos Basicos.pdf', 'uploads\\Presentacion Conceptos Basicos.pdf', '2024-05-13 20:11:27', 19, 66, 0.00, 'Libro fundamentos basicos de la fisica, volumen 1'),
(61, 'Presentacion Conceptos Basicos.pdf', 'uploads\\Presentacion Conceptos Basicos.pdf', '2024-05-13 20:12:08', 19, 68, 4.00, 'Libro fundamentos basicos de la fisica, volumen 1 Serway vuille');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calificaciones`
--

CREATE TABLE `calificaciones` (
  `id` int(11) NOT NULL,
  `archivo_id` int(11) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `calificacion` int(11) DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `calificaciones`
--

INSERT INTO `calificaciones` (`id`, `archivo_id`, `usuario_id`, `calificacion`, `fecha`) VALUES
(8, 50, 19, 4, '2024-05-13 19:06:15'),
(9, 51, 19, 2, '2024-05-13 19:06:34'),
(10, 52, 19, 1, '2024-05-13 19:06:43'),
(11, 53, 19, 5, '2024-05-13 19:06:50'),
(12, 54, 19, 3, '2024-05-13 19:06:57'),
(13, 55, 19, 2, '2024-05-13 19:22:11'),
(14, 56, 19, 5, '2024-05-13 19:22:19'),
(15, 57, 19, 4, '2024-05-13 19:22:25'),
(16, 58, 19, 4, '2024-05-13 19:22:39'),
(17, 59, 19, 3, '2024-05-13 19:22:45'),
(18, 52, 19, 2, '2024-05-13 19:23:36'),
(19, 53, 19, 1, '2024-05-13 19:24:03'),
(20, 61, 19, 4, '2024-05-13 20:13:57'),
(21, 61, 19, 4, '2024-05-13 20:55:15');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `calificar`
--

CREATE TABLE `calificar` (
  `valor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `calificar`
--

INSERT INTO `calificar` (`valor`) VALUES
(1),
(5),
(2),
(4),
(2),
(3),
(1),
(5),
(1),
(1),
(5),
(3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `folders`
--

CREATE TABLE `folders` (
  `FolderID` int(11) NOT NULL,
  `FolderName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `folders`
--

INSERT INTO `folders` (`FolderID`, `FolderName`) VALUES
(66, 'Fundamentos de Ingeniería '),
(67, 'Fundamentos de Electrónica '),
(68, 'Fisica '),
(69, 'Calculo '),
(70, 'Programación'),
(71, 'Matemáticas Discretas '),
(72, 'Bases de Datos'),
(73, 'Matemáticas Especiales '),
(74, 'Profundización'),
(75, 'Ingeniería de Software'),
(76, 'Estadística'),
(77, 'Ecuaciones Diferenciales '),
(78, 'Análisis Numérico'),
(79, 'Bases de Datos'),
(80, 'Inteligencia Artificial');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informacion_academica`
--

CREATE TABLE `informacion_academica` (
  `id` int(11) NOT NULL,
  `usuario` varchar(255) NOT NULL,
  `sede` varchar(100) DEFAULT NULL,
  `programa` varchar(255) DEFAULT NULL,
  `semestre` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `informacion_academica`
--

INSERT INTO `informacion_academica` (`id`, `usuario`, `sede`, `programa`, `semestre`) VALUES
(1, 'JuanQ1234', 'Extensión Facatativá', 'Ingeniería de Sistemas ', 'Tercer Semestre'),
(2, 'karol20', 'Extensión Facatativá', 'Ingeniería de Sistemas ', 'Tercer Semestre'),
(3, 'Ender', 'Extensión Facatativá', 'Ingeniería de Sistemas ', 'Tercer Semestre'),
(4, 'Valentina1', 'Extensión Facatativá', 'Ingeniería de Sistemas ', 'Tercer Semestre'),
(5, 'Nyaw1009', 'Extensión Facatativá', 'Ingenieria en Sistemas', 'Tercer Semestre'),
(6, 'Danny2005', 'Extensión Facatativá', 'Ingenieria en Sistemas', 'Tercer Semestre'),
(7, 'Marifer02', 'Extensión Facatativá', 'Ingenieria en Sistemas', 'Tercer Semestre'),
(8, 'SofiR2303', 'Seccional Ubaté', 'Ingenieria en Sistemas', 'Quinto Semestre'),
(9, 'JuanMa67', 'Extensión Chia', 'Ingenieria en Sistemas', 'Septimo Semestre'),
(10, 'MalejaG12', 'Extensión Chia', 'Ingenieria en Sistemas', 'Noveno Semestre'),
(11, 'PedritoL09', 'Extensión Chia', 'Ingenieria en Sistemas', 'Tercer Semestre'),
(12, 'FerMar34', 'Extensión Chia', 'Ingenieria en Sistemas', 'Sexto Semestre'),
(13, 'PipeG12', 'Extensión Facatativá', 'Ingenieria en Sistemas', 'Octavo Semestre'),
(14, 'Pa0laR', 'Extensión Facatativá', 'Ingenieria en Sistemas', 'Primero Semestre'),
(15, 'Alejito67S', 'Extensión Chia', 'Ingenieria en Sistemas', 'Quinto Semestre'),
(16, 'ValeH33rrera', 'Extensión Facatativá', 'Ingenieria en Sistemas', 'Quinto Semestre'),
(17, 'SebasE344', 'Extensión Facatativá', 'Ingenieria en Sistemas', 'Cuarto Semestre');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `usuario` varchar(100) NOT NULL,
  `correo` varchar(150) NOT NULL,
  `password` varchar(100) NOT NULL,
  `rol` enum('user','admin') DEFAULT 'user',
  `habilitado` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `login`
--

INSERT INTO `login` (`id`, `usuario`, `correo`, `password`, `rol`, `habilitado`) VALUES
(1, 'JuanQ1234', 'Jdiegoquiroga@ucundinamarca.edu.co', 'JuanQ1234', 'admin', 1),
(2, 'karol20', 'kaperez@ucundinamarca.edu.co', 'Karolperez200705', 'admin', 0),
(3, 'Ender', 'nfelipegonzales@ucundinamarca.edu.co', 'NikoPipe0414', 'admin', 1),
(4, 'Valentina1', 'lvalentinaortiz@ucundinamarca.edu.co', 'Valentina1', 'admin', 0),
(9, 'Nyaw1009', 'jandresperez@ucundinamarca.edu.co', '21902150jJ', 'user', 0),
(10, 'Danny2005', 'dfsolano@ucundinamarca.edu.co', 'Daniel13', 'user', 1),
(11, 'Marifer02', 'mpenalosa@ucundinamarca.edu.co', 'MariaF12', 'user', 1),
(12, 'SofiR2303', 'asofíaramírez@ucundinamarca.edu.co', 'Sofia220', 'user', 1),
(13, 'JuanMa67', 'jmanuelcastañeda@ucundinamarca.edu.co', 'JuanMa08', 'user', 1),
(14, 'MalejaG12', 'malejandragómez@ucundinamarca.edu.co', 'Melajita234', 'user', 1),
(15, 'PedritoL09', 'pjosélopez@ucundinamarca.edu.co', 'PedroPedroPe23', 'user', 1),
(16, 'FerMar34', 'lfernandamartínez@ucundinamarca.edu.co', 'Fer45634', 'user', 1),
(17, 'PipeG12', 'afelipegarcía@ucundinamarca.edu.co', 'Felipe45654', 'user', 1),
(18, 'Pa0laR', 'parodríguez@ucundinamarca.edu.co', 'Rodrigu34323', 'user', 1),
(19, 'Alejito67S', 'dalesánchez@ucundinamarca.edu.co', 'Alejandro13_', 'user', 1),
(20, 'ValeH33rrera', 'vmarcelaherrera@ucundinamarca.edu.co', 'HerreraM2', 'user', 1),
(21, 'SebasE344', 'seduardomedina@ucundinamarca.edu.co', 'Sevis232', 'user', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mensajes`
--

CREATE TABLE `mensajes` (
  `id` int(11) NOT NULL,
  `usuario` varchar(255) DEFAULT NULL,
  `sala` varchar(255) DEFAULT NULL,
  `contenido` text DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `archivos`
--
ALTER TABLE `archivos`
  ADD PRIMARY KEY (`FileID`),
  ADD KEY `FolderID` (`FolderID`),
  ADD KEY `FK_UserID` (`UserID`);

--
-- Indices de la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `archivo_id` (`archivo_id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `folders`
--
ALTER TABLE `folders`
  ADD PRIMARY KEY (`FolderID`);

--
-- Indices de la tabla `informacion_academica`
--
ALTER TABLE `informacion_academica`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario` (`usuario`);

--
-- Indices de la tabla `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `correo` (`correo`),
  ADD UNIQUE KEY `usuario` (`usuario`);

--
-- Indices de la tabla `mensajes`
--
ALTER TABLE `mensajes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `archivos`
--
ALTER TABLE `archivos`
  MODIFY `FileID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT de la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `folders`
--
ALTER TABLE `folders`
  MODIFY `FolderID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT de la tabla `informacion_academica`
--
ALTER TABLE `informacion_academica`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `mensajes`
--
ALTER TABLE `mensajes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=243;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `archivos`
--
ALTER TABLE `archivos`
  ADD CONSTRAINT `FK_UserID` FOREIGN KEY (`UserID`) REFERENCES `login` (`id`),
  ADD CONSTRAINT `archivos_ibfk_2` FOREIGN KEY (`FolderID`) REFERENCES `folders` (`FolderID`);

--
-- Filtros para la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD CONSTRAINT `calificaciones_ibfk_1` FOREIGN KEY (`archivo_id`) REFERENCES `archivos` (`FileID`),
  ADD CONSTRAINT `calificaciones_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `archivos` (`UserID`);

--
-- Filtros para la tabla `informacion_academica`
--
ALTER TABLE `informacion_academica`
  ADD CONSTRAINT `informacion_academica_ibfk_1` FOREIGN KEY (`usuario`) REFERENCES `login` (`usuario`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
