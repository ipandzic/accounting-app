    <template>
        <div class="parties">
        <h1>Parties</h1>
        <form v-on:submit="addParty">
          <input type="text" v-model="newParty.name" placeholder="Enter Name">
  
          <br />

          <input type="submit" value="Submit">
        </form>

        <ul>
          <li v-for="party in parties">
            {{party.name}} <button v-on:click="deleteParty(party)">X</button>
          </li>
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
          addParty: function (e) {
            this.parties.push({
              name: this.newParty.name,
              internal: this.newParty.internal,
              active: this.newParty.active
            })
            e.preventDefault()
          },
          deleteParty: function (party) {
            this.parties.splice(this.parties.indexOf(party), 1)
          }
        },
        created: function () {
          this.$http.get('http://127.0.0.1:8000/api/party/', {
            headers:
            {
              'Authorization': 'Token ' + '03f718dda3c1484c26337db75181a23ff7841c6d'
            }
          }).then(function (response) {
            this.parties = response.data
          })
        }
      }

    </script>

    <style scoped>
        
    </style>
