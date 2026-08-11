# MongoDB

## Comandos de Navefación básicos
```javascript
show dbs
use mi_base_de_datos
show collections
db.dropDatabase()
```

## Operaciones CRUD básicas

- ### Create
    ```javascript
    db.users.insertOne({
        name: "John",
        age: 28,
        email: "john@gmail.com",
        is_active: true,
        created_at: new Date()
    })

    db.users.insertMany([
        {
            name: "Ana",
            age: 22,
            role: "admin"
        },
        {
            name: "Beatriz",
            age: 35,
            role: "user"
        }
    ])
    ```

- ### Read
    ```javascript
    db.users.find()
    db.users.find().pretty()
    db.users.find({ role: "admin" }) // Retorna una lista
    db.users.findOne({ role: "admin" }) // Retornar la primera coincidencia
    db.users.find({}, { name: 1, age: 1, _id: 0 })
    ```

- ### Update
    ```javascript
    db.users.updateOne(
        { name: "Ana" },
        { $set: { is_active: false } }
    )

    db.users.updateMany(
        { role: "user" },
        { $set: { is_active: true } }
    )
    ```

- ### Delete
    ```javascript
    db.users.deleteOne({ name: "Ana" })
    db.users.deleteMany({ is_active: true })
    ```

## Operadores de consulta y actualización

### Operadores de comparación
- $eq: Igual a
- $ne: Distonto de
- $gt / $gte: Mayor que / Mayor o igual que
- $lt / $lte: Menor que / Menor o igual que
- $in / $nin: Contenido en / No contenido en un arreglo

```javascript
db.users.find({
    age: { $gte: 20, $lte: 30 }
})

db.users.find({
    role: { $in: ["admin", "user"] }
})
```

### Operadores lógicos
- $and: Y
- $or: Ó
- $not: Negación
- $nor: Ninguna condición se cumple

```javascript
db.users.find({
    $or: [
        { role: "admin" },
        { age: { $gt: 40 } }
    ]
})
```

### Operadores de elementos y arreglos
```javascript
// Comprobar si un campo existe
db.users.find({
    phone: { $exists: true }
})

// Agregar un elemento a un arreglo sin duplicados
db.users.updateOne(
    { _id: ObjectId("...") },
    { $addToSet: { hobbies: "Programación" } }
)

// Eliminar un elemento de un arreglo
db.users.updateOne(
    { _id: ObjectId("...") },
    { $pull: {hobbies: "Programación" } }
)
```

## Agregaciones (Aggregation Pipeline)
````javascript
db.transactions.aggregate([
    { $match: { status: "completed" } }, // 1. Filtrar
    { $group: { total: { $sum: "$amount" } } }, // 2. Agrupar
    { $sort: { created_at: -1 } }, // Ordenar
    { $limit: 10 }, // Limitar
])
````

## Indexación y rendimiento
```javascript
// Crear un índice en orden ascendente (1)
db.users.createIndex(
    { email: 1 },
    { unique: true }
)

// Crear un índice compuesto
db.users.createIndex({ name: 1, email: 1 })

// Ver índices de una colección
db.users.getIndexes()

// Analizar el rendimiento de una consulta
db.users.find({ email: "john@gmail.com" }).explain("executionStats")
```

## Paradigma de uso
`Colección pedidos`
```javascript
{
    _id: ObjectId("..."),
    created_at: "2026-08-10",
    total: 1250,
    client: {
        name: "John Doe",
        email: "john@gmail.com"
    },
    items: [
        { name: "Zapatillas Pumba", price: 200, quantity: 2 }
        { name: "Gorras Adiddas", price: 150, quantity: 1 }
    ]
}
```