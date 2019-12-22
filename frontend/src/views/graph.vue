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
                       <el-input v-model="input0" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" circle></el-button>
                       </el-row>
                    <h4>Running Time: 0 s</h4>
                        <el-table
                            :data="tableData"
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
                       <el-input v-model="input1" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" circle></el-button>
                       </el-row>
                    <h4>Running Time: 0 s</h4>
                        <el-table
                            :data="tableData"
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
                       <el-input v-model="input2" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" circle></el-button>
                       </el-row>
                    <h4>Running Time: 0 s</h4>
                        <el-table
                            :data="tableData"
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
                       <el-input v-model="input3" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" circle></el-button>
                       </el-row>
                    <h4>Running Time: 0 s</h4>
                        <el-table
                            :data="tableData"
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
                       <el-input v-model="input4" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" circle></el-button>
                       </el-row>
                    <h4>Running Time: 0 s</h4>
                        <el-table
                            :data="tableData"
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
            <div class="six">
                <el-card class="box-card">
                    <div class="text item">
                     <h3> 6. TOP N 演员合作导演数</h3>
                       <el-row>
                       <el-input v-model="input5" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" circle></el-button>
                       </el-row>
                    <h4>Running Time: 0 s</h4>
                        <el-table
                            :data="tableData"
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
             <div class="seven">
                <el-card class="box-card">
                    <div class="text item">
                     <h3> 7. TOP N 导演合作演员数</h3>
                       <el-row>
                       <el-input v-model="input6" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" circle></el-button>
                       </el-row>
                    <h4>Running Time: 0 s</h4>
                        <el-table
                            :data="tableData"
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
            <div class="eight">
                <el-card class="box-card">
                    <div class="text item">
                     <h3> 8. TOP N 导演合作导演数</h3>
                       <el-row>
                       <el-input v-model="input7" placeholder="请输入内容" style="width:30%;padding-right:20px"></el-input>
                       <el-button icon="el-icon-search" circle></el-button>
                       </el-row>
                    <h4>Running Time: 0 s</h4>
                        <el-table
                            :data="tableData"
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
        </el-main>
        <el-aside width="200px"></el-aside>
    </el-container>
</el-container>
</template >

<script>
  export default {
     
  data() {
    return {
      input0: '',
      input1: '',
      input2: '',
      input3: '',
      input4: '',
      input5: '',
      input6: '',
      input7: ''
    }
  },

    methods: {
    onclick0() {
      this.$router.push({ path: "/" });
    },
     onclick1() {
      this.$router.push({ path: "/graphdata" });
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