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
<div style="width:100%; align:center;">
<v-card class="d-flex align-center mb-6`" color="grey lighten-2" flat height="100" style="width:400px; margin: auto; top: 200px;" tile>
  <v-card class="pa-2" outlined tile >
    <v-toolbar color="primary" dark flat>
      <v-toolbar-title align="center">登陆</v-toolbar-title>
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