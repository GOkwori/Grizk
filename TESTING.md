# Testing

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

### HTML Validation

For my HTML files I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

I have had to follow a different approach for validating my HTML for this project as the majority of my pages are developed using Jinja syntax such as '{% extends "base.html" %}' and '{{ form|crispy }}' and most require user authentication. The HTML validator will throw errors if I were to use my website's URL so I have had to follow the below approach for every page:

- Via the deployed Heroku app link, I have navigated to each individual page.
- Right clicking on the screen/CTRL+U/⌘+U on Mac, allows a menu to appear, giving me the option to 'View page source'.
- The complete HTML code for the deployed page will appear, allowing you to select the entire code using CTRL+A/⌘+A on Mac.
- Paste the copied code into the [validate by input](https://validator.w3.org/#validate_by_input) option.
- Check for errors and warnings, fix any issues, revalidate by following the above steps and record the results.

![html validation](docs/testing_images/html_validation.png)  

All HTML pages were validated and received a 'No errors or warning to show' for code that I had written, result as shown above.

| HTML Source Code/Page | Errors | Warnings | Screen Shot |
| ---- | ------ | -------- | -------- |
| Home | 0 | 0 | |
| Log In | 0 | 0 |
| Register | 0 | 0 |
| Account | 0 | 0 |
| Wishlist | 0 | 0 |
| Admin Dashboard | 0 | 0 |
| Admin Article List | 0 | 0 |
| Admin Add Article | 0 | 0 |
| Admin Edit Article | 0 | 0 |
| Admin Delete Article | 0 | 0 |
| Admin Product List | 0 | 0 |
| Admin Product Detail | 0 | 0 |
| Admin Add Product | ID error -> Errors/Warnings present as a result of Bootstraps form elements, not from the code that I have created. The name ID from the contact form html within the base.html is clashing with the name ID from the add product html. These ID elements are embedded within the Bootstrap forms and are inaccessible to me without breaking my code up and reconfiguring the code. This is the same for the `<p>` and `<strong>` error. This was double checked with the Assessment Team Oct'23 who confirmed that code not authored by myself, and is Bootstrap/CrispyForms rendering, would not be subject to assessment mark down as long as it is referenced in the README. I will reinvestigate and break into the code when my Diploma has been awarded to remove errors like these. ![html validation duplicate id bootstrap forms](docs/testing_images/add_prod_er.png) | As before |
| Admin Edit Product | 0 | 0 |
| Admin Delete Product | 0 | 0 |
| All Products | 0 | 0 |
| User Article List | 0 | 0 |
| Bag - Empty | 0 | 0 |
| Bag - Products | 0 | 0 |
| Checkout | Errors/Warnings present as a result of Bootstraps form elements, not from the code that I have created. The name/email ID from the contact form html within the base.html is clashing with the name/email ID from the checkout html. These ID elements are embedded within the Bootstrap forms and are inaccessible to me without breaking my code up and reconfiguring the code. This was double checked with the Assessment Team Oct'23 who confirmed that code not authored by myself, and is Bootstrap/CrispyForms rendering, would not be subject to assessment mark down as long as it is referenced in the README. I will reinvestigate and break into the code when my Diploma has been awarded to remove errors like these. ![html validation duplicate id bootstrap forms](docs/testing_images/contactus_form_id.png) ![html validation duplicate id bootstrap forms](docs/testing_images/contact_html_issue.png) | As before |
| Wear| 0 | 0 |
| Care | 0 | 0 |
| Eat | 0 | 0 |
| Travel | 0 | 0 |
| Read | 0 | 0 |
| Profile/Account | 0 | 0 |
| Order History | 0 | 0 |
| Wishlist | 0 | 0 |
| Forgot Password | 0 | 0 |
| Error 403 | 0 | 0 |
| Error 404 | 0 | 0 |
| Error 500 | 0  | 0 |
| Footer - Contact Us & Thank You page | 0 | 0 |
| Footer    | Privacy Policy | External link - N/A | External link - N/A |
| Footer - Terms & Conditions   | Outside of my control there are multiple errors present as this page contains HTML Content from [Termly.com](https://termly.io/products/terms-and-conditions-generator/) to display the Terms & Conditions for Everneed. None of my templated code contains errors and I felt that attempting to correct all of the Termly errors would render the document incorrectly. I used Termly as they provided this content without personal cost to me. | As before. |