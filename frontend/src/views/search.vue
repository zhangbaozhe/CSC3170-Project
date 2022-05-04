<template>
  <div>
    <div class="hd">Hi!User</div>
    <el-divider></el-divider>
    <div style="margin-top: 15px">
      <div class="in">
        <el-input
          placeholder="请输入内容"
          v-model="input"
          class="input-with-select"
        >
          <el-button
            @click="View"
            slot="append"
            icon="el-icon-search"
          ></el-button>
        </el-input>
      </div>
    </div>
    <div class="md">
      <el-select v-model="value1" class="md" placeholder="Department">
        <el-option
          v-for="item in options1"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <el-select v-model="value2" class="md" placeholder="Subject">
        <el-option
          v-for="item in options2"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
    </div>

    <div class="sc">
      <el-card class="box-card" v-for="inf in info" v-bind:key="inf.CourseID">
        <div slot="header" class="clearfix">
          <span>
            {{ inf.CourseName }}
          </span>
          <el-button
            @click="View(inf.CourseID)"
            style="float: right"
            type="primary"
            >View</el-button
          >
        </div>
        <div class="text item">
          <el-row :gutter="20" class="rg">
            <el-col :span="22"
              ><div class="grid-content bg-purple">
                Score:{{ inf.a }}/5
              </div></el-col
            >
            <el-col :span="2"
              ><div class="grid-content bg-purple">
                {{ inf.School }}
              </div></el-col
            >
          </el-row>
          <el-row :gutter="20" class="rg">
            <el-col :span="22"
              ><div class="grid-content bg-purple">
                {{ inf.count }} comments
              </div></el-col
            >
            <el-col :span="2"
              ><div class="grid-content bg-purple">
                credicts:{{ inf.Credits }}
              </div></el-col
            >
          </el-row>
        </div>
      </el-card>

      <el-card class="box-card" v-for="inf in info2" v-bind:key="inf.CourseID">
        <div slot="header" class="clearfix">
          <span>
            {{ inf.CourseName }}
          </span>
          <el-button
            @click="View(inf.CourseID)"
            style="float: right"
            type="primary"
            >View</el-button
          >
        </div>
        <div class="text item">
          <el-row :gutter="20" class="rg">
            <el-col :span="22"
              ><div class="grid-content bg-purple">
                Score: No comment yet
              </div></el-col
            >
            <el-col :span="2"
              ><div class="grid-content bg-purple">
                {{ inf.School }}
              </div></el-col
            >
          </el-row>
          <el-row :gutter="20" class="rg">
            <el-col :span="22"
              ><div class="grid-content bg-purple">0 comments</div></el-col
            >
            <el-col :span="2"
              ><div class="grid-content bg-purple">
                credicts:{{ inf.Credits }}
              </div></el-col
            >
          </el-row>
        </div>
      </el-card>
    </div>

    <div class="in">
      推荐课程:
      <el-link href="https://www.baidu.com" target="_blank" type="primary"
        >CSC3170</el-link
      >
      <el-link href="https://www.baidu.com" target="_blank" type="primary"
        >CSC3170</el-link
      >
      <el-link href="https://www.baidu.com" target="_blank" type="primary"
        >CSC3170</el-link
      >
      <el-link href="https://www.baidu.com" target="_blank" type="primary"
        >CSC3170</el-link
      >
      <el-link href="https://www.baidu.com" target="_blank" type="primary"
        >CSC3170</el-link
      >
      <el-link href="https://www.baidu.com" target="_blank" type="primary"
        >CSC3170</el-link
      >
    </div>
  </div>
</template>


<style>
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
  width: 1000px;
  height: 200px;
  margin: 0 auto;
}
.search {
  width: 10%;
}
.right {
  text-align: right;
}
.el-row {
  margin-bottom: 20px;
  &:last-child {
    margin-bottom: 0;
  }
}
.el-col {
  border-radius: 4px;
}
.bg-purple-dark {
}
.bg-purple {
}
.bg-purple-light {
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.rg {
  width: 100%;
}
.el-dropdown-link {
  cursor: pointer;
  color: #409eff;
}
.el-icon-arrow-down {
  font-size: 12px;
}
.el-select .el-input {
  width: 130px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
.md {
  margin: 0 auto;
  width: 300px;
  height: 40px;
  display: flex;
}
.hd {
  font-size: 200%;
  text-align: right;
  height: 50px;
}
.in {
  width: 60%;
  margin: 0 auto;
}
.sc {
  width: 1000px;
  height: 800px;
  overflow: scroll;
  overflow-x: hidden;
  margin: 0 auto;
}
</style>

<script>
import axios from "axios";

export default {
  data() {
    return {
      input: "",
      options1: [
        {
          value: "all",
          label: "all",
        },
        {
          value: "SDS",
          label: "SDS",
        },
        {
          value: "SSE",
          label: "SSE",
        },
        {
          value: "HSS",
          label: "HSS",
        },
        {
          value: "SME",
          label: "SME",
        },
        {
          value: "BIO",
          label: "BIO",
        },
      ],
      options2: [
        {
          value: "all",
          label: "all",
        },
        {
          value: "CSC",
          label: "CSC",
        },
        {
          value: "MAT",
          label: "MAT",
        },
        {
          value: "DDA",
          label: "DDA",
        },
        {
          value: "STA",
          label: "STA",
        },
        {
          value: "ECO",
          label: "ECO",
        },
      ],
      value1: "",
      value2: "",
      info: [],
      info2: [],
    };
  },
  methods: {
    View(i) {
      console.log("yes");
      window.open("http://localhost:8080/course/" + i);
      console.log(i);
    },
  },
  created() {
    axios.get("http://127.0.0.1:3170/api/search/").then((response) => {
      this.info = response.data;
      console.log(this.info);
    });
    axios.get("http://127.0.0.1:3170/api/search0/").then((response) => {
      this.info2 = response.data;
      console.log(this.info2);
    });
  },
  watch: {
    value1: {
      handler(val) {
        console.log(val);
        axios
          .get("http://127.0.0.1:3170/api/search1/", {
            params: {
              Department: val,
            },
          })
          .then((response) => {
            this.info = response.data;
            console.log(this.info);
          });
        axios
          .get("http://127.0.0.1:3170/api/search2/", {
            params: {
              Department: val,
            },
          })
          .then((response) => {
            this.info2 = response.data;
            console.log(this.info2);
          });
      },
    },
  },
};
</script>