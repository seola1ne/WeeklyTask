import { useMutation, useQueryClient } from "react-query";
import { createTodo } from "./api";

export const useAddTodoMutation = () => {
    const queryClient = useQueryClient();

    return useMutation(
      (Todo) => {
        return createTodo(Todo);
      },
      {
        onSuccess: () => {
          console.log("Todo 추가됨");
          queryClient.invalidateQueries("Todo");
        },
        onError: () => {
          console.log("Todo 추가되지 않음");
        },
      }
    );
  };