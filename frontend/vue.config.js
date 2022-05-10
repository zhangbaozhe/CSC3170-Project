const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ], 
})

module.exports = {
  devServer: {
    proxy: 'http://175.178.163.91:3170'
  }
}