    <template>
        <div class="transactions">
        <h3>Add Transaction</h3>
        
        <form v-on:submit="addTransaction">
          <input type="text" v-model="newTransaction.comments" placeholder="Enter Comment">
          <br />

          <input type="submit" value="Submit">

        </form>
      <hr>
        <h1>Transactions</h1>
        <ul>
          <li v-for="transaction in transactions">
            {{transaction.comments}}: {{transaction.direction}}: 
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
              comments: this.newTransaction.comments
            })
            this.$http.post('http://127.0.0.1:8000/api/transaction/',
              {
                'comments': this.newTransaction.comments
              }, {
                headers: {
                  'Authorization': 'Token ' + '5e5b8ec4a2adadf779061069b59a4ed0d6df2417'
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
                'Authorization': 'Token ' + '5e5b8ec4a2adadf779061069b59a4ed0d6df2417'
              }
            })
          }
        },
        created: function () {
          this.$http.get('http://127.0.0.1:8000/api/transaction/', {
            headers:
            {
              'Authorization': 'Token ' + '5e5b8ec4a2adadf779061069b59a4ed0d6df2417'
            }
          }).then(function (response) {
            this.transactions = response.data
          })
        }
      }

    </script>

    <style scoped>
    </style>
