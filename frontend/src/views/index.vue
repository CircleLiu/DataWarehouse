/* eslint-disable */
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
              <el-button icon="el-icon-search" @click="search" circle></el-button>
               <el-button icon="el-icon-refresh-right" @click="cleartable" circle></el-button>
            </el-row>
            <el-table
            :data="tableData"
            stripe
            style="width: 100%">
            <el-table-column
            prop="ao"
            label="AND/OR">
            </el-table-column>
            <el-table-column
            prop="field"
            label="FIELD">
            </el-table-column>
            <el-table-column
            prop="condition"
            label="CONDITION">
            </el-table-column>
            <el-table-column
            prop="value"
            label="VALUE">
            </el-table-column>
            <el-table-column label="操作" >
          <template slot-scope="scope">
               <el-button @click.native.prevent="deleteRow(scope.$index)" size="small"> 移除 </el-button>
               </template>
        </el-table-column> 
            </el-table>
        </div>
    <el-divider></el-divider>
         <div>
        <h3>ADD CONDITION</h3>
         <el-row :gutter="20" class="line"> 
             <el-col :span=5>
              <p>AND/OR</p>
             </el-col>
             <el-col :span=5>
              <p>FIELD</p>
             </el-col>
             <el-col :span=5>
               <p>CONDITION</p>
               </el-col>
             <el-col :span=7>
               <p>VALUE</p>
               </el-col>
             
         </el-row>
         <el-row :gutter="20" class="select"> 
           <el-col :span=5>
              <el-select v-model="value0" placeholder="ADD">
                  <el-option
                  v-for="item in options0"
                  :key="item.value0"
                  :label="item.label0"
                  :value="item.value0">
                  </el-option>
              </el-select>
           </el-col>
           <el-col :span=5>
              <el-select v-model="value1" placeholder="Field">
                <el-option
                v-for="item in options1"
                :key="item.value1"
                :label="item.label1"
                :value="item.value1">
                </el-option>
              </el-select>
           </el-col>
           <el-col :span=5>
            <el-select v-model="value2" placeholder="=">
                <el-option
                v-for="item in options2"
                :key="item.value2"
                :label="item.label2"
                :value="item.value2">
                </el-option>
            </el-select>
           </el-col>
           <el-col :span=7>
            <el-input v-model="input" placeholder="请输入内容"></el-input>
           </el-col>
           <el-col :span=2>
            <el-button type="success" plain @click="addRow()">ADD</el-button>
           </el-col>
         </el-row>
         </div>
        </el-card>

        <el-card class="box-card">
        <div class="text item">
            <h3>RESULT</h3>
            <h4>Total: {{total_num}} items</h4>
            <h4>Running Time: {{timeuse}} ms</h4>
            <el-table
            :data="infiledList"
            stripe
            style="width: 100%">
            <el-table-column
            prop="asin"
            label="PRODUCT ID"
            >
            </el-table-column>
            <el-table-column
            prop="name"
            label="TITLE">
            </el-table-column>
            <el-table-column
            prop="price"
            label="PRICE">
            </el-table-column>
            <el-table-column
            prop="running_time"
            label="TIME">
            </el-table-column>
          <el-table-column
            prop="rank"
            label="SALES RANK">
            </el-table-column>
            <el-table-column
            prop="publication_date"
            label="PUBLICATION DATE	">
            </el-table-column>
         
              <el-table-column
            prop="release_date"
            label="RELEASE DATE">
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
          value0: 'AND',
          label0: 'AND'
        }, {
          value0: 'OR',
          label0: 'OR'
        }],
        options1: [{
          value1: 'asin',
          label1: 'Product ID'
        },{
          value1: 'name',
          label1: 'Movie'
        },{
          value1: 'actor',
          label1: 'Actor'
        },{
          value1: 'director',
          label1: 'Director'
        },{
          value1: 'author',
          label1: 'Author'
        },{
          value1: 'language',
          label1: 'Language'
        },{
          value1: 'media',
          label1: 'Media'
        },{
          value1: 'genre',
          label1: 'Genre'
        },{
          value1: 'studio',
          label1: 'Studio'
        },{
          value1: 'release_date',
          label1: 'Release Date'
        },{
          value1: 'price',
          label1: 'Price'
        },{
          value1: 'running_time',
          label1: 'Running Time'
        },{
          value1: 'rank',
          label1: 'Sales Rank'
        },{
          value1: 'VersionCount',
          label1: 'Version Count'
        },],
        options2: [{
          value2: '!=',
          label2: '!='
        }, {
          value2: '=',
          label2: '='
        }, {
          value2: '>',
          label2: '>'
        }, {
          value2: '<',
          label2: '<'
        }, {
          value2: '>=',
          label2: '>='
        }, {
          value2: '<=',
          label2: '<='
        }, {
          value2: 'like',
          label2: 'like'
        }],
          navList:[
            {name:'/homeindex',navItem:'发现项目'},
            {name:'/graphdata',navItem:'社区动态'},
        ],
        value0: '',
        value1: '',
        value2: '',
        input: '',
        total_num: 0,
        timeuse: 0,
        tableData: [],
        infiledList: [],
      }
    },
    methods: {
    onclick0() {
      this.$router.push({ path: "/" });
    },
     onclick1() {
      this.$router.push({ path: "/graphdata" });
    },
      deleteRow(index) {
        this.tableData.splice(index, 1)
      },
     addRow(){
       this.tableData.push({
         ao: this.value0,
         field: this.value1,
         condition: this.value2,
         value: this.input
       })
     },
     search() {
       var start = Date.now()
       this.$axios({
         method: 'POST',
         url: 'http://127.0.0.1:5000/getproduct',
         data: this.tableData,
         timeout: 60000
       })
       .then((response) => {
          this.timeuse = Date.now() - start
          this.total_num = response.data.length
          this.infiledList = response.data
        })
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

  .el-col {
    text-align: left;
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