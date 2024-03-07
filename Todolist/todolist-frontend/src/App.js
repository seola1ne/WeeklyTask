import { useState } from "react";
import Todo from "./ToDo";
import styled from "styled-components"

function App() {
  return (
    <ToDoContainer>
      <Todo />
    </ToDoContainer>
  );
}

export default App;

const ToDoContainer = styled.div`
  width: 1200px;
  padding: 50px 60px;

  button {
    background-color: white;
    border: 1px solid black;
    padding: 4px 6px;
    border-radius: 5px;

    &:hover {
      transition: ease 0.15s;
      background-color: lightblue;
      cursor: pointer;
    }
  }

  input {
    padding: 4px 8px;
  }
`;