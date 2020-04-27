<template>
  <v-app id="inspire">
    <v-navigation-drawer :clipped="$vuetify.breakpoint.lgAndUp" v-model="drawer" app>
      <v-list dense rounded>
        <template v-for="item in items">
          <v-row v-if="item.heading" :key="item.heading" align="center">
            <v-col cols="6">
              <v-subheader v-if="item.heading">{{ item.heading }}</v-subheader>
            </v-col>
            <v-col cols="6" class="text-center">
              <a href="#!" class="body-2 black--text">编辑</a>
            </v-col>
          </v-row>
          <v-list-group
            v-else-if="item.children"
            :key="item.text"
            v-model="item.model"
            :prepend-icon="item.model ? item.icon : item['icon-alt']"
            append-icon
          >
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title>{{ item.text }}</v-list-item-title>
              </v-list-item-content>
            </template>
            <v-list-item v-for="(child, i) in item.children" :key="i" link>
              <v-list-item-action v-if="child.icon">
                <v-icon>{{ child.icon }}</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>{{ child.text }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
          <v-list-item v-else :key="item.text" link>
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ item.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar :clipped-left="$vuetify.breakpoint.lgAndUp" app color="blue darken-3" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title style="width: 300px" class="ml-0 pl-4">
        <span class="hidden-sm-and-down">查看标注</span>
      </v-toolbar-title>
      <v-text-field
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="mdi-magnify"
        label="搜索"
        class="hidden-sm-and-down"
      />
      <v-spacer />
      <v-btn icon large>
        <v-icon>mdi-apps</v-icon>
      </v-btn>
      <v-btn icon large>
        <v-icon>mdi-bell</v-icon>
      </v-btn>
      <v-btn icon large>
        <v-avatar size="36px" item>
          <v-img src="static/logo.png" alt="贝叶科技" />
        </v-avatar>
      </v-btn>
    </v-app-bar>
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center"></v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'Viewer',
  props: {
    source: String
  },
  components: {
  },
  data () {
    return {
      dialog: false,
      drawer: null,
      items: [
        { icon: 'mdi-contacts', text: '联系人' },
        { icon: 'mdi-history', text: '最近联系' },
        { icon: 'mdi-content-copy', text: '重复' },
        {
          icon: 'mdi-chevron-up',
          'icon-alt': 'mdi-chevron-down',
          text: '标签',
          model: true,
          children: [{ icon: 'mdi-plus', text: '创造标签' }]
        },
        {
          icon: 'mdi-chevron-up',
          'icon-alt': 'mdi-chevron-down',
          text: '更多',
          model: false,
          children: [
            { text: '导入' },
            { text: '导出' },
            { text: '打印' },
            { text: '撤销更改' },
            { text: '其他联系人' }
          ]
        },
        { icon: 'mdi-settings', text: '设置' },
        { icon: 'mdi-message', text: '反馈' },
        { icon: 'mdi-help-circle', text: '帮助' },
        { icon: 'mdi-cellphone-link', text: '下载App' },
        { icon: 'mdi-keyboard', text: '使用旧版本' }
      ]
    }
  }
}
</script>
