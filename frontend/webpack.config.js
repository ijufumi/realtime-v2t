const path = require("path");
const webpack = require('webpack');

module.exports = {
    entry: "./src/index.tsx",
    module: {
        rules: [
            {
                test: /\.(tsx|jsx)?$/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: [
                            '@babel/preset-env',
                            '@babel/preset-typescript',
                            '@babel/react'
                        ],
                        plugins: [
                            '@babel/plugin-proposal-class-properties'
                        ]
                    }
                },
                exclude: /node_modules/
            },
            {
                test: /\.css$/,
                loader: ["style-loader", "css-loader"]
            },
            {
                test: /\.(png|jpe?g|gif|svg|woff|woff2|ttf|eot|ico)$/,
                use: {
                    loader: 'file-loader?name=assets/[name].[hash].[ext]'
                }
            }
        ]
    },
    resolve: {
        extensions: [".tsx", ".ts", ".js", ".jsx", ".css"]
    },
    output: {
        path: path.resolve(__dirname, "dist"),
        filename: "bundle.js"
    },
    plugins: [
        new webpack.DefinePlugin({
            'process.env.REACT_APP_API_ENDPOINT': JSON.stringify(process.env.REACT_APP_API_ENDPOINT)
        }),
    ],
    devServer: {
        contentBase: path.join(__dirname, "dist"),
        compress: true,
        open: true,
        port: 9000
    }
};
