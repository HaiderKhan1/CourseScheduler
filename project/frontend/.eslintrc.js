module.exports = {
  env: {
    browser: true,
    es2021: true
  },
  settings: {
    react: {
      version: "detect"
    }
  },
  extends: [
    'plugin:react/recommended',
    'standard'
  ],
  overrides: [
  ],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module'
  },
  plugins: [
    'react'
  ],
  rules: {
    "multiline-ternary": "off",
    "react/prop-types": "off",
    semi: "off",
    quotes: "off",
    "space-before-function-paren": "off",
    "comma-dangle": "off",
  },
}
