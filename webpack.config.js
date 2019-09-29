const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
var WebpackNotifierPlugin = require('webpack-notifier');

module.exports = {
    mode: 'development',
    context: __dirname,
    entry: './assets/js/app',
    output: {
        path: path.resolve('./assets/bundles/'),
        filename: 'app.js'
    },

    plugins: [
        new BundleTracker({filename: './webpack-stats.json'}),
        new VueLoaderPlugin(),
        new MiniCssExtractPlugin({
            filename: "app.css"
        }),
        new WebpackNotifierPlugin({
            alwaysNotify: true,
        }),
    ],

    module: {
        rules:  [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
            {
                test: /\.s[ac]ss$/i,
                use: [
                    {
                        loader: MiniCssExtractPlugin.loader
                    }, 
                    {
                        loader: "css-loader",
                    },
                    {
                        loader: "sass-loader",
                    }
                ],
            },
        ],
        
    },
    resolve: {
        alias: {vue: 'vue/dist/vue.js'}
    },
};