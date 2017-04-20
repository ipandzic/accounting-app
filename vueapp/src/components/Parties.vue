    <template>
        <div class="parties">
        <h3>Add Party</h3>
        <form v-on:submit="addParty">
          <input type="text" v-model="newParty.name" placeholder="Enter Name">
  
          <br />
          Is the party domestic?<input type="checkbox" class=toggle v-model="newParty.is_domestic">

          <br />
          <input type="text" v-model="newParty.vat_ptc" placeholder="Enter VAT">
          <br />
          <input type="radio" id="one" value="true" v-model="newParty.is_active">
          <label for="one">Yes</label>
          <br />
          <input type="radio" id="two" value="false" v-model="newParty.is_active">
          <label for="two">No</label>   
          <br />
          <input type="text" v-model="newParty.projects" placeholder="Enter projects">

          <input type="submit" value="Submit">
        </form>
      
      <hr>
        <h1>Parties</h1>
        <ul>
          <li v-for="party in parties">
            Name: {{party.name}}  <br />
            Domestic: {{party.is_domestic}} <br />
            VAT: {{party.vat_ptc}} <br />
            Active: {{party.is_active}}
            <button v-on:click="deleteParty(parties)">X</button>
          </li>

        </ul>

        </div>
    </template>

    <script>
      export default {
        name: 'parties',
        data () {
          return {
            newParty: {},
            parties: []
          }
        },
        methods: {
          addParty: function (party) {
            this.parties.push({
              name: this.newParty.name,
              is_domestic: this.newParty.is_domestic,
              is_active: this.newParty.is_active
            })
            this.$http.post('http://127.0.0.1:8000/api/party/',
              {
                name: this.newParty.name,
                is_domestic: this.newParty.is_domestic,
                vat_ptc: this.newParty.vat_ptc,
                is_active: this.newParty.is_active,
                projects: this.newParty.projects
              }, {
                headers: {
                  'Authorization': 'Token ' + '5e5b8ec4a2adadf779061069b59a4ed0d6df2417'
                }
              }
            )
            party.preventDefault()
          },
          deleteParty: function (party) {
            this.parties.splice(this.parties.indexOf(party), 1)
            this.$http.delete('http://127.0.0.1:8000/api/party/' + party.id, {
              headers:
              {
                'Authorization': 'Token ' + '5e5b8ec4a2adadf779061069b59a4ed0d6df2417'
              }
            })
          }
        },
        created: function () {
          this.$http.get('http://127.0.0.1:8000/api/party/', {
            headers:
            {
              'Authorization': 'Token ' + '5e5b8ec4a2adadf779061069b59a4ed0d6df2417'
            }
          }).then(function (response) {
            this.parties = response.data
          })
        }
      }

    </script>

    <style scoped>
    </style>
