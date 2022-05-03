<template>
  <div id="building">
    <v-container mt-16 py-16>
      <v-row justify="center" align="center" class="mt-16">
        <v-card class="px-2 pb-3" max-width="400px" flat outlined tile>
          <div class="text-center mt-4">
            <h1 class="primary--text text-uppercase">
              <span>Sign Up</span>
            </h1>
          </div>

          <v-card-text>
            <v-row justify="center" align="center" dense>
              <v-col cols="12" xs="12" sm="12" md="12">
                <v-text-field
                  id="login"
                  label="New User Name"
                  type="text"
                  v-model="userName"
                  :rules="rules.userNameRules"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12" xs="12" sm="12" md="12">
                <v-text-field
                  id="password"
                  label="New Password"
                  type="password"
                  v-model="password"
                  :rules="rules.passwordRules"
                ></v-text-field>
              </v-col>

              <v-col cols="12" xs="12" sm="12" md="12">
                <v-btn block tile color="primary" depressed @click="submit">
                  SignUp
                </v-btn>
              </v-col>

              <v-col cols="12" xs="12" sm="12" md="12">
                <v-btn block @click="toLogin" tile depressed> Log In </v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-row>
    </v-container>
    <!-- ？？ -->
    <v-snackbar v-model="snackbar">
      {{ tip }}
      <template v-slot:action="{ attrs }">
        <v-btn color="pink" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      userName: "",
      ID: "",
      tip: "",
      allUsersObjectArray: [], // This should be filled by axios
      allUsersArray: [], 
      loginSuccess: false,
      snackbar: false,
      password: "",
      rules: {
        passwordRules: [
          (val) => (val || "").length > 0 || "This field is required"
        ],
        userNameRules: [
          (v) => 
            (v || '').length > 0 && !this.allUsersArray.includes(v || "") || 
            `This field should not be empty and this name ${v} should be unique`
        ], // TODO:
      },
    };
  },
  created() {
    // first use axios to get all the users
    // TODO: add this api in the backend and add views
    axios
      .get("http://127.0.0.1:3170/api/get_users/")
      .then((response) => {
        this.allUsersObjectArray = response.data;
        for (var i = 0; i < this.allUsersObjectArray.length; i++) {
          this.allUsersArray.push(this.allUsersObjectArray[i]["Username"])
        }
        console.log("GET RESPONSE")
        console.log(this.allUsersArray)
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    submit: function () {
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
      if (this.userName != "" && this.password != "" && !this.allUsersArray.includes(this.userName))
        console.log("TO SIGN UP")
        let data = new FormData()
        data.append("USERNAME", this.userName)
        data.append("PASSWORD", this.password)
        axios
          .post("http://127.0.0.1:3170/api/register_user/", 
            data, 
            { headers: {'Content-Type': 'application/x-www-form-urlencoded'} }
          ) 
          .then((response) => {
              console.log(response) 
              window.location.href = "/login";
            })
          .catch((error) => { console.log(error) })
    },
    toLogin: function () {
      window.location.href = "/login";
    },
  },
};
</script>


  
<style>
#building {
  width: 100%;
  height: 100%;
  background-size: cover;
  position: absolute;
  background-repeat: no-repeat;
}
</style>