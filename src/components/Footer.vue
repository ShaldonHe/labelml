<template>
    <v-footer dark>
      <span
        style="text-align: center; margin:0 auto; width:100%; height:40px;"
      >Copyright {{date}} © {{corporation}}</span>
    </v-footer>
</template>
<script>
export default {
    name: "footer",
    data () {
        return {
            date: "2020",
            corporation: "北京贝叶科技有限公司" 
        }
    }
    
}
</script>