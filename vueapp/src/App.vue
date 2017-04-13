<template>
  <div id="app">
  <projects></projects>
  </div>
</template>

<script>
import Projects from './components/Projects'

export default {
  name: 'app',
  components: {
    Projects
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
