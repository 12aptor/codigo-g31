# PostgreSQL

## Crear tablas

```sql
CREATE TABLE movies (
	id SERIAL PRIMARY KEY,
	title VARCHAR(255),
	director VARCHAR(100),
	year INT,
	length_minutes INT
);

CREATE TABLE boxoffice (
    id SERIAL PRIMARY KEY,
    domestic_sales INT,
    movie_id INT REFERENCES movies(id)
);
```

## Insertar registros

```sql
INSERT INTO movies (title, director, year, length_minutes)
VALUES
    ('Toy Story', 'John Lasseter', 1995, 81),
	('Finding Nemo', 'Andrew Stanton', 2003, 100),
	('The Incredibles', 'Brad Bird', 2004, 115),
	('Ratatouille', 'Brad Bird', 2007, 111),
	('Up', 'Pete Docter', 2009, 96),
	('Toy Story 3', 'Lee Unkrich', 2010, 103),
	('Inside Out', 'Pete Docter', 2015, 95),
	('Coco', 'Lee Unkrich', 2017, 105),
	('Toy Story 4', 'Josh Cooley', 2019, 100),
	('Soul', 'Pete Docter', 2020, 100);

INSERT INTO boxoffice (domestic_sales, movie_id)
VALUES
    (100, 1),
    (115, 2),
    (111, 3),
    (96, 4),
    (103, 5);
```

## Consultar registros

## SELECT

```sql
-- Consultar todos los registros
SELECT * FROM movies;

-- Consultar campos específicos
SELECT title, director FROM movies;
```

## Buscar con restricciones

- =, !=, <, >, <=, >=: Operadores de comparación
    ```sql
    SELECT * FROM movies WHERE year > 2000;
    ```

- **BETWEEN**: Rango de valores
    ```sql
    SELECT * FROM movies WHERE year BETWEEN 2000 AND 2005;
    ```

- **IN**: Lista de valores
    ```sql
    SELECT * FROM movies WHERE year IN (2003, 2020, 2007);
    ```

- **LIKE**: Buscar por patrones
    ```sql
    SELECT * FROM movies WHERE title LIKE 'Toy St%';
    ```

- **%**: Cualquier número de caracteres

- **_**: Cualquier caracter

## Ordenar resultados

```sql
SELECT * FROM movies WHERE year > 2000 ORDER BY title DESC;
```

- **ASC**: Ascendente

- **DESC**: Descendente

## Limitar resultados

- **LIMIT**: Limitar la cantidad de registros

    ```sql
    SELECT * FROM movies
    WHERE year > 2000
    ORDER BY title DESC
    LIMIT 2;
    ```

- **OFFSET**: Desplazar la cantidad de registros

    ```sql
    SELECT * FROM movies
    LIMIT 2
    OFFSET 4;
    ```

## Operadores AND, OR, NOT

- **AND**: Operador lógico Y

    ```sql
    SELECT * FROM movies WHERE year > 2000 AND year < 2010;
    ```

- **OR**: Operador lógico O

    ```sql
    SELECT * FROM movies WHERE year = 2003 OR year = 2010;
    ```

- **NOT**: Operador lógico NOT

    ```sql
    SELECT * FROM movies WHERE NOT year = 2003;
    ```

## Operador UPDATE

```sql
UPDATE movies SET year = 2021 WHERE id = 1;
```

## Operador DELETE

```sql
DELETE FROM movies WHERE id = 10;
```

## Operador JOIN

```sql
SELECT title, domestic_sales
FROM movies
JOIN boxoffice
ON movies.id = boxoffice.movie_id;
```