    <template>
        <div class="projects">
        <h3>Add Project</h3>
        
        <form v-on:submit="addProject">
          <input type="text" v-model="newProject.name" placeholder="Enter Name">
          <br />Is the project internal?<input type="checkbox" class=toggle v-model="newProject.internal">
          <br />
          Is the project active?
          <input type="radio" id="one" value="true" v-model="newProject.is_active">
          <label for="one">Yes</label>
          <input type="radio" id="two" value="false" v-model="newProject.is_active">
          <label for="two">No</label>   
          <br />

          <input type="submit" value="Submit">

        </form>
      <hr>
        <h1>Projects:</h1>
        <ul>
          <li v-for="project in projects">
            {{project.name}}: <br />Internal: {{project.internal}}
            <br />Active: {{project.is_active}} <button v-on:click="deleteProject(project)">X</button>
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
            projects: [],
            parties: []
          }
        },
        methods: {
          addProject: function (project) {
            this.projects.push({
              name: this.newProject.name,
              internal: this.newProject.internal,
              active: this.newProject.active
            })
            this.$http.post('http://127.0.0.1:8000/api/project/',
              {
                'name': this.newProject.name,
                'internal': this.newProject.internal,
                'is_active': this.newProject.is_active
              }, {
                headers: {
                  'Authorization': 'Token ' + '816ade3644a5f8ce210adbca8bd701fddb82f729'
                }
              }
              )
            this.$http.get('http://127.0.0.1:8000/api/project/', {
              headers:
              {
                'Authorization': 'Token ' + '816ade3644a5f8ce210adbca8bd701fddb82f729'
              }
            }).then(function (response) {
              this.projects = response.data
            })
            project.preventDefault()
          },
          deleteProject: function (project) {
            this.projects.splice(this.projects.indexOf(project), 1)
            this.$http.delete('http://127.0.0.1:8000/api/project/' + project.id, {
              headers:
              {
                'Authorization': 'Token ' + '816ade3644a5f8ce210adbca8bd701fddb82f729'
              }
            })
          }
        },
        created: function () {
          this.$http.get('http://127.0.0.1:8000/api/project/', {
            headers:
            {
              'Authorization': 'Token ' + '816ade3644a5f8ce210adbca8bd701fddb82f729'
            }
          }).then(function (response) {
            this.projects = response.data
          })
          this.$http.get('http://127.0.0.1:8000/api/party/', {
            headers:
            {
              'Authorization': 'Token ' + '816ade3644a5f8ce210adbca8bd701fddb82f729'
            }
          }).then(function (response) {
            this.parties = response.data
          })
        }
      }

    </script>

    <style scoped>
    </style>
