<template>
  <div id="msg-show">
    <v-card v-for="msg in info.results" v-bind:key="msg.url">
      <p>Message ID: {{ msg.MSG_ID }} </p>
      <p>Message contents: {{ msg.MSG_CONTENT }} </p>
    </v-card>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'HelloWorld',
  data: function() {
    return {
      info: ''
    }
  }, 
  created() {
    console.log("MOUNTED")
    axios
      .get('http://127.0.0.1:3170/api/hellowrold/')
      .then(response => (this.info = response.data))
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>