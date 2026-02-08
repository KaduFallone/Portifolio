const { response } = require('../app');
const tasksModel = require('../models/tasksModel');


const getALL = async (_request, response) =>{
    const tasks = await tasksModel.getALL();

    return response.status(200).json(tasks);
};

const createTask = async(request, response) =>{
    const createdTask = await tasksModel.createTask(request.body);

    return response.status(201).json(createdTask);
}

const deleteTask = async (request, response) =>{
    const {id} = request.params;

    await tasksModel.deleteTask(id);
    
    return response.status(204).json();
};

const updateTask = async(request, response) =>{
    const {id} = request.params;

    await tasksModel.updateTasks(id, request.body);

    return response.status(204).json();
};

const getONE = async (request, response, ) =>{
    const {id} = request.params;

    const tasks = await tasksModel.getONE(id);
    
    return response.status(200).json(tasks);
};

module.exports = {
    getALL,
    createTask,
    deleteTask,
    updateTask,
    getONE
};