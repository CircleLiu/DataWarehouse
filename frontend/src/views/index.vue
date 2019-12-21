<template>
<el-container>
        <el-header>
            <el-menu
            :default-active="activeIndex2"
            class="el-menu-demo"
            mode="horizontal"
            @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b">
            <el-menu-item index="/homeindex" @click="onclick0">AMAZON DATA</el-menu-item>
            <el-menu-item index="/graphdata" @click="onclick1">GRAPH COMPUTATION</el-menu-item>
            </el-menu>
        </el-header>
    <el-container>
        <el-aside width="200px"></el-aside>

        <el-main>
        <el-card class="box-card">
        <div class="Add condition">
            <h3>ADDED CONDITION</h3>
            <el-row>
              <el-button icon="el-icon-search" circle></el-button>
               <el-button icon="el-icon-refresh-right" circle></el-button>
              </el-row>
            <el-table
            :data="tableData"
            stripe
            style="width: 100%">
            <el-table-column
            prop="ADD/OR"
            label="ADD/OR"
            width="180">
            </el-table-column>
            <el-table-column
            prop="FIELD"
            label="FIELD">
            </el-table-column>
            <el-table-column
            prop="CONDITION"
            label="CONDITION">
            </el-table-column>
            <el-table-column
            prop="VALUE"
            label="VALUE">
            </el-table-column>
            <el-table-column label="操作" >
          <template slot-scope="scope">
               <el-button @click.native.prevent="deleteRow()" size="small"> 移除 </el-button>
               </template>
        </el-table-column> 
            </el-table>
        </div>
    <el-divider></el-divider>
         <div>
        <h3>ADD CONDITION</h3>
         <div class="line"> 
             <p>ADD/OR</p>
             <p>FIELD</p>
             <p>CONDITION</p>
             <p>VALUE</p>
             <p>ADD</p>
         </div>
         <div class="select"> 
            <el-select style="width:10%" v-model="value0" placeholder="ADD">
                <el-option
                v-for="item in options0"
                :key="item.value0"
                :label="item.label0"
                :value="item.value0">
                </el-option>
            </el-select>
               <el-select style="width:20%;padding-left:25px" v-model="value1" placeholder="Field">
                <el-option
                v-for="item in options1"
                :key="item.value1"
                :label="item.label1"
                :value="item.value1">
                </el-option>
            </el-select>
            <el-select style="width:10%;padding-left:65px"  v-model="value2" placeholder="!=">
                <el-option
                v-for="item in options2"
                :key="item.value2"
                :label="item.label2"
                :value="item.value2">
                </el-option>
            </el-select>
            <el-input style="width:17%;padding-left:45px" v-model="input" placeholder="请输入内容"></el-input>
            <el-button style="margin-left:39px" type="success" plain @click="addRow()">ADD</el-button>
         </div>
         </div>
        </el-card>

        <el-card class="box-card">
        <div class="text item">
            <h3>Results</h3>
            <el-table
            :data="infiledList"
            stripe
            style="width: 100%">
            <el-table-column
            prop="product_id"
            label="PRODUCT ID"
            >
            </el-table-column>
            <el-table-column
            prop="title"
            label="TITLE">
            </el-table-column>
            <el-table-column
            prop="price"
            label="PRICE">
            </el-table-column>
            <el-table-column
            prop="time"
            label="TIME">
            </el-table-column>
          <el-table-column
            prop="sales rank"
            label="SALES RANK">
            </el-table-column>
            <el-table-column
            prop="publication date"
            label="PUBLICATION DATE	">
            </el-table-column>
         
              <el-table-column
            prop="release date"
            label="RELEASE DATE">
            </el-table-column>
              <el-table-column
            prop="version count"
            label="VERSION COUNT">
            </el-table-column>
               <el-table-column
            prop="binding"
            label="BINDING">
            </el-table-column>
            </el-table>
        </div>
        </el-card>

        </el-main>
        <el-aside width="200px"></el-aside>
    </el-container>
</el-container>
</template >

<script>
  export default {
    data() {
      return {
        options0: [{
          value0: '选项1',
          label0: 'ADD'
        }, {
          value0: '选项2',
          label0: 'OR'
        }],
        options1: [{
          value1: '选项1',
          label1: 'Movie'
        },{
          value1: '选项2',
          label1: 'Actor'
        },{
          value1: '选项3',
          label1: 'Author'
        },{
          value1: '选项4',
          label1: 'Language'
        },{
          value1: '选项13',
          label1: 'Binding'
        },{
          value1: '选项6',
          label1: 'Genre'
        },{
          value1: '选项7',
          label1: 'Studio'
        },{
          value1: '选项8',
          label1: 'ReleaseDate'
        },{
          value1: '选项9',
          label1: 'Rrice'
        },{
          value1: '选项10',
          label1: 'Running Time'
        },{
          value1: '选项11',
          label1: 'Sales Rank'
        },{
          value1: '选项12',
          label1: 'Version Count'
        },{
          value1: '选项5',
          label1: 'Director'
        },],
        options2: [{
          value2: '选项1',
          label2: '!='
        }, {
          value2: '选项2',
          label2: '='
        }],
          navList:[
            {name:'/homeindex',navItem:'发现项目'},
            {name:'/graphdata',navItem:'社区动态'},
        ],
        value0: '',
        value1: '',
        value2: ''
      }
    },
    methods: {
    onclick0() {
      this.$router.push({ path: "/homeindex" });
    },
     onclick1() {
      this.$router.push({ path: "/graphdata" });
    },
      deleteRow() {//删除该行
                rows.splice();
              },
     addRow(){
       tableData.push({ })
     }
  }
  };
</script>
<style>
  .el-header{
    background-color: #333;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
  .line,select{
      display:flex;
      flex-flow: row

  }
  p{
      color: #909399;
      position: relative;
    word-wrap: normal;
    text-overflow: ellipsis;
    display: inline-block;
    vertical-align: middle;
    width: 100%;
    box-sizing: border-box;
    white-space: normal;
    word-break: break-all;
    line-height: 23px;
    padding-left: 10px;
    padding-right: 10px;
    overflow: hidden;
    text-align: left;
    font-weight: bold;
        font-size: 14px;
  }
  .input{
      margin:20px;
  }
</style>