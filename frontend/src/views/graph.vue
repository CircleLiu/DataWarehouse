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
          
            <el-menu-item index="/" @click="onclick0">AMAZON DATA</el-menu-item>
            <el-menu-item index="/graphdata" @click="onclick1">GRAPH COMPUTATION</el-menu-item>
            </el-menu>
        </el-header>
    <el-container>
        <el-aside width="200px"></el-aside>
        <el-main>
            <div class="one">
                <el-card class="box-card">
                    <div class="text item">
                   <h3> 1. 演员 X 合作演员名单</h3>
                       <el-row>
                       <el-input v-model="input[0]" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" @click="onsearch('actor_with_actor', 0)" circle></el-button>
                       </el-row>
                    <h4>Running Time: {{timeuse[0]}} ms</h4>
                        <el-table
                            :data="tableData[0]"
                            stripe
                            style="width: 100%">
                            <el-table-column
                            prop="name"
                            label="NAME"
                            >
                            </el-table-column>
                            <el-table-column
                            prop="count"
                            label="COUNT"
                            >
                            </el-table-column>
                        </el-table>
                    </div>
                </el-card>
            </div>
            <div class="two">
                <el-card class="box-card">
                    <div class="text item">
                     <h3> 2. 演员 X 合作导演名单</h3>
                       <el-row>
                       <el-input v-model="input[1]" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" @click="onsearch('actor_with_director', 1)" circle></el-button>
                       </el-row>
                    <h4>Running Time: {{timeuse[1]}} ms</h4>
                        <el-table
                            :data="tableData[1]"
                            stripe
                            style="width: 100%">
                            <el-table-column
                            prop="name"
                            label="NAME"
                            >
                            </el-table-column>
                            <el-table-column
                            prop="count"
                            label="COUNT"
                            >
                            </el-table-column>
                        </el-table>
                    </div>
                 </el-card>
            </div>
            <div class="three">
                <el-card class="box-card">
                    <div class="text item">
                     <h3> 3. 导演 X 合作演员名单</h3>
                       <el-row>
                       <el-input v-model="input[2]" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" @click="onsearch('director_with_actor', 2)" circle></el-button>
                       </el-row>
                    <h4>Running Time: {{timeuse[2]}} s</h4>
                        <el-table
                            :data="tableData[2]"
                            stripe
                            style="width: 100%">
                            <el-table-column
                            prop="name"
                            label="NAME"
                            >
                            </el-table-column>
                            <el-table-column
                            prop="count"
                            label="COUNT"
                            >
                            </el-table-column>
                        </el-table>
                    </div>
                </el-card>
            </div>
            <div class="four">
                <el-card class="box-card">
                    <div class="text item">
                     <h3> 4.导演 X 合作导演名单</h3>
                       <el-row>
                       <el-input v-model="input[3]" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" @click="onsearch('director_with_director', 3)" circle></el-button>
                       </el-row>
                    <h4>Running Time: {{timeuse[3]}} ms</h4>
                        <el-table
                            :data="tableData[3]"
                            stripe
                            style="width: 100%">
                            <el-table-column
                            prop="name"
                            label="NAME"
                            >
                            </el-table-column>
                            <el-table-column
                            prop="count"
                            label="COUNT"
                            >
                            </el-table-column>
                        </el-table>
                    </div>
                </el-card>
            </div>
            <div class="five">
                <el-card class="box-card">
                    <div class="text item">
                     <h3> 5. TOP N 演员合作演员数</h3>
                       <el-row>
                       <el-input v-model="input[4]" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" @click="onsearch('collaboration_of_actor', 4)" circle></el-button>
                       </el-row>
                    <h4>Running Time: {{timeuse[4]}} ms</h4>
                        <el-table
                            :data="tableData[4]"
                            stripe
                            style="width: 100%">
                            <el-table-column
                            prop="name1"
                            label="NAME"
                            ></el-table-column>
                            <el-table-column
                            prop="name2"
                            label="NAME"
                            ></el-table-column>
                            <el-table-column
                            prop="count"
                            label="COUNT"
                            ></el-table-column>
                        </el-table>
                    </div>
                </el-card>
            </div>
            <div class="six">
                <el-card class="box-card">
                    <div class="text item">
                     <h3> 6. TOP N 演员合作导演数</h3>
                       <el-row>
                       <el-input v-model="input[5]" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" @click="onsearch('collaboration_of_director_and_actor', 5)" circle></el-button>
                       </el-row>
                    <h4>Running Time: {{timeuse[5]}} ms</h4>
                        <el-table
                            :data="tableData[5]"
                            stripe
                            style="width: 100%">
                            <el-table-column
                            prop="actor"
                            label="ACTOR"
                            >
                            </el-table-column>
                            <el-table-column
                            prop="director"
                            label="DIRECTOR"
                            >
                            </el-table-column>
                            <el-table-column
                            prop="count"
                            label="COUNT"
                            >
                            </el-table-column>
                        </el-table>
                    </div>
                </el-card>
            </div>
            <div class="seven">
                <el-card class="box-card">
                    <div class="text item">
                     <h3> 7. TOP N 导演合作导演数</h3>
                       <el-row>
                       <el-input v-model="input[6]" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" @click="onsearch('collaboration_of_director', 6)" circle></el-button>
                       </el-row>
                    <h4>Running Time: {{timeuse[6]}} ms</h4>
                        <el-table
                            :data="tableData[6]"
                            stripe
                            style="width: 100%">
                            <el-table-column
                            prop="name1"
                            label="NAME"
                            >
                            </el-table-column>
                            <el-table-column
                            prop="name2"
                            label="NAME"
                            >
                            </el-table-column>
                            <el-table-column
                            prop="count"
                            label="COUNT"
                            >
                            </el-table-column>
                        </el-table>
                    </div>
                </el-card>
            </div>
        </el-main>
        <el-aside width="200px"></el-aside>
    </el-container>
</el-container>
</template >

<script>
  export default {
     
  data() {
    return {
      input: ['','','','','','','',''],
      timeuse: [0, 0, 0, 0, 0, 0, 0, 0],
      tableData: [[],[],[],[],[],[],[],[]]
    }
  },

    methods: {
    onclick0() {
      this.$router.push({ path: "/" });
    },
     onclick1() {
      this.$router.push({ path: "/graphdata" });
    },
    onsearch(methodName, index) {
        var start = Date.now()
        this.$axios({
         method: 'POST',
         url: 'http://127.0.0.1:5000/' + methodName,
         data: {name: this.input[index]},
         timeout: 60000
       })
       .then((response) => {
           this.timeuse[index] = Date.now() - start
          
          this.$set(this.tableData, index, response.data)
        })
        .catch((res) => {
            console.log(res)
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
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }
  
</style>