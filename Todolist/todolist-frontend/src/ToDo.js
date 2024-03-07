import { useState, useEffect } from "react";
import ToDoItem from "./ToDoItem";
import { getTodos, createTodo, toggleCompletion, deleteTodo } from "./api/todo/api";

function ToDo() {
  const [input, setInput] = useState("");
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    getTodos().then(setTodos);
  }, []);

  const onChange = (event) => setInput(event.target.value);

  const onSubmit = async (event) => {
    event.preventDefault();
    if (input === "") {
      return;
    }
    const newTodo = await createTodo({ text: input, done: false });
    setTodos(prevTodos => [...prevTodos, newTodo]);
    setInput("");
  }

  const onComplete = async (id) => {
    const updatedTodo = await toggleCompletion(id);
    setTodos(todos.map(todo => todo._id === id ? updatedTodo : todo));
  }

  const onRemove = async (id) => {
    await deleteTodo(id);
    setTodos(todos.filter(todo => todo._id !== id));
  }

  return (
    <div>
      <h1>My Todos {todos.length}</h1>
      <form onSubmit={onSubmit}>
        <input 
          onChange={onChange} 
          value={input} 
          type="text" 
          placeholder="Todo를 입력하세요"
        />
        <button style={{ marginLeft: '5px' }}>추가하기</button>
      </form>
      <hr />
      {todos.map(item => (
        <ToDoItem
          key={item._id} 
          todo={item} 
          onComplete={onComplete} 
          onRemove={onRemove}
        />
      ))}
    </div>
  );
}

export default ToDo;
