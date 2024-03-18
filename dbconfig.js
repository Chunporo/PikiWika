var sql = require('mssql')

var config = {
    server: "localhost",
    user: "sa",
    password:"123",
    database:"Pikawiki",
}

const conn = new sql.ConnectionPool(config).connect().then(pool => {
    return pool;
})

module.exports = {
    conn: conn,
    sql: sql
}