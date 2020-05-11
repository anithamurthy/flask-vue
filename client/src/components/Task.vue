<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-25">
        <h1>Tasks</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.task-modal>Add Task</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Title</th>
              <th scope="col">Description</th>
              <th scope="col">UserId</th>
              <th scope="col">Repeat</th>
              <th scope="col">Participants</th>
              <th scope="col">WhatTime</th>
              <th scope="col">Duration</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(task, index) in tasks" :key="index">
              <td> {{ task._id }}</td>
              <td>{{ task.Title }}</td>
              <td>{{ task.Description }}</td>
              <td>{{ task.UserId }}</td>
              <td>{{ task.Repeat }}</td>
              <td>{{ task.Participants }}</td>
              <td>{{ task.WhatTime }}</td>
              <td>{{ task.Duration }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                        type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.task-update-modal
                        @click="updateTask(task)">
                      Update
                  </button>
                  <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeleteTask(task)">
                       Delete
                   </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addTaskModal"
            id="task-modal"
            title="Add a new task"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addTaskForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-description-group"
                      label="Description:"
                      label-for="form-description-input">
            <b-form-input id="form-description-input"
                          type="text"
                          v-model="addTaskForm.description"
                          required
                          placeholder="Enter description">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-userid-group"
                       label="UserID:"
                       label-for="form-description-input">
            <b-form-input id="form-userid-input"
                          type="text"
                          v-model="addTaskForm.userid"
                          required
                          placeholder="Enter userid">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-repeat-group"
                      label="Repeat:"
                      label-for="form-repeat-input">
            <b-form-input id="form-repeat-input"
                          type="text"
                          v-model="addTaskForm.repeat"
                          required
                          placeholder="Enter task repetition. eg. weekly">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-participants-group"
                      label="Participants:"
                      label-for="form-participants-input">
            <b-form-input id="form-participants-input"
                          type="text"
                          v-model="addTaskForm.participants"
                          required
                          placeholder="Enter participants of the event. eg.parent1">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-whattime-group"
                      label="Time:"
                      label-for="form-whattime-input">
            <b-form-input id="form-whattime-input"
                          type="text"
                          v-model="addTaskForm.whattime"
                          required
                          placeholder="Enter the time of the task.">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-duration-group"
                      label="Duration:"
                      label-for="form-duration-input">
            <b-form-input id="form-duration-input"
                          type="text"
                          v-model="addTaskForm.duration"
                          required
                          placeholder="Enter the duration of the task.eg. 30min">
            </b-form-input>
          </b-form-group>
          <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
          </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="updateTaskModal"
           id="task-update-modal"
           title="Update"
           hide-footer>
        <b-form @submit="onSubmitEdit" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-update-group"
                  label="Title:"
                  label-for="form-title-update-input">
          <b-form-input id="form-title-update-input"
                      type="text"
                      v-model="updateForm.Title"
                      required
                      placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-description-update-group"
                    label="Description:"
                    label-for="form-description-update-input">
          <b-form-input id="form-description-update-input"
                        type="text"
                        v-model="updateForm.Description"
                        required
                        placeholder="Enter description">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-repeat-update-group"
                     label="Repeat:"
                     label-for="form-repeat-update-input">
          <b-form-input id="form-repeat-update-input"
                        type="text"
                        v-model="updateForm.Repeat"
                        required
                        placeholder="Enter repeat sequence, eg. weekly">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-participants-update-group"
                     label="Participants:"
                     label-for="form-participants-update-input">
          <b-form-input id="form-participants-update-input"
                        type="text"
                        v-model="updateForm.Participants"
                        required
                        placeholder="Enter names of participants">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-whattime-update-group"
                     label="WhatTime:"
                     label-for="form-whattime-update-input">
          <b-form-input id="form-whattime-update-input"
                        type="text"
                        v-model="updateForm.WhatTime"
                        required
                        placeholder="Enter time">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-taskid-update-group"
                     label="TaskID:"
                     label-for="form-taskid-update-input">
          <b-form-input id="form-taskid-update-input"
                        type="text"
                        :disabled=1
                        v-model="updateForm._id"
                        required
                        placeholder="Task Id">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-userid-update-group"
                     label="UserID:"
                     label-for="form-userid-update-input">
          <b-form-input id="form-userid-update-input"
                        type="text"
                        v-model="updateForm.UserId"
                        required
                        placeholder="User Id">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-duration-update-group"
                     label="Duration:"
                     label-for="form-duration-update-input">
          <b-form-input id="form-duration-update-input"
                        type="text"
                        v-model="updateForm.Duration"
                        required
                        placeholder="Duration of the task">
          </b-form-input>
        </b-form-group>
        <b-button-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
    </b-button-group>
    </b-form>
   </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  name: 'Task',
  data() {
    return {
      tasks: [],
      addTaskForm: {
        title: '',
        description: '',
        userid: '',
        repeat: '',
        participants: '',
        whattime: '',
        duration: '',
      },
      message: '',
      showMessage: false,
      updateForm: {
        title: '',
        description: '',
        userid: '',
        taskid: '',
        repeat: '',
        participants: '',
        whattime: '',
        duration: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/task';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
          console.log(res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addTask(payload) {
      const path = 'http://localhost:5000/create/task';
      axios.post(path, payload)
        .then(() => {
          this.getTasks();
          this.message = 'Task added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    initForm() {
      console.log('Entered initForm');
      this.addTaskForm.title = '';
      this.addTaskForm.description = '';
      this.addTaskForm.userid = '';
      this.addTaskForm.repeat = '';
      this.addTaskForm.participants = '';
      this.addTaskForm.whattime = '';
      this.addTaskForm.duration = '';
      this.updateForm.title = '';
      this.updateForm.description = '';
      this.updateForm.userid = '';
      /* eslint no-underscore-dangle: 0 */
      this.updateForm._id = '';
      this.updateForm.repeat = '';
      this.updateForm.participants = '';
      this.updateForm.whattime = '';
      this.updateForm.duration = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      const payload = {
        Title: this.addTaskForm.title,
        Description: this.addTaskForm.description,
        UserId: this.addTaskForm.userid,
        Repeat: this.addTaskForm.repeat,
        Participants: this.addTaskForm.participants,
        WhatTime: this.addTaskForm.whattime,
        Duration: this.addTaskForm.duration,
      };
      this.addTask(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      this.initForm();
    },
    updateTask(task) {
      console.log('Entered updateTask: ');
      this.updateForm = task;
      console.log(this.updateForm);
    },
    onSubmitEdit(evt) {
      evt.preventDefault();
      this.$refs.updateTaskModal.hide();
      const payload = {
        Title: this.updateForm.Title,
        Description: this.updateForm.Description,
        Repeat: this.updateForm.Repeat,
        Participants: this.updateForm.Participants,
        WhatTime: this.updateForm.WhatTime,
        Duration: this.updateForm.Duration,
        UserId: this.updateForm.UserId,
      };
      this.editTask(payload, this.updateForm._id);
    },
    editTask(payload, taskid) {
      const path = `http://localhost:5000/update-task/${taskid}`;
      console.log('Entered editTask');
      console.log(payload);
      axios.put(path, payload)
        .then(() => {
          this.getTasks();
          this.message = 'Task updated';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getTasks();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.updateTaskModal.hide();
      this.initForm();
      this.getTasks();
    },
    removeTask(taskid) {
      const path = `http://localhost:5000/delete-task/${taskid}`;
      axios.delete(path)
        .then(() => {
          this.getTasks();
          this.message = 'Task removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
       console.error(error);
          this.getTasks();
        });
    },
    onDeleteTask(task) {
      this.removeTask(task._id);
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
