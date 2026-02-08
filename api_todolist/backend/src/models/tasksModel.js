const connection = require('./connectio');

const getALL = async () => {
    const [tasks] = await connection.execute('SELECT * FROM tasks');

    return tasks;
};

const createTask = async (task) =>{
    const {title} = task;
    
    const dateUTC = new Date(Date.now()).toUTCString();

    const query ='INSERT INTO tasks(title, status, created_at) VALUES (?, ?, ?)';

    const [createdTask] = await connection.execute(query, [title, 'pendente', dateUTC]);

    return {insertId: createdTask.insertId};
}

const deleteTask = async (id) => {
    const query = 'DELETE FROM tasks WHERE id = ? ';

    const removeTask = await connection.execute(query, [id]);
}

const updateTasks = async (id, task) =>{
    //            'UPDATE tasks SET title = ?, status = ? WHERE id = ?'
    const query = 'UPDATE tasks SET title = ?, status = ? WHERE id = ?';

    const{title, status} = task;

    const updatedTask = await connection.execute(query, [title, status, id]);
};

const getONE = async (id) => {
    const query = 'SELECT * FROM tasks WHERE id = ?';

    const [tasks] = await connection.execute(query, [id]);

    return tasks;
};


module.exports = {
    getALL,
    createTask,
    deleteTask,
    updateTasks,
    getONE
    
};