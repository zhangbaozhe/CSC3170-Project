/* eslint-disable */
<template>
  <div>
    <div class="header">
      <el-row>
        <el-col :span="6">
          <img
            src="https://i.cuhk.edu.cn/static/assets/images/white-logo-4.png"
            alt="无法显示"
          />
        </el-col>
        <el-col :span="12">
          <br /><br />
          <h1>{{ this.courseName }}</h1>
        </el-col>
        <el-col :span="6">
          <br />
          <div>School: {{ this.school }}</div>
          <div>Credit:</div>
          <div>FinalScore: {{ this.FScore }}</div>
        </el-col>
      </el-row>
      <hr />
    </div>
    <br />
    <div class="box1">
      <ul class="list1">
        <li
          v-for="comment in CommentInfo"
          v-bind:key="comment.CommentID"
          id="comment"
        >
          <el-card class="box-card">
            <div slot="header" class="clearfix">
              <span>{{ comment.Username }}</span>
              <span>&nbsp;&nbsp;&nbsp;{{ comment.Score }}</span>

              <!-- 点踩 -->
              <v-btn
                class="ma-2"
                text
                icon
                :color="DisLikeColor1[comment.CommentID]"
                @click="OnClick([0, comment.CommentID])"
              >
                <v-icon>mdi-thumb-down</v-icon>
              </v-btn>
              
              <!-- 点赞 -->
              <v-btn
                class="ma-2"
                text
                icon
                :color="LikeColor1[comment.CommentID]"
                @click="OnClick([1, comment.CommentID])"
              >
                <v-icon>mdi-thumb-up</v-icon>
              </v-btn>

              <el-button
                style="float: right; padding: 3px 0"
                type="text"
                @click="open1(comment.CommentID)"
                >Response</el-button
              >
            </div>
            <div class="text">
              {{ comment.Content }}
              <br /><br />
            </div>
            <div>
              <el-row>
                <el-col :span="6"
                  ><div class="grid-content bg-purple">
                    Year: {{ comment.Year }}
                  </div></el-col
                >
                <el-col :span="6"
                  ><div class="grid-content bg-purple-light">
                    Semester: {{ comment.Semester }}
                  </div></el-col
                >
                <el-col :span="6"
                  ><div class="grid-content bg-purple">
                    Instructor: {{ comment.Instructor }}
                  </div></el-col
                >
                <el-col :span="6">
                  <div class="grid-content bg-purple">
                    <el-button
                      @click="get(comment.CommentID)"
                      type="primary"
                      style="margin-left: 16px"
                    >
                      Comments
                    </el-button>
                    <el-drawer
                      title="我是标题"
                      :visible.sync="drawer"
                      :with-header="false"
                      class="drawer1"
                    >
                     <li  v-for="mul in multiComment"
                    v-bind:key="mul.multiCommentID">
                      <el-card class="box-card">
                        <div slot="header" class="clearfix">
                          <!-- TODO: this is for multi comments, variables to be changed-->
                          <span>{{ mul.Username }}</span>
                        </div>
                        <span>{{ mul.Content }}</span>
                      </el-card>
                      </li>
                    </el-drawer>
                  </div>
                </el-col>
              </el-row>
            </div>
            <div></div>
          </el-card>
        </li>
      </ul>
    </div>
    <br /><br />
    <div class="box2">
      <div class="box2_1">
        <el-divider></el-divider>
        <el-row :gutter="40">
          <el-col :span="16">
            <el-select v-model="year" placeholder="Year" clearable>
              <el-option
                v-for="item in options1"
                :key="item.year"
                :label="item.label"
                :value="item.year"
              >
              </el-option>
            </el-select>
          </el-col>
          <el-col :span="8">
            <el-select v-model="semester" placeholder="Semeter" clearable>
              <el-option
                v-for="item in options2"
                :key="item.semester"
                :label="item.label"
                :value="item.semester"
              >
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <br />
        <el-row :gutter="40">
          <el-col :span="16">
            <div class="grid-content bg-purple">
              <el-input
                v-model="instructor"
                placeholder="Instructor"
              ></el-input>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content bg-purple">
              <div class="block">
                <span class="demonstration">Score</span>
                <el-rate v-model="score"></el-rate>
              </div>
            </div>
          </el-col>
        </el-row>
        <br />
        <el-row>
          <el-col :span="20"
            ><el-input
              type="textarea"
              :autosize="{ minRows: 2, maxRows: 4 }"
              placeholder="请输入内容"
              v-model="firstComment"
            >
            </el-input
          ></el-col>
          <el-col :span="4"
            ><el-button type="primary" @click="submit"
              >Submit</el-button
            ></el-col
          >
          <!-- todo @OnClick -->
        </el-row>
      </div>
    </div>
    <v-snackbar v-model="snackbar">
      {{ submitNotOKMsg }}
      <template v-slot:action="{ attrs }">
        <v-btn color="pink" text v-bind="attrs" @click="snackbar = false">
          close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "Course",
  data() {
    return {
      count: 0,
      instructor: "",
      comment: "",
      firstComment: "", //1's comment
      multiComment: [], // multi-comment
      multiInputContent: "",
      userID: "", // the user ID right now in this page
      commentedUserIDs: [], // TODO: be loaded with the user IDs who have commented
      submitNotOKMsg: "You have already submitted a comment!",
      snackbar: false,
      courseID: 0,
      courseName: "",
      school: "",
      credit: -1,
      FScore: -1,
      LikeColor: "grey",
      DisLikeColor: "grey",
      LikeColor1: {},
      DisLikeColor1: {},

      options1: [
        //year-table
        {
          year: "2018",
          label: "2018",
        },
        {
          year: "2019",
          label: "2019",
        },
        {
          year: "2020",
          label: "2020",
        },
        {
          year: "2021",
          label: "2021",
        },
        {
          year: "2022",
          label: "2022",
        },
      ],
      year: "", //year bind value

      options2: [
        {
          semester: "All",
          label: "All",
        },
        {
          semester: "Spring",
          label: "Spring",
        },
        {
          semester: "Autumn",
          label: "Autumn",
        },
      ],
      semester: "", //semester

      score: null, //score

      drawer: false,
      CommentInfo: [],
    };
  },
  methods: {
    load() {
      this.count += 2;
    },
    get(courseID) {
      this.drawer = true;
      axios.get("http://127.0.0.1:3170/api/seccomment/", {
            params: {
              parentID:courseID,
            }
          }).then((response) => {
      this.multiComment = response.data; 
    });
    console.log(this.multiComment);
    },
    isToSubmitOK() {
      return !this.commentedUserIDs.includes(this.userID);
    },

    submit() {
      // FIXME: edit Comments and other relation tables
      if (this.commentedUserIDs.includes(this.userID)) {
        snackbar = true;
        return;
      }
      const backendAPI = "http://127.0.0.1:3170/api/";
      let submitData = new FormData();
      submitData.append("USERID", this.userID);
      submitData.append("COURSEID", this.courseID);
      submitData.append("YEAR", this.year);
      submitData.append("SEMESTER", this.semester);
      submitData.append("INSTRUCTOR", this.instructor);
      submitData.append("SCORE", this.score);
      submitData.append("CONTENT", this.firstComment);
      submitData.append("LIKENUM", 0); // init to 0
      submitData.append("DISLIKENUM", 0); // init to 0
      axios
        .post(backendAPI + "course/submit_comment/", submitData, {
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
      // location.reload(); // reload the webpage after submit the comment
    },

    OnClick(num) {
      if (num[0] == 0) {
        //点踩
        console.log("点踩");
        console.log(num[1]);
        if (this.DisLikeColor1[num[1]] == "grey") {
          this.DisLikeColor1[num[1]] = "red";
          console.log("yes");
          if (this.LikeColor1[num[1]] == "red") {
            this.LikeColor1[num[1]] = "grey";
          }
        } 
        else if (this.DisLikeColor1[num[1]] == "red") {
          this.DisLikeColor1[num[1]] = "grey";
        }
        // console.log(this.DisLikeColor);
        console.log(num[1]);
      }  
      else if (num[0] == 1) {
        //点赞
        console.log("点赞");
        if (this.LikeColor1[num[1]] == "grey") {
          console.log("red now")
          this.LikeColor1[num[1]] = "red";
          if (this.DisLikeColor1[num[1]] == "red") {
            this.DisLikeColor1[num[1]] = "grey";
          }
        } else if (this.LikeColor1[num[1]] == "red") {
          console.log("grey now")
          this.LikeColor1[num[1]] = "grey";
        }
        // console.log(this.LikeColor)
        console.log(num[1]);
      }
    },
    open1(parentCommentID) {
      console.log(parentCommentID);
      this.$prompt("Please enter your response", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          this.$message({
            type: "success",
            message: "Successfully post your response",
          });
          this.multiInputContent = value;
          console.log(this.multiInputContent);
          const backendAPI = "http://127.0.0.1:3170/api/";
          let submitData = new FormData();
          submitData.append("USERID", this.userID);
          submitData.append("CONTENT", this.multiInputContent);
          submitData.append("ParentCommentID", parentCommentID);
          axios
          .post(backendAPI + "course/submit_sec_comment/", submitData, {
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
          })
          .then((response) => {
            console.log(response);
          })
          .catch((error) => {
            console.log(error);
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消输入",
          });
        });
    },
  },
  watch: {},
  created() {
    console.log("MOUNTED");
    this.userID = this.$store.state.userID;
    this.courseID = this.$route.params.id;
    axios
      .get("http://127.0.0.1:3170/api/course", {
        params: { courseID: this.$route.params.id },
      })
      .then((response) => {
        this.CommentInfo = response.data["Comments"];
        this.courseName = response.data["CourseName"];
        this.school = response.data["School"];
        this.FScore = response.data["FinalScore"];
        for (let i = 0; i < this.CommentInfo.length; i++) {
          // console.log(this.CommentInfo[i].likeList)
          // console.log(this.CommentInfo[i].dislikeList)
          if(this.CommentInfo[i].likeList.includes(this.userID)){
            this.LikeColor1[this.CommentInfo[i].CommentID] = "red";
          }
          else{
            this.LikeColor1[this.CommentInfo[i].CommentID] = "grey";
          }
          if(this.CommentInfo[i].dislikeList.includes(this.userID)){
            this.DisLikeColor1[this.CommentInfo[i].CommentID] = "red";
          }
          else{
            this.DisLikeColor1[this.CommentInfo[i].CommentID] = "grey";
          }
        };
        console.log(this.CommentInfo);
        // console.log(response.data);
        console.log(this.LikeColor1);
        console.log(this.DisLikeColor1);
      });
  },
};
</script>

<style scoped>
.text {
  font-size: 20px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 480px;
}
.box1 {
  width: 800px;
  /* max-height: 500px; */
  margin: 0 auto;
}
.box2 {
  width: 600px;
  /* max-height: 500px; */
  margin: 0 auto;
  border-radius: 4px;
}
.list1 {
  width: 800px;
  max-height: 600px;
  overflow: scroll;
  overflow-x: hidden;
  border-radius: 4px;
  list-style: none;
}
.box-card {
  width: 600px;
  margin: 0 auto;
}
.el-col {
  border-radius: 4px;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.box2_1 {
  width: 650px;
  height: 200px;
  border-radius: 4px;
}
.header {
  text-align: center;
  margin-top: 0px;
}
.el-textarea__inner {
  align-self: center;
}
.el-textarea {
  height: 20%;
  align-items: center;
}
.enter2 {
  height: 40px;
  margin: 100% auto;
}
.drawer1 {
  justify-content: space-between;
}

.ma-2 {
  float: right;
  padding: 3px 0;
  width: 22px;
  height: 22px;
}
</style>