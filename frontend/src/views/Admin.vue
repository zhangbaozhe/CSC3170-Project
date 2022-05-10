<template>
  <div id="admin">
    
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
        <v-select
          v-model="School"
          :items="Schools"
          label="School"
          required
          class="d-flex pa-2 ma-2"
        ></v-select>
        <v-select
          v-model="Credit"
          :items="Credits"
          label="Credits"
          required
          class="d-flex pa-2 ma-2"
        ></v-select>

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
        <v-card-title class="d-flex pa-2 ma-2">
            Course Code: {{ course.CourseName }}
        </v-card-title>
        <v-card-text class="d-flex pa-2 ma-2">
            Course Name: {{ course.CourseFullName }}
        </v-card-text>
        <v-card-actions>
            <v-btn color="error" class="mr-4" @click="deleteCourse(course.CourseID)">
                delete
            </v-btn>
        </v-card-actions>
    </v-card>

    <!-- List the comments and they can be deleted -->
    <v-card v-for="comment in Comments" v-bind:key="comment.url" class="d-flex pa-2 ma-2">
        <v-card-title class="d-flex pa-2 ma-2">
            User ID: {{ comment.UserID}}
            CommentID: {{ comment.CommentID }}
        </v-card-title>
        <v-card-text class="d-flex pa-2 ma-2">
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
        <v-card-title class="d-flex pa-2 ma-2">
            UserID: {{ user.UserID}}
        </v-card-title>
        <v-card-text class="d-flex pa-2 ma-2">
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
  name: "Admin",
  data: function () {
    // Notice that here the name mapping
    // CourseCode -> CourseName (backend)
    // CourseName -> CourseFullName (backend)
    return {
      info: "",
      valid: true, 
      School: "", 
      Credit: "", 
      Schools: ['SSE', 'SME', 'HSS', 'SDS'], 
      Credits: ['1', '2', '3'], 
      CourseCode: '', 
      CourseCodeRules: [
        v => !(this.CourseCodes.includes(v || '')) || 
          `This code is already exists in ${this.CourseCodes}`
      ], 
      CourseName: '', 
      CourseNameRules: [
        v => (v || '').length <= 20 ||
          `The content exceeds the max length of 20`
      ], 
      Courses: [], 
      CourseCodes: [], 
      Users: [], 
      Comments: [], 
    };
  },
  methods: {
    submitCourse(CourseCode, CourseName){
        // submit the course
        let data = new FormData()
        data.append("CourseName", this.CourseCode)
        data.append("CourseFullName", this.CourseName)
        data.append("School", this.School)
        data.append("Credits", this.Credit)
        axios.post("http://175.178.163.91:3170/api/admin/course/", 
            data, 
            {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}
        )
        .then((response) => { console.log(response) 
          location.reload()})        
        .catch((error) => { console.log(error) })
        
    }, 
    deleteCourse(CourseID) {
        axios.delete("http://175.178.163.91:3170/api/admin/course/", 
            //{headers: {'Content-Type': 'application/x-www-form-urlencoded'}}, 
            {data: {"id" : CourseID}}
        )
        .then((response)=>{
          console.log(response)
          location.reload()
        })
        
    }, 
    deleteComment(CommentID) {
        let data = new FormData()
        data.append("id", CommentID)
        axios.delete("http://175.178.163.91:3170/api/admin/comment/", 
        //{headers: {'Content-Type': 'application/x-www-form-urlencoded'}}, 
        {data: {"id" : CommentID}})
        .then((response)=>{
          console.log(response)
          location.reload()})
        
    }, 
    deleteUser(UserID) {
        let data = new FormData()
        data.append("id", UserID)
        axios.delete("http://175.178.163.91:3170/api/admin/user/", 
        //{headers: {'Content-Type': 'application/x-www-form-urlencoded'}}, 
        {data: {"id" : UserID}})
        .then((response)=>{
          console.log(response)
          location.reload()})
        
    }, 
    reset () {
      this.$refs.form.reset()
    }

  }, 
  created() {
    axios.get("http://175.178.163.91:3170/api/admin/all/").then((response) => {
      console.log(response)
      this.Courses = response.data.Courses;
      for (let i = 0; i < this.Courses.length; i++) {
        this.CourseCodes.push(this.Courses[i].CourseName)
      }
      this.Users = response.data.Users;
      this.Comments = response.data.Comments;
    });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>