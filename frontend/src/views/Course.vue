/* eslint-disable */
<template>
  <div>
    <div class="header">
      <el-row>
        <el-col :span="6">
          <img
            src="https://i.cuhk.edu.cn/static/assets/images/white-logo-4.png/"
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
          <div>Credit: {{ this.credit }}</div>
          <div>FinalScore: {{ this.FScore }}</div>
        </el-col>
      </el-row>
      <hr />
    </div>
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
                icon
                :color="DisLikeColor1[comment.CommentID]"
                @click="OnClick([0, comment.CommentID])"
              >
                <v-icon>mdi-thumb-down</v-icon
                ><span>{{ DisLikeNum[comment.CommentID] }}</span>
              </v-btn>

              <!-- 点赞 -->
              <v-btn
                class="ma-2"
                icon
                :color="LikeColor1[comment.CommentID]"
                @click="OnClick([1, comment.CommentID])"
              >
                <v-icon>mdi-thumb-up</v-icon
                ><span>{{ LikeNum[comment.CommentID] }}</span>
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
                      <li
                        v-for="mul in multiComment"
                        v-bind:key="mul.multiCommentID"
                      >
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
    <v-snackbar v-model="scoreSnackbar">
      You have not scored yet!
      <template v-slot:action="{ attrs }">
        <v-btn color="pink" text v-bind="attrs" @click="scoreSnackbar = false">
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
      mulCommentedUserIDs: [],
      submitNotOKMsg: "You have already submitted a comment!",
      snackbar: false,
      scoreSnackbar: false,
      courseID: 0,
      courseName: "",
      school: "",
      credit: -1,
      FScore: -1,
      LikeColor: "grey",
      DisLikeColor: "grey",
      LikeColor1: {},
      DisLikeColor1: {},
      LikeList1: {},
      DisLikeList1: {},
      LikeNum: {},
      DisLikeNum: {},

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
      axios
        .get("http://127.0.0.1:3170/api/seccomment/", {
          params: {
            parentID: courseID,
          },
        })
        .then((response) => {
          this.multiComment = response.data;
          console.log(this.multiComment);
        });
    },

    submit() {
      if (this.commentedUserIDs.includes(this.userID)) {
        console.log("HELLLLLLLLLLLLLLLLL");
        this.snackbar = true;
        return;
      }
      if (this.score == 0) {
        console.log("HELLLLLLLL");
        this.scoreSnackbar = true;
        return;
      }
      console.log(this.score);
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
      //  location.reload(); // reload the webpage after submit the comment
    },

    OnClick(num) {
      let tmpStatus = 0; // 判断是否已点过赞/踩
      if (
        this.DisLikeColor1[num[1]] == "grey" &&
        this.LikeColor1[num[1]] == "grey"
      ) {
        tmpStatus = 0;
      }
      if (
        this.LikeColor1[num[1]] == "red" &&
        this.DisLikeColor1[num[1]] == "grey"
      ) {
        tmpStatus = 1;
      }
      if (
        this.DisLikeColor1[num[1]] == "red" &&
        this.LikeColor1[num[1]] == "grey"
      ) {
        tmpStatus = 2;
      }
      if (
        this.DisLikeColor1[num[1]] == "red" &&
        this.LikeColor1[num[1]] == "red"
      ) {
        console.log("both red");
      }
      if (num[0] == 0) {
        //点踩
        if (this.DisLikeColor1[num[1]] == "grey") {
          this.DisLikeColor1[num[1]] = "red";
          this.DisLikeNum[num[1]] = this.DisLikeNum[num[1]] + 1;
          if (this.LikeColor1[num[1]] == "red") {
            this.LikeColor1[num[1]] = "grey";
            this.LikeNum[num[1]] = this.LikeNum[num[1]] - 1;
          }
        } else if (this.DisLikeColor1[num[1]] == "red") {
          this.DisLikeColor1[num[1]] = "grey";
          this.DisLikeNum[num[1]] = this.DisLikeNum[num[1]] - 1;
        }
      } else if (num[0] == 1) {
        //点赞
        if (this.LikeColor1[num[1]] == "grey") {
          this.LikeColor1[num[1]] = "red";
          this.LikeNum[num[1]] = this.LikeNum[num[1]] + 1;
          if (this.DisLikeColor1[num[1]] == "red") {
            this.DisLikeColor1[num[1]] = "grey";
            this.DisLikeNum[num[1]] = this.DisLikeNum[num[1]] - 1;
          }
        } else if (this.LikeColor1[num[1]] == "red") {
          this.LikeColor1[num[1]] = "grey";
          this.LikeNum[num[1]] = this.LikeNum[num[1]] - 1;
        }
      }
      if (tmpStatus == 0) {
        //没操作过
        if (
          this.LikeColor1[num[1]] == "grey" &&
          this.DisLikeColor1[num[1]] == "grey"
        ) {
          tmpStatus = 0; //操作过，但又变成不点赞不点踩
        } else if (
          this.LikeColor1[num[1]] == "red" &&
          this.DisLikeColor1[num[1]] == "grey"
        ) {
          tmpStatus = 1;
        } else if (
          this.LikeColor1[num[1]] == "grey" &&
          this.DisLikeColor1[num[1]] == "red"
        ) {
          tmpStatus = 2;
        } else {
          console.log("something goes wrong");
        }
        this.$axios.post("http://127.0.0.1:3170/api/like/", {
          userID: this.userID,
          status: tmpStatus,
          commentID: num[1],
          likeNum: this.LikeNum[num[1]],
          dislikeNum: this.DisLikeNum[num[1]],
        });
      } else {
        if (
          this.LikeColor1[num[1]] == "grey" &&
          this.DisLikeColor1[num[1]] == "grey"
        ) {
          tmpStatus = 0;
        } else if (
          this.LikeColor1[num[1]] == "red" &&
          this.DisLikeColor1[num[1]] == "grey"
        ) {
          tmpStatus = 1;
        } else if (
          this.LikeColor1[num[1]] == "grey" &&
          this.DisLikeColor1[num[1]] == "red"
        ) {
          tmpStatus = 2;
        } else {
          console.log("something went wrong");
        }
        this.$axios
          .put("http://127.0.0.1:3170/api/like/", {
            userID: this.userID,
            status: tmpStatus,
            commentID: num[1],
            likeNum: this.LikeNum[num[1]],
            dislikeNum: this.DisLikeNum[num[1]],
          });
      }
    },
    open1(parentCommentID) {
      this.mulCommentedUserIDs = [];
      axios
        .get("http://127.0.0.1:3170/api/mulcomment/", {
          params: {
            parentID: parentCommentID,
          },
        })
        .then((response) => {
          for (let i = 0; i < response.data.length; i++) {
            if (
              !this.mulCommentedUserIDs.includes(response.data[i]["UserID"])
            ) {
              this.mulCommentedUserIDs.push(response.data[i]["UserID"]);
            }
          }
        });
      this.$prompt("Please enter your response", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          this.multiInputContent = value;
          if (this.mulCommentedUserIDs.includes(this.userID)) {
            this.$message({
              type: "info",
              message: "You have already submitted a second comment",
            });
            return;
          } else if (
            this.multiInputContent == null ||
            this.multiInputContent.replace(/[ ]/g, "").length == 0
          ) {
            this.$message({
              type: "info",
              message: "Comment cannot be empty",
            });
          } else {
            console.log(this.multiInputContent);
            const backendAPI = "http://127.0.0.1:3170/api/";
            let submitData = new FormData();
            submitData.append("USERID", this.userID);
            submitData.append("CONTENT", this.multiInputContent);
            submitData.append("ParentCommentID", parentCommentID);
            axios
              .post(backendAPI + "seccomment/", submitData, {
                headers: {
                  "Content-Type": "application/x-www-form-urlencoded",
                },
              })
              .then((response) => {
                console.log(response);
              })
              .catch((error) => {
                console.log(error);
              });
            this.$message({
              type: "success",
              message: "Successfully post your response",
            });
          }
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
    // console.log(this.LikeColor1);
    // console.log(this.DisLikeColor1);
    axios
      .get("http://127.0.0.1:3170/api/course/", {
        params: { courseID: this.$route.params.id },
      })
      .then((response) => {
        this.CommentInfo = response.data["Comments"];
        this.courseName = response.data["CourseName"];
        this.school = response.data["School"];
        this.FScore = response.data["FinalScore"];
        this.credit = response.data["Credits"];
        // TODO: to check this
        this.commentedUserIDs = response.data["CommentedUsers"];
        for (let i = 0; i < this.CommentInfo.length; i++) {
          this.$set(
            this.LikeList1,
            this.CommentInfo[i].CommentID,
            this.CommentInfo[i].likeList
          );
          this.$set(
            this.DisLikeList1,
            this.CommentInfo[i].CommentID,
            this.CommentInfo[i].dislikeList
          );
          this.$set(
            this.LikeNum,
            this.CommentInfo[i].CommentID,
            this.CommentInfo[i].LikeNum
          );
          this.$set(
            this.DisLikeNum,
            this.CommentInfo[i].CommentID,
            this.CommentInfo[i].DislikeNum
          );

          if (this.CommentInfo[i].likeList.includes(this.userID)) {
            this.$set(this.LikeColor1, this.CommentInfo[i].CommentID, "red");
          } else {
            this.$set(this.LikeColor1, this.CommentInfo[i].CommentID, "grey");
          }
          if (this.CommentInfo[i].dislikeList.includes(this.userID)) {
            this.$set(this.DisLikeColor1, this.CommentInfo[i].CommentID, "red");
          } else {
            this.$set(
              this.DisLikeColor1,
              this.CommentInfo[i].CommentID,
              "grey"
            );
          }
        }
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
  background-color: purple;
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
.butt {
  float: right;
  padding: 3px 0;
  width: 30px;
  height: 30px;
}
</style>