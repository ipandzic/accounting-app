    <template>
        <div class="transactions">
        <h1>Transactions</h1>
        <form v-on:submit="addTransaction">
          <input type="text" v-model="newTransaction.name" placeholder="Enter Name">
  
          <br />

          <input type="submit" value="Submit">
        </form>

        <ul>
          <li v-for="transaction in transactions">
            {{transaction.name}} <button v-on:click="deleteTransaction(transactions)">X</button>
          </li>
          </li>
        </ul>

        </div>
    </template>

    <script>
      export default {
        name: 'transactions',
        data () {
          return {
            newTransaction: {},
            transactions: []
          }
        },
        methods: {
          addTransaction: function (e) {
            this.transactions.push({
              name: this.newTransaction.name
            })
            e.preventDefault()
          },
          deleteTransaction: function (transaction) {
            this.transactions.splice(this.transactions.indexOf(transaction), 1)
          }
        },
        created: function () {
          this.$http.get('http://127.0.0.1:8000/api/transaction/', {
            headers:
            {
              'Authorization': 'Token ' + '03f718dda3c1484c26337db75181a23ff7841c6d'
            }
          }).then(function (response) {
            this.transactions = response.data
          })
        }
      }

    </script>

    <style scoped>
        
    </style>
