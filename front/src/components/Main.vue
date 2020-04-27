<template>
<div>
  <router-link to="/en">英文页面</router-link>
  <router-link to="/ch">中文页面</router-link>

</div>
</template>

<script>
export default {
  name: 'Main',
  data () {
    return {
      msg: '欢迎来到Vurtify的世界'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
