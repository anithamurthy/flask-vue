
<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Members</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Member</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Name</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(member, index) in members" :key="index">
              <td>{{ member.Title }}</td>
              <td>{{ member.Name }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Members',
  data() {
    return {
      members: [],
    };
  },
  methods: {
    getMembers() {
      const path = 'http://localhost:5000/members';
      axios.get(path)
        .then((res) => {
          this.members = res.data.members;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMembers();
  },
};
</script>
