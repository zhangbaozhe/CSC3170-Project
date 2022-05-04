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
          <h1>CSC3170</h1>
        </el-col>
        <el-col :span="6">
          <br />
          <div>School:</div>
          <div>Credit:</div>
          <div>FScore:</div>
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
                :color="DisLikeColor"
                @click="OnClick([0, comment.CommentID])"
              >
                <v-icon>mdi-thumb-down</v-icon>
              </v-btn>

              <!-- 点赞 -->
              <v-btn
                class="ma-2"
                text
                icon
                :color="LikeColor"
                @click="OnClick([1, comment.CommentID])"
              >
                <v-icon>mdi-thumb-up</v-icon>
              </v-btn>

              <el-button
                style="float: right; padding: 3px 0"
                type="text"
                @click="open1"
                >Response</el-button
              >
            </div>
            <div class="text">
              {{ comment.C }}
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
                      @click="drawer = true"
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
                      <el-card class="box-card">
                        <div slot="header" class="clearfix">
                          <span>{{ comment.MUserName }}</span>
                        </div>
                        <span>{{ comment.Content }}</span>
                      </el-card>
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

  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "Course",
  data() {
    return {

      count: 0,
      instructor: "", //instructor TODO: to be submitted
      comment: "",
      firstComment: "", //1's comment
      multiComment: "", // multi-comment
      userID: "",
      courseID: "1", // TODO: to be passed from Search
      LikeColor: "grey",
      DisLikeColor: "grey",
      LikeColor1: [],
      DisLikeColor1: [],

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

    submit() {
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
      submitData.append("CREDITS", 3);
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

        console.log(this.firstComment); //just for test
      } else if (num == 1) {

        if (this.DisLikeColor == "grey") {
          this.DisLikeColor = "red";
          console.log("yes");
          if (this.LikeColor == "red") {
            this.LikeColor = "grey";
          }
        } else if (this.DisLikeColor == "red") {
          this.DisLikeColor = "grey";
        }
        // console.log(this.DisLikeColor);
        console.log(num[1]);
      } else if (num[0] == 1) {
        //点赞

        console.log("点赞");
        if (this.LikeColor == "grey") {
          this.LikeColor = "red";
          if (this.DisLikeColor == "red") {
            this.DisLikeColor = "grey";
          }
        } else if (this.LikeColor == "red") {
          this.LikeColor = "grey";
        }
        // console.log(this.LikeColor)
        console.log(num[1]);
      }
    },
    open1() {
      this.$prompt("Please enter your response", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
      })
        .then(({ value }) => {
          this.$message({
            type: "success",
            message: "Successfully post your response",
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
    this.courseID = this.$route.params.id
    axios.get("http://127.0.0.1:3170/api/course", {
        params:{courseID: this.$route.params.id}
      }
    ).then((response) => {
      this.CommentInfo = response.data;
      console.log(this.courseID)
      // console.log(this.CommentInfo[0].CommentID);
      // console.log(this.CommentInfo[1].CommentID);
      console.log(response.data);
      console.log(response.data);
      for (let i = 0; i < this.CommentInfo.length; i++) {
        let key = this.CommentInfo[i].CommentID;
        let value = { [key]: "gery" };
        this.LikeColor1.push(value);
        this.DisLikeColor1.push(value);
        console.log(this.LikeColor1);
        console.log(this.LikeColor1);
        console.log(this.DisLikeColor1[1]);
        console.log(this.DisLikeColor1[2]);
      }
    });

    // console.log(this.LikeColor1);
    // console.log(this.LikeColor1);
    // console.log(this.DisLikeColor1[1]);
    // console.log(this.DisLikeColor1[2]);

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