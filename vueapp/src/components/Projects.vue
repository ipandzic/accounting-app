    <template>
        <div class="projects">
        <h1>Projects</h1>
        <form v-on:submit="addProject">
          <input type="text" v-model="newProject.name" placeholder="Enter Name">
          <br />Is the project internal?<input type="checkbox" class=toggle v-model="newProject.internal">
          <br />

          <input type="radio" id="one" value="true" v-model="newProject.active">
          <label for="one">Yes</label>
          <br />
          <input type="radio" id="two" value="false" v-model="newProject.active">
          <label for="two">No</label>   
          <br />

          <input type="submit" value="Submit">
        </form>
        <ul>
          <li v-for="project in projects">
            {{project.name}}: <br />Internal: {{project.internal}}
            <br />Active: {{project.active}} <button v-on:click="deleteProject(project)">X</button>
          </li>
        </ul>

        </div>
    </template>

    <script>
      export default {
        name: 'projects',
        data () {
          return {
            newProject: {},
            projects: []
          }
        },
        methods: {
          addProject: function (e) {
            this.projects.push({
              name: this.newProject.name,
              internal: this.newProject.internal,
              active: this.newProject.active
            })
            e.preventDefault()
          },
          deleteProject: function (project) {
            this.projects.splice(this.projects.indexOf(project), 1)
          }
        },
        created: function () {
          this.$http.get('http://127.0.0.1:8000/api/project/', {headers: { 'Authorization': 'Bearer' + 'fa9bcbabf7c716d5b91451bd3c3686657fddf11f', 'Access-Control-Allow-Origin': true }}).then(function (response) {
            this.projects = response.data
          })
        }
      }
    </script>

    <style scoped>
        
    </style>
