# WebcrawlStyleCreator

Project By: Matthew Canute, Young-Min Kim, Donggu Lee, Adriena Wong

<b>Currently the server hosting our website is down. To run it in a local environment, please see RUNNING.txt in the main_project folder.</b>

Colours and fonts have a huge impact on how visitors view online content, whether it's a company website or a personal blog. With so many possible colours and fonts, it's difficult to choose the perfect combination for a site. Our ‘Web Style Generator’ will recommend the perfect style by comparing a user’s typical text content with other similar websites or blogs. Additionally, we wanted to look at possible colour or font trends within certain categories of websites and blogs using the same datasets.

We built a frontend website (​http://www.webstylegenerator.com/​) that generates style recommendations based on the user’s input text for websites and blogs separately. It gives an immediate visual of how the colours and fonts would look together. Built using Flask, this webpage allows users to input a piece of sample text from their website/blog. The webpage would then suggest colours and fonts based on the text's semantically similarity to other Tumblr blogs or websites currently on the Internet as scraped from Alexa's Top Websites page (https://www.alexa.com/topsites). Also, as a direct result of scraping websites and blogs, we obtained a really fascinating dataset that could be used for further analyses. For example, by periodically scraping websites or blogs in a similar way, website style preferences and trends could be tracked over time. Also, association rules between popular colour and font pairings could be analysed. Finally, colours used by certain industries could be examined as well. Overall, this could be generally helpful to marketers looking to design a website.

We plotted the RGB values of the main three colours found on websites in a 255 x 255 x 255 graph. It was interesting to see that there were clearly clusters of colours that are typically unused. In general, all colours across the greyscale were widely used by both websites and blogs. Bold primary colours were popular for websites whereas for blogs, there was a larger variety of colours but it was clear that pastel colours were more popular.

Webpage Colours Visualization:

![image](https://user-images.githubusercontent.com/29899423/97764693-d814b200-1ae5-11eb-8b20-947c6b9bfef3.png)


Tumblr Blog Colours Visualization:

![image](https://user-images.githubusercontent.com/29899423/97764663-c6330f00-1ae5-11eb-9dac-9df94a1168b6.png)


# Final Report

[Report.pdf](https://github.com/atwong88/WebStyleGenerator/files/5468099/Report.pdf)


