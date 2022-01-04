# Detecting-phishing-sites

Hackers use many sorts of attacks- one of them is phishing; The attacker use an imposter site to trick the user and make him insert his username, password, ID whatever the hacker desire.
In many cases the attacker trick successfully the user mostly because leak of knowledge, that's why there is a true need of detecting such sites.

Usage- run the program, insert URL to check, get a safty grade for the site.

unshorten_url(url) – in case of redirection or a short URL this function uncover the real URL / the final destination URL in case of redirection.

url_response_status(url) – this function returns the response of the server – 404 – not found, 200 – ok, 403 forbidden and so on.
In case server response is 404 I end the program. 

check_special_signs(url) – one of the ways to detect phishing site is by using special signs such as '@', '%' and recently '#'.
@ - is a reserved sign in HTML.
% - is a way to decode a URL using hexadecimal to ASCII characters.
In this method I also implemented regular expression to determine more sites faster.

dots_counter(url) – another way to determine a phishing site is by counting how many dots there are in the URL domain, if there are more then 5 dots it will raise a flag and notify about it.

scrapping(url) – one of the most powerful ways to determine if a site is a phishing site or is not, this technique is used to gain the HTML of the website by that, I can search exactly what I want in the url, exposing it to its bare bones.
it allows me to look for suspicious files, url, submit buttons etc.
There is a downside worth to mention, it require lots of research to know what to look for and not only that, everything might hide in there – perfection is a must.

url_length(url) – another parameter I check is the length of the url, usually a standard URL is no longer than 150 characters.
is_ip(url) – this method checks if the site provided by the user is an Ip address, usually those types of URLs are redirecting to another website.

ssl_certificate_check(url) – trusted website such as Amazon, eBay and so on, not only use "HTTPS" protocol for secured site but also use payment services.
Those payment services require HTTPS protocol and provide certificate the site is safe for payment.
This is the reason why I choose to check certificate, it's an immediate authentication that the site is safe.

is_valid_certificate(ssock) – its goal is to check if the certificate is valid by exporting the expiration date and compare it with the current date, so in case the certificate is not valid it is irrelevant.
transfer_date_to_timestamp(date) – in order to compare the current day date and the end date of the certificate I used time stamp function.
