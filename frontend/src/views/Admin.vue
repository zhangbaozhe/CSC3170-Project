<template>
  <div id="msg-show">
    
    <!-- List the courses and they can be added or deleted -->
    <v-card class="d-flex pa-2 ma-2">
      <v-form
        ref="form"
        v-model="valid"
        lazy-validation
        class="d-flex pa-2 ma-2"
      >
        <v-text-field
          v-model="CourseCode"
          :rules="CourseCodeRules"
          label="Course Code"
          required
          class="d-flex pa-2 ma-2"
        ></v-text-field>
        <v-text-field
          v-model="CourseName"
          label="Course Name"
          :rules="CourseNameRules"
          :counter="20"
          required
          class="d-flex pa-2 ma-2"
        ></v-text-field>

        <v-btn 
          :disabled="!valid"
          color="success"
          class="mr-4" 
          @click="submitCourse(CourseCode, CourseName)"
        > 
          submit 
        </v-btn>

        <v-btn color="error" class="mr-4" @click="reset"> 
          clear 
        </v-btn>

      </v-form>
    </v-card>

    <v-card v-for="course in Courses" v-bind:key="course.url" class="d-flex pa-2 ma-2">
        <v-card-title>
            Course Name: {{ course.CourseName }}
        </v-card-title>
        <v-card-actions>
            <v-btn color="error" class="mr-4" @click="deleteCourse(course.CourseID)">
                delete
            </v-btn>
        </v-card-actions>
    </v-card>

    <!-- List the comments and they can be deleted -->
    <v-card v-for="comment in Comments" v-bind:key="comment.url" class="d-flex pa-2 ma-2">
        <v-card-title>
            CommentID: {{ comment.CommentID }}
        </v-card-title>
        <v-card-text>
            Comment content: {{ comment.Content }}
        </v-card-text>
        <v-card-actions>
            <v-btn color="error" class="mr-4" @click="deleteComment(comment.CommentID)">
                delete
            </v-btn>
        </v-card-actions>
    </v-card>

    <!-- List the users and they can be deleted -->
    <v-card v-for="user in Users" v-bind:key="user.url" class="d-flex pa-2 ma-2">
        <v-card-title>
            UserID: {{ user.UserID}}
        </v-card-title>
        <v-card-text>
            Username: {{ user.Username }}
        </v-card-text>
        <v-card-actions>
            <v-btn color="error" class="mr-4" @click="deleteUser(user.UserID)">
                delete
            </v-btn>
        </v-card-actions>
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
      CourseCode: '', 
      CourseCodeRules: [
        v => !(this.msgIDs.includes(v || '')) || 
          `This code is already exists in ${this.CourseCodes}`
      ], 
      CourseName: '', 
      CourseNameRules: [
        v => (v || '').length <= 20 ||
          `The content exceeds the max length of 20`
      ], 
      Courses: [], 
      Users: [], 
      Comments: [], 
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
            // { MSG_ID: this.MSG_ID, MSG_CONTENT: this.MSG_CONTENT }, 
            data, 
            { headers: {'Content-Type': 'application/x-www-form-urlencoded'} }

        )
        .then((response) => { console.log(response) })
        .catch((error) => { console.log(error) })

        //location.reload()
      }
      
    }, 
    submitCourse(CourseCode, CourseName){
        // submit the course
        let data = new FormData()
        data.append(CourseCode + " " + CourseName)
        axios.post("http://127.0.0.1:3170/api/xxxxxxx/", 
            data, 
            {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}
        )
        .then((response) => { console.log(response) })
        .catch((error) => { console.log(error) })
    }, 
    deleteCourse(CourseID) {
        // TODO: 
    }, 
    deleteComment(CommentID) {

    }, 
    deleteUser(UserID) {

    }, 
    reset () {
      this.$refs.form.reset()
    }

  }, 
  created() {
    // TODO: to do 
    axios.get("http://127.0.0.1:3170/api/admin/").then((response) => {
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