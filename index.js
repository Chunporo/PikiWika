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

app.get("/pokemon/name/:pokename", async function (req, res) {
    var name = req.params.pokename;
    var pool = await conn;
    console.log(name)
    var sqlString = "SELECT * FROM pokemon where pname = @varName";
    return await pool.request().input('varName', sql.NVarChar, name).query(sqlString, function (err, data) {
        
        if (data.recordset.length > 0) {
            res.send(data.recordset);
        } else {
            res.send(null);
        }
    });
});

app.get("/pokemon/move/name/:name", async function (req, res) {
    var name = req.params.name;
    var pool = await conn;
    console.log(name)
    var sqlString = "SELECT * FROM Pokemon_Move_Name(@varName)";
    return await pool.request().input('varName', sql.NVarChar, name).query(sqlString, function (err, data) {
        
        if (data.recordset.length > 0) {
            res.send(data.recordset);
        } else {
            res.send(null);
        }
    });
});


app.get("/pokemon/move/id/:id", async function (req, res) {
    var id = req.params.id;
    var pool = await conn;
    var sqlString = "SELECT * FROM Pokemon_Move_Id(@varId)";
    return await pool.request().input('varId', sql.Int, id).query(sqlString, function (err, data) {
        
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

app.get("/move/name/:movename", async function (req, res) {
    var name = req.params.movename;
    var pool = await conn;
    console.log(name)
    var sqlString = "SELECT * FROM moves where mname = @varName";
    return await pool.request().input('varName', sql.NVarChar, name).query(sqlString, function (err, data) {
        
        if (data.recordset.length > 0) {
            res.send(data.recordset);
        } else {
            res.send(null);
        }
    });
});

app.get("/type", async function (req, res) {
    var pool = await conn;
    var sqlString = "SELECT * FROM types";
    return await pool.request().query(sqlString, function (err, data) {
        res.send(data.recordset)
    });
});

app.get("/type/:id", async function (req, res) {
    var id = req.params.id;
    var pool = await conn;
    var sqlString = "SELECT * FROM types where typeid = @varId";
    return await pool.request().input('varId', sql.Int, id).query(sqlString, function (err, data) {
        
        if (data.recordset.length > 0) {
            res.send(data.recordset);
        } else {
            res.send(null);
        }
    });
});

app.get("/type/name/:typename", async function (req, res) {
    var name = req.params.typename;
    var pool = await conn;
    console.log(name)
    var sqlString = "SELECT * FROM types where tname = @varName";
    return await pool.request().input('varName', sql.NVarChar, name).query(sqlString, function (err, data) {
        
        if (data.recordset.length > 0) {
            res.send(data.recordset);
        } else {
            res.send(null);
        }
    });
});

app.get("/ability", async function (req, res) {
    var pool = await conn;
    var sqlString = "SELECT * FROM abilities";
    return await pool.request().query(sqlString, function (err, data) {
        res.send(data.recordset)
    });
});

app.get("/ability/:id", async function (req, res) {
    var id = req.params.id;
    var pool = await conn;
    var sqlString = "SELECT * FROM abilities where abilityid = @varId";
    return await pool.request().input('varId', sql.Int, id).query(sqlString, function (err, data) {
        
        if (data.recordset.length > 0) {
            res.send(data.recordset);
        } else {
            res.send(null);
        }
    });
});

app.get("/ability/name/:abilityname", async function (req, res) {
    var name = req.params.abilityname;
    var pool = await conn;
    console.log(name)
    var sqlString = "SELECT * FROM abilities where aname = @varName";
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


const PORT = process.env.PORT || 3000;
//Open host 
app.listen(PORT, function () {
});