const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const app = express();
const port = 3001;
const todoRoutes = require("./routes/todo");

mongoose.connect('mongodb://127.0.0.1:27017/todos', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('DB 연결 성공'))
  .catch(e => console.error(e));

app.use(cors({
  origin: '*',
}));

app.use(express.json());
app.use(todoRoutes);

app.listen(port, () => console.log(`Server is running on port ${port}`));
