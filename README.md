# Hero Community

## <i> Full Stack Frameworks With Django - Code institute </i>

---

> **Hero Community** - is a social app for CrossFitters in order to share, compare, coach, track, log and motivate!

---

[![Generic badge](https://img.shields.io/badge/Django-3.1.4-s.svg)](https://shields.io/) [![Python 3.8](https://img.shields.io/badge/Python-3.8.6-blue.svg)](https://www.python.org/downloads/release/python-360/) [![Generic badge](https://img.shields.io/badge/Heroku-Postgres-s.svg)](https://shields.io/)

---

## Demo

![mockups](media/mockup.png)

[![Generic badge](https://img.shields.io/badge/Hero_Community_live_Demo-Here-<>.svg)](https://hero-community.herokuapp.com/)

---

## Table of Contents

> 1.  [**UX**](#ux)
> 2.  [**Scope**](#scope)
> 3.  [**Structure and Wireframe Mockups**](#structure)
>     - [**Navigation**](#navigation)
>     - [**Focus Shop**](#focus-shop)
>     - [**Blog**](#blog)
>     - [**Memberships**](#Membership)
>     - [**Workouts**](#workouts)
>     - [**Dashboard**](#dashboard)
>     - [**Home Page**](#home-page)
>     - [**About Page**](#about-page)
>     - [**Contact Page**](#contact-page)
>     - [**Programs**](#programs)
> 4.  [**Surface**](#surface)
> 5.  [**Technologies**](#technologies)
> 6.  [**Features**](#features)
>     - [**Home Page Features**](#home-page-features)
>     - [**Blog Features**](#blog-features)
>     - [**Focus Shop Features**](#focus-shop-features)
>     - [**Memberships Features**](#memberships-features)
>     - [**Programs Features**](#programs-features)
>     - [**Workouts Features**](#workouts-features)
>     - [**Dashboard Features**](#dashboard-features)
> 7.  [**Testing**](#testing)
> 8.  [**Deployment**](#deployment)
> 9.  [**Credits & Acknowledgements**](#credits)

---

## UX

My goal was to make a web application similar to the existing website [BeyondTheWhiteboard](https://beyondthewhiteboard.com/).

The basic idea is to create an online platform where a commnity of users can log their workout results and compare to each other and see what level they are at as a function of the total community results. BeyondTheWhiteboard has a lot of feautures on their application, each of which was worth exploring, but due to the limited amount of time available to me I limited the scope of the site functionality to logging, ranking, comparing, commenting and grouping.

Users can make use of the websites functionality for a one time payment of €9,99. I might also have opted for a subscription payment of say €0,99 per month.

### User Stories

#### User

- As a user, I want to be able to get instructions for a workout.
- As a user, I want to be able to log my results for a workout.
- As a user, I want to be able to review my previous results.
- As a user, I want to be able to edit my results.
- As a user, I want to be able to view the results of others.
- As a user, I want to be able to see what rank I have.
- As a user, I want to be able to see what rank others have.
- As a user, I want to be able to see what level I have.
- As a user, I want to be able to see what level other users have.
- As a user, I want to be able to review results of other users.
- As a user, I want to be able to create, edit, delete groups of fellow users to which I wish to compare my results.
- As a user, I want to be able to keep a custom created group private.
- As a user, I want to be able to switch between which group I select.
- As a user, I want to be able to comment on workout results.
- As a user, I want to be able to determine which result I need to reach a certain level.
- As a user, I want to be able to create an account and profile.
- As a user, I want to be able to signup/login using a social account.
- As a user, I want to be able to edit my profile information.

#### Admin

- As administrator, I expect to be able to add, edit, delete workouts on the website.
- As administrator, I expect to be able to add, edit, delete logs on the website.
- As administrator, I expect to be able to add, edit, delete comments on the website.

---

<div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

## Scope

- **Hero Community** is a social application for CrossFitters, which intends to motify the user to workout by a sort of "gamification" of CrossFit: You can challenge yourself to increase your levels and compete with anyone on the website. Only users that have created and payed for an account will have access to the websites functionality.
  We will be using [Django](https://www.djangoproject.com/) web frameworks and the site will be hosted on [Heroku](https://www.heroku.com/postgres) using [Heroku Postgres](https://www.heroku.com/postgres) for the database and [Amazone AWS](https://aws.amazon.com/) to host the static files.

- **User**
  To become a user registration is required. Once users are logged in they will be able to access their profile page which shows the profile information, their workout stats and their level statics.
  From there they can navigate to the WOD's page to view the current workout of the day, recent member activity and member ranking for the workout in question.
  They can also navigate to the Community page where they can select their group for the website, create, edit or delete a group, view other members level statistics and group stats.

- **Administration**
  For creating, editing, deleting workouts the admin can go to the workout page where in the main module the CRUD buttons will appear only if the admin is logged in as a superuser. For editing and deleting logs and comments, CRUD icons will appear next to every log/comment, where for a regular user they would only appear next to logs/comments that they posted.

---

<div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

## Structure

The basic structure of the web page is

- _Navigation_ - Top level
- _Body_ - Main page elements
-_Footer_ - Credits link.

The Landing Page, Sign-up Page and Login Page are publically accesible. After a user has signed up and logged in the user is redirected to the create profile page (logout is still accesible). After the user has created a profile (and completed payment),all pages of the site are accessible: Profile page, WOD's page, Community page. These last pages are all structured to contain three "modules".

I had a very basic idea for the website structure before I started writing the code, which I sketched out in some very simple [wireframes](https://github.com/MauRuRo/MSP4-CrossFitCommunityApp/tree/master/documentation) at the start of the process.

#### Sign Up (Registration) and Login

I have used a 3rd Party package called [Allauth](https://django-allauth.readthedocs.io/en/latest/) to take care of the logic.
The users are asked to fill in the Registration with fields ‘Email’, ‘Username’, and password, this is done twice to make sure they are both the same.
You may also use the social account sign up. Facebook and Google.

**Sign Up and Login.**
You may use the social account buttons to sign in or use the form.
The form has two fields, ‘email’ and ‘Password’ and a remember me button and a link to your if you have forgotten your password.
All of [Allauth](https://django-allauth.readthedocs.io/en/latest/) HTML pages have been more or less customised to fit the themes of the site.



### **Navigation**

#### Navbar

The navbar is fixed to top of each page. For smaller width screens the navbar will collapse to a bootstrap collapsed navber (taking the form of a hamburger button). The navbar only has four items: Profile, WOD's, Community and Log Out (or incase you are not logged in it's: Home, Log In, Sign Up). There are no sub lists in the nav items. To create optimal UX all site functionality can be easily and intuitively accessed through just these four pages.

The navbar also includes the user profile image and the site emblem when logged in, or just the website emblem when logged out. When clicking on or hovering over the website emblem a information layover will appear with general information aobut the website.

##### The Footer

The footer stays at the bottom of each page. It contains only a credits link for the website creator (me). As this is just a learning excercise and not a real world application; If this website ever commercially deploys the footer can be used to also contain some legalize links, and other miscalaneous details (contact details, social links).

---

<div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

## **Home Page**

The home page or Index page is the landing page for users who do not have, or are not yet signed in to an account.
It displays a enticing text encouring the user buy an account and it displays a caroussel with some images and text which demonstrate the website's capabilities.


## **Profile Page**

- **User Workout Stats**
  This module contains the workout stats for the user; describing the amount of workouts in the past year, the past month and the past week. If the amount of workouts per week or per month is less then the weekly/monthly average (based on the passed year) the text changes from blue to red. Depending on the users "progress" a different motivational gif and accompanying text will be shown.

- **User Hero Levels**
  This module displays the user's levels. It annotates a general fitness level ("Hero Level"). It also gives average levels per workout category (of which there are eight). And if a use clicks on the category level bar it can also see the workouts and their corresponding results and levels that build toward the average level in a popover. From that popover users can also navigate to each specific workout on the workout page listed there. The module also conains an information icon which toggles an div with information about that module.

- **Profile Information**
  This module displays the user's profile information. It also contains a edit button which swithces the module to an edit module for said profile information.

## **WOD's Page**

- ***Log Cards***
  This page makes use of "Log cards" in two of it's modules. These are collapsed information holders with only basic information on top (date, workout, result, profile name). It also shows wheter a result is a PR for the user and it shows the user profile picture and their country flag (which can be clicked to filter by country, though full country filtering functionallity works better when selecting the country group on the community page). If the user clicks the center div on the card it expands to reveal some extra information, including comments made by members and a little div with a form with textarea where the user can make their own comment. When applicapble (if current user is creator of the object), crud icons appear next to the comment or log information to enable the user to edit/delete.

- **Activity**
  This module shows the logging activity by members (filtered by the group selected in the community module) ordered by date (latest on top). The user can show recent acivity for all members of the group or just themselves. The user can also choose to see acitvity for only the selected workout or for all workouts. The module is a scrolling list. The list consists of 'log cards' (see above). On page load, it loads max 25 cards per category. If the user scrolls down, halfway through the div site makes a call to the database to load the next 25 cards, and so on. If the website is too slow or the user is to fast, there is also a button on the bottom of the list to click to load more cards.

- **Workout of the Day**
  This module displays the workout of the day, as selected by the site administrator. It contains information about the workout (title, category, description) and also a "story" about the 'hero' (deceased service man/woman) after whom the workout is named. The content for these workout descriptions and information was taken from [BeyondTheWhiteboard](https://beyondthewhiteboard.com/). Furthermore the module also contains a slider, which the user can use to determine the result needed for certain level. 

  The module also includes two buttons (top-right): "Log" (which toggles the Log module in place of the Ranking module) and "Workouts" (which toggles the Workout module in place of the Activity module)

  For the superuser the module also contains CRUD buttons for workouts.

- **Ranking**
  This module shows the ranked resuls of members (filtered by the group selected in the community module). It is not a simple ordered and numbered list: equal results have equal rank numbers, and the next rank after a sequance of equal results skips a number equal to the amount of equal results. E.g( 1, 2, 3, 3, 5, 5, 7, 8, 9). The user can show ranked logs for men or women and can also show the ranking for just the current day or the entire past year. The module is a scrolling list. The list consists of 'log cards' (see above). On page load, it loads max 25 cards per category. If the user scrolls down, halfway through the div site makes a call to the database to load the next 25 cards, and so on. If the website is too slow or the user is to fast, there is also a button on the bottom of the list to click to load more cards. On page load the module automatically scrolls to the result of the user (and loads the 'page' of 25 logs on which the user's result is on). If their are ranks higher than those loaded on the page a button will appear on top of the list to load the higher ranking results.

- **Workouts**
  This module contains a list of workouts per category and a search bar to look for a specific workout. It also indicates which workout is selected as workout of the day. All workouts listed are links to the page for that workout.

- **Log**
  This module shows the log submit or log edit form. Depending on the workout type, the field for "For time", "AMRAP" or "Max Weight" result is shown. 

## **Community Page**

The Cart is where you see a list of all the products that you have added.
Center block design. The top horizontal half is a list of all the products and information:

- Image on the left
- Name
- Prince
- Quantity and quantity adjuster - Here you see the quantity of a product, if you want to adjust, or remove the product.

The Order Summary is below the products list and hold all the financial details of the order:

- Cart Total
- Discounts - (if applicable)
- Subtotal
- Delivery charge
- Tax amount - (Note is is added into the total amount)
- Grand Total
- Keep shopping button - will take you back to the shop.
- Checkout button - will take to the check out.

<details>
<summary>Shopping Cart Wireframes(Click for image)</summary>

<p align="center">
<img src="media/wireframes/Cart.png">
</p>

</details>

#### Checkout

Full page layout with the user order form to complete:

- Contact details and delivery address.
- Save information to profile button that if pressed the information will be autofilled in next time they use the store.
- Adjust cart button - If you need to adjust the cart.
- Complete Order - Sends the card informtion to [Stripe](https://stripe.com/)

> #### Stripe Development Card
>
> A [Stripe](https://stripe.com/) payment system is inplace and >takes all major cards.
> The numbers below are used to test the Stripe Payment software.
>
> - Card number - 4242 4242 4242 4242
> - CVC - Any 3 digit number.
> - Expire date - Any date in the future

<details>
<summary>Checkout Page Wireframes (Click for image)</summary>

<p align="center">

![Checkout](media/wireframes/Checkout_D_M.png)

</p>
</details>

#### Checkout Success

Two center blocks one on the left and right both hold all your order details.
Breadcrumbs in the top left will take you to your dashboard.

Left block contains:

- Order Details
- Stripe Receipt - Clicking the receipt will sent to a new page with you Stripe receipt

Right Block contains

- Contact Details
- Shipping information

<details>
<summary>Checkout Success Wireframes(Click for image)</summary>

<p align="center">

![Checkout Success](media/wireframes/Checkoutsuccess_D_M.png)

</p>
</details>

---

<div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

## **Blog**

The blog post is the main source of communication in Focus, it is how all the user connect with each other, by writing blogs about how they are getting on, there experienceses and succesess they have had. Products or workouts they have used from the Focus Shop or Membership Programs. A special Category call 'Members' is for members to support each other,and get support from our Focus Fitness Trainers.
Featured Blogs are chosen by our Trainers and is generally written by Pro trainers or athletes.

The Blog Page is broken down into separate parts

- **Featured Blogs**
  Is the first thing you see. And uses a carcel to scrole through.

- **Category selection**
  A green and grey Category selection box is on the right-hand side.
  Here you will find all the available categories, and some information on each.
  Each category is colour coded.

  - **Members**
    This is for our users to connect with each other, write blogs about how they are enjoying one of our Focus Products or how a Membership program is working for them. If they have a question or comments on how to do anything they will be answered by our Focus Trainers in this category. By leaving comments on their blog post.

  - **Covid-19**
    In this category, we will talk about everything COVID and gym-related, its managing training in lockdowns and gym hygiene.

  - **Dieting**
    All blog post that are diet-related, tips tricks and pitfalls

  - **Endurance**
    All blogs that focus on the endurance training side of thing, Running, Cycling, Swimming

  - **Strength Training**
    All blogs that have to do with resistance training, bodybuilding, exercise techniques, tips, tricks and pitfalls
  - **Recovery**
    All blogs to do with the recovery side of the gym. Sleep, post-gym products, tips, tricks and pitfalls.

- **Blogs**
  This is where all the other blogs live.
  All blog borders are colour coded as per there category, to make it easer to see what category a blog is at a glance.
  They are ordered, newest to oldest.

- **Members Blogs**
  Underneath the Category selection box, is the Members blogs, a list of all the user member’s blogs show here.

<details>
<summary>Blog List Wireframes (Click for image)</summary>

<p align="center">

![Blog](media/wireframes/blog_list_D_mo.png)

</p>

</details>

#### Blog Categories Page

Once the category selection has been made, they will be redirected to this page.
All the blog post in that category will be displayed.
Only logged in users may see the Members posts

<details>
<summary>Blog Categories Wireframes (Click for image)</summary>

<p align="center">

![blog_cat](media/wireframes/blog_cat.png)

</p>
</details>

#### **Blog Detail Page**

Once the user has selected the blog post they would like to read, They are redirected to this page.
The blog post with the only element on this page.
Witch in include:

- Blogs Title
- Blog author
- Blog Content
- The amount of views, likes, and comments the post have
- When the blog was created.

Once the user has finished reading the post there is a section where a user may ‘like’ or leave a comment.
Note only logged in user may use this feature.

<details>
<summary>Blog Detais Wireframes (Click for image)</summary>

<p align="center">

![detail_blog](media/wireframes/detail_blog.png)

</p>

</details>

#### **Create and Edit Blog Page**

The create and edit blogs views share the same page: blog_form.html
This page is a form that has all the needed fields to fill out when creating or editing a blog.
The difference is when your creating a post the form is blank with ‘placeholders’ to guide you.
When your editing a post, all the fields are prefilled with the data needed to edit.
The information icon in the top right, has informatin about how to write a blog post.

<details>
<summary>Blog Create/Edit Wireframes (Click for image)</summary>

<p align="center">

![blog_forms](media/wireframes/blog_forms.png)

</p>
</details>

#### Blog Author Page

By Clicking on the authors name in the details blog page, you will be redirected to this page.
Here you will be able to see all the blogs that this user has written.
Each title is a link to the blog and you can see the amount of likes, comments, and thumps up each post has.

<details>
<summary>Blog Create/Edit Wireframes (Click for image)</summary>

<p align="center">

![Blog_author](media/wireframes/Blog_author.png)

</p>

</details>

#### **Memberships**

Are an important part of how Focus Fitness works. There are 2 types of memberships
_Free_ and _Professional_.

- **Free** memberships are given to anyone who joins Focus by logging in. When you log in you profile is made and _free_ status is given.
- **Professional** membership is a monthly subscription.
  To become a _Professional_ member, Click the ‘Select' button on the card and you will be redirected to the members-payment page.
  This page is a simple center block design with the memberships details and monthly billing amount.
  Below is the Stripe Payment Field.
  To Cancel a Subscription, it can be done viva the Dashboard in the subscription tab.

#### **Programs**

Only Subscribed users may use this app.
The Programs page is where the user can find the programs they have subscribed to.
The page is center based with horizontal cards stacked on top of each other.
They consist of the different categories.

- Endurance Training
- Static Stretching
- Strength training
- Dieting

More can be added in the administration section.

#### Programs Details

The page is a center block design and is divided in half.
On the Left hand side is the description of the category the member has chosen.
On the right hand side is the list of workouts within that Program.
The workouts are all video based and can be added or ordered in any way the trainer wishes to show them.

<details>
<summary>Programs WireFrame(Click for image)</summary>

<p align="center">

![Programs](media/wireframes/Programs.png)

</p>
</details>

#### **Workouts**

Once the workout is selected, you will be redirected to the workout.
Its a center-block design which displays the title and the context of the work out.
Below this is a video, which will fit the size of the user's display.

<details>
<summary>Workouts WireFrame(Click for image)</summary>

<p align="center">

![workdouts](media/wireframes/workdouts.png)

</p>
</details>

#### **Dashboard**

The Dashboard is where the login in user can access all their personal information.
It is divided into 3 parts.

- _Profile Admin_
- _My Blogs_
- _Orders History_

<details>
<summary>Dashboard Wireframes (Click for image)</summary>

<p align="center">

![dashBoard](media/wireframes/dashBoard.png)

</p>

</details>

#### **About**

The About page has a centre block format with a heading and information about Focus Fitness.

<details>
<summary>About Page Wireframes (Click for image)</summary>

<p align="center">

![About](media/wireframes/About.png)

</p>
</details>

#### **Contact Us**

The Contact us page is where you can contact us viva email.

<details>
<summary>Contact Us Wireframes (Click for image)</summary>

<p align="center">

![Contact](media/wireframes/Contact.png)

</p>
</details>

#### **Data Base**

For this Project we used [SQLite](https://www.sqlite.org/index.html) in development because it is integrated as default in [Django](https://www.djangoproject.com/). and [Heroku Postgres](https://www.heroku.com/postgres) in production
[AWS S3](https://aws.amazon.com/s3/) buckets are used to hold all the Static Files.

<details>
<summary>Focus Fitness Schema (Click for image)</summary>

<p align="center">

![Focus schema](media/wireframes/focus_schema.png)

</p>
</details>

---

<div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

## Surface

#### Fonts

- [Montserrat](https://fonts.google.com/specimen/Montserrat?query=montserrat) - Primary Font
- [Audiowide](https://fonts.google.com/specimen/Audiowide) - Secondary Font

The primary font [Montserrat]("https://fonts.google.com/specimen/Montserrat") is used for the body of all pages. I chose it because of its readability and accessibility. It complements the secondary font.
The Secondary is [Audiowide](https://fonts.google.com/specimen/Audiowide") is used in the logo and transposes well to the Heading and buttons, the technology styled typeface gives it a young and edgie feel, yet cleanly readable.

#### Colour Scheme

- ![#f7f7f7](https://placehold.it/15/f7f7f7/000000?text=+) `rgb(247, 247, 247)` - Primary-(Headings and text)
- ![#000000cc](https://placehold.it/15/000000cc/000000?text=+) `rbg(0, 0, 0, 0.8)` - Secondary (Header, Footer Backgrounds)
- ![#1bd87d](https://placehold.it/15/1bd87d/000000?text=+) `rgb(27, 216, 125)` - Supplementary colour 1
- ![#e7313f](https://placehold.it/15/e7313f/000000?text=+) `rgb(231, 49, 63)` - Supplementary colour 2
- ![#e5ce21](https://placehold.it/15/e5ce21/000000?text=+) `rgb(229, 206, 33)` - Supplementary colour 3
- ![#0275d8](https://placehold.it/15/0275d8/000000?text=+) `rgb(91, 192, 222)` - Supplementary colour 4

The colour scheme is all about contrast, there are a lot a dark background with white text and bold bright colours used sparingly throughout the site.
The Supplementary colours ![#1bd87d](https://placehold.it/15/1bd87d/000000?text=+) ![#e7313f](https://placehold.it/15/e7313f/000000?text=+) ![#e5ce21](https://placehold.it/15/e5ce21/000000?text=+) ![#0275d8](https://placehold.it/15/0275d8/000000?text=+) follow the Olympic weightlifting colours standard. The colours are bold and work with the theme.

#### Images

Images are used extensively. The images chosen are all gym and fitness related. They are used as a background in most of the site. Original pictures were darkened to fit with the theme of the project.
All images were found on [Unsplash](https://unsplash.com/) and have a CC licence.
A list of all the photographers can be found [here](#media)

<div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

---

## Technologies

### Core Languages, Frameworks, Editors

- [HTML 5](https://en.wikipedia.org/wiki/HTML) ~ Markup language designed to be displayed in a web browser.
- [CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) ~ Style sheet language used for describing the presentation of a document in HTML.
- [Python 3.8](https://code.jquery.com/) ~ High-level, general-purpose programming language.
- [Django 3.1.4](https://www.djangoproject.com/) ~ Django is a high-level Python Web framework.
- [jQuery 3.5.1](https://code.jquery.com/) ~ lightweight JavaScript library.
- [Bootstrap 4.5.3](https://getbootstrap.com/) ~ Design and customize responsive mobile-first sites.
- [Heroku](https://heroku.com) ~ A cloud based platform - as a service enabling deployment of CRUD applications.
- [Heroku Postgres](https://www.heroku.com/postgres) ~ PostgreSQL's capabilities - as a fast, functional, and powerful data resource.
- [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler) ~ A Heroku platform that can perform scheduled tasks (cronjobs) at set intervals.

#### Third-Party Tools

- [GitHub](https://github.com/) ~ Distributed version control and source code management (SCM) functionality of Git, plus its own features.
- [Travis](https://travis-ci.org/) ~ Travis CI is a hosted continuous integration service used to build and test software projects hosted at GitHub and Bitbucket.********
- [Font Awesome](https://fontawesome.com/) ~ Font Awesome icons
- [Git](https://git-scm.com/) ~ Distributed version control system
- [Codacy](https://app.codacy.com/) ~ Automated Code Review *****
- [W3 Validator](https://validator.w3.org/nu/) ~ The HTML Validation Service.
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) ~ A CSS validator checks your Cascading Style Sheets to make sure that they comply with the CSS standards set by the W3 Consortium.
- [TinyPNG](https://tinypng.com/) ~ A smart lossy compression technique to reduce the file size of your PNG files.******
- [Google Fonts](https://fonts.google.com/) ~ A library free licensed font families, an interactive web directory for browsing the library.

<div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

---

## Features

### Existing Features

#### Top Navbar

- Changes Dymamicaly
  This changes depending on the membership status of the user.
  If the user is not logged in it shows the basic menu with 'Sign up/Login' and shopping cart
  ![admin_no_user](media/wireframes/admin_no_user.png)

- Username and Admin Login
  When the use is logged in the top right is now the users 'Username' and a user icon.
  If the user is a ‘Staff’ member a link to the admin ear is shown.
  The basic menu extends to include Programs and dashboard and logout tabs.
  ![admin_nav](media/wireframes/admin_nav.png)

#### Footer

- Footer Navigation Changes Dymamicaly.
  The footer is dynamic and changes if the user is loged in or out. If logged out, the menu button say _login_, _Blog_, _Shop_, _Sign up_,
  If the user is logged in the menu changes to:
  _Subscribes_, _Blog_, _Shop_, _Logout_.
  And if the user is a Pro member, _Subscribes_ changes to _Programs_.
- Newsletter:
  The Newsletter sign ups form is in the footer. This way it is always on every page.
- Back to Top.
  The Back to the top button is global but you see it mostly in the footer, This is a handly way to get back to the top of the page.

#### Home Page Features

##### Section 1.

- Dynamic buttons
  The 4 main buttons in section 1 of the main page are dynamic and change with the user membership level.
  A public user will see Shop Sign up and Login Blog

  ![btn_no_user](media/wireframes/btn_no_user.png)

  If the user has logged in but not a Pro member the button will change to

  ![btn_user](media/wireframes/btn_user.png)

  If the user is a Pro member the buttons will change to

  ![btn_member](media/wireframes/btn_member.png)

##### Section 2

The 3 cards are links to different parts of the site.
They are clickable and lead to:

1. The Trainging Program categories.
2. The blogs main page.
3. The Focus shop.

##### Section 3

- **Dynamic Subscription section**.
  The subscription section users membership status.
  If the user is a Pro member this section is hidden. This gives the user less scrolling to get to the shop or the featured blogs.

#### Section 4

- **The Special Offers section**:
  Holds all the special offers that are listed.
- **Clickable Products**:
  The products are clickable and will take you to that products detailed page, where you can add to cart.
  controlled in the admin All the products that are displayed here are controlled in the admin ears.
- **Hidden Dynamically**:
  If there are no special offers the section will be hidden.

#### Section 5

- **Featured Blogs**: All the featured blogs are shown here with the help of Bootstrap's Carousel.
- **Clickable blogs**:
  The blogs are clickable and will take you to the blog details where you can read it.
- **Controlled in the admin**:
  All featured blogs are controlled in the admin area.

 <div align="right">

[Back to Top :arrow_up:](#testing)

</div>

---

### Blog Features

- **Featured** **Blogs**:
  The same feature that is used in Home page Section 5 is used in the blog list page.
- **Search Blogs**:
  The search bar in the blogs section will look for a matching word or words in either the name or content of the blogs. If there are any Matches will generate a results page. If there are none there is a link back to the blog page.

- **Colour Code Categories**:
  The Categories in the blog menu are colour coded to make it easier to distinguish the blogs. Each blog post - has a coloured border that matches the category colour.
- **Likes, Views and Comments**:
  Every time a logged on user clicks and views a blog it is recorded and shown on the blogs views counter. If a blog is liked it shows up in the thumbs up count. And the same if a blog is commented on.
- **Members Blog section**:
  The members block is where all the members blog will be posted.
- **Members blogs restricted access**
  Only logged in users may view the member blogs
- **Find all blog from author**:
  When you are on the blog's detailed page clicking on the authors name will bring you to their blogs page. Here you will be able to see all the blogs they have written.
  All the blogs in their page are ordered from newest to oldest.
- **Commenting on Blogs**:
  This way the users can connect with each other, ask questions, leave answers, or just comment.
- **Creating and Editing blogs**:
  Only logged in users may create or comment on blogs
- **User access**:
  Only login users may create or comment on blogs
- **Blog Author Control**
  Only the blogs authors may edit there blogs
- **Word Processors (Ckeditor)**:
  The word processor call 'Ckeditor' is used to create or edit blogs, this gives the user a lovely interface to write, link, and add pictures to a blog post.
- **Controlled from Admin**:
  Blogs can be written and edited front the admin area. If blogs are not inline with the rules and code of conduct, they can be deleted without the author's permission.

 <div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

### Focus Shop Features

- **Product** **Filtering**:
  You can filter the products in the shop with category selectors:
  - All products - lets you sort by price, lowest to highest or by category in an alphabetical order.
  - Activewaer & EQP - lets you sort by individual Activewear & EQP categories.
  - Supplements - let you sort by individual supplements categories.
  - Special Offers - shows you all the Special Offers.

This makes it quicker to find the product you are looking for.

- **Sort By Selector**:
  Here you can sort the products by:

  - _Price_ -(low-high) or (high-low).
  - _Name_ - (A-Z) or (Z-A).
  - _Category_ (A-Z) or (Z-A).
  - _Rating_ (low-high) or (high-low).

- **Product cards**:
  The Product cards are clickable and will take you to the details product page. If the product does not have an image a 'No Image' image will take its place.

- **Out of Stock**:
  You can make a product out of stock from the admin area.
- **Controlled from Admin**:
  The admin area is the place where you can add, edit or delete products from your inventory. Only authorised users may do this.
- **Reviews**:
  Products can get reviewed by logged in users, this is done on the product details page.
- **Stars Rating**:
  Products can get a star rating by logged in user, each review and rate is listed with the product, A overall rating is made using this. The overall rating is displayed with the product on the product card.

- **Search Bar**:
  The search bar will look for a matching word or words in either the name or description of the products.
- **Special offers**:
  Products are put on special offer from the admin area. A ‘was’ price tells the user the old price. It will be hidden if the ‘was’ price is smaller than the price.
- **Quantity selector**
  Lets you add more items to your order.
- **Size selector**:
  Lets the user choose a size if the product has a size, otherwise this will be hidden.
- **Shopping Cart Icon**:
  The shopping cart icon in the top right next to the username, is all ways shown. If the cart is empty it says ‘Empty’ if there cart has items, There is a running grand total that turns green and including all the discounts charges and taxes, No surprises at the checkout.
- **Add to Cart Message**:
  When you add an item to the cart, a message will appear letting you know it was successful, and give the user a quick way to checkout with a checkout button.
- **Detailed Price Breakdown**:
  In the cart section of the shop, a breakdown of all the charges are on the right, so you know how much you paid for what.
- **Adjust Cart**:
  The user can adjust or delete from the cart if they have made a mistake.
- **Secure Payment method**:
  Using [Stripe](https://stripe.com) is a secure way to place your orders
- **Order Receipt Emailed**:
  Once the order has been submitted and Stripe receives payment a webhook is sent with back to Focus, once we have received this, we send an email with all the order details and the Stripe Payment Receipt.
- **Backup Order with Webhook**:
  If for some reason the user leaves the page before the order is complete but the payment goes through, the billing details and shipping address is sent with the payment, this way we can get them in the webhooks.

### Memberships Features

- **Memberships**
  When a new use logs in for the first time a free membership is given to them.
- **Members access**
  members grains you asses to:
  - _Writing Blog_
  - _Commenting on blog posts_
  - _review and rating products_
  - _The Dashboard_
  - _Programs (Pro only)_
- **Subscriptions**:
  A user can become a pro member by subscribing to Focus
- **Stripe Subscription**:
  Using [Stripe](https://stripe.com) subscriptions make sure that the user is charged, and sends a webhook motifinig of that payment and date. When we have this we send an email letting the user know that the subscription has been successful.
- **Monthly Receipt emails**:
  With the webhooks from Stripe whenever a payment is made we send the user an emailed receipt.

### Programs Features

- **Controlled from Admin**:
  All programs are added, edited and deleted from the admin area only.
- **Dynamically Added/Edited**
  When new context or existing content is added or edited, it will automatically be updated on the programs page.

### Workouts Features

- **Controlled from Admin**:
  Workouts are added from the admin area only.
- **Dynamically Added/Edited**:
  When a new Workout is added it will automatically be added to the programs workout list.
- **Cloudinary**:
  The video files itself are not stored in the Focus database, they are linked with a url from a video hosting server. Focus fitness uses [Cloudinary](https://cloudinary.com/).

<details>
<summary>How To add a video to Cloudinary and add to Focus.</summary>

1. Make a Cloudinary account.
2. Login and make a file to keep you videos in.
3. Upload the video, when if has finished it will show you the Url.
4. Copy the Url.
5. In the Focus admin section click on workouts tab in the Programs section.
6. Click ‘Add Workout’.
7. Fill out all the fields in the form.
8. Where it says 'Video url' paste in the videos url.
9. Press 'Save'.

</details>

### DashBoard Features

- **Change User Password**:
  In the profile admin section the user can change their password
- **Change User Delivery Details**: Here the user may change or fill in all their delivery details.
- **Membership Select Access**:
  The user can see what level of membership they are, and find the date due to the next payment (if applicable).
- **Users Blogs**:
  Here you can see all the blogs the user has written, if they haven’t written any yet, there is a link to start.
- **Orders History**:
  A list of all the previous orders the user has made in the shop. They are arranged from news to oldest.

### Future Features

- Full Profile Page:
  A full profile page with all picture and bio.

- Log your workouts:
  A workout log page that you fill out in your workouts to keep track of your progress.
- Newsletter marketing manager:
  I would like to have my Newsletters email list auto upload to an email service that takes care of the mass emails

 <div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

---

## Testing

Testing, Bugs and Validation information and be found at [Testing.md](https://github.com/Clinton-Davis/focus_fitness/blob/master/testing.md)

---

## Deployment

### Local Deployment

To be able to clone this project there are a few things you will need.

- [Git](https://git-scm.com/) - Install Git, installation docs and be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Pip](https://pip.pypa.io/en/stable/installing/) - install pip, installation docs can be found [here](https://pip.pypa.io/en/stable/installing/)
- A [Gmail](https://www.gmail.com/mail/help/intl/en/about.html?utm_expid=...) account with app secret key.

Once you have [Git](https://git-scm.com/) and [Pip](https://pip.pypa.io/en/stable/installing/) installed.

1. From the terminal create the directory you want to work in.

   ```bash
   $ mkdir <filename>
   ```

2. Change into Directory

   ```bash
   $ cd <filename>
   ```

3. Clone the repository from github.

   ```bash
   $ git clone https://github.com/Clinton-Davis/focus_fitness.git
   ```

4. Change into focus_fitness directory.

   `$ cd focus_fitness`

5. Install [virtualenv](https://pypi.org/project/virtualenv/)

   ```bash
   $ pip install virtualenv
   ```

6. Create a virtual environment (env)

   ```bash
   $ virtualenv env
   ```

7. Activate env with:

   ```bash
   $ source env/Scripts/activate
   ```

8. In focus folder make a `.env` file and add the variables below.

   > There is a handy .templates.env file with all the variables.

   | Key                 |      Value      |
   | ------------------- | :-------------: |
   | SECRET_KEY          | < Your Values > |
   | EMAIL_HOST_PASS     | < Your Values > |
   | EMAIL_HOST_USER     | < Your Values > |
   | NOTIFY_EMAIL        | < Your Values > |
   | DEFAULT_FROM_EMAIL  | < Your Values > |
   | STRIPE_PUBLIC_KEY   | < Your Values > |
   | STRIPE_SECRET_KEY   | < Your Values > |
   | STRIPE_SECSTRIPE_WH | < Your Values > |

9. Install all the requirements needed to run the project.

   ```bash
   $ pip install -r requirements.txt
   ```

10. Open up blog.forms and comment out lines 8 and 9

    ```python
    # for item in choices:
    #     choices_list.append(item)
    ```

11. Then migrate

    ```bash
    $ python manage.py migrate
    ```

12. Once the migrations are complete, uncomment blog.forms

    ```python
    for item in choices:
        choices_list.append(item)
    ```

13. Before creating a superuser you'll need to load the required fixtures.

    > The reason for this is that a signal is used to assign a membership to a user when they are created, If there is no memberships it can't assign anything and causes an error.

    ```bash
    $ python manage.py loaddata fixtures/required.json
    ```

14. Create superuser.

    ```bash
    $ python manage.py createsuperuser
    ```

15. To populate the shop with products, load products data.

    ```bash
    $ python manage.py loaddata products.json
    ```

16. If you want to use the allauth social accounts, and have you [Facebook](https://developers.facebook.com/products/facebook-login/) secrets setup. add them to the `.env` file.
    | Key | Value |
    |----------|:-------------:|
    | SOCIAL_AUTH_FACEBOOK_KEY | < Your Values >|
    | SOCIAL_AUTH_FACEBOOK_SECRET | < Your Values > |

    If you are not using the social accounts, comment out lines 60/61 in settings.py (INSTALLED_APPS) socialaccounts.

17. Run project with

    ```bash
    $ python manage.py runserver
    ```

 <div align="right">

[Back to Top :arrow_up:](#table-of-contents)

</div>

### Heroku Deployment

You will need a [AWS](https://aws.amazon.com/s3/) account and a [S3 bucket](https://aws.amazon.com/s3/) to hold all the static files for this project.
If you would like to use the [allauth](https://django-allauth.readthedocs.io/en/latest/) socialaccounts logins, you can find out more here. [Facebook](https://developers.facebook.com/products/facebook-login/) and [Google](https://developers.google.com/identity/sign-in/web/sign-in)

1.  Open Heroku.
2.  Install the Heroku Command Line Interface (CLI). You use the CLI to manage and scale your applications, provision add-ons, view your application logs, and run your application locally.
    Create an account and navigate to the dash dashboard.
3.  Click on the **New** button.
4.  Click - **Create New App**.
5.  Create a corresponding app name that we use to deploy our application. The apps **name** must be **unique.**.
6.  Pick a server location that is closest to you.
7.  Once the app is created click on the resources button and choose the Heroku Postgres to attach a postgres database to your project.
8.  To be able to run on Heroku A few more libraries are needed.
    [Guniorn](https://gunicorn.org/) a (WSGI HTTP Server), [dj-databas-url](https://pypi.org/project/dj-database-url/) to connect with PostgreSQL and [Psycopg](https://www.psycopg.org/)(PostgreSQL adapter)

        ```bash
        $ pip install Gunicorn, dj-database, Psycopg
        ```

9.  To migrate to the postgres db. First `import dj-databas-url` at the top of the setting.py.
10. Then comment out the default database configuration and add:

    ```python
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('< Put your DATABASE_URL here >'))
    }
    ```

    > In Heroku, Click into the settings tab and navigate to **'reveal config vars'**.
    > Here you will find the _'DATABASE_URL'_.

11. Make migrations by following steps 10-15 in [Local deployment](#local-deployment).
12. After migrations are complete, change database configurations to:

    ```python
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    ```

    > This uses Postgres in deployment and sqlite3 in development.

13. Enter in all your AWS variables as well as all your `.env` variables into Heroku's Config Vars.

    | Key                   |      Value      |
    | --------------------- | :-------------: |
    | AWS_SECRET_ACCESS_KEY | < Your Values > |
    | AWS_ACCESS_KEY_ID     | < Your Values > |
    | USE_AWS               |      True       |

    > You will get in them when you setup your [AWS bucket](https://aws.amazon.com/s3/).
    > If you are wanting to use the [allauth](https://django-allauth.readthedocs.io/en/latest/) social accounts, uncomment out lines 60-61 from settings.py (INSTALLED_APPS socialaccounts) and add your [Facebook](https://developers.facebook.com/products/facebook-login/) secrets into the 'Config Vars'. [Googel](https://developers.google.com/identity/sign-in/web/sign-in) setup here.

    | Key                         |      Value      |
    | --------------------------- | :-------------: |
    | SOCIAL_AUTH_FACEBOOK_KEY    | < Your Values > |
    | SOCIAL_AUTH_FACEBOOK_SECRET | < Your Values > |

14. In your Terminal. Navigate to your directory.
    Login to Heroku using the Terminal

        ```bash
        $ heroku login
        ```

15. Create a `Procfile` This file tells heroku how to run the project

    ```bash
    $ web: gunicorn focus_fitness.wsgi:application
    ```

16. Freeze your requirements

    ```bash
    $ pip freeze > requirements.txt
    ```

17. Add files and commit to github using

    ```bash
    $ git add .
    ```

18. Commit changes to Github

    ```bash
    $ commit -m "You message"
    ```

19. Now that heroku is ready to go, Inside the Django setting.py you will need to set up the AWS configs so the static files have a place to go.
    Add

        ```python
        if 'USE_AWS' in os.environ:
            AWS_STORAGE_BUCKET_NAME = < Your Bucket Name >
            AWS_S3_REGION_NAME = < Your server location >
            AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
            AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
            AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
            AWS_DEFAULT_ACL = None

        # Static and media files

            STATICFILES_STORAGE = 'custom_storages.StaticStorage'
            STATICFILES_LOCATION = 'static'
            DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
            MEDIAFILES_LOCATION = 'media'
            STATIC_URL = f'http://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
            MEDIA_URL = f'http://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
        ```

        >Specifies the hosts that focus can run on

        ```python
            ALLOWED_HOSTS = ['127.0.0.1', 'focus-fitness.herokuapp.com']
         ```

20. You are ready to push to Heroku

    ```bash
    $ git push heroku master
    ```

21. When your app is deployed successfully. Click '_Open App_' in to top right hand corner of Heroku to open app in browser.

 <div align="right">

[Back to Top :arrow_up: ](#table-of-contents)

</div>

---

## Credits

### Code

- The project’s code was developed by following the [Code Institute](https://codeinstitute.net/) and [Just Django](https://justdjango.com/) video lessons and based on the understanding of the course material, The code has been customized and enhanced to fit with the purpose of the project. In some places the logic is used and in others the code. Some comments with credits have been added where needed.
- YouTubers Matt from [Just Django](https://justdjango.com/) and John from [Codemy.com](https://codemy.com/) have been extremely helpful in finding additional information during the building of this project.
- The [Django Documentation](https://docs.djangoproject.com/en/3.1/) and [Stack Overflow](https://stackoverflow.com/) have been referred to constantly and super helpful in deciphering the different django debugging error codes.
- The Ripple Effect on the buttons click is thanks to Leonardo Monteiro Fernandes ~ [Ripple Effect](https://medium.com/@leonardo.monteiro.fernandes/css-techniques-for-material-ripple-effect-3f0ece3062a0)
- [CSS-Tricks](https://css-tricks.com/snippets/css/media-queries-for-standard-devices/) for iphone and ipad media queries.

#### Content and Media

**Content**
The Supplements section of the shop is all obtained from [Bodybuilding.com](bodybuilding.com)
Blogs are taken from [BodyBuilding.com](bodybuilding.com) and [puregym.com](https://www.puregym.com) with credits to:

- Basic setup for README.md file - [Clint-Davis](https://github.com/Clinton-Davis/focus_fitness)
- Cardio for Gym Bros: 5 Conditioning Finishers for Lifters - [Thomas King](https://www.bodybuilding.com/author/jon-erik-kawamoto-cscs-cep)
- The surprising way exercise helps your heart -[ Hobart Swan](https://www.bodybuilding.com/author/hobart-swan)
- How To Avoid Rebound Weight Gain - [ATP Science](https://www.bodybuilding.com/author/contributing-writer)
- 8 Ways To Maximize Your Post-Workout Recovery- [Shannon Clark](https://www.bodybuilding.com/author/shannon-clark)
- The Importance Of Sleep - [David Robson](https://www.bodybuilding.com/author/david-robson)
- 4 Reasons You're Not Adding Muscle - [Dan North](https://www.bodybuilding.com/author/dan-north)
- The Real Fitness Lessons Of Lockdown - [Lee Boyce](https://www.bodybuilding.com/author/lee-boyce)
- Upper Body Dumbbell Workout - [@kaypuregym](https://www.instagram.com/kaypuregym/) and [@bethtruemanfit](https://www.instagram.com/bethtruemanfit/)
- How To Clean Cardio Machines - [puregym.com](https://www.puregym.com).
- 5 Functional Exercises To Master - [PAUL JOSEPH](https://www.puregym.com/personal-trainer/paul-joseph/)
- How To Support Your Immune System - [PureGym](https://www.puregym.com/blog/how-to-support-your-immune-system/)
- Going Plant-Based? Read This First - [puregym.com](https://www.puregym.com)
- The Program's content is taken from [wikipedia](https://www.wikipedia.org/)

**Video Media**
The workout videos were taken from [YouTube](https://www.youtube.com/) with credits to:
Home Workout to IMPROVE STAMINA - [LEANSQUAD](https://www.youtube.com/channel/UCI_VPUgIs60oLH162pVhpOQ)
Stretch | Five-Minute Full Body Stretch - [Bowflex](https://global.bowflex.com/)
3 Perfect Stretches to Start Your Day! - [Calisthenicmovement](https://www.youtube.com/channel/UCZIIRX8rkNjVpP-oLMHpeDw)
Increase Your Mobility & Flexibility- [Calisthenicmovement](https://www.youtube.com/channel/UCZIIRX8rkNjVpP-oLMHpeDw)
10 Min Sweat Workout - [Pamela Reif](https://www.youtube.com/channel/UChVRfsT_ASBZk10o0An7Ucg)
How To Start Eating Healthy (LIFE CHANGING) - [CHRIS HERIA](https://www.youtube.com/channel/UCaBqRxHEMomgFU-AkSfodCw)
5 Best Shoulder Exercises - [CHRIS HERIA](https://www.youtube.com/channel/UCaBqRxHEMomgFU-AkSfodCw)
Effective Complete arm workout [CHRIS HERIA](https://www.youtube.com/channel/UCaBqRxHEMomgFU-AkSfodCw)
Lose Belly Fat Effortlessly -[ Gravity Transformation - Fat Loss Experts](https://www.youtube.com/channel/UC0CRYvGlWGlsGxBNgvkUbAg)
Intermittent Fasting Top 5 Mistakes - [Thomas DeLauer](https://www.youtube.com/channel/UC70SrI3VkT1MXALRtf0pcHg)
What Happens Inside When You Burn Fat -[ Gravity Transformation - Fat Loss Experts](https://www.youtube.com/channel/UC0CRYvGlWGlsGxBNgvkUbAg)
Basics of Resistance Training Principle - [ Gravity Transformation - Fat Loss Experts](https://www.youtube.com/channel/UC0CRYvGlWGlsGxBNgvkUbAg)
Pictures
The images used for this website are from [Unsplash](https://unsplash.com/) and hold a CC license
Photo by [Javier Santos Guzmán](https://unsplash.com/@buildingjavier?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/).
Photos by [Evan Wise](https://unsplash.com/@evanthewise?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)
Photos by [Damir Spanic](https://unsplash.com/@spanic?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)
Photo by [Sven Mieke](https://unsplash.com/@sxoxm?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/)
Icons by [Icons8](https://icons8.com/)

###### <i>Disclaimer: This project was created for educational use only as part of the Code Institute Full Stack Software Development Course for Milestone 4 Django!</i>

 <div align="right">

[ Back to Top :arrow_up:](#table-of-contents)

</div>