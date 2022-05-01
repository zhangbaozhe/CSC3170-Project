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
import axios from 'axios'
export default {
  data() {
    return {
      
      
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