/* eslint-disable */
<template>
    <div>
        <div class="header">
            

            <el-row>
                <el-col :span="6">
                    <img src="https://i.cuhk.edu.cn/static/assets/images/white-logo-4.png" alt="无法显示">   
                </el-col>
                <el-col :span="12">
                        <br/><br/>
                        <h1>CSC3170</h1>
                        
                </el-col>
                <el-col :span="6">
                    <br/>
                    <div>
                        School:
                    </div>
                    <div>
                        Credit:
                    </div>
                    <div>
                        FScore:
                    </div>

                </el-col>
            </el-row>
            <hr>
        </div>
        <br/>
        <div class = "box1">
            <ul class = "list1">
                <li>
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>用户名</span>
                            <span>&nbsp;&nbsp;&nbsp;给分</span>
                            
                            <el-button style="float: right; padding: 3px 0" type="text" @click="OnClick(0)">点踩</el-button>
                            <el-button style="float: right; padding: 3px 0" type="text" @click="OnClick(1)">点赞</el-button>
                            <el-button style="float: right; padding: 3px 0" type="text" @click="open1">Response</el-button>
                            
                        </div>
                        <div class="text">
                            content
                            <br/><br/>
                        </div>
                        <div>
                            <el-row>
                                <el-col :span="6"><div class="grid-content bg-purple">Year:</div></el-col>
                                <el-col :span="6"><div class="grid-content bg-purple-light">Semester:</div></el-col>
                                <el-col :span="6"><div class="grid-content bg-purple">Instructor:</div></el-col>
                                <el-col :span="6">
                                    <div class="grid-content bg-purple">
                                        <el-button @click="drawer = true" type="primary" style="margin-left: 16px;">
                                            Comments
                                        </el-button>
                                        <el-drawer title="我是标题" :visible.sync="drawer" :with-header="false" class="drawer1">
                                            <el-card class="box-card">
                                                <div slot="header" class="clearfix">
                                                    <span>James</span>
                                                </div>
                                                <span>What do u mean?</span>
                                            </el-card>
                                        </el-drawer>
                                    </div>
                                </el-col>
                            </el-row>
                        </div>
                        <div>
                            
                        </div>
                    </el-card>
                </li>
                <li>
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>用户名</span>
                            <span>&nbsp;&nbsp;&nbsp;给分</span>
                            <el-button style="float: right; padding: 3px 0" type="text">点踩</el-button>
                            <el-button style="float: right; padding: 3px 0" type="text">点赞</el-button>
                        </div>
                        <div class="text">
                            content
                            <br/><br/>
                        </div>
                        <div>
                            <el-row>
                                <el-col :span="8"><div class="grid-content bg-purple">Year:</div></el-col>
                                <el-col :span="8"><div class="grid-content bg-purple-light">Semester:</div></el-col>
                                <el-col :span="8"><div class="grid-content bg-purple">Instructor:</div></el-col>
                            </el-row>
                        </div>
                    </el-card>
                </li>
                <li>
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>用户名</span>
                            <span>&nbsp;&nbsp;&nbsp;给分</span>
                            <el-button style="float: right; padding: 3px 0" type="text">点踩</el-button>
                            <el-button style="float: right; padding: 3px 0" type="text">点赞</el-button>
                        </div>
                        <div class="text">
                            content
                            <br/><br/>
                        </div>
                        <div>
                            <el-row>
                                <el-col :span="8"><div class="grid-content bg-purple">Year:</div></el-col>
                                <el-col :span="8"><div class="grid-content bg-purple-light">Semester:</div></el-col>
                                <el-col :span="8"><div class="grid-content bg-purple">Instructor:</div></el-col>
                            </el-row>
                        </div>
                    </el-card>
                </li>
                <li>
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>用户名</span>
                            <span>&nbsp;&nbsp;&nbsp;给分</span>
                            <el-button style="float: right; padding: 3px 0" type="text">点踩</el-button>
                            <el-button style="float: right; padding: 3px 0" type="text">点赞</el-button>
                        </div>
                        <div class="text">
                            content
                            <br/><br/>
                        </div>
                        <div>
                            <el-row>
                                <el-col :span="8"><div class="grid-content bg-purple">Year:</div></el-col>
                                <el-col :span="8"><div class="grid-content bg-purple-light">Semester:</div></el-col>
                                <el-col :span="8"><div class="grid-content bg-purple">Instructor:</div></el-col>
                            </el-row>
                        </div>
                    </el-card>
                </li>
            </ul>
        </div>
        <br/><br/>
        <div class = 'box2'>
            <div class="box2_1">
                <el-divider></el-divider>
                <el-row :gutter="40">
                <el-col :span="16">
                        <el-select v-model="value1" placeholder="Year" clearable>
                            <el-option
                            v-for="item in options1"
                            :key="item.value1"
                            :label="item.label"
                            :value="item.value1">
                            </el-option>
                        </el-select>
                </el-col>
                <el-col :span="8">
                    <el-select v-model="value2" placeholder="Semeter" clearable>
                            <el-option
                            v-for="item in options2"
                            :key="item.value2"
                            :label="item.label"
                            :value="item.value2">
                            </el-option>
                        </el-select>
                </el-col>
            </el-row>
            <br>
            <el-row :gutter="40">
            <el-col :span="16">
                <div class="grid-content bg-purple">
                    <el-input v-model="instructor" placeholder="Instructor"></el-input>
                </div>
            </el-col>
            <el-col :span="8">
                <div class="grid-content bg-purple">
                    <div class="block">
                        <span class="demonstration">Score</span>
                        <el-rate v-model="value3"></el-rate>
                    </div>
                </div>
            </el-col>
            </el-row>
            <br/>
            <el-row>
                <el-col :span="20"><el-input type="textarea" :autosize="{ minRows: 2, maxRows: 4}" placeholder="请输入内容" v-model="textarea2"> </el-input></el-col>
                <el-col :span="4"><el-button type="primary">Submit</el-button></el-col>
            </el-row>
            
            </div>
        </div>
        
    </div>
</template>

<script>
    export default {
        name: 'PageSix',
         data () {
            return {
                count: 0,
                instructor: '',
                comment:'',
                textarea2: '',
                textarea3: '',

                options1: [{
                value1: '选项1',
                label: '2018'
                }, {
                value1: '选项2',
                label: '2019'
                }, {
                value1: '选项3',
                label: '2020'
                }, {
                value1: '选项4',
                label: '2021'
                }, {
                value1: '选项5',
                label: '2022'
                }],
                value1: '',

                options2: [{
                value2: '选项1',
                label: 'All'
                }, {
                value2: '选项2',
                label: 'Spring'
                }, {
                value2: '选项3',
                label: 'Autumn'
                }, {
                value2: '选项4',
                label: 'HSS'
                }, ],
                value2: '',

                value3: null,
                drawer: false,
            }
            },
        methods: {
            load () {
                this.count += 2
            },
            OnClick(num){
                if(num == 0){
                    console.log('点踩')
                }
                else if(num == 1){
                    console.log('点赞')
                }
            },
            open1() {
                this.$prompt('Please enter your response', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                }).then(({ value }) => {
                this.$message({
                    type: 'success',
                    message: 'Successfully post your response'
                });
                }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '取消输入'
                });       
                });
            }
        },
        watch:{
            
        }

    }
</script>

<style scoped>
    .text {
    font-size: 28px;
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
    width: 480px;
  }
  .box1{
      width: 800px;
      /* max-height: 500px; */
      margin:0 auto;
  }
    .box2{
    width: 600px;
    /* max-height: 500px; */
    margin:0 auto;
    border-radius: 4px
  }
  .list1{
      width: 800px;
      max-height: 600px;
      overflow: scroll;
      overflow-x: hidden;
      border-radius: 4px;
  }
  .box-card{
      width: 600px;
      margin:0 auto;
  }
  .el-row {
    /* margin-bottom: 20px; */
    /* width:600px; */
  }
  .el-col {
    border-radius: 4px;
  }
  /* .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  } */
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .box2_1{
      width: 650px;
      height:200px;
      border-radius: 4px;
  }
  .header {
        text-align: center;
        margin-top: 0px;
    }
    .el-textarea__inner{
        align-self: center;
    }
    .el-textarea{
        height: 20%;
        align-items: center;
    }
    .enter2{
        height: 40px;
        margin:100% auto;
    }
    .drawer1{
        justify-content: space-between;
    }
</style>