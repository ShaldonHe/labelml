<template>


  <v-app dark>
    <v-toolbar class="dark">
      <v-toolbar-title v-text="title"></v-toolbar-title>
    </v-toolbar>
    <main>
      <section>
        <v-parallax src="/static/skin-1.jpg" weight="600">
        
          <v-layout
            column
            align-center
            justify-center
            class="white--text"
          >
            <h1 class="white--text mb-2 display-3">皮肤病理切片标注</h1>
            <div class="headline mb-3 text-xs-center">深度融合皮肤病理场景的智能标注系统</div>
            <div><v-btn
              class="blue lighten-2 mt-5"
              dark
              large
              ripple
              to='/project/example_data'
            >
            Demo
            </v-btn>
                        <v-btn
              class="blue lighten-2 mt-5"
              dark
              large
              ripple
              to='/login'
            >登陆
            </v-btn>
                        <v-btn
              class="blue lighten-2 mt-5"
              dark
              large
              ripple
              to='/regist'
            >
            注册
            </v-btn></div>
            
          </v-layout>
        </v-parallax>
      </section>

      <section>
        <v-layout
          column
          wrap
          class="my-5"
          align-center
        >
          <v-flex xs12>
            <v-container grid-list-xl>
              <v-layout row wrap align-center>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">color_lens</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">直观的用户界面</div>
                    </v-card-title>
                    <v-card-text>
                      系统引入可扩充的快捷键交互, 智能编辑工具以加速皮肤病理切片的标注.
                    </v-card-text>
                  </v-card>
                </v-flex>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">flash_on</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline">AI加速</div>
                    </v-card-title>
                    <v-card-text>
                      AI加持,可定制的深度学习模型,以及主动学习策略,加速整个标注流程.
                    </v-card-text>
                  </v-card>
                </v-flex>
                <v-flex xs12 md4>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="blue--text text--lighten-2">build</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">深度融合医疗场景</div>
                    </v-card-title>
                    <v-card-text>
                      结合医疗场景,引入病史,病患信息,皮肤采样部位等临床场景中的多模态信息以辅助标注过程,增加标注的精确度!
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
      </section>

      <section>
        <v-parallax src="/static/skin.jpg" height="380">
          <v-layout column align-center justify-center>
            <div class="headline white--text mb-3">高效,便捷,准确的标注皮肤病理切片</div>
            <em>贝叶科技-BeYes</em>
            <v-btn
              class="blue lighten-2 mt-5"
              dark
              large
              href="/pre-made-themes"
            >
              开始标注
            </v-btn>
          </v-layout>
        </v-parallax>
      </section>

      <section>
        <v-container grid-list-xl>
          <v-layout row wrap justify-center class="my-5">
            <v-flex xs12 sm4>
              <v-card class="elevation-0 transparent">
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline">公司信息</div>
                </v-card-title>
                <v-card-text>
                  贝叶科技-智能皮肤病理分析领域引导者.
                </v-card-text>
              </v-card>
            </v-flex>
            <v-flex xs12 sm4 offset-sm1>
              <v-card class="elevation-0 transparent">
                <v-card-title primary-title class="layout justify-center">
                  <div class="headline">联系我们</div>
                </v-card-title>
                <v-list class="transparent">
                  <v-list-tile>
                    <v-list-tile-action>
                      <v-icon class="blue--text text--lighten-2">place</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                      <v-list-tile-title>中国北京市海淀区西小口东升科技园北领地C1-108</v-list-tile-title>
                    </v-list-tile-content>
                  </v-list-tile>
                  <v-list-tile>
                    <v-list-tile-action>
                      <v-icon class="blue--text text--lighten-2">email</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                      <v-list-tile-title>sheldon.he@be-yes.com</v-list-tile-title>
                    </v-list-tile-content>
                  </v-list-tile>
                </v-list>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </section>

      <v-footer class="blue darken-2">
        <v-layout row wrap align-center>
          <v-flex xs12>
            <div class="white--text ml-3">
              本系统由北京贝叶科技有限公司技术部数据组运营
              <v-icon class="red--text">favorite</v-icon>
            </div>
          </v-flex>
        </v-layout>
      </v-footer>
    </main>
  </v-app>  
</template>

<script>


export default {
  name: 'home',
  components: {},
  props: [],
  data () {
      return {
          drawer: true,
          title: 'BeYes皮肤病理标注系统'
      }
  }
}
</script>


<style scoped>

</style>