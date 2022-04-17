Week ending 10 APR

Learned:
1- Mersenne Twister! The random() function in python uses this. http://www.math.sci.hiroshima-u.ac.jp/m-mat/MT/emt.html

2- When using the css ::before selector,we have to use content in the rules and put something or an empty string in order to see the before work.

3- DOM manipulation is wild. I learned I can declare a variable on an element, and create a custom element. I used it to make a global color scheme in my css. 

4- Attempting to serve static assets over http for an https site, breaks the rules allowed by current browsers. Good for security, and good opportunity to learn some details for me. I updated my portfolio and was serving font-awesome and google fonts via the a href link breaks things. The fix was here S/O Stack Overflow https://stackoverflow.com/questions/26616400/fonts-and-font-awesome-icons-not-loading-over-ssl 

And some more details here https://www.paulirish.com/2010/the-protocol-relative-url/

It took me a very long time to trouble shoot, BUT I felt the neurons connecting. Love it.

5 - used setTimemout() to delay the ending of my confetti upon completing the step slider. It is async so I just need to make sure I am aware of the rest of the function so I don't break it.

6 - I successfully troubleshot a non-responsive slider indicator color fill. It was because inside my function I mistakenly referred to my variable as active when it was named actives. 

Successes:
Updated my portfolio site. https://www.leroygardner.dev/
5 - Django things...it is very cool I can hit localhost.../api/things and get back a json objects api routes

6- Setting up querysets is very cool too, and then using serializers to manipulate the data returned on the queryset

Tech:
JWT tokens
Postman!!! Saved some URLs as a variable.

Concepts:
Authentication using DRF (https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication) and https://github.com/jazzband/djangorestframework-simplejwt, Authorization

Questions:
Learn more about this __all__ convention in python/django 
