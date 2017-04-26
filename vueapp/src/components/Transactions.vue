    <template>
        <div class="transactions">
        <h3>Add Transaction</h3>
        
        <form v-on:submit="addTransaction">
          <input type="text" v-model="newTransaction.comments" placeholder="Enter Comment">
          <br />
          <input type="text" v-model="newTransaction.party" placeholder="Enter Party Name">
          <br />

          <input type="submit" value="Submit">

        </form>
      <hr>
        <h1>Transactions</h1>
        <ul>
          <li v-for="transaction in transactions">
            {{transaction.comments}}:
            <button v-on:click="deleteTransaction(transaction)">X</button>
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
          addTransaction: function (transaction) {
            this.transactions.push({
              comments: this.newTransaction.comments,
              party: this.newTransaction.party
            })
            this.$http.post('http://127.0.0.1:8000/api/transaction/',
              {
                'comments': this.newTransaction.comments,
                'party': this.newTransaction.party
              }, {
                headers: {
                  'Authorization': 'Token ' + '816ade3644a5f8ce210adbca8bd701fddb82f729'
                }
              }
              )
            transaction.preventDefault()
          },
          deleteTransaction: function (transaction) {
            this.transactions.splice(this.transactions.indexOf(transaction), 1)
            this.$http.delete('http://127.0.0.1:8000/api/transaction/' + transaction.id, {
              headers:
              {
                'Authorization': 'Token ' + '816ade3644a5f8ce210adbca8bd701fddb82f729'
              }
            })
          }
        },
        created: function () {
          this.$http.get('http://127.0.0.1:8000/api/transaction/', {
            headers:
            {
              'Authorization': 'Token ' + '816ade3644a5f8ce210adbca8bd701fddb82f729'
            }
          }).then(function (response) {
            this.transactions = response.data
          })
        }
      }

    </script>

    <style scoped>
    </style>
