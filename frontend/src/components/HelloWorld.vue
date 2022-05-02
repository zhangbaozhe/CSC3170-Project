<template>
  <div id="msg-show">
    <v-card class="pa-6 ma-2">
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
      >
        <v-text-field
          v-model="MSG_ID"
          :rules="msgIDRules"
          label="MESSAGE ID"
          required
        ></v-text-field>
        <v-text-field
          v-model="MSG_CONTENT"
          label="MESSAGE CONTENT"
          :rules="msgContentRules"
          :counter="20"
          required
        ></v-text-field>

        <v-btn 
          :disabled="!valid"
          color="success"
          class="mr-4" 
          @click="submit"
        > 
          submit 
        </v-btn>

        <v-btn 
          color="error"
          class="mr-4"
          @click="reset"
        > 
          clear 
        </v-btn>

      </v-form>
    </v-card>
    <v-card v-for="msg in info" v-bind:key="msg.url" class="pa-6 ma-2">
      <p>Message ID: {{ msg["MSG_ID"] }}</p>
      <p>Message contents: {{ msg["MSG_CONTENT"] }}</p>
    </v-card>
  </div>
</template>


<script>
import axios from "axios"

export default {
  name: "HelloWorld",
  data: function () {
    return {
      valid: true, 
      MSG_ID: '', 
      msgIDRules: [
        v => !(this.msgIDs.includes((Number(v) || ''))) || 
          `This ID is already exists in ${this.msgIDs}`
      ], 
      MSG_CONTENT: '', 
      msgContentRules: [
        v => (v || '').length <= 20 ||
          `The content exceeds the max length of 20`
      ], 
      info: [],
      msgIDs: [], 
    };
  },
  methods: {
    submit () {
      if (this.$refs.form.validate()) {
        console.log("CAN POST")
        console.log(this.MSG_ID)
        let data = new FormData()
        data.append("MSG_ID", this.MSG_ID)
        data.append("MSG_CONTENT", this.MSG_CONTENT)

        axios.post("http://127.0.0.1:3170/api/helloworld/", 
            { MSG_ID: this.MSG_ID, MSG_CONTENT: this.MSG_CONTENT }, 
            //data, 
            //{ headers: {'Content-Type': 'application/x-www-form-urlencoded'} }

        )
        .then((response) => { console.log(response) })
        .catch((error) => { console.log(error) })

        location.reload()
      }
      
    }, 
    reset () {
      this.$refs.form.reset()
    }

  }, 
  created() {
    console.log("MOUNTED");
    axios.get("http://127.0.0.1:3170/api/helloworld/").then((response) => {
      this.info = response.data
      for (var i = 0; i < this.info.length; i++) {
        console.log(this.info[i]["MSG_ID"])
        this.msgIDs.push(Number(this.info[i]["MSG_ID"]))
      }
      console.log(this.msgIDs)
      console.log(this.info)
    });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>