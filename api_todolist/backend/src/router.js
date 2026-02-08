const express = require('express');

const tasksMiddleware = require('./middlewares/tasksMiddleware');

const router = express.Router();

const tasksController  = require('./controllers/tasksController');

router.get('/tasks', tasksController.getALL );

router.post('/tasks', tasksMiddleware.validateFieldTitle, tasksController.createTask);

router.delete('/tasks/:id', tasksController.deleteTask);

router.put('/tasks/:id', tasksMiddleware.validateFieldTitle, tasksMiddleware.validateFieldStatus, tasksController.updateTask);

router.get('/tasks/:id', tasksController.getONE);

module.exports = router;