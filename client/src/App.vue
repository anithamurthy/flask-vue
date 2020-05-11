<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Members</router-link> |
      <router-link to="/task">Task</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  margin-top: 60px

}

#nav {
  padding: 30px;
}
table.v-table thead th {
      font-size: 30px !important;

 }
table.v-table tbody td {
    font-size: 15px !important;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
