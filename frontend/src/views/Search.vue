<template>

<div>
    <div class='hd'>Hi!User</div>
    <el-divider></el-divider>
   <div style="margin-top: 15px;">
<div class='in'>
  <el-input placeholder="请输入内容" v-model="input" class="input-with-select">
    <el-button @click='View' slot="append" icon="el-icon-search"></el-button>
  </el-input>
</div>
</div>
<div class="md">
<el-select v-model="value1" class='md' placeholder="Department">
    <el-option
      v-for="item in options1"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
<el-select v-model="value2" class='md' placeholder="Subject">
    <el-option
      v-for="item in options2"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
</div>


  <ul>
    <li>
<div class = 'sc'>
   <el-card class="box-card">
  <div slot="header" class="clearfix">
    <span>
      CSC3170
    </span>
    <el-button @click="View" style="float: right;" type="primary">View</el-button>
  </div>
  <div class="text item">
  <el-row :gutter="20" class = 'rg'>
  <el-col :span="22"><div class="grid-content bg-purple">Score:n/5</div></el-col>
  <el-col :span="2"><div class="grid-content bg-purple">SDS</div></el-col>
  </el-row>
  <el-row :gutter="20" class = 'rg'>
  <el-col :span="22"><div class="grid-content bg-purple">n comments</div></el-col>
  <el-col :span="2"><div class="grid-content bg-purple">credicts:n</div></el-col>
  </el-row>
  </div>
</el-card>
    

<el-card class="box-card">
  <div slot="header" class="clearfix">
    <span>
      CSC3180
    </span>
    <el-button @click="View" style="float: right;" type="primary">View</el-button>
  </div>
  <div class="text item">
     <el-row :gutter="20" class = 'rg'>
  <el-col :span="22"><div class="grid-content bg-purple">Score:n/5</div></el-col>
  <el-col :span="2"><div class="grid-content bg-purple">SDS</div></el-col>
  </el-row>
  <el-row :gutter="20" class = 'rg'>
  <el-col :span="22"><div class="grid-content bg-purple">n comments</div></el-col>
  <el-col :span="2"><div class="grid-content bg-purple">credicts:n</div></el-col>
  </el-row>
  </div>
</el-card>

<el-card class="box-card">
  <div @click="View" slot="header" class="clearfix">
    <span>
      CSC3100
    </span>
    <el-button @click="View" style="float: right;" type="primary">View</el-button>
  </div>
  <div class="text item">
  <el-row :gutter="20" class = 'rg'>
  <el-col :span="22"><div class="grid-content bg-purple">Score:n/5</div></el-col>
  <el-col :span="2"><div class="grid-content bg-purple">SDS</div></el-col>
  </el-row>
  <el-row :gutter="20" class = 'rg'>
  <el-col :span="22"><div class="grid-content bg-purple">n comments</div></el-col>
  <el-col :span="2"><div class="grid-content bg-purple">credicts:n</div></el-col>
  </el-row>
  </div>
</el-card>

<el-card class="box-card">
  <div slot="header" class="clearfix">
    <span>
      CSC3001
    </span>
    <el-button @click="View" style="float: right;" type="primary">View</el-button>
  </div>
  <div class="text item">
   <el-row :gutter="20" class = 'rg'>
  <el-col :span="22"><div class="grid-content bg-purple">Score:n/5</div></el-col>
  <el-col :span="2"><div class="grid-content bg-purple">SDS</div></el-col>
  </el-row>
  <el-row :gutter="20" class = 'rg'>
  <el-col :span="22"><div class="grid-content bg-purple">n comments</div></el-col>
  <el-col :span="2"><div class="grid-content bg-purple">credicts:n</div></el-col>
  </el-row>
  </div>
</el-card>

<el-card class="box-card">
  <div slot="header" class="clearfix">
    <span>
      CSC3002
    </span>
   <el-button @click="View" style="float: right;" type="primary">View</el-button>
  </div>
  <div class="text item">
  <el-row :gutter="20" class = 'rg'>
  <el-col :span="22"><div class="grid-content bg-purple">Score:n/5</div></el-col>
  <el-col :span="2"><div class="grid-content bg-purple">SDS</div></el-col>
  </el-row>
  <el-row :gutter="20" class = 'rg'>
  <el-col :span="22"><div class="grid-content bg-purple">n comments</div></el-col>
  <el-col :span="2"><div class="grid-content bg-purple">credicts:n</div></el-col>
  </el-row>
  </div>
</el-card>
        </div>
    </li>
  </ul>
<div class='in'>
    推荐课程:
    <el-link href="https://www.baidu.com" target="_blank" type="primary">CSC3170</el-link>
    <el-link href="https://www.baidu.com" target="_blank" type="primary">CSC3170</el-link>
    <el-link href="https://www.baidu.com" target="_blank" type="primary">CSC3170</el-link>
    <el-link href="https://www.baidu.com" target="_blank" type="primary">CSC3170</el-link>
    <el-link href="https://www.baidu.com" target="_blank" type="primary">CSC3170</el-link>
    <el-link href="https://www.baidu.com" target="_blank" type="primary">CSC3170</el-link>
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
    clear: both
  }

  .box-card {
    width: 1000px;
    height: 200px;
    margin:0 auto;

  }
  .search {
    width: 10%;
  }
  .right{
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
  .rg{
    width: 100%;
  }
  .el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
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
  .md{
    margin:0 auto;
    width: 300px;
    height: 40px;
    display: flex;
  }
  .hd{
  font-size: 200%;
  text-align: right;
  height: 50px;
}
  .in{
      width: 60%;
      margin:0 auto;
  }
  .sc{
      width: 1000px;
      height: 800px;
      overflow: scroll;
      overflow-x: hidden;
      margin:0 auto;  
  }
</style>

<script>

export default {
  data() {
    return {
      input: '',
      options1: [{
          value: '选项0',
          label: 'all'
        }, {
          value: '选项1',
          label: 'SDS'
        }, {
          value: '选项2',
          label: 'SSE'
        }, {
          value: '选项3',
          label: 'HSS'
        }, {
          value: '选项4',
          label: 'SME'
        }, {
          value: '选项5',
          label: 'BIO'
        }],
        options2: [{
          value: '选项0',
          label: 'all'
        }, {
          value: '选项1',
          label: 'CSC'
        }, {
          value: '选项2',
          label: 'MAT'
        }, {
          value: '选项3',
          label: 'DDA'
        }, {
          value: '选项4',
          label: 'STA'
        }, {
          value: '选项5',
          label: 'ECO'
        },], 
        value1: '',
        value2: '',
    }
  },
  methods:{
    View(){
      window.open('https://www.baidu.com')
    }
  }
};
</script>