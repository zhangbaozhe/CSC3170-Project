<template>
  <div id="building">
    <v-container mt-16 py-16>

      <v-row justify="center" align="center" class="mt-16">
        <v-card 
          class="px-2 pb-3" 
          max-width=400px 
          flat
          outlined
          tile
        >
          <div class="text-center mt-4">
            <h1 class="primary--text text-uppercase">
              
              <span>Sign Up</span>
            </h1>
          </div>

          <v-card-text>
            <v-row justify="center" align="center" dense>
              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
                <v-text-field
                  id="login"
                  label="New User Name"
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
                  label="New Password"
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
                  SignUp
                </v-btn>
              </v-col>

              <v-col 
                cols="12" xs="12" sm="12" md="12"
              >
                <v-btn 
                  block 
                  @click="toLogin"
                  tile
                  depressed
                >
                    Log In
                </v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-row>
    </v-container>
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
    toLogin: function(){
      window.location.href = "/login";
    },
  },
}
</script>


  
<style>
#building{
width:100%;			
height:100%;			
background-size: cover; 
position: absolute; 
background-repeat: no-repeat;
}
</style>