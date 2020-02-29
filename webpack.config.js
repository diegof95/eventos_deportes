const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    entry: {
        css_libs: __dirname + '/css_libs.js'
    },
    output: {
        filename: '[name].js',
        path: __dirname + '/static/dist'
    },
    mode: 'development',
    module: {
        rules: [
          {
            test: /\.css$/,
            use: [MiniCssExtractPlugin.loader, 'css-loader']
          }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
             filename: '[name].css',
        })
    ]
};