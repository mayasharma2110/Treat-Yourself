# Treat Yourself

[Link to live project.](.....)

This is a website for a site selling chocolate, hot chocolate, tea and coffee.  

It is aimed for those who are interested in purchasing any of the above, the site helps users pick the right products for them by having sorting options by price/ratings and also having different sections in the site for the 4 different cagetories of products.

## Table of Contents

* [UX](#ux)
  * [User Stories](#user-stories)
    * [First Time Visitor Goals](#first-time-visitor-goals)
    * [Returning Visitor Goals](#returning-visitor-goals)
    * [Frequent User Goals](#frequent-user-goals)
  * [Strategy](#strategy)
    * [Business Goals](#business-goals)
    * [User Goals](#user-goals)
  * [Scope](#scope)
  * [Structure](#structure)
  * [Skeleton](#skeleton)
   * [Wireframes Navbar](#wireframes-navbar)
   * [Wireframes Home](#wireframes-home)
   * [Wireframes Login](#wireframes-login)
   * [Wireframes Register](#wireframes-register)
   * [Wireframes Logout](#wireframes-logout)
   * [Wireframes Products](#wireframes-products)
   * [Wireframes Product Detail](#wireframes-product-detail)
   * [Wireframes Bag](#wireframes-bag)
   * [Wireframes Checkout](#wireframes-checkout)
   * [Wireframes Profile](#wireframes-profile)
   * [Wireframes Add Product](#wireframes-add-product)
   * [Wireframes Edit Product](#wireframes-edit-product)
   * [Wireframes Comments](#wireframes-comments)
  * [Surface](#surface)
    * [Colours](#colours)
    * [Imagery](#imagery)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features Left to Implement](#features-left-to-inplement)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
  * [Manual Testing](#manual-testing)
  * [Online Validation](#online-validation)
  * [Lighthouse Validation](#lighthouse-validation) 
  * [User Stories from the UX Section](#user-stories-from-the-ux-section)
* [Deployment](#deployment)
  * [Creation](#creation)
  * [Heroku](#heroku)
  * [Local Clone](#local-clone)
  * [Forking](#forking)
* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

## UX

### User Stories

#### First Time Visitor Goals

* As a first time user, I want to know the purpose of the site.

* As a first time user, I want to be able to see products that appeal to me by filtering on the 4 main categories of the site, the subcategories within the 4 main categories and also sorting by price or overall rating. I want to be able to quickly add a product to my basket from this page (default of 1 quantity and not on subscription).

* As a first time user, I want to be able to the specific details of a product I am interested in (description, price and rating) from here I want to be able to add products to my shopping basket.

* As a first time user I want to be able to search for a specific term (for the name or description of a product), on filtering or searching for a term I want to see the number of results displayed.

* As a first time user, I want to be able to see the total in my shopping basket at any given time.

* As a first time user, I want to be able to view my shopping basket and update the quantity of a product or remove it within the page.

* As a first time user, I want to be able to purchase products successfully (get taken to a page which confirms the order has been successful) and see these in my profile when logged in. 

#### Returning Visitor Goals

* As a returning user, I have similar needs of a first time user.

* As a returning user, I want to be able to register for an account, log in and log out.

* As a returning user, I want to receive an email confirmation once I sign up to the site and I also want to be able to recover my password if I forget it.

* As a returning user, I want the site to save my default shipping and billing information for easier checkout in the future (if I am registered to the site and logged in).

* As a returning user, I want to rate products I have tried to help other users find good products.

#### Frequent User Goals

* As a frequent user, I have similar needs of a first time and returning user.

* As a frequent user, I want to subscribe so that I get my favourite products on a regular schedule that I can choose.

### Strategy

#### Business goals

* As a business owner, I want to help users find new products they may enjoy.

* As a business owner, I want to help users purchase products.

* As a business owner, I want to be able to manage the products (picture, price, description etc) that are displayed on the site and remove any that are not for sale anymore.

#### User Goals

* To find existing and new products they may like.

* To purchase any products as a one off or purchase on a subscription.

* To have the ability to view past orders I have made from my profile.

* To have the ability to rate products I have previously tried.

### Scope

Key features to be included based on user stories are:

* Responsive website on mobile, tablet and laptop size devices.

* The home page will contain a selection of the products available on the site to entice users to view the products in more detail and hopefully make a purchase.

* The register page will allow users to create their own account for the site by entering a username, email address and password.

* The login page will allow registered users to login with thier username or email and password.

* The logout page will be a check to confirm a user definately wants to logout.

* The products page will show the users the products with some main details like price and rating.

* The product detail page will show the further details of the product like the description. 

* The shopping bag pag will show what a user currently has in their basket and a link for them to checkout and complete thier purchase.

* The checkout page will allow users to enter their shipping and billing information to complete the purchase, if they are logged in their default payment and delivery information will be automatically populated.

* The profile page will show a users past orders and it will also allow then to update their default delivery information.

* The add product page will be available to admin only, this will allow them to enter a products name, description, picture and price.

* The edit product page will be similar to the add procut page and will be available to admin only, the only difference is that this will auto populate with the products current information and allow the admin to update any details.

### Structure

All pages of the website will have a consistent navigation bar. The home, login and register links will be available to users who aren't yet registered and/or logged into the site. All users regardless or registration or login status will be able to view all products, view product detail pages, add products to their shopping basket, view the basket  and make a purchase. Logged in users and admin (superusers) will be able to view their profile and also logout. Admin (superusers) will be able to edit and delete products. Below the navbar there will also be a header with links to view all products (by price, rating or category) or one of the 4 main categories of products (chocolate, hot chocolate, tea and coffee), under these 4 main categories there will be subgategories as follows: Chocolate (white, milk, dark and all), hot chocolate (classic, nutty, other, all), tea (black, white, other, all) and coffee (dark roast, light roast, medium roast, all). This header will also be displayed on all pages of the site.

The website will use Materializecss grids to make the layout responsive to different devices and screen sizes.

* The home page will contain a selection of the products available on the site to entice users to view the products in more detail and hopefully make a purchase. This will also contain a link to enter the store and view the specific products.

* The register page will allow users to create their own account for the site by entering a username, email address and password. This will also contain a link for registered users to login.

* The login page will allow registered users to login with thier username or email and password. This will also contain a link for unregistered users to register an account and a link for users who are registered to reset thier password if they forgot it.

* The logout page will be a check to confirm a user definately wants to logout.

* The products page will contain the number of products available given a certain selection or search made by the user and below it the products with some main details like price and rating. There will also be quick links for the users to add 1 of any item to their shopping basket, this can be amended on the basket page.

* The product detail page will show the description of the product with the other variables like price rating. From here users can select a one-off purchase and the quantity or they can subscribe to get their favourite product sent regularly to them. 

* The shopping bag pag will show what a user currently has in their basket. If the user does not have any items they will be prompted to return to the products page to add some items to the bag. If the user does have items this will be displayed on the page and they will have the ability to update the quantity of any items or remove them from the bag if they changed their mind. If the user has some items a link to checkout will also be displayed and take the user to the checkout page.

* The checkout page will allow users to enter their shipping and billing information to complete the purchase, if they are logged in their default payment and delivery information will be automatically populated. If a user is logged in there will also be a default checked box if a user wants/needs to update any information on this page and save it to their profile, if a user if not registered or logged in there will be a prompt to login or register an account.

* The profile page will show a users past orders and it will also allow then to update their default delivery information. The profile page will also list any products a user has purchased in the past and allow them to rate the products they have tried before to help other users pick good products and also an option to add one of these products quickly and easily to thier bag.

* The add product page will be available to admin only, this will allow them to enter a products name, description, picture and price.

* The edit product page will be similar to the add procut page and will be available to admin only, the only difference is that this will auto populate with the products current information and allow the admin to update any details.

### Skeleton

I used pen and paper to make the wireframes for this project. The website was designed to have 11 pages - Home, Login, Register, Logout, Products, Product detail, Bag, Checkout, Profile, Add product (admin only) and Edit product (admin only). 

#### Wireframes Navbar

![Navbar Wireframes](static/wireframes/navbar.jpg)  

#### Wireframes Home

![Home Wireframes](static/wireframes/home.jpg)  

#### Wireframes Login

![Login Wireframes](static/wireframes/login.jpg)  

#### Wireframes Register

![Register Wireframes](static/wireframes/register.jpg)  

#### Wireframes Logout

![Logout Wireframes](static/wireframes/logout.jpg)  

#### Wireframes Products

![Products Wireframes](static/wireframes/products.jpg)  

#### Wireframes Product Detail

![Product Detail Wireframes](static/wireframes/product_detail.jpg)  

#### Wireframes Bag

![Bag Wireframes](static/wireframes/bag.jpg)  

#### Wireframes Checkout

![Checkout Wireframes](static/wireframes/checkout.jpg)  

#### Wireframes Profile

![Profile Wireframes](static/wireframes/profile.jpg)  

#### Wireframes Add Product 

![Add Product Wireframes](static/wireframes/add_product.jpg)  

#### Wireframes Edit

![Edit Product Wireframes](static/wireframes/edit_product.jpg)  

#### Wireframes Comments

Please note there are a few changes to the final site since the wireframes were made:

### Surface

#### Colours
I looked at pupolar sites selling these products including: [Hotel Chocolat](https://www.hotelchocolat.com/uk), [Throntons](https://www.thorntons.co.uk/), [Whittard](https://www.whittard.co.uk/) and [T2 Tea](https://www.t2tea.com/en/uk/). I chose a main color of purple (#8e24aa purple darken-1) to represent a luxury brand for the site. The site [here](https://color.adobe.com/create/color-wheel) helped me fine square complementary colours of green (#43a047 green darken-1) and blue (#1e88e5 blue darken-1). General text for descriptions, prices etc of products uses dark grey (#424242 grey darken-3).

#### Imagery
I picked a selection of the product images to show on the home screen to entice users to view the products in more detail and hopefully make a purchase. For each of the 4 categories I chose images to show these specific products (chocolate, hot chocolate, tea and coffee). Further information on this is given in the credits - media section of this readme.

## Features

### Existing Features

* The site is responsive on mobile, tablet and laptop size devices.

### Features Left to Implement

## Technologies Used

* HTML - used to create the main content for the website.

* CSS - used to add style and colour to the content.

* [Materializecss](https://materializecss.com/)
  * Used to help make this website responsive for different devices and to create the collapsible navbar.
  * Used to make the cards on the home page reveal the review details for each book.
  * Used to help create the colours and style on the site. 
  * Used to validate user information in the add/edit review forms. 

* Javascript - used to help make the site responsive to the user's input - defensive programming before deleting a review, book or genre to check if the user is sure they want to proceed.

* jQuery - used to help make the site responsive to the user's input - defensive programming before deleting a review, book or genre to check if the user is sure they want to proceed.

* [MongoDB](https://www.mongodb.com/) used to create, store and update the data used in this site.

* [Python](https://www.python.org/) and [Flask](https://flask.palletsprojects.com/en/2.0.x/) - used to get data from the database in MongoDB to the live site.

* [Gitpod](https://www.gitpod.io/) - used to write the code for the website.

* [GitHub](https://github.com/) - used to store the current and previous versions of the code. 

* [Heroku](https://www.heroku.com/) - used to host the live website.

* [Tinypng](https://tinypng.com/) - used to compress the images so they loaded quicker on the website.

* [Django](https://www.djangoproject.com/) - used to ...

* [AWS](https://aws.amazon.com/) - used to ... 

* [Stripe](https://stripe.com/gb) - used to ...

## Testing

### Manual Testing

Expected -Feature is expected to do X why the user does Y
Testing - Tested the feature by doing Y
Result - The feature did not respond due to A,B,C
or
Result - The feature acted as normally and it did Y
Fix - I did Z to the code because something was missing
And test user stories with relevant screenshots.

- There was an issue with users being able to add more than 10 of any item at a time - for example - by adding 6 of an item and then going back and adding another 5. I had to update my logic in the bag views to hadle this and return an message error if a user tries to do this by.
- Users can only update the quantity of one-off purchases and not for subscriptions, this is on purpose. They cant add more than one subscription for the same product from either the product detail page or the bag.
- Subscription only works on the frontend and has not been set up to take regular (in this case monthly) payments from the users card, as this would require extra secrity steps and to save the users card details and billing information which is more complex than this course covers.
- It would be good to allow users to choose the frequency of their subscription (monthly, every 2 months etc).

### Online Validation

* I checked the website loads and responds as expected on Google Chrome and Microsoft Edge browsers. 

* Used chrome developer tools to check responsiveness on mobile, tablet and laptop devices.  
I also checked the website on my HP 15 inch laptop, Philips 20 inch monitor and Sony smartphone.

* Used the [w3c validator](https://validator.w3.org/) to validate my html (for all pages of the website) to check for no errors or warnings. For html there was 1 warning on all pages due to the section for flash messages (shown below).
  ![HTML warning](static/testing/html-warning.PNG) <br>
  There were additionally some extra errors/warnings due to the materializecss being used that the validator did not have access to (see below also). <br>
  ![Other HTML warnings](static/testing/other-html-warnings.png)

* Used the [jigsaw validator](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my style.css file to check for no errors or warnings. 
I did not validate css of the whole website as this included the imported materializecss files.

* Used [Jshint](https://jshint.com/) to validate my js files and ensure no warnings or errors.

* Used [PEP8 Online](http://pep8online.com/) to validate my python files and ensure no warnings or errors.

### Lighthouse Validation

I used [lighthouse](https://developers.google.com/web/tools/lighthouse) in chrome developer tools to check the websites performance in terms of 
performance, accessibility, best practises and SEO.
This was done for all pages of the website and for desktop devices only due to time.
The summary table below shows these metrics.

| Device | Page |  Performance | Accessibility  | Best Practises  | SEO |
|---|---|---|---|---|---|
| Desktop  |  Home | % | % | % | % |

Full reports can be found below:

### User Stories from the UX Section

* First Time Visitor Goals  

  * As a first time user, I want to ...
    * How the site meets this user need.

* Returning Visitor Goals

  * As a returning user, I want to ...
    * How the site meets this user need.

* Frequent User Goals
    
  * As a frequent user, I want to ...
    * How the site meets this user need.

* Business Goals

  * As a business owner, I want to ...
    * How the site meets this business need.

## Deployment

### Creation

* All code was written in Gitpod and used [this template](https://github.com/Code-Institute-Org/gitpod-full-template) from Code Institute.
* Files were added to the staging area using "git add ."
* Files were committed to the local repository using "git commit -m 'commit message here'".
* Committed changes were pushed to the GitHub repository.

### Heroku

To deploy the project to a live website the below steps were followed:

* Go to Heroku.com and log in (if not registered you must create an account first).
* Make sure your project has a file specifying which applications are needed to run your site, use the below code to automatically generate this
> pip3 freeze --local > requirements.txt
* Also make sure you have a Procfile which tells Heroku which file runs the app (in our case it is app.py), use the below code to generate this. The Procfile may add a blank line which can cause issues so check and remove this if needed.
>  echo web: python app.py > Procfile (note that this has no extension)
* In Heroku click on create a new app. The Heroku app name must be unique and generally uses - instead of spaces and all lowercase letters. Then select the region closest to you and create app.
* To connect our app to Heroku we can setup an automatic deployment from our GitHub repo. Within your Heroku app go to the deployment tab and click on GitHub for the deployment method. Make sure your GitHub profile is displayed below and enter the repository name and search. Make sure your repo is displayed and click connect to this app.
* Before enabling automatic deployment, we still have a couple more steps.
* Click on the settings tab in your app and click on reveal config vars, you can then enter the information that is in the hidden env.py file. Typically, you need to include IP, PORT, SECRET_KEY, MONGO_URI and MONGO_DBNAME.
* Git add, commit and push the changes in your Gitpod (adding the requirements and Procfile files) as epxplained in the above section.
* Go back to your Heroku app and the deployment tab - now click to enable automatic deployment and then click deploy branch.
* Heroku will now receive the code from GitHub and build your app, once it is complete you should see that your app has been successfully deployed.
* Now the deployed site is available and should automatically update whenever changes are pushed to GitHub from Gitpod.

### Local Clone
To make a local copy of a repository on your own GitHub account you can clone it.
This allows others to view the original code and/or make changes to it (on their own local copy).
Changing the code on your local repository will not affect the original code or deployed website.

To clone a repository in GitHub you can follow the steps below:
* Log into GitHub and locate the repository you wish to clone.
* Click on the code button (to the left of the green Gitpod button) and copy the https URL given.
* Open Gitpod (or another editor if you prefer).
* Use the "git clone 'insert copied URL here'" command.
* A clone of the original repository will now be available for you locally 
on your own repository to view/edit as you wish.

### Forking

Forking is another way to  make a local copy of a repository on your own GitHub account to do this follow the below steps:

* Log into GitHub and locate the repository you wish to fork.
* At the top-right of the repository (and top-right of the green Gitpod button), locate the fork button.
* A copy of the original repository will now be available for you locally 
on your own repository to view/edit as you wish.

## Credits

### Code

* The Materializecss library was used to help make this website responsive for different devices and to create the collapsible navbar. 

### Content

* For each of the products on the site I had a look at popular sites [Hotel Chocolat](https://www.hotelchocolat.com/uk), [Throntons](https://www.thorntons.co.uk/), [Whittard](https://www.whittard.co.uk/) and [T2 Tea](https://www.t2tea.com/en/uk/) to gain inspiration for the products on this site. Additioanlly these sites helped me get an idea for a good layout of the site.

* I used an images from online, information below in the media section.

### Media

* I found the following image online from [xxx](xxx), this is the file static/images/xxx.jpg. The owner of the image is xxx and their page on the site is [here](xxx). Please note I did some cropping to the original image but no other changes were made.
  
### Acknowledgments

* Code Institute for teaching me the basics of HTML, CSS, Materializecss, JavaScript, jQuery, Python, MongoDB, Flask, Django, AWS and Stripe to allow me to create this website.

* My mentor Antonio Rodriguez who helped provide feedback on this website and improvements that could be made.

* The Slack community for providing support throughout the course so far.  

* Thanks to the fellow students on Slack and my friends who viewed the website and gave feedback on any improvements/changes that could be made. 

* The websites that I used to gain inspiration for creating my own book review site: [Hotel Chocolat](https://www.hotelchocolat.com/uk), [Throntons](https://www.thorntons.co.uk/), [Whittard](https://www.whittard.co.uk/) and [T2 Tea](https://www.t2tea.com/en/uk/).