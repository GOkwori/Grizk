# Grizk

![Grizk shown on a variety of screen sizes](./documentation/responsiveness/intro_screen.PNG)

Visit the deployed site: [Grizk](https://ecommerce-grizk-2f04b3042fc5.herokuapp.com/)

## Introduction

Grizk is an e-commerce platform specializing in sophisticated, cutting-edge electronic gadgets designed for tech enthusiasts. Developed as a showcase of a modern and dynamic online store, Grizk offers a wide range of the latest tech products including smart devices, high-end electronics, and accessories, all curated to meet the needs of a digitally connected lifestyle. This project was built using Django, HTML, CSS, JavaScript, and Python as part of my Full Stack Software Development journey.

Grizk combines state-of-the-art technology with a seamless user experience, offering customers the ability to discover, explore, and purchase gadgets from leading brands. The platform integrates a variety of functionalities to enhance the shopping experience, including advanced product search, smooth navigation, and secure payment processing.

With technology evolving rapidly, there is an increasing demand for reliable and user-friendly platforms where consumers can purchase the latest electronics confidently. Grizk aims to address this need by providing a trusted, convenient, and efficient shopping experience for tech-savvy users. The platform highlights the newest releases, trending gadgets, and exclusive deals, making it a go-to destination for anyone looking to stay at the forefront of the tech world.

For testing purchases, you can use the following [Stripe Dummy Card](https://stripe.com/docs/testing) details:

- **Success Card Number:** 4242-4242-4242-4242
- **Expiry Date:** Any future date in MM/YY format
- **CVN:** Any 3-digit number
- **Postcode:** Any 5 numerals  

**Note:** Any payments made using a valid debit/credit card will not be processed, and no charges will be applied. Orders placed for testing purposes will not be fulfilled.

For full Admin access to the Django Admin panel, you can use the following link: [Grizk Admin](https://ecommerce-grizk-2f04b3042fc5.herokuapp.com/admin/)

To access the Admin Dashboard frontend view with relevant credentials, visit: [Grizk Admin Dashboard](https://ecommerce-grizk-2f04b3042fc5.herokuapp.com/products/admin_dashboard/)

AccountSphere empowers you to manage your financial workflows seamlessly in one integrated platform. Embrace smarter financial management today!

![GitHub Last Commit](https://img.shields.io/badge/Last%20Commit%20-%20October%202024%20-%20blue)
![GitHub Languages](https://img.shields.io/badge/Languages%20-%204%20-%20teal)
![HTML](https://img.shields.io/badge/1%20-%20HTML%20-%20orange)
![CSS](https://img.shields.io/badge/2%20-%20CSS%20-%20blueviolet)
![JavaScript](https://img.shields.io/badge/3%20-%20JavaScript%20-%20gold)
![Python](https://img.shields.io/badge/4%20-%20Python%20-%20green)
![Contributors](https://img.shields.io/badge/Contributors%20-%201%20-%20navy)
![Testing](https://img.shields.io/badge/Testing%20-%20Passed%20-%20lime)

- - -

## Table of Contents

- [Grizk](#Grizk)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Customer Goals](#customer-goals)
  - [Business Goals](#business-goals)
- [UX/UI - User Experience/User Interface](#uxui---user-experienceuser-interface)
  - [Design Inspiration](#design-inspiration)
    - [colour Scheme](#colour-scheme)
    - [Typography \& Iconography](#typography--iconography)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
  - [Agile Methodologies](#agile-methodologies)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [Sprints](#sprints)
  - [Marketing](#marketing)
  - [User Stories](#user-stories)
    - [Visitor User Stories](#visitor-user-stories)
    - [Epic - Home View \& User Account](#epic---home-view--user-account)
    - [Epic - Products](#epic---products)
    - [Epic - Basket Management \& Purchasing](#epic---basket-management--purchasing)
    - [Epic - Wishlist](#epic---wishlist)
    - [Epic - Newsletter](#epic---newsletter)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton \& Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
    - [Defensive Design](#defensive-design)
- [Features](#features)
  - [User View - Guests/Account Holders](#user-view---guestsaccount-holders)
  - [CRUD Functionality](#crud-functionality)
  - [Features Showcase](#features-showcase)
  - [Future Features](#future-features)
- [Technologies \& Languages Used](#technologies--languages-used)
  - [Libraries \& Frameworks](#libraries--frameworks)
  - [Tools \& Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project SetUp](#django-project-setup)
    - [Elephant SQL](#elephant-sql)
  - [Heroku Deployment](#heroku-deployment)
  - [Google Mail Setup](#google-mail-setup)
  - [AWS Config](#aws-config)
    - [Media Folder Setup](#media-folder-setup)
    - [Django AWS Connect](#django-aws-connect)
  - [Stripe Config](#stripe-config)
  - [Clone Project](#clone-project)
  - [Fork Project](#fork-project)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
  - [Acknowledgements](#acknowledgements)


## Overview

Grizk is a cutting-edge electronics store that specializes in providing the latest tech gadgets and sophisticated devices to meet the needs of modern consumers. With a focus on quality and innovation, Grizk brings together a curated selection of electronics from top brands, ranging from smart home devices and mobile accessories to the latest laptops and wearables. Users on Grizk are invited to:

- Explore the store as Guests, with full browsing capabilities
- Register for an Account to access enhanced features
- Utilize the Wishlist to save and track favorite products
- Browse products by category, brand, and price to find the perfect gadget
- Add products to their cart, edit quantities, and proceed to a secure checkout
- As registered users, view their order history and track past purchases
- Subscribe to weekly newsletters for updates on new releases, exclusive deals, and tech news

Grizk is designed to be fully accessible across all modern browsers and is optimized for a seamless experience on different screen sizes, ensuring that users can browse and shop effortlessly whether on desktop, tablet, or mobile devices. With a sleek, intuitive interface, Grizk makes it easy for users to find and purchase the best electronics on the market.

## Customer Goals

Grizk aims to provide a streamlined, intuitive shopping experience that caters to tech enthusiasts of all levels. Customers can easily discover the latest gadgets, compare products, and make informed decisions based on detailed descriptions, specifications, and user reviews. It is anticipated that customers will create accounts on Grizk to take full advantage of features such as wishlist management, faster checkouts, and order tracking. Grizk also encourages customers to stay informed and engaged with tech trends through its regular newsletters, which offer insights into the latest products, promotions, and tech news.

By focusing on quality and user experience, Grizk strives to build trust and loyalty among its customers, making it a go-to destination for anyone looking to keep up with the latest in tech innovation.

## Business Goals

Grizk provides robust and user-friendly administrative functionality for the business owner through an accessible, easy-to-navigate Admin Dashboard. The dashboard simplifies inventory management, order processing, and customer service, allowing admins to make quick and efficient updates to product listings, track orders, and manage customer queries. Additional frontend forms enable seamless content management, including the ability to add, edit, and remove product listings and articles.

Grizk's goal is to establish a solid base of repeat customers who seek reliable, cutting-edge technology from trusted brands. The platform is designed to scale with the business, supporting ongoing growth and new feature development. Marketing efforts, such as targeted social media campaigns, email newsletters, and blog content, help to raise brand awareness and attract new users, driving continued engagement and sales. With a focus on innovation, quality, and customer satisfaction, Grizk aims to be a leader in the competitive world of electronics e-commerce.


## UX/UI - User Experience/User Interface

### Design Inspiration

Grizk’s design captures the essence of modern tech elegance, leveraging a sleek, dark-themed aesthetic that echoes sophistication and innovation. The primary colour scheme revolves around jet black (`#000`) as the background, paired with striking orange-red (`#ff4500`) accents, symbolizing energy and cutting-edge technology. This colour combination is not only visually appealing but also enhances the readability and focus of the content across all devices.

The site maintains a responsive design, ensuring that users on mobile, tablet, and desktop can seamlessly navigate through Grizk’s interface. Key visual elements such as buttons, icons, and product cards are intuitively designed to stand out against the dark background, ensuring that users can quickly identify interactive components.

A minimalist logo, designed using [LogoAI](https://www.logoai.com), is prominently displayed as the favicon and brand signature across the site. The logo’s clean lines and bold colours reinforce the store’s identity as a go-to destination for high-tech enthusiasts.

![Grizk logo](documentation/features/logo.PNG)  
*Grizk logo*

### Dark Theme with Electric Accents

The dark-themed design, with a solid black background, was chosen not only for its sleek, high-tech appearance but also to provide a comfortable, strain-free experience for users browsing for extended periods. Orange-red highlights are strategically used to emphasize calls to action, such as "Add to Cart" and "Checkout," ensuring these elements are easily noticeable.

Buttons across the site feature a smooth hover effect where the colours invert — from black with red accents to a red background with black text. This visual feedback enhances user interactions and draws attention to clickable elements.

### Header & Navigation

The header employs a radial gradient (`#220202` to `#000000`), giving a subtle, polished look that matches the dark theme. Navigation elements are styled with bold, orange-red text that is easy to read and aligns with the overall visual consistency. 

The navigation bar remains sticky across all screens, ensuring users can access essential sections such as the cart, profile, and categories without scrolling back up. For a seamless experience, dropdown menus and off-canvas sections (for wishlist and cart) match the site’s dark theme and accent colours, providing a unified visual presentation.

![Header Navigation](documentation/features/navigation.PNG)  
*Intuitive header and navigation for streamlined browsing*

### Footer Design

The footer continues the radial gradient design, providing a cohesive finish to each page. It features social media icons that subtly increase in size when hovered over, inviting users to connect without overwhelming the screen. Subscription forms are embedded within bordered panels, elegantly styled with orange-red outlines that stand out against the dark background, encouraging users to engage with newsletters and updates.

![Footer Design](documentation/features/footer.PNG)  
*Footer with gradient design and intuitive social icons*

### Product Showcase & Visual Feedback

Product images are displayed in a clean, distraction-free layout to ensure the gadgets are the center of attention. Each product card is designed to hover slightly when interacted with, giving a sense of depth and enhancing the overall user experience. The site employs a flexbox grid system to arrange products dynamically, ensuring consistency across varying screen sizes.

Visual feedback is implemented throughout the interface, including subtle animations and hover effects. For example, toasts pop up on the right side of the screen to confirm actions like adding items to the cart or removing products from the wishlist, ensuring users are always informed.

### Dual Carousel Implementation

#### Home Page Carousel (Landing)

Upon entering the Grizk site, users are greeted by a captivating carousel on the homepage. This landing carousel showcases the latest promotions, featured products, and exclusive offers. Each slide features high-resolution product images, a brief description, and a prominent call-to-action button ("Explore Now), styled with the site's signature colours. 

The carousel uses smooth slide transitions (`transform 0.3s ease-in-out`) to create an engaging browsing experience. Users can navigate through slides using intuitive swipe gestures on mobile devices or click through arrows on desktops. The design ensures a seamless, immersive first impression, setting the tone for a sophisticated shopping journey.

#### Top Deals Carousel

Further down on the homepage, a secondary carousel highlights top deals, seasonal promotions, and special offers. This section follows a similar design but emphasizes discounts and limited-time offers. Each product card within the carousel is designed to slightly enlarge on hover (`scale(1.05)`), giving a sense of interactivity and depth. The hover effect draws users' attention to these key deals, encouraging exploration.

Both carousels adapt seamlessly across devices, ensuring consistent viewing experiences whether on mobile or desktop. Image resizing and responsive text adjustments allow for clear, legible content presentation without compromising aesthetics.

![Home Page](./documentation/features/carousel_main.PNG)  
*Dynamic carousels engaging users with key offers*

![Top Deals Carousel](./documentation/features/carousel_deals.PNG)  
*Visually engaging carousel showcasing top deals*

### Cart & Wishlist Off-Canvas Design

#### Off-Canvas Cart

Grizk introduces an off-canvas cart feature that slides in from the side of the screen when activated. This allows users to quickly view and manage their cart items without leaving the current page. 

The cart's design follows the dark theme, with the bright accent colours ensuring important details like item names, quantities, and prices stand out. Buttons to "Checkout" and "Continue Shopping" invert colours on hover, providing immediate feedback to user actions. Each product listed has quantity adjustment controls and a "Remove" button, giving users full control over their purchases.

#### Off-Canvas Wishlist

The off-canvas wishlist functions similarly to the cart, enabling users to save products for later. This panel slides in smoothly, showing all saved products with options to add them to the cart or remove them from the wishlist. The same dark colour scheme and accent colours maintain consistency, ensuring users know they are still within the Grizk environment.

Both off-canvas panels are designed to be responsive, adjusting seamlessly to smaller screens. Controls are adequately spaced, and scrollbars appear as needed, ensuring smooth navigation and usability.

![Cart & Wishlist Off-Canvas](./documentation/features/offcanvas.PNG)  
*Seamlessly integrated off-canvas panels for cart and wishlist*


### Responsive Design & Media Queries

Grizk’s design is fully responsive, utilizing media queries to adapt layouts for different devices. For instance, elements adjust seamlessly between mobile views (`max-width: 320px`) and larger desktops (`min-width: 1801px`), ensuring a smooth and consistent experience. Features like dropdowns, carousels, and off-canvas components scale appropriately, providing intuitive navigation and user interaction across all platforms.


|  |  | | | 
| --- | --- | --- | --- | 
| ![Home Page](./documentation/responsiveness/home_page.PNG)| ![Product Page](./documentation/responsiveness/product_page.PNG) | ![Product Detail](./documentation/responsiveness/product_detail_page.PNG) | ![Cart](./documentation/responsiveness/cart_page.PNG) |
| ![Checkout Success](./documentation/responsiveness/checkout_success_page.PNG)| ![Login Page](./documentation/responsiveness/login_page.PNG) | ![Registration](./documentation/responsiveness/registration_page.PNG) | ![Password Reset](./documentation/responsiveness/reset_password_page.PNG) |

*Consistent, responsive design for all screen sizes*

### Animations & Transitions

Animations are carefully integrated to enhance user interaction without detracting from the browsing experience. For instance, product images gently enlarge on hover (`scale(1.05)`) to draw focus, while buttons smoothly change colour on hover, indicating interactivity. This provides a polished, fluid user experience that aligns with Grizk’s futuristic aesthetic.

Grizk is designed not just as an e-commerce platform but as a digital shopping experience that embodies the sophistication of the tech products it offers. Through thoughtful design, intuitive navigation, and responsive elements, Grizk ensures users are fully engaged from browsing to checkout, no matter their device.

## Colour Scheme

![Grizk colour Scheme](./documentation/colour-palette/colour_palette.PNG)  
*Grizk colour Scheme*

Grizk employs a bold, modern colour palette that emphasizes contrast and clarity, essential for an electronics e-commerce platform. The CSS uses well-defined variables to ensure consistency across the site:

- `--electric-orange`: #ff4500;
- `--deep-black`: #000;
- `--midnight-maroon`: #220202;
- `--soft-gray`: #22223b;
- `--vivid-white`: #fff;
- `--steel-gray`: #aab7c4;
- `--bright-yellow`: #ffc824;

These colours were chosen to provide a sleek, high-tech aesthetic that appeals to tech enthusiasts. The primary colour, `electric-orange` (#ff4500), serves as a bright accent used throughout the site, from call-to-action buttons to hyperlinks and notifications. It ensures that essential elements stand out against the dark, muted backgrounds, guiding users' attention seamlessly. 

### Primary and Accent colours

The `deep-black` (#000) background delivers a sophisticated, minimalist canvas, allowing the `electric-orange` to shine as the main accent colour. This vibrant hue is featured prominently on buttons, interactive elements, and hover effects, ensuring that users can intuitively navigate the site. A touch of `midnight-maroon` (#220202) adds depth and warmth, subtly incorporated in background gradients and header elements to break up the dark theme without overwhelming the user.

### Button and Interactive Elements

Interactive elements on Grizk, such as buttons and clickable links, employ a striking colour contrast. The standard button style features a `black` background with `electric-orange` borders and text, creating a dynamic, eye-catching appearance. On hover, the colours invert—buttons light up in `electric-orange` while the text turns `black`. This creates a clear, responsive visual cue, enhancing the user’s experience and interaction with the site.

![Grizk Main Button](./documentation/features/button.PNG)  
*Grizk Main Button Design*

### Consistency and Feedback Mechanisms

Grizk utilizes `soft-gray` (#22223b) for secondary backgrounds, borders, and certain text elements to maintain visual balance. When users interact with fields or buttons, a `bright-yellow` (#ffc824) or `electric-orange` appears to provide immediate feedback, confirming the action is available or complete. This approach simplifies navigation, making it easy for users to understand where they are on the site and how they can interact with it.

### Accessibility and Contrast Testing

Colour accessibility is a priority for Grizk. Using [Adobe colour](https://colour.adobe.com/create/colour-accessibility), we ensured that all primary text and essential visual elements meet or exceed WCAG 2.1 guidelines for contrast. This makes the site accessible to users with visual impairments. Below are examples of how these tests were conducted to guarantee clarity and usability:

![Grizk colour Accessibility Check](./documentation/colour-palette/color-accessibility.PNG)  
*Grizk colour Accessibility Check*

### Button Contrast

Buttons were rigorously tested to ensure that they are easy to see and interact with on both desktop and mobile devices. colour contrasts between the `electric-orange` and background hues ensure that buttons remain legible under various lighting conditions. This helps prevent misclicks and guides users smoothly through their shopping experience.


### Final Thoughts

Grizk’s colour scheme contributes to a sleek, cohesive design that resonates with tech-savvy users. The high-contrast, minimalist aesthetic emphasizes usability, drawing attention to key actions and features. Consistency across the site ensures a seamless experience, whether users are browsing on desktop or mobile. The combination of `electric-orange` accents with deep, muted backgrounds fosters an inviting yet sophisticated feel, enhancing the overall brand identity of Grizk.

## Typography & Iconography

![Grizk Font Pairing](./documentation/typography/typo.PNG)  
*Grizk Font Pairing*

For Grizk, typography was chosen to convey a sense of modernity, precision, and clarity, essential for an electronics e-commerce platform where users need to quickly grasp product information. The primary typeface used is **Roboto**. 

**Roboto** serves as the main sans-serif font, providing a sleek, modern, and easily readable style that aligns with the brand's high-tech image. It is used extensively for titles, headings, and important labels across the platform, ensuring content is presented clearly and prominently. On the other hand, **Fira Code**, a monospaced font, was chosen for product details and specifications, emphasizing the technical aspects of the electronics listed on the site. This combination provides a robust contrast that enhances the readability and structure of the content, improving the overall user experience.

### Iconography

Grizk's iconography complements its clean, modern aesthetic, using simple, clear icons from the **Font Awesome** library. Icons are employed strategically to guide users through their journey on the site—whether it’s adding products to the cart, favoriting items, or navigating different categories. For example, the shopping cart, wishlist heart, and user account icons are immediately recognizable and provide visual cues to users, enhancing their navigation experience.


# Project Planning

## Strategy Plane

The primary objective for **Grizk** was to develop a sophisticated e-commerce platform specializing in cutting-edge tech gadgets. The goal was to ensure a seamless, intuitive, and enjoyable shopping experience, reflecting Grizk's identity as a modern, user-centric electronics store. The platform needed to be fully responsive, offering a consistent experience across all devices, while integrating advanced features such as secure payment systems, intuitive navigation, and personalization options.

Grizk was built to meet the following core goals:

### Site Goals
- **Responsive Design:** Ensure the platform is accessible across all devices, including desktops, tablets, and mobile phones. Users should have a fluid and consistent shopping experience, no matter where they access the site from.
- **User Authentication:** Provide secure and reliable login and registration options for customers, with the ability to save items to a wishlist, view past orders, and receive personalized recommendations.
- **Guest Access:** Allow guests to browse, explore products, and add items to the cart without requiring them to register, simplifying the user journey for first-time visitors.
- **Seamless Checkout:** Utilize **Stripe** as the primary payment gateway, ensuring secure and efficient transactions. The checkout process should be straightforward, with clear feedback and confirmation at each step.
- **Advanced Product Management:** Feature a robust backend for inventory management, enabling easy updates to product details, categories, and availability. 
- **Wishlist & Off-Canvas Panels:** Provide customers with the ability to save their favorite products and access them quickly via intuitive off-canvas panels for easy viewing and management.
- **Integrated Marketing Tools:** Implement features like newsletter subscriptions, personalized recommendations, and SEO-friendly content to drive engagement and improve visibility on search engines.
- **Engaging UI/UX Design:** Design a visually appealing and easy-to-navigate site, with consistent branding elements, to build trust and make the shopping experience enjoyable.
- **Enhanced Security & User Privacy:** Secure user data through encryption and adhere to the best practices in cybersecurity, ensuring that customers can shop with confidence.

## Development Approach

The design and visual assets of the website were curated and created to convey a sleek, modern feel, emphasizing Grizk's commitment to delivering high-quality tech gadgets. **Figma** was utilized to design the initial wireframes and prototypes, ensuring a cohesive design language across all pages and features. The hero images, promotional banners, and product showcases were designed to be visually striking, grabbing the user's attention while maintaining brand consistency.

During the development phase, **Bootstrap** was employed to streamline the responsive design process, while custom **CSS** was used to enhance the visual appeal and interactivity of elements such as buttons, modals, and toast notifications. To maintain uniformity, CSS variables were defined for colors, fonts, and component properties, enabling rapid updates and scaling.

## Key Features Implemented

1. **User-Centric Feedback & Toast Notifications**
   - Users receive immediate feedback during interactions, such as adding items to the cart, completing a purchase, or updating account information. This was achieved using visually distinct toast notifications that match Grizk's color scheme, ensuring clarity and consistency across the site.

2. **Secure Payment Integration with Stripe**
   - Stripe's robust and reliable payment processing was integrated to ensure secure, efficient transactions. Clear visual indicators and confirmations guide the user through the checkout, minimizing friction and improving trust.

3. **Visual Appeal Through Cohesive Branding**
   - Grizk's brand identity is consistently reflected throughout the site using carefully chosen font, color schemes, and iconography. This approach fosters brand recognition and enhances user engagement, as customers can easily associate the visual style with quality and reliability.

4. **Dynamic Off-Canvas Panels for Cart & Wishlist**
   - The off-canvas panels allow users to easily manage their cart and wishlist items without disrupting their browsing experience. These panels slide in smoothly, offering quick access to item details, quantity controls, and direct links to proceed to checkout.

## Future Development & Expansion
- **AI-Powered Product Recommendations:** Plans to integrate machine learning algorithms to provide tailored product suggestions based on user behavior and preferences.
- **Interactive 3D Product Views:** Enable customers to view products in a more engaging, interactive format, offering 360-degree visualizations.
- **Enhanced Marketing Integration:** Further development of marketing tools, including dynamic newsletters, limited-time offers, and seasonal promotions, to drive engagement and sales.
- **Multi-Language Support:** Expand accessibility by offering the site in multiple languages, catering to a broader, global audience.

Grizk was developed with scalability and flexibility in mind, ensuring that future enhancements and features can be seamlessly integrated. With a solid foundation in place, Grizk aims to set the standard for tech e-commerce, providing an unmatched user experience that caters to both tech enthusiasts and casual shoppers alike.


## Agile Methodologies

Grizk was developed using Agile planning methodologies, ensuring a structured, iterative approach to building the platform. Leveraging tools like **[GitHub Projects](https://github.com/)**, the development process was organized around Epics, Milestones, and Sprints, allowing for efficient tracking of tasks and priorities. Using GitHub’s issue boards, each task was clearly defined, labeled, and assigned to specific sprints. This setup streamlined the workflow, enabling focused development phases and reducing potential errors.

### MoSCoW Prioritization

To effectively manage feature development and prioritize tasks, the MoSCoW Prioritization method was adopted for Grizk, which helped categorize the project components as follows:

- **Must Haves**: Essential and critical elements that were non-negotiable. These formed the core functionalities of the project and were vital for achieving the MVP (Minimum Viable Product). For Grizk, this included secure authentication, seamless checkout, and responsive product browsing.
- **Should Haves**: Important features that added value to the overall platform but were not critical for the MVP launch. These were addressed after the 'Must Haves' were implemented, such as the Wishlist and enhanced search filtering.
- **Could Haves**: Desirable enhancements that would improve the user experience or functionality but were not essential. These were considered bonuses and were planned only if time permitted after core features were completed. Examples included custom animations, advanced filters, and social sharing options.
- **Won't Haves**: Features that were deemed unnecessary for the current project scope or release. These were either postponed for future iterations or discarded entirely to maintain focus on core functionalities.

### Sprints

The development process was divided into well-defined **Sprints**, each focusing on specific areas of the Grizk platform. This helped maintain momentum and allowed for incremental progress with clear milestones. The flexibility of Agile allowed for adjustments in the scope and tasks as the project evolved, ensuring that key features were prioritized and integrated effectively.

| Sprint No. | Sprint Content                               | Start/Finish Dates      |
|------------|---------------------------------------------|-------------------------|
| #1         | **Project Setup**: Initial setup, repo configuration, base framework installations, and environment preparation. | 01/07/24 - 10/07/24     |
| #2         | **User Authentication & Navigation**: Implemented secure user login, registration, and navigation structure. | 11/07/24 - 20/07/24     |
| #3         | **Product Management & CRUD Operations**: Developed product listing, adding, updating, and deletion capabilities. | 21/07/24 - 30/07/24     |
| #4         | **Shopping Cart Functionality**: Added cart system with item additions, removals, and quantity management. Styling for responsive design. | 31/07/24 - 10/08/24     |
| #5         | **Wishlist Feature**: Integrated wishlist with off-canvas display for easy management of saved items. | 11/08/24 - 15/08/24     |
| #6         | **Product Details & Carousel Implementation**: Enhanced product detail views and added carousel elements on the homepage. | 16/08/24 - 20/08/24     |
| #7         | **Admin Dashboard & Inventory Management**: Designed and implemented an intuitive admin interface for inventory control. | 21/08/24 - 25/08/24     |
| #8         | **User Notifications & Correspondence**: Integrated email notifications, toasts, and order confirmations for enhanced user engagement. | 26/08/24 - 05/09/24     |
| #9         | **Documentation, Testing & Final Touches**: Comprehensive testing, bug fixing, and documentation preparation for final delivery. | 06/09/24 - 23/10/24     |

### Agile Advantages

Using Agile methodology ensured that development was **iterative** and **adaptive**, allowing for frequent feedback loops and early problem detection. Each sprint concluded with a review phase, where the functionalities were tested, refined, and polished. This approach ensured a robust, user-focused platform at the end of the development cycle, meeting the high standards set for Grizk.

- **Efficient Collaboration**: Regular updates, stand-ups, and meetings enabled smooth communication between team members, making sure everyone was aligned on goals and priorities.
- **Quick Adaptation to Changes**: If a new feature or adjustment was deemed necessary during the development phase, the Agile framework allowed for rapid incorporation, ensuring Grizk remained up-to-date with user needs and market trends.
- **Scalability**: The modular approach adopted in Agile sprints made it easier to scale and build upon Grizk’s initial features, paving the way for future enhancements without disrupting the core structure.



## User Stories

User stories and features were documented and managed on [GitHub Projects](https://github.com).

### Visitor User Stories

| User Story | Priority |
|------------|----------|
| As a **customer**, I can **view the site's home page** so that I can **understand Grizk's mission and explore the tech gadgets it offers.** | **MUST HAVE** |
| As a **customer**, I can **see and use the navigation bar** so that I can **easily navigate through different categories and features of the site.** | **MUST HAVE** |
| As a **customer**, I can **enter keywords into the search bar** so that I can **quickly find a specific gadget or product.** | **MUST HAVE** |

### Epic - Home View & User Account

| User Story | Priority |
|------------|----------|
| As a **customer**, I can **create and manage an account with Grizk** so that I can **store my personal details, order history, and streamline my checkout experience.** | **MUST HAVE** |
| As a **customer**, I can **edit my account details** so that I can **ensure my information is always accurate and up-to-date.** | **MUST HAVE** |
| As a **user**, I can **enter my login details** so that I can **access my account and saved preferences on Grizk.** | **MUST HAVE** |
| As a **user**, I can **click on visible links in the footer** so that I can **easily access important information like FAQs, Contact, and Policies.** | **MUST HAVE** |
| As a **user**, I can **register my email and receive a verification link** so that I can **create a secure account on Grizk.** | **SHOULD HAVE** |
| As a **customer**, I can **use the Contact Us form** so that I can **get in touch with Grizk's support for inquiries or assistance.** | **SHOULD HAVE** |

### Epic - Products

| User Story | Priority |
|------------|----------|
| As a **user**, I can **filter and sort products on the 'All Products' page** so that I can **refine my search and shop more efficiently.** | **MUST HAVE** |
| As a **user**, I can **click on a specific category in the navbar** so that I can **view products grouped by their type, brand, or features.** | **MUST HAVE** |
| As a **customer**, I can **click on an individual product** so that I can **view detailed information such as specs, price, and available options.** | **MUST HAVE** |
| As a **site admin**, I can **add new products via a frontend form** so that I can **expand Grizk's product range without complex backend operations.** | **MUST HAVE** |
| As a **site admin**, I can **edit existing product information** so that I can **keep product details current and accurate.** | **MUST HAVE** |
| As a **site admin**, I can **delete products from the inventory** so that I can **remove discontinued or outdated products from the store.** | **MUST HAVE** |

### Epic - Cart Management & Checkout

| User Story | Priority |
|------------|----------|
| As a **customer**, I can **easily add items to my cart from the product page** so that I can **prepare for checkout without navigating away.** | **MUST HAVE** |
| As a **customer**, I can **adjust the quantity or remove items directly from the cart** so that I can **have full control over what I'm purchasing.** | **MUST HAVE** |
| As a **customer**, I can **view my cart total and itemized list from any page** so that I can **track my spending at all times.** | **MUST HAVE** |
| As a **customer**, I can **securely checkout and complete my purchase** so that I can **have a seamless payment experience.** | **MUST HAVE** |
| As a **customer**, I can **receive a confirmation email with my order details** so that I can **keep a record of my purchase.** | **MUST HAVE** |
| As a **site user**, I can **view customized error pages with 'Home' links** so that I can **easily navigate back if a page is not available or requires login.** | **MUST HAVE** |

### Epic - Wishlist

| User Story | Priority |
|------------|----------|
| As a **logged-in user**, I can **add products to a wishlist** so that I can **save items I'm interested in for future purchase.** | **COULD HAVE** |
| As a **logged-in user**, I can **remove items from my wishlist** so that I can **keep my list relevant and organized.** | **COULD HAVE** |

### Epic - Promotions & Deals

| User Story | Priority |
|------------|----------|
| As a **customer**, I can **see promotional banners and deals on the homepage carousel** so that I can **take advantage of special offers and discounts.** | **MUST HAVE** |
| As a **site admin**, I can **update deals and promotional content** so that I can **manage campaigns and highlight specific products.** | **SHOULD HAVE** |

### Epic - Newsletter & Community

| User Story | Priority |
|------------|----------|
| As a **customer**, I can **subscribe to Grizk's newsletter** so that I can **receive updates on the latest tech gadgets, sales, and exclusive offers.** | **SHOULD HAVE** |
| As a **customer**, I can **enter my email into the newsletter form** so I can **stay informed on the latest tech trends and innovations.** | **SHOULD HAVE** |
| As a **site admin**, I can **manage newsletter subscriptions** so that I can **engage with users and promote Grizk's community.** | **SHOULD HAVE** |


## Scope Plane

The development of **Grizk** was centered around creating a smooth and engaging shopping experience for tech enthusiasts, while also building on advanced e-commerce functionalities, such as integrating with payment systems and providing enhanced user management features. The scope was carefully defined to focus on essential elements of a functional online electronics store, while also allowing room for innovative features that set Grizk apart.

The primary goal was to deliver a fully operational e-commerce platform that could handle user accounts, secure payments, product management, and smooth checkout processes. Through the strategic planning process, the project scope expanded to include additional features aimed at enhancing user engagement and supporting the overall shopping experience.

### Core Focus: Streamlined User Experience & Stripe Integration

While maintaining the core functionality of a working e-commerce platform, the Grizk project was also an opportunity to learn and master the **Stripe API** and **webhook handlers** to manage payments seamlessly. The integration of Stripe was a focal point, ensuring that transactions were smooth, secure, and reliable. The project’s scope was managed to prioritize essential functionality, guaranteeing the successful delivery of the MVP (Minimum Viable Product).

### Feature Expansion: Pushing Boundaries Beyond the Basics

While planning, it became clear that Grizk could further innovate by adopting themes and features not typically seen in standard e-commerce projects. For instance, introducing a **Wishlist** feature allowed customers to save higher-priced items and come back to them later, understanding that premium tech gadgets often have a higher price point.

With a clean and efficient **Django MVT (Model-View-Template)** architecture, it was possible to develop these features quickly. The addition of an **Admin frontend panel** ensured that product and article management could be done efficiently, enabling the business to start accepting orders immediately.

### Essential Features Implemented

- **User Account Management:** 
  - Seamless account creation and management using **Django AllAuth** to simplify authentication, secure login, and user profile management.
  
- **Payment Integration:**
  - Integration of a **secure and reliable payment system via Stripe**, including payment processing, invoice generation, and refund handling, with webhook integration for real-time updates.

- **Product Inventory Management:**
  - Full **CRUD (Create, Read, Update, Delete)** operations for product management, enabling admins to manage inventory efficiently.

- **Wishlist Feature:**
  - Users can **save products to a Wishlist**, allowing them to bookmark items for future purchases. This feature is especially beneficial for high-value tech gadgets that may require consideration before purchase.

- **Shopping Experience with Cart and Checkout:**
  - Users can easily **add items to their cart, view a summary of their order, and proceed through a streamlined checkout process**. Ensuring that the purchase experience is intuitive and seamless was a key aspect of Grizk’s scope.

- **Responsive Design:**
  - The site was built to be **fully responsive**, offering an optimal browsing experience across all device types, from desktops to mobile phones.

- **Detailed Business Information:**
  - Inclusion of comprehensive **business details and policies**, helping customers make informed purchases and understand terms and conditions.


## Structural Plane

Grizk's development was rooted in a solid structural framework, utilizing **custom CSS** combined with **Bootstrap 5** for a seamless and responsive user experience. The project started with the foundational structure provided by **Code Institute's Boutique Ado e-commerce project**, which served as a base. However, significant customization and enhancements were made to align with Grizk's vision of a modern and streamlined tech gadget marketplace. This approach allowed Grizk to retain reliable, core e-commerce functionalities while delivering a unique and engaging user interface.

### Core Framework & Customization

Built upon **Bootstrap 5**, Grizk leverages the powerful grid system and pre-built components to deliver a responsive, mobile-first design. Given that many users shop on their mobile devices, Grizk prioritizes smooth transitions across screen sizes, ensuring a consistent and fluid experience whether users are on desktops, tablets, or smartphones.

Grizk's structure benefited greatly from adopting **Code Institute’s Boutique Ado walkthrough project**. This foundation was picked apart, restructured, and extensively customized to suit Grizk’s brand identity and e-commerce needs:
- **Simplified Navbar:** Inspired by the modern e-commerce experience, the default Bootstrap navbar was reworked to provide a cleaner, more intuitive navigation. 
- **Responsive Icons & Graphics:** Icons were carefully selected from **Fontawesome** during the wireframing process in **Uizard**, enhancing the overall visual experience. Grizk's branding, including the logo, is consistent across the site, used as a favicon and integrated into marketing materials such as newsletters.

### Form Styling & UX Enhancements

Form elements throughout Grizk were customized to enhance user experience:
- **Custom Input Borders:** Instead of the default blue highlight seen in many browsers, form fields now feature a **2px solid red-orange border**, consistent with Grizk's primary color scheme. This change ensures that every element remains on-brand, even during user interactions.
- **Form Validation:** Validation styles were adapted to ensure clarity and simplicity, making error messages easily noticeable without overwhelming the design. Input fields provide immediate visual feedback, ensuring users know exactly where corrections are needed.

### Advanced Layout Components

Grizk integrates advanced components to elevate the shopping experience:
- **Integrated Carousels:** The home page landing features a dynamic **auto-rotating carousel** that showcases new arrivals, top-rated gadgets, and promotions. Additionally, a dedicated **carousel for Top Deals** offers quick browsing of discounted products, helping users discover great deals. These carousels, built using Bootstrap components, were enhanced with smoother animations for a sleek visual effect.
- **Offcanvas Cart & Wishlist:** Grizk includes **offcanvas panels** for the cart and wishlist, enabling users to manage their items without leaving the current page. Users can easily add, edit, or remove items, providing a streamlined, uninterrupted shopping journey.

### Typography & Readability

Typography choices were carefully selected to ensure readability across all devices:
- Grizk uses a blend of **Roboto** fonts for clean, modern text presentation. Typography plays a vital role in maintaining the professional and polished look of Grizk, enhancing user experience by clearly displaying product descriptions, features, and essential information.
- Text hierarchies guide users naturally through headlines, product details, and calls to action, helping to ensure a seamless browsing and purchasing experience.

### Grid Layouts & Flexibility

The **Bootstrap grid system** enabled effortless layout adjustments, ensuring the design remains responsive and adaptable to different screen sizes and resolutions. Specific features include:
- **Product Grid Layouts:** Products are displayed in a **dynamic grid view** that adjusts according to screen size. On larger screens, more items are displayed per row, while smaller devices show a condensed view, ensuring that product details remain prominent.
- **Footer Accordion Sections:** To maintain a clean design, the footer uses accordion panels to organize FAQs, support links, and quick navigation. This keeps content accessible without overwhelming the visual flow.

### Enhancing User Interactions with Bootstrap Components

Grizk's user interface benefits from Bootstrap's array of interactive elements:
- **Accordion Panels:** These are used for FAQs, support information, and other expandable content, keeping the interface clean while ensuring users can quickly access additional details.
- **Toasts & Modals:** **Toast notifications** provide users with real-time feedback on their actions, such as adding items to the cart or completing a purchase. **Modals** simplify user interactions for tasks like login, registration, and quick product views, ensuring smooth and efficient navigation.

### Adopting Code Institute's Boutique Ado Project

Leveraging **Code Institute’s Boutique Ado project** as a starting point provided a reliable structure for Grizk. This walkthrough project ensured that essential e-commerce functionalities were implemented effectively, including payment processing, user authentication, and product management. From this solid base, Grizk expanded with extensive customizations, ensuring that the final product not only met but exceeded modern e-commerce standards.

## Skeleton & Surface Planes

### Wireframes

[Uizard](https://app.uizard.io) was instrumental in the design planning phase for Grizk, providing a seamless and intuitive way to create and adjust wireframes for different devices. From the outset, Grizk was envisioned as a sophisticated e-commerce platform for tech enthusiasts, and Uizard helped bring this vision to life. The ability to design across **desktop, tablet, and mobile** layouts ensured that Grizk offers a consistent and responsive experience across all devices. 

With Uizard's extensive plugin ecosystem, it was easy to incorporate icons and other design elements that match Grizk's sleek, modern aesthetic. Below are some of the wireframes that guided the development process, showcasing the layout and structure of key pages on different devices:

| Page | Wireframe | Mock-up | 
| -- | -- | -- | 
| Home Page| ![ Home Page ](./documentation/wireframe/home_page_wire.PNG) | ![ Home Page ](./documentation/wireframe/home_page_mock.PNG) | 
| Product Page |![ Product Page ](./documentation/wireframe/product_wire.PNG) | ![ Product Page ](./documentation/wireframe/product_mock.PNG) |

These wireframes provided a blueprint for Grizk’s development, ensuring the design remained user-centric and intuitive. By visualizing the layout, interactions, and content early in the process, we could make necessary adjustments that contributed to a smooth and visually appealing final product.
