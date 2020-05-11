import Vue from 'vue';
import Router from 'vue-router';
import Task from './components/Task.vue';
import Members from './components/Members.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Members',
      component: Members,
    },
    {
      path: '/task',
      name: 'Task',
      component: Task,
    },
  ],
});
