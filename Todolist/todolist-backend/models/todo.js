const mongoose = require("mongoose");
const { Schema, model } = mongoose;

const todoSchema = new Schema({
  id: Number,
  text: { type: String, required: true },
  done: { type: Boolean, default: false },
});

const Todo = model('Todo', todoSchema);


module.exports = Todo;