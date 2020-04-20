<!--<template>
  <v-app id="inspire" align="center" justify="center">
    <v-content>
      <v-container class="fill-height" fluid dark>
        <v-row align-center justify-center>
          <v-col cols="12" sm="8" md="4">
            <v-card class="elevation-12">
              <v-toolbar color="primary" dark flat>
                <v-toolbar-title>登陆</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form>
                  <v-text-field label="登陆" name="login" prepend-icon="person" type="text" />
                  <v-text-field id="password" label="密码" name="password" prepend-icon="lock" type="password" />
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-spacer />
                <v-btn color="primary">登陆</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>-->

<template>
<div style="width:100%;">
  <v-card style="width:400px;" justify="center" >
    <v-toolbar color="primary" dark flat>
      <v-toolbar-title>登陆</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      <v-form>
        <v-text-field label="登陆" name="login" prepend-icon="person" type="text" />
        <v-text-field id="password" label="密码" name="password" prepend-icon="lock" type="password" />
      </v-form>
    </v-card-text>
    <v-card-actions>
      <v-spacer />
      <v-btn color="primary">登陆</v-btn>
    </v-card-actions>
  </v-card>
</div>
</template>

<script>
export default {
  name: "login",
  props: {
    source: String
  }
};
</script>