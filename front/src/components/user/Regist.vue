<template>
  <v-app id="inspire" style="background-color:grey;">
      <v-card style="width:600px;margin:auto; ">
        <v-card-title class="grey darken-2">创建联系人</v-card-title>
        <v-container>
          <v-row class="mx-2">
            <v-col class="align-center justify-space-between" cols="12">
              <v-row align="center" class="mr-0">
                <v-avatar size="40px" class="mx-3">
                  <img src="//ssl.gstatic.com/s2/oz/images/sge/grey_silhouette.png" alt />
                </v-avatar>
                <v-text-field placeholder="名称" />
              </v-row>
            </v-col>
            <v-col cols="6">
              <v-text-field prepend-icon="mdi-account-card-details-outline" placeholder="公司" />
            </v-col>
            <v-col cols="6">
              <v-text-field placeholder="职称" />
            </v-col>
            <v-col cols="12">
              <v-text-field prepend-icon="mdi-mail" placeholder="邮箱" />
            </v-col>
            <v-col cols="12">
              <v-text-field type="tel" prepend-icon="mdi-phone" placeholder="(+86) 18000000000" />
            </v-col>
            <v-col cols="12">
              <v-text-field prepend-icon="mdi-text" placeholder="备注" />
            </v-col>
          </v-row>
        </v-container>
        <v-card-actions>
          <v-btn text color="primary">更多</v-btn>
          <v-spacer />
          <v-btn text color="primary" @click="dialog = false">取消</v-btn>
          <v-btn text @click="dialog = false">保存</v-btn>
        </v-card-actions>
      </v-card>
  </v-app>
</template>

<script>
export default {
  name: 'Regist',
  props: {
    source: String
  },
  components: {
  },
  data () {
    return {
    }
  }
}
</script>
