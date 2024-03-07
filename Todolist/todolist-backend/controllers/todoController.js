const Todo = require("../models/todo");

exports.getTodos = async (req, res) => {
  const todos = await Todo.find();
  res.send(todos);
};

exports.createTodo = async (req, res) => {
  const newTodo = new Todo(req.body);
  const result = await newTodo.save();
  res.send(result);
};

exports.toggleCompletion = async (req, res) => {
  const todo = await Todo.findById({ _id: req.params.id });
  if (!todo) return res.status(404).send("Todo not found");
  todo.done = !todo.done;
  const result = await todo.save();
  res.send(result);
};

exports.deleteTodo = async (req, res) => {
  const result = await Todo.deleteOne({ _id: req.params.id });
  if (result.deletedCount === 0) return res.status(404).send("Todo not found");
  res.send(result);
};
