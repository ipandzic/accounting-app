    <template>
        <div class="projects">
        <h3>Add Project</h3>
        
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
      <hr>
        <h1>Projects</h1>
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
          this.$http.get('http://127.0.0.1:8000/api/project/', {
            headers:
            {
              'Authorization': 'Token ' + '03f718dda3c1484c26337db75181a23ff7841c6d'
            }
          }).then(function (response) {
            this.projects = response.data
          })
        }
      }

    </script>

    <style scoped>
        
    </style>
