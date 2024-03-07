import { instance } from "../instance/instance";

export const getTodos = async () => {
    const { data } = await instance.get(`/`);
    return data;
}

export const createTodo = async (Todo) => {
    const { data } = await instance.post(`/`, Todo);
    return data;
}

export const toggleCompletion = async (TodoId) => {
    const { data } = await instance.put(`/${TodoId}`, TodoId);
    return data;
}

export const deleteTodo = async (TodoId) => {
    const { data } = await instance.delete(`/${TodoId}`, TodoId);
    return data;
}