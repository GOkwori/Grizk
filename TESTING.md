# Testing

![Profile Page](./documentation/responsiveness/intro_screen.PNG)


This is the TESTING file for the [grizk](https://ecommerce-grizk-2f04b3042fc5.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

## Testing Contents  
  
- [Testing](#testing)
  - [Testing Contents](#testing-contents)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [JavaScript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [CSS Validation](#css-validation)
    - [Lighthouse Scores](#lighthouse-scores)
    - [Wave Accessibility Score](#wave-accessibility-score)
  - [Manual Testing](#manual-testing)
    - [User Input/Form Validation](#user-inputform-validation)
    - [Browser Compatibility](#browser-compatibility)
    - [Responsiveness](#responsiveness)
    - [Testing User Stories](#testing-user-stories)
    - [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Bugs](#bugs)
    - [Unresolved/Known Bugs](#unresolvedknown-bugs)

## Validation

### `HTML Validation`

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

I have had to follow a different approach for validating my HTML for this project as the majority of my pages are developed using Jinja syntax such as '{% extends "base.html" %}' and '{{ form|crispy }}' and most require user authentication. The HTML validator will throw errors if I were to use my website's URL so I have had to follow the below approach for every page:

- Via the deployed Heroku app link, I have navigated to each individual page.
- Right clicking on the screen/CTRL+U/⌘+U on Mac, allows a menu to appear, giving me the option to 'View page source'.
- The complete HTML code for the deployed page will appear, allowing you to select the entire code using CTRL+A/⌘+A on Mac.
- Paste the copied code into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, revalidate by following the above steps and record the results.

![html validation](./documentation/testing/validation/html/home.PNG) 

All HTML pages were validated and received a 'No errors or warning to show' for code that I had written, result as shown above.

| HTML Source Code/Page | Errors | Warnings | Status |
| ---- | ------ | -------- | -------- |
| `Home` | None | None | Passed |
|`Log In` | None | None | Passed |
| `Log Out` | None | None | Passed |
| `Register` | 4 | 0 | During the development of Grizk, several template rendering issues were encountered, particularly involving the integration with Django Allauth. Errors such as unclosed <span> elements, stray tags, and incorrectly structured help text were identified. These issues primarily resulted from how form fields and help texts were being rendered in custom templates. ![html validation](./documentation/testing/validation/html/register_error.PNG)  | 
| `Account` | None | None | Passed | 
| `Wishlist` | None | None | Passed |
| `Admin Dashboard` | None | None | Passed | 
| `Admin Blog List` | None | None | Passed |
| `Admin Add Blog` | None | None | Passed | 
| `Admin Edit Blog` | None | None | Passed |
| `Admin Product List` | None | None | Passed |
| `Admin Product Detail` | None | None | Passed |
| `Admin Add Product` | None | None | Passed |
| `Admin Edit Product` | None | None | Passed |
| `Admin Delete Product` | None | None | Passed |
| `All Products` | None | None | Passed |
| `User Blog List` |None | None | Passed |
| `Cart - Empty` | None | None | Passed | 
| `Checkout` | None | None | Passed |
| `Checkout-success` | None | None | Passed |
| `Blog` | None | None | Passed |
| `Profile/Account` | None | None | Passed |
| `Order History` | None | None | Passed |
| `Wishlist` | None | None | Passed |
| `Forgot Password` | None | None | Passed |
| `Error 403` | None | None | Passed |
| `Error 404` | None | None | Passed |
| `Error 500` | None | None | Passed |


### `JavaScript Validation`

[JSHint](https://jshint.com/) was used to validate the JavaScript code implemented in the Grizk platform. External JS files utilized for Bootstrap, jQuery, and FontAwesome were excluded from this validation process to focus on custom scripts developed for the project.

| Page | Screenshot | Errors | 
| ---- | ---------- | ------ | 
|` Home`  | ![JS from Static folder](./documentation/testing/validation/js/base_js.PNG) | none | 
| `Base Script` | ![JS from Template section](./documentation/testing/validation/js/base_script.PNG) | none | 
| `Cart - Quantity Script` | ![JS from Cart page](./documentation/testing/validation/js/cart_script.PNG) | none | 
| `Stripe Payment Integration` | ![JS from Stripe elements](./documentation/testing/validation/js/checkout_js.PNG) | none | 
| `Products Filtering Script` | ![JS from product filtering script](./documentation/testing/validation/js/product_script.PNG) | none | 
| `CountryField JS` | ![JS from profile script](./documentation/testing/validation/js/profile_js.PNG) | none | 


### Python Validation

The [CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate all Python files created and edited within the project. No issues were detected, and all line lengths were verified to conform to PEP8 standards. Below is a table summarizing the validation results, accompanied by screenshots showing the successful validation of each component. Entries marked as "Not applicable" indicate that no Python files were relevant or created for that feature.

| Feature   | admin  | forms  | models  | urls  | views  | App  |
|-----------|--------|--------|---------|-------|--------|---------|
| **Blog**      | Not applicable | ![Python Validation](./documentation/testing/validation/python/blog_form.PNG) | ![Python Validation](./documentation/testing/validation/python/blog_model.PNG) | ![Python Validation](./documentation/testing/validation/python/blog_url.PNG) | ![Python Validation](./documentation/testing/validation/python/blog_views.PNG) | ![Python Validation](./documentation/testing/validation/python/blog_app.PNG) |
| **Cart**      | Not applicable | Not applicable | Not applicable | ![Python Validation](./documentation/testing/validation/python/cart_url.PNG) | ![Python Validation](./documentation/testing/validation/python/cart_views.PNG) | Context ![Python Validation](./documentation/testing/validation/python/cart_contexts.PNG) |
| **Checkout**  | ![Python Validation](./documentation/testing/validation/python/checkout_admin.PNG) | ![Python Validation](./documentation/testing/validation/python/checkout_forms.PNG) | ![Python Validation](./documentation/testing/validation/python/checkout_model.PNG) | ![Python Validation](./documentation/testing/validation/python/checkout_url.PNG) | ![Python Validation](./documentation/testing/validation/python/checkout_views.PNG) | ![Python Validation](./documentation/testing/validation/python/checkout_app.PNG) |
| **Home**      | Not applicable | Not applicable | Not applicable | ![Python Validation](./documentation/testing/validation/python/home_url.PNG) | ![Python Validation](./documentation/testing/validation/python/home_view.PNG) | ![Python Validation](./documentation/testing/validation/python/home_app.PNG) |
| **Products**  | ![Python Validation](./documentation/testing/validation/python/product_admin.PNG) | ![Python Validation](./documentation/testing/validation/python/product_form.PNG) | ![Python Validation](./documentation/testing/validation/python/profile_model.PNG) | ![Python Validation](./documentation/testing/validation/python/blog_url.PNG) | ![Python Validation](./documentation/testing/validation/python/product_view.PNG) | ![Python Validation](./documentation/testing/validation/python/profile_app.PNG) |
| **Profiles**  | Not applicable | ![Python Validation](./documentation/testing/validation/python/profile_form.PNG) | ![Python Validation](./documentation/testing/validation/python/profile_model.PNG) | ![Python Validation](./documentation/testing/validation/python/profile_url.PNG) | ![Python Validation](./documentation/testing/validation/python/profile_view.PNG) | App ![Python Validation](./documentation/testing/validation/python/profile_app.PNG) |
| **Wishlist**  | ![Python Validation](./documentation/testing/validation/python/wishlist_admin.PNG) | Not applicable | Not applicable | ![Python Validation](./documentation/testing/validation/python/wishlist_url.PNG) | ![Python Validation](./documentation/testing/validation/python/wishlist_views.PNG) | ![Python Validation](./documentation/testing/validation/python/wishlist_app.PNG) |


