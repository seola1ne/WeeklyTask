import styled from "styled-components";

function ToDoItem({ todo, onComplete, onRemove }) {
  return (
    <StyledLi>
        <input 
            type="checkbox" 
            checked={todo.done}
            onChange={() => onComplete(todo._id)}
        />
        <span style={{ textDecoration: todo.done ? 'line-through' : 'none' }}>
            {todo.text}
        </span>
        <button style={{ marginLeft: '5px' }} onClick={() => onRemove(todo._id)}>
            삭제
        </button>
    </StyledLi>
  );
}

export default ToDoItem;

const StyledLi = styled.li`
  margin: 8px auto;
`;