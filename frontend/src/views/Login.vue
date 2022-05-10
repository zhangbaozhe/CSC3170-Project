<template>
  <div id="building">
    <!-- 
    <v-container mt-16 py-16>
      <v-row justify="center" align="center" class="mt-16">-->
          <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
          <div class="card1">
          <div class="text-center mt-4">
            <h1 class="primary--text text-uppercase">
              <span class="font-weight-light">Course</span>
              <span>Comment</span>
            </h1>
          </div>

          <v-card-text>
            <v-row justify="center" align="center" dense>
              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
                <v-text-field
                  id="login"
                  label="User Name"
                  type="text"
                  v-model = "userName"
                  
                  required
                ></v-text-field>
              </v-col>

              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
                <v-text-field
                  id="password"
                  label="Password"
                  type="password"
                  v-model="password"
                  :rules="[rules.required]"
                ></v-text-field>
              </v-col>

              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
                <v-btn 
                  block 
                  tile 
                  color="primary"
                  depressed
                  @click="submit" 
                >
                  Login
                </v-btn>
              </v-col>

              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
                <v-btn 
                  block 
                  @click="toSignUp"
                  tile
                  depressed
                >
                    Sign Up
                </v-btn>
              </v-col>
            </v-row>
          </v-card-text>
          </div>
      <!--</v-row>
    </v-container>-->
    <!-- ？？ -->
    <v-snackbar v-model="snackbar">
      {{tip}}
      <template v-slot:action="{ attrs }">
        <v-btn
          color="pink"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>

  </div>
</template>

<script>
export default {
  data() {
    return {
      
      tip: "",  
      userName:"",
      ID:"",
      loginSuccess: false,
      snackbar: false,
      password: "",
      rules: {
        required: value => !!value || 'Required.',
        name: [val => (val || '').length > 0 || 'This field is required'],
      } 
    }
  },
  methods: {
    submit: function(){
      console.log(this.userName);
      if (this.userName == "") {
        this.tip = "Input your User Name !";
        this.snackbar = true;
        return false;
      }
      if (this.password == "") {
        this.tip = "Input your Password !";
        this.snackbar = true;
        return false;
      }
      this.$axios.get("http://175.178.163.91:3170/api/login/",{
        params:{
          username:this.userName,
          password:this.password
        }
      }).then((response) => {
        console.log(response.data.status)
        console.log(typeof(response.data.status))
        if(response.data.status == 'failed'){
          // TODO: this may be redundant in this response callback
          this.tip = this.data.messages
          this.snackbar = true
          return
        }
        if(response.data.status == 'success'){
          this.loginSuccess = true
          this.$store.commit("loginUpdate")
          this.$store.commit("userNameUpdate", this.userName)
          this.$store.commit("userIDUpdate", response.data.userID)
          console.log(this.$store.state.userID)
          window.location.href = "/home";
        }
      })
      .catch((error) => {
        // for error 400
        console.log(error)
        console.log("TEST 400")
        console.log(error.response.data.status)
        if(error.response.data.status == 'failed'){
          this.tip = error.response.data.messages
          console.log(error.response.data.messages)
          this.snackbar = true
          return
        }
        if(error.response.data.status == 'success'){
          // TODO: this may be redundant in this error callback
          this.loginSuccess = true
          this.$store.commit("loginUpdate")
          this.$store.commit("userNameUpdate", this.userName)
          this.$store.commit("userIDUpdate", response.data.userID)
          window.location.href = "/home";
        }
      } )
    },
    toSignUp: function(){
      window.location.href = "/signup";
    },
  },
}
</script>


  
<style>
#building{
width:100%;			
height:1000px;			
background-size: cover; 
position: absolute; 
background-repeat: no-repeat;
}
.card1{
  margin: auto;
  width:25%;
  height:25%;
}
</style>