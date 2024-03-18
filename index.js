var express = require('express');
var app = express();
var bodyParser = require('body-parser')
app.use(bodyParser.json());

const {conn, sql} = require('./dbconfig')

// app.post("/register", function (req, res) {
//     res.send("Hello")
// });

// app.get("", function (req, res) {
//     res.send('<form method="POST" action="/register"><button>Register</button></form>')
// });


app.get("/pokemon", async function (req, res) {
    var pool = await conn;
    var sql_query = req.query;
    // if sql_query.id is not Null
    console.log(sql_query);
    var sqlString = "SELECT * FROM Pokemon";
    return await pool.request().query(sqlString, function (err, data) {
        res.send(data.recordset)
    });
});

app.get("/pokemon/:id", async function (req, res) {
    var id = req.params.id;
    var pool = await conn;
    var sqlString = "SELECT * FROM Pokemon where pokemonid = @varId";
    return await pool.request().input('varId', sql.Int, id).query(sqlString, function (err, data) {
        
        if (data.recordset.length > 0) {
            res.send(data.recordset);
        } else {
            res.send(null);
        }
    });
});

app.get("/pokemon/:name", async function (req, res) {
    var name = req.params.name;
    var pool = await conn;
    var sqlString = "SELECT * FROM Pokemon where pname = @varName";
    return await pool.request().input('varName', sql.NVarCharVarChar, name).query(sqlString, function (err, data) {
        
        if (data.recordset.length > 0) {
            res.send(data.recordset);
        } else {
            res.send(null);
        }
    });
});


app.get("/move", async function (req, res) {
    var pool = await conn;
    var sqlString = "SELECT * FROM moves";
    return await pool.request().query(sqlString, function (err, data) {
        res.send(data.recordset)
    });
});

app.get("/move/:id", async function (req, res) {
    var id = req.params.id;
    var pool = await conn;
    var sqlString = "SELECT * FROM moves where moveid = @varId";
    return await pool.request().input('varId', sql.Int, id).query(sqlString, function (err, data) {
        
        if (data.recordset.length > 0) {
            res.send(data.recordset);
        } else {
            res.send(null);
        }
    });
});

app.get("/move/:name", async function (req, res) {
    var name = req.params.name;
    var pool = await conn;
    var sqlString = "SELECT * FROM moves where mname = @varName";
    return await pool.request().input('varName', sql.NVarChar, name).query(sqlString, function (err, data) {
        
        if (data.recordset.length > 0) {
            res.send(data.recordset);
        } else {
            res.send(null);
        }
    });
});
// app.put("/update", function (req, res) {
//     res.send("Hello")
// });

// app.delete("/delete", function (req, res) {
//     res.send("Hello")
// });


//Open host 
app.listen(3000, function () {
});